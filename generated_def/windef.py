#Generated file

class Flag(long):
    def __new__(cls, name, value):
        return super(Flag, cls).__new__(cls, value)
       
    def __init__(self, name, value):
        self.name = name

    def __repr__(self):
        return "{0}({1})".format(self.name, hex(self))

NULL = Flag("NULL", 0)
MAX_PATH = Flag("MAX_PATH", 260)
ANYSIZE_ARRAY = Flag("ANYSIZE_ARRAY", 1)
IMAGE_SIZEOF_SHORT_NAME = Flag("IMAGE_SIZEOF_SHORT_NAME", 8)
IMAGE_NUMBEROF_DIRECTORY_ENTRIES = Flag("IMAGE_NUMBEROF_DIRECTORY_ENTRIES", 16)
STD_INPUT_HANDLE = Flag("STD_INPUT_HANDLE", -10)
STD_OUTPUT_HANDLE = Flag("STD_OUTPUT_HANDLE", -11)
STD_ERROR_HANDLE = Flag("STD_ERROR_HANDLE", -12)
WARMING_NOT_SAME_FLAG_FOR_WINXP = Flag("WARMING_NOT_SAME_FLAG_FOR_WINXP", 0)
PROCESS_ALL_ACCESS = Flag("PROCESS_ALL_ACCESS", 0x001F0FFF)
THREAD_ALL_ACCESS = Flag("THREAD_ALL_ACCESS", 0x001F03FF)
STARTF_USESHOWWINDOW = Flag("STARTF_USESHOWWINDOW", 0x00000001)
STARTF_USESIZE = Flag("STARTF_USESIZE", 0x00000002)
STARTF_USEPOSITION = Flag("STARTF_USEPOSITION", 0x00000004)
STARTF_USECOUNTCHARS = Flag("STARTF_USECOUNTCHARS", 0x00000008)
STARTF_USEFILLATTRIBUTE = Flag("STARTF_USEFILLATTRIBUTE", 0x00000010)
STARTF_RUNFULLSCREEN = Flag("STARTF_RUNFULLSCREEN", 0x00000020)
STARTF_FORCEONFEEDBACK = Flag("STARTF_FORCEONFEEDBACK", 0x00000040)
STARTF_FORCEOFFFEEDBACK = Flag("STARTF_FORCEOFFFEEDBACK", 0x00000080)
STARTF_USESTDHANDLES = Flag("STARTF_USESTDHANDLES", 0x00000100)
SW_HIDE = Flag("SW_HIDE", 0)
SW_SHOWNORMAL = Flag("SW_SHOWNORMAL", 1)
SW_NORMAL = Flag("SW_NORMAL", 1)
SW_SHOWMINIMIZED = Flag("SW_SHOWMINIMIZED", 2)
SW_SHOWMAXIMIZED = Flag("SW_SHOWMAXIMIZED", 3)
SW_MAXIMIZE = Flag("SW_MAXIMIZE", 3)
SW_SHOWNOACTIVATE = Flag("SW_SHOWNOACTIVATE", 4)
SW_SHOW = Flag("SW_SHOW", 5)
SW_MINIMIZE = Flag("SW_MINIMIZE", 6)
SW_SHOWMINNOACTIVE = Flag("SW_SHOWMINNOACTIVE", 7)
SW_SHOWNA = Flag("SW_SHOWNA", 8)
SW_RESTORE = Flag("SW_RESTORE", 9)
SW_SHOWDEFAULT = Flag("SW_SHOWDEFAULT", 10)
SW_FORCEMINIMIZE = Flag("SW_FORCEMINIMIZE", 11)
SW_MAX = Flag("SW_MAX", 11)
DEBUG_PROCESS = Flag("DEBUG_PROCESS", 0x00000001)
DEBUG_ONLY_THIS_PROCESS = Flag("DEBUG_ONLY_THIS_PROCESS", 0x00000002)
CREATE_SUSPENDED = Flag("CREATE_SUSPENDED", 0x00000004)
DETACHED_PROCESS = Flag("DETACHED_PROCESS", 0x00000008)
CREATE_NEW_CONSOLE = Flag("CREATE_NEW_CONSOLE", 0x00000010)
NORMAL_PRIORITY_CLASS = Flag("NORMAL_PRIORITY_CLASS", 0x00000020)
IDLE_PRIORITY_CLASS = Flag("IDLE_PRIORITY_CLASS", 0x00000040)
HIGH_PRIORITY_CLASS = Flag("HIGH_PRIORITY_CLASS", 0x00000080)
REALTIME_PRIORITY_CLASS = Flag("REALTIME_PRIORITY_CLASS", 0x00000100)
CREATE_NEW_PROCESS_GROUP = Flag("CREATE_NEW_PROCESS_GROUP", 0x00000200)
CREATE_UNICODE_ENVIRONMENT = Flag("CREATE_UNICODE_ENVIRONMENT", 0x00000400)
CREATE_SEPARATE_WOW_VDM = Flag("CREATE_SEPARATE_WOW_VDM", 0x00000800)
CREATE_SHARED_WOW_VDM = Flag("CREATE_SHARED_WOW_VDM", 0x00001000)
CREATE_FORCEDOS = Flag("CREATE_FORCEDOS", 0x00002000)
BELOW_NORMAL_PRIORITY_CLASS = Flag("BELOW_NORMAL_PRIORITY_CLASS", 0x00004000)
ABOVE_NORMAL_PRIORITY_CLASS = Flag("ABOVE_NORMAL_PRIORITY_CLASS", 0x00008000)
INHERIT_PARENT_AFFINITY = Flag("INHERIT_PARENT_AFFINITY", 0x00010000)
INHERIT_CALLER_PRIORITY = Flag("INHERIT_CALLER_PRIORITY", 0x00020000)
CREATE_PROTECTED_PROCESS = Flag("CREATE_PROTECTED_PROCESS", 0x00040000)
EXTENDED_STARTUPINFO_PRESENT = Flag("EXTENDED_STARTUPINFO_PRESENT", 0x00080000)
PROCESS_MODE_BACKGROUND_BEGIN = Flag("PROCESS_MODE_BACKGROUND_BEGIN", 0x00100000)
PROCESS_MODE_BACKGROUND_END = Flag("PROCESS_MODE_BACKGROUND_END", 0x00200000)
CREATE_BREAKAWAY_FROM_JOB = Flag("CREATE_BREAKAWAY_FROM_JOB", 0x01000000)
CREATE_PRESERVE_CODE_AUTHZ_LEVEL = Flag("CREATE_PRESERVE_CODE_AUTHZ_LEVEL", 0x02000000)
CREATE_DEFAULT_ERROR_MODE = Flag("CREATE_DEFAULT_ERROR_MODE", 0x04000000)
CREATE_NO_WINDOW = Flag("CREATE_NO_WINDOW", 0x08000000)
PROFILE_USER = Flag("PROFILE_USER", 0x10000000)
PROFILE_KERNEL = Flag("PROFILE_KERNEL", 0x20000000)
PROFILE_SERVER = Flag("PROFILE_SERVER", 0x40000000)
CREATE_IGNORE_SYSTEM_DEFAULT = Flag("CREATE_IGNORE_SYSTEM_DEFAULT", 0x80000000)
STATUS_WAIT_0 = Flag("STATUS_WAIT_0", ( 0x00000000L ))
STATUS_ABANDONED_WAIT_0 = Flag("STATUS_ABANDONED_WAIT_0", ( 0x00000080L ))
STATUS_USER_APC = Flag("STATUS_USER_APC", ( 0x000000C0L ))
STATUS_TIMEOUT = Flag("STATUS_TIMEOUT", ( 0x00000102L ))
STATUS_PENDING = Flag("STATUS_PENDING", ( 0x00000103L ))
DBG_EXCEPTION_HANDLED = Flag("DBG_EXCEPTION_HANDLED", ( 0x00010001L ))
DBG_CONTINUE = Flag("DBG_CONTINUE", ( 0x00010002L ))
STATUS_SEGMENT_NOTIFICATION = Flag("STATUS_SEGMENT_NOTIFICATION", ( 0x40000005L ))
DBG_TERMINATE_THREAD = Flag("DBG_TERMINATE_THREAD", ( 0x40010003L ))
DBG_TERMINATE_PROCESS = Flag("DBG_TERMINATE_PROCESS", ( 0x40010004L ))
DBG_CONTROL_C = Flag("DBG_CONTROL_C", ( 0x40010005L ))
DBG_PRINTEXCEPTION_C = Flag("DBG_PRINTEXCEPTION_C", ( 0x40010006L ))
DBG_RIPEXCEPTION = Flag("DBG_RIPEXCEPTION", ( 0x40010007L ))
DBG_CONTROL_BREAK = Flag("DBG_CONTROL_BREAK", ( 0x40010008L ))
DBG_COMMAND_EXCEPTION = Flag("DBG_COMMAND_EXCEPTION", ( 0x40010009L ))
STATUS_GUARD_PAGE_VIOLATION = Flag("STATUS_GUARD_PAGE_VIOLATION", ( 0x80000001L ))
STATUS_DATATYPE_MISALIGNMENT = Flag("STATUS_DATATYPE_MISALIGNMENT", ( 0x80000002L ))
STATUS_BREAKPOINT = Flag("STATUS_BREAKPOINT", ( 0x80000003L ))
STATUS_SINGLE_STEP = Flag("STATUS_SINGLE_STEP", ( 0x80000004L ))
STATUS_LONGJUMP = Flag("STATUS_LONGJUMP", ( 0x80000026L ))
STATUS_UNWIND_CONSOLIDATE = Flag("STATUS_UNWIND_CONSOLIDATE", ( 0x80000029L ))
DBG_EXCEPTION_NOT_HANDLED = Flag("DBG_EXCEPTION_NOT_HANDLED", ( 0x80010001L ))
STATUS_ACCESS_VIOLATION = Flag("STATUS_ACCESS_VIOLATION", ( 0xC0000005L ))
STATUS_IN_PAGE_ERROR = Flag("STATUS_IN_PAGE_ERROR", ( 0xC0000006L ))
STATUS_INVALID_HANDLE = Flag("STATUS_INVALID_HANDLE", ( 0xC0000008L ))
STATUS_INVALID_PARAMETER = Flag("STATUS_INVALID_PARAMETER", ( 0xC000000DL ))
STATUS_NO_MEMORY = Flag("STATUS_NO_MEMORY", ( 0xC0000017L ))
STATUS_ILLEGAL_INSTRUCTION = Flag("STATUS_ILLEGAL_INSTRUCTION", ( 0xC000001DL ))
STATUS_NONCONTINUABLE_EXCEPTION = Flag("STATUS_NONCONTINUABLE_EXCEPTION", ( 0xC0000025L ))
STATUS_INVALID_DISPOSITION = Flag("STATUS_INVALID_DISPOSITION", ( 0xC0000026L ))
STATUS_ARRAY_BOUNDS_EXCEEDED = Flag("STATUS_ARRAY_BOUNDS_EXCEEDED", ( 0xC000008CL ))
STATUS_FLOAT_DENORMAL_OPERAND = Flag("STATUS_FLOAT_DENORMAL_OPERAND", ( 0xC000008DL ))
STATUS_FLOAT_DIVIDE_BY_ZERO = Flag("STATUS_FLOAT_DIVIDE_BY_ZERO", ( 0xC000008EL ))
STATUS_FLOAT_INEXACT_RESULT = Flag("STATUS_FLOAT_INEXACT_RESULT", ( 0xC000008FL ))
STATUS_FLOAT_INVALID_OPERATION = Flag("STATUS_FLOAT_INVALID_OPERATION", ( 0xC0000090L ))
STATUS_FLOAT_OVERFLOW = Flag("STATUS_FLOAT_OVERFLOW", ( 0xC0000091L ))
STATUS_FLOAT_STACK_CHECK = Flag("STATUS_FLOAT_STACK_CHECK", ( 0xC0000092L ))
STATUS_FLOAT_UNDERFLOW = Flag("STATUS_FLOAT_UNDERFLOW", ( 0xC0000093L ))
STATUS_INTEGER_DIVIDE_BY_ZERO = Flag("STATUS_INTEGER_DIVIDE_BY_ZERO", ( 0xC0000094L ))
STATUS_INTEGER_OVERFLOW = Flag("STATUS_INTEGER_OVERFLOW", ( 0xC0000095L ))
STATUS_PRIVILEGED_INSTRUCTION = Flag("STATUS_PRIVILEGED_INSTRUCTION", ( 0xC0000096L ))
STATUS_STACK_OVERFLOW = Flag("STATUS_STACK_OVERFLOW", ( 0xC00000FDL ))
STATUS_DLL_NOT_FOUND = Flag("STATUS_DLL_NOT_FOUND", ( 0xC0000135L ))
STATUS_ORDINAL_NOT_FOUND = Flag("STATUS_ORDINAL_NOT_FOUND", ( 0xC0000138L ))
STATUS_ENTRYPOINT_NOT_FOUND = Flag("STATUS_ENTRYPOINT_NOT_FOUND", ( 0xC0000139L ))
STATUS_CONTROL_C_EXIT = Flag("STATUS_CONTROL_C_EXIT", ( 0xC000013AL ))
STATUS_DLL_INIT_FAILED = Flag("STATUS_DLL_INIT_FAILED", ( 0xC0000142L ))
STATUS_FLOAT_MULTIPLE_FAULTS = Flag("STATUS_FLOAT_MULTIPLE_FAULTS", ( 0xC00002B4L ))
STATUS_FLOAT_MULTIPLE_TRAPS = Flag("STATUS_FLOAT_MULTIPLE_TRAPS", ( 0xC00002B5L ))
STATUS_REG_NAT_CONSUMPTION = Flag("STATUS_REG_NAT_CONSUMPTION", ( 0xC00002C9L ))
STATUS_STACK_BUFFER_OVERRUN = Flag("STATUS_STACK_BUFFER_OVERRUN", ( 0xC0000409L ))
STATUS_INVALID_CRUNTIME_PARAMETER = Flag("STATUS_INVALID_CRUNTIME_PARAMETER", ( 0xC0000417L ))
STATUS_ASSERTION_FAILURE = Flag("STATUS_ASSERTION_FAILURE", ( 0xC0000420L ))
STATUS_POSSIBLE_DEADLOCK = Flag("STATUS_POSSIBLE_DEADLOCK", ( 0xC0000194 ))
WAIT_IO_COMPLETION = Flag("WAIT_IO_COMPLETION", STATUS_USER_APC)
STILL_ACTIVE = Flag("STILL_ACTIVE", STATUS_PENDING)
EXCEPTION_ACCESS_VIOLATION = Flag("EXCEPTION_ACCESS_VIOLATION", STATUS_ACCESS_VIOLATION)
EXCEPTION_DATATYPE_MISALIGNMENT = Flag("EXCEPTION_DATATYPE_MISALIGNMENT", STATUS_DATATYPE_MISALIGNMENT)
EXCEPTION_BREAKPOINT = Flag("EXCEPTION_BREAKPOINT", STATUS_BREAKPOINT)
EXCEPTION_SINGLE_STEP = Flag("EXCEPTION_SINGLE_STEP", STATUS_SINGLE_STEP)
EXCEPTION_ARRAY_BOUNDS_EXCEEDED = Flag("EXCEPTION_ARRAY_BOUNDS_EXCEEDED", STATUS_ARRAY_BOUNDS_EXCEEDED)
EXCEPTION_FLT_DENORMAL_OPERAND = Flag("EXCEPTION_FLT_DENORMAL_OPERAND", STATUS_FLOAT_DENORMAL_OPERAND)
EXCEPTION_FLT_DIVIDE_BY_ZERO = Flag("EXCEPTION_FLT_DIVIDE_BY_ZERO", STATUS_FLOAT_DIVIDE_BY_ZERO)
EXCEPTION_FLT_INEXACT_RESULT = Flag("EXCEPTION_FLT_INEXACT_RESULT", STATUS_FLOAT_INEXACT_RESULT)
EXCEPTION_FLT_INVALID_OPERATION = Flag("EXCEPTION_FLT_INVALID_OPERATION", STATUS_FLOAT_INVALID_OPERATION)
EXCEPTION_FLT_OVERFLOW = Flag("EXCEPTION_FLT_OVERFLOW", STATUS_FLOAT_OVERFLOW)
EXCEPTION_FLT_STACK_CHECK = Flag("EXCEPTION_FLT_STACK_CHECK", STATUS_FLOAT_STACK_CHECK)
EXCEPTION_FLT_UNDERFLOW = Flag("EXCEPTION_FLT_UNDERFLOW", STATUS_FLOAT_UNDERFLOW)
EXCEPTION_INT_DIVIDE_BY_ZERO = Flag("EXCEPTION_INT_DIVIDE_BY_ZERO", STATUS_INTEGER_DIVIDE_BY_ZERO)
EXCEPTION_INT_OVERFLOW = Flag("EXCEPTION_INT_OVERFLOW", STATUS_INTEGER_OVERFLOW)
EXCEPTION_PRIV_INSTRUCTION = Flag("EXCEPTION_PRIV_INSTRUCTION", STATUS_PRIVILEGED_INSTRUCTION)
EXCEPTION_IN_PAGE_ERROR = Flag("EXCEPTION_IN_PAGE_ERROR", STATUS_IN_PAGE_ERROR)
EXCEPTION_ILLEGAL_INSTRUCTION = Flag("EXCEPTION_ILLEGAL_INSTRUCTION", STATUS_ILLEGAL_INSTRUCTION)
EXCEPTION_NONCONTINUABLE_EXCEPTION = Flag("EXCEPTION_NONCONTINUABLE_EXCEPTION", STATUS_NONCONTINUABLE_EXCEPTION)
EXCEPTION_STACK_OVERFLOW = Flag("EXCEPTION_STACK_OVERFLOW", STATUS_STACK_OVERFLOW)
EXCEPTION_INVALID_DISPOSITION = Flag("EXCEPTION_INVALID_DISPOSITION", STATUS_INVALID_DISPOSITION)
EXCEPTION_GUARD_PAGE = Flag("EXCEPTION_GUARD_PAGE", STATUS_GUARD_PAGE_VIOLATION)
EXCEPTION_INVALID_HANDLE = Flag("EXCEPTION_INVALID_HANDLE", STATUS_INVALID_HANDLE)
EXCEPTION_POSSIBLE_DEADLOCK = Flag("EXCEPTION_POSSIBLE_DEADLOCK", STATUS_POSSIBLE_DEADLOCK)
CONTROL_C_EXIT = Flag("CONTROL_C_EXIT", STATUS_CONTROL_C_EXIT)
EXCEPTION_DEBUG_EVENT = Flag("EXCEPTION_DEBUG_EVENT", 1)
CREATE_THREAD_DEBUG_EVENT = Flag("CREATE_THREAD_DEBUG_EVENT", 2)
CREATE_PROCESS_DEBUG_EVENT = Flag("CREATE_PROCESS_DEBUG_EVENT", 3)
EXIT_THREAD_DEBUG_EVENT = Flag("EXIT_THREAD_DEBUG_EVENT", 4)
EXIT_PROCESS_DEBUG_EVENT = Flag("EXIT_PROCESS_DEBUG_EVENT", 5)
LOAD_DLL_DEBUG_EVENT = Flag("LOAD_DLL_DEBUG_EVENT", 6)
UNLOAD_DLL_DEBUG_EVENT = Flag("UNLOAD_DLL_DEBUG_EVENT", 7)
OUTPUT_DEBUG_STRING_EVENT = Flag("OUTPUT_DEBUG_STRING_EVENT", 8)
RIP_EVENT = Flag("RIP_EVENT", 9)
TH32CS_SNAPHEAPLIST = Flag("TH32CS_SNAPHEAPLIST", 0x00000001)
TH32CS_SNAPPROCESS = Flag("TH32CS_SNAPPROCESS", 0x00000002)
TH32CS_SNAPTHREAD = Flag("TH32CS_SNAPTHREAD", 0x00000004)
TH32CS_SNAPMODULE = Flag("TH32CS_SNAPMODULE", 0x00000008)
TH32CS_SNAPMODULE32 = Flag("TH32CS_SNAPMODULE32", 0x00000010)
TH32CS_SNAPALL = Flag("TH32CS_SNAPALL", ( TH32CS_SNAPHEAPLIST | TH32CS_SNAPPROCESS | TH32CS_SNAPTHREAD | TH32CS_SNAPMODULE ))
TH32CS_INHERIT = Flag("TH32CS_INHERIT", 0x80000000)
CONTEXT_I386 = Flag("CONTEXT_I386", 0x00010000)
CONTEXT_CONTROL = Flag("CONTEXT_CONTROL", 0x00000001L)
CONTEXT_INTEGER = Flag("CONTEXT_INTEGER", 0x00000002L)
CONTEXT_SEGMENTS = Flag("CONTEXT_SEGMENTS", 0x00000004L)
CONTEXT_FLOATING_POINT = Flag("CONTEXT_FLOATING_POINT", 0x00000008L)
CONTEXT_DEBUG_REGISTERS = Flag("CONTEXT_DEBUG_REGISTERS", 0x00000010L)
CONTEXT_EXTENDED_REGISTERS = Flag("CONTEXT_EXTENDED_REGISTERS", 0x00000020L)
CONTEXT_FULL = Flag("CONTEXT_FULL", ( CONTEXT_CONTROL | CONTEXT_INTEGER | CONTEXT_SEGMENTS ))
CONTEXT_ALL = Flag("CONTEXT_ALL", ( CONTEXT_FULL | CONTEXT_FLOATING_POINT | CONTEXT_DEBUG_REGISTERS | CONTEXT_EXTENDED_REGISTERS ))
CONTEXT_FULL = Flag("CONTEXT_FULL", CONTEXT_I386 | CONTEXT_FULL)
CONTEXT_ALL = Flag("CONTEXT_ALL", CONTEXT_I386 | CONTEXT_ALL)
PAGE_NOACCESS = Flag("PAGE_NOACCESS", 0x01)
PAGE_READONLY = Flag("PAGE_READONLY", 0x02)
PAGE_READWRITE = Flag("PAGE_READWRITE", 0x04)
PAGE_WRITECOPY = Flag("PAGE_WRITECOPY", 0x08)
PAGE_EXECUTE = Flag("PAGE_EXECUTE", 0x10)
PAGE_EXECUTE_READ = Flag("PAGE_EXECUTE_READ", 0x20)
PAGE_EXECUTE_READWRITE = Flag("PAGE_EXECUTE_READWRITE", 0x40)
PAGE_EXECUTE_WRITECOPY = Flag("PAGE_EXECUTE_WRITECOPY", 0x80)
PAGE_GUARD = Flag("PAGE_GUARD", 0x100)
PAGE_NOCACHE = Flag("PAGE_NOCACHE", 0x200)
PAGE_WRITECOMBINE = Flag("PAGE_WRITECOMBINE", 0x400)
MEM_COMMIT = Flag("MEM_COMMIT", 0x1000)
MEM_RESERVE = Flag("MEM_RESERVE", 0x2000)
MEM_DECOMMIT = Flag("MEM_DECOMMIT", 0x4000)
MEM_RELEASE = Flag("MEM_RELEASE", 0x8000)
MEM_FREE = Flag("MEM_FREE", 0x10000)
MEM_PRIVATE = Flag("MEM_PRIVATE", 0x20000)
MEM_MAPPED = Flag("MEM_MAPPED", 0x40000)
MEM_RESET = Flag("MEM_RESET", 0x80000)
MEM_TOP_DOWN = Flag("MEM_TOP_DOWN", 0x100000)
MEM_WRITE_WATCH = Flag("MEM_WRITE_WATCH", 0x200000)
MEM_PHYSICAL = Flag("MEM_PHYSICAL", 0x400000)
MEM_ROTATE = Flag("MEM_ROTATE", 0x800000)
MEM_LARGE_PAGES = Flag("MEM_LARGE_PAGES", 0x20000000)
MEM_4MB_PAGES = Flag("MEM_4MB_PAGES", 0x80000000)
SEC_FILE = Flag("SEC_FILE", 0x800000)
SEC_IMAGE = Flag("SEC_IMAGE", 0x1000000)
SEC_PROTECTED_IMAGE = Flag("SEC_PROTECTED_IMAGE", 0x2000000)
SEC_RESERVE = Flag("SEC_RESERVE", 0x4000000)
SEC_COMMIT = Flag("SEC_COMMIT", 0x8000000)
SEC_NOCACHE = Flag("SEC_NOCACHE", 0x10000000)
SEC_WRITECOMBINE = Flag("SEC_WRITECOMBINE", 0x40000000)
SEC_LARGE_PAGES = Flag("SEC_LARGE_PAGES", 0x80000000)
MEM_IMAGE = Flag("MEM_IMAGE", SEC_IMAGE)
WRITE_WATCH_FLAG_RESET = Flag("WRITE_WATCH_FLAG_RESET", 0x01)
DELETE = Flag("DELETE", ( 0x00010000L ))
READ_CONTROL = Flag("READ_CONTROL", ( 0x00020000L ))
WRITE_DAC = Flag("WRITE_DAC", ( 0x00040000L ))
WRITE_OWNER = Flag("WRITE_OWNER", ( 0x00080000L ))
SYNCHRONIZE = Flag("SYNCHRONIZE", ( 0x00100000L ))
STANDARD_RIGHTS_REQUIRED = Flag("STANDARD_RIGHTS_REQUIRED", ( 0x000F0000L ))
STANDARD_RIGHTS_READ = Flag("STANDARD_RIGHTS_READ", ( READ_CONTROL ))
STANDARD_RIGHTS_WRITE = Flag("STANDARD_RIGHTS_WRITE", ( READ_CONTROL ))
STANDARD_RIGHTS_EXECUTE = Flag("STANDARD_RIGHTS_EXECUTE", ( READ_CONTROL ))
STANDARD_RIGHTS_ALL = Flag("STANDARD_RIGHTS_ALL", ( 0x001F0000L ))
SPECIFIC_RIGHTS_ALL = Flag("SPECIFIC_RIGHTS_ALL", ( 0x0000FFFFL ))
TOKEN_ASSIGN_PRIMARY = Flag("TOKEN_ASSIGN_PRIMARY", ( 0x0001 ))
TOKEN_DUPLICATE = Flag("TOKEN_DUPLICATE", ( 0x0002 ))
TOKEN_IMPERSONATE = Flag("TOKEN_IMPERSONATE", ( 0x0004 ))
TOKEN_QUERY = Flag("TOKEN_QUERY", ( 0x0008 ))
TOKEN_QUERY_SOURCE = Flag("TOKEN_QUERY_SOURCE", ( 0x0010 ))
TOKEN_ADJUST_PRIVILEGES = Flag("TOKEN_ADJUST_PRIVILEGES", ( 0x0020 ))
TOKEN_ADJUST_GROUPS = Flag("TOKEN_ADJUST_GROUPS", ( 0x0040 ))
TOKEN_ADJUST_DEFAULT = Flag("TOKEN_ADJUST_DEFAULT", ( 0x0080 ))
TOKEN_ADJUST_SESSIONID = Flag("TOKEN_ADJUST_SESSIONID", ( 0x0100 ))
TOKEN_ALL_ACCESS_P = Flag("TOKEN_ALL_ACCESS_P", ( STANDARD_RIGHTS_REQUIRED | TOKEN_ASSIGN_PRIMARY | TOKEN_DUPLICATE | TOKEN_IMPERSONATE | TOKEN_QUERY | TOKEN_QUERY_SOURCE | TOKEN_ADJUST_PRIVILEGES | TOKEN_ADJUST_GROUPS | TOKEN_ADJUST_DEFAULT ))
TOKEN_ALL_ACCESS = Flag("TOKEN_ALL_ACCESS", ( TOKEN_ALL_ACCESS_P | TOKEN_ADJUST_SESSIONID ))
SE_PRIVILEGE_ENABLED_BY_DEFAULT = Flag("SE_PRIVILEGE_ENABLED_BY_DEFAULT", ( 0x00000001L ))
SE_PRIVILEGE_ENABLED = Flag("SE_PRIVILEGE_ENABLED", ( 0x00000002L ))
SE_PRIVILEGE_REMOVED = Flag("SE_PRIVILEGE_REMOVED", ( 0X00000004L ))
SE_PRIVILEGE_USED_FOR_ACCESS = Flag("SE_PRIVILEGE_USED_FOR_ACCESS", ( 0x80000000L ))