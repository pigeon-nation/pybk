# pybk
Brackets for functions in native Python.

Usage Example:
```python3
from pybk import AsmModule, Hashable, ReturnVal

example = lambda a, b: {
    c := a + b,
    v := False if c < 10 else True,
    l := Hashable([
        c + i for i in range(a)
    ]),
    ReturnVal(c, v, l())
}

module = AsmModule({
    "example": example
})

print(module.example(4, 5))
print(module.example(5, 5))

```
