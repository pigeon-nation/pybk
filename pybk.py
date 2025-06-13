class DynamicReturn:
    def __call__(self):
        if len(self.data) == 0:
            return None
        elif len(self.data) == 1:
            return self.data[0]
        else:
            return self.data

class ReturnVal(DynamicReturn):
    def __init__(self, /, *data):
        self.data = data
    
class Hashable(DynamicReturn):
    def __init__(self, /, *data):
        self.data = data

class AsmModule:
    def __init__(self, funcs):
        for fname in funcs.keys():
            setattr(self, fname, retw(funcs[fname]))

def retw(f):
    def wrapf(*a, **k):
        setr = f(*a, **k)
        for item in setr:
            if isinstance(item, ReturnVal):
                return item()
        return None
    return wrapf
