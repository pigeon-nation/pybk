class DynamicReturn:
    def __init__(self, /, *data):
        self.data = data

    def __call__(self):
        if len(self.data) == 0:
            return None
        elif len(self.data) == 1:
            return self.data[0]
        else:
            return self.data

class ReturnVal(DynamicReturn):
    def __repr__(self):
        return "<ReturnVal> " + repr(self.__call__())

class Hashable(DynamicReturn):
    def __repr__(self):
        return "<Hashable> " + repr(self.__call__())

class AsmModule:
    def __init__(self, funcs):
        for fname in funcs.keys():
            setattr(self, fname, self._ret_wrapper(funcs[fname]))

    def _ret_wrapper(self, f):
        def _wrapper_func(*a, **k):
            setr = f(*a, **k)
            for item in setr:
                if isinstance(item, ReturnVal):
                    return item()
            return None
        return _wrapper_func
