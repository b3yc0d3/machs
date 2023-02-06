# MIT License
# 
# Copyright (c) 2023 Niklas K.
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# A place where all functions life, that don't fit in other files/categoris or are just to small

import os
import sys
import importlib.util
from pathlib import Path
from os import path as OPath
from mlib.var import *
from mlib.project import project_root

# Declare subdirectorys that also containing build files
def subdir(*dirs):
    for dir in dirs:
        dir_path = OPath.join(Path().absolute(), dir)
        
        if not OPath.isdir(dir_path):
            print(f"\x1b[1;31mError: Subdirectory `{dir}` does not exists.\x1b[0m")
            exit(1)
        
        sub_module_file = OPath.join(dir_path, "machs")
        
        # check if "machs" file exists in there
        if OPath.isfile(sub_module_file):
            os.chdir(dir_path)
            _execute_module(sub_module_file)
            
            # reset cwd
            os.chdir(project_root())
        else:
            print(f"\x1b[1;31mError: Subdirectory `{dir}` does not contain any build script.\x1b[0m")
            exit(1)

# Execite a python file with currenty functions etc.
def _execute_module(path):
    with open(path) as f:
        code = compile(f.read(), path, 'exec')
        exec(code, globals(), locals())

# Define custom variables
# If "value" is unset, it returns the value stored under "key"
#def eval(key, value = None):
def var(key, value = None):
    #global VARIABLES
    
    #if value != None:
    #    VARIABLES[str(key)] = value
    #else:
    #    return VARIABLES[str(key)]
    
    if value != None:
        globals()[str(key)] = value
        locals()[str(key)] = value
    else:
        return globals()[str(key)]