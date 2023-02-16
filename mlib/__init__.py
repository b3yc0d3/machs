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

import sys
PYTHON_VERSION = [str(n) for n in [sys.version_info.major, sys.version_info.minor, sys.version_info.micro]]
PYTHON_VERSION_INT = int("".join(PYTHON_VERSION))
PYTHON_VERSION_HUMAN = ".".join(PYTHON_VERSION)

if not PYTHON_VERSION_INT >= 3100:
    print(f"Sorry, your python `{PYTHON_VERSION_HUMAN}` version isn't campatable.\nPython 3.10 or newer is required")
    exit(1)

from mlib.std import *
from mlib.var import *
from mlib.project import *
from mlib.command import *
from mlib.dependencys import *
from mlib.onfiguration import *
from mlib.internals import *

# Non mutable dict for lib infos
machs = ConstDict({
    "version": "0.1.1"
})