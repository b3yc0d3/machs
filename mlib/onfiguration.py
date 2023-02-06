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

import re
from mlib.enums import ReplcType

class ConfigurationData():
    def __init__(self):
        self.values = []
        
    def set_quoted(self, key, value):
        self.values.append([key, value, ReplcType.QUOTED])
        
    def set_digit(self, key, value):
        self.values.append([key, value, ReplcType.DIGIT])
        
    def set_raw(self, key, value):
        self.values.append([key, value, ReplcType.RAW])
        
def configure_file(input, output, configuration):
    cfgIn = open(input, "r").read().splitlines()
    cfgOut = cfgIn
        
    for l in range(len(cfgIn)):
        for pair in configuration.values:
            key = pair[0]
            value = pair[1]
            rType = pair[2]
            
            regex = re.compile(r"(@" + key + r"@)", re.IGNORECASE)
            
            replcValue = ""
            match rType:
                case ReplcType.QUOTED:
                    replcValue = f"\"{value}\""
                case ReplcType.DIGIT | ReplcType.RAW:
                    replcValue = value
        
            cfgOut[l] = re.sub(regex, replcValue, cfgIn[l])
        
    out = open(output, "w")
    out.write("\n".join(cfgOut))
    out.close()