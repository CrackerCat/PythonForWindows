import ctypes
import msvcrt
import os
import copy
import sys

import k32testing as kernel32proxy
import generated_def.windef as windef
import winobject
import native_exec
from generated_def.winstructs import *

# Function resolution !

def swallow_ctypes_copy(ctypes_object):
    new_copy = type(ctypes_object)()
    ctypes.memmove(ctypes.byref(new_copy), ctypes.byref(ctypes_object), ctypes.sizeof(new_copy))
    return new_copy

def get_func_addr(dll_name, func_name):
        dll = ctypes.WinDLL(dll_name)
        return kernel32proxy.GetProcAddress(dll._handle, func_name)
        
def enumerate_processes():
    process_entry = winobject.WinProcess()
    process_entry.dwSize = ctypes.sizeof(process_entry)
    snap = kernel32proxy.CreateToolhelp32Snapshot(windef.TH32CS_SNAPPROCESS, 0)
    kernel32proxy.Process32First(snap, process_entry)
    res = []
    res.append(swallow_ctypes_copy(process_entry))
    while kernel32proxy.Process32Next(snap, process_entry):
         res.append(swallow_ctypes_copy(process_entry))
    return res

def enumerate_threads():
    thread_entry = winobject.WinThread()
    thread_entry.dwSize = ctypes.sizeof(thread_entry)
    snap = kernel32proxy.CreateToolhelp32Snapshot(windef.TH32CS_SNAPTHREAD, 0)
    threads = []
    kernel32proxy.Thread32First(snap, thread_entry)
    threads.append(copy.copy(thread_entry))
    while kernel32proxy.Thread32Next(snap, thread_entry):
        threads.append(copy.copy(thread_entry))
    return threads
    
def is_wow_64(hProcess):
    try:
        fnIsWow64Process =  get_func_addr("kernel32.dll", "IsWow64Process")
    except kernel32proxy.Kernel32Error:
        return False
    IsWow64Process  = ctypes.WINFUNCTYPE(BOOL, HANDLE, ctypes.POINTER(BOOL))(fnIsWow64Process)
    Wow64Process = BOOL()
    res = IsWow64Process(hProcess, ctypes.byref(Wow64Process))
    if res:
        return bool(Wow64Process)
    raise ctypes.WinError()
 
def create_file_from_handle(handle, mode="r"):
    fd = msvcrt.open_osfhandle(handle, os.O_TEXT)
    return os.fdopen(fd, mode, 0)
    
def get_handle_from_file(f):
    return msvcrt.get_osfhandle(f.fileno())
    
def create_console():  
    kernel32proxy.AllocConsole()
    stdout_handle = kernel32proxy.GetStdHandle(windef.STD_OUTPUT_HANDLE)
    console_stdout = create_file_from_handle(stdout_handle, "w")
    sys.stdout = console_stdout
    
    stdin_handle = kernel32proxy.GetStdHandle(windef.STD_INPUT_HANDLE)
    console_stdin = create_file_from_handle(stdin_handle, "r+")
    sys.stdin = console_stdin
    
    stderr_handle = kernel32proxy.GetStdHandle(windef.STD_ERROR_HANDLE)
    console_stderr = create_file_from_handle(stderr_handle, "w")
    sys.stderr = console_stderr
    
class VirtualProtected(object):
    def __init__(self, addr, size, new_protect):
        if (addr % 0x1000):
            addr = addr - addr % 0x1000
        self.addr = addr
        self.size = size
        self.new_protect = new_protect
        
    def __enter__(self):
        self.old_protect = DWORD()
        kernel32proxy.VirtualProtect(self.addr, self.size, self.new_protect, ctypes.byref(self.old_protect))
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        kernel32proxy.VirtualProtect(self.addr, self.size, self.old_protect.value, ctypes.byref(self.old_protect))
        return False