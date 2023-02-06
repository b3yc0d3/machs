# some finicy class for creating non mutable dicts
class ConstDict:
    def __init__(self,srcdict):
        self._srcdict = srcdict
       
    @property
    def version(self):
        return self._srcdict["version"]
    
    def __getitem__(self,idx):
        return self._srcdict[idx]