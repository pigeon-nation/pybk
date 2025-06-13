# pybk
Brackets for functions in native Python.

Usage Example:
```python3
from pybk import AsmModule, Hashable, ReturnVal

example = lambda a, b: {               # define an example function
    c := a + b,                        # c = a + b.
    v := False if c < 10 else True,    # v = true if c is greater than or equal to 10.
    l := Hashable([                    # hashable is used to allow lists and other non-hashable types to be used.
        x := c + i for i in range(a)   # a loop demo, which can modify variables, and also creates a list which is stored by Hashable.
    ]),
    ReturnVal(c, v, l(), x)            # return statment. calling a Hashable type returns its contents, which can be done in an expression.
}

module = AsmModule({                   # assemble the module. this is necessary, as the functions have to be re-defined through a custom wrapper.
    "example": example                 # "example" is the name used to refer to the function one it would be a function in the module.
})

print(module.example(4, 5))            # module.example is how the function is accessed. all data would be returned as though it was from a normal function.
print(module.example(5, 5))

```
