import platform as pf

class get_window:
    def __init__(self, Print:bool):
        self.pyversion='Run Python version:'+pf.python_version()
        self.os='System environment:'+pf.platform()
        self.processor='Central Processing Unit:'+pf.processor()
        if Print:
            if pf.system()=='Windows':
                print('We get '+pf.system()+'® opt:',end='\n ')
            print(self.pyversion,end='\n ')
            print(self.os,end='\n ')
            print(self.processor)
    def GetPythonVersion(self, *_obj):
        if len(_obj):
            return pf.python_version()
        return self.pyversion
    getpyver=GetPythonVersion
    def GetOS(self, *_obj):
        if len(_obj):
            if  _obj[0]=='Name'or _obj[0]=='name'or _obj[0]=='NAME':
                return pf.system()
            return pf.platform()
        return self.os
    getos=GetOS
    def GetProvessing(self, *_obj):
        if len(_obj):
            return pf.processor()
        return self.processor
    getCPU=GetProvessing