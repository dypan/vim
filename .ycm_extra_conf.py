import os
import ycm_core

C_BASE_FLAGS = [
        '-Wall',
        '-Wextra',
        '-Werror',
        '-Wno-long-long',
        '-Wno-variadic-macros',
        '-fexceptions',
        '-ferror-limit=10000',
        '-DNDEBUG',
        '-std=c11',
        '-I/usr/lib/',
        '-I/usr/include/',
        '-I/usr/include/c++/4.8.5/'
        ]

CPP_BASE_FLAGS = [
        '-Wall',
        '-Wextra',
        '-Wno-long-long',
        '-Wno-variadic-macros',
        '-fexceptions',
        '-ferror-limit=10000',
        '-DNDEBUG',
        '-std=c++1z',
        '-xc++',
        '-I/usr/lib/',
        '-I/usr/include/',
        '-I/usr/include/c++/4.8.5/'
        ]
SOURCE_EXTENTIONS = ['.cpp', '.cxx', '.cc', '.c',]
def FlagsForFile( filename, **kwargs ):
    return {
    'flags': CPP_BASE_FLAGS,
    'do_cache': True
    }

