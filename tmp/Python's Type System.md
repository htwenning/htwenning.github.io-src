## **Python's Type System**

微软发布了一个静态类型检查器 [pyright](https://github.com/Microsoft/pyright) , 但是使用它之前还是需要对python的类型系统有个基本知识才能更好地掌握。

Python是动态强类型编程语言， 强类型是指一个变量的类型是固定的，动态是指一个变量可以被赋予各种类型的值。

在version 2时代或者python兴起开发web时， 因为python的动态性带来了非常好的开发速度，但是越来越复杂的系统，加上开发者的习惯不同，导致代码复杂，难以维护。

Python在3.5版本开始逐渐引入type hint, 按时间顺序如下：

- [pep-483 The Theory of Type Hints (Python 3.5) 19-Dec-2014](https://www.python.org/dev/peps/pep-0483/)
- [pep-484 Type Hints (Python 3.5) 29-Sep-2014](https://www.python.org/dev/peps/pep-0484/)
- [pep-526 Syntax for Variable Annotations (Python 3.6) 09-Aug-2016](https://www.python.org/dev/peps/pep-0526/)
- [pep-544 Protocols: Structural subtyping (static duck typing) (Python 3.7) 05-Mar-2017](https://www.python.org/dev/peps/pep-0544/)



 Here we assume that type is a set of values and a set of functions that one can apply to these values.

subtype relationship

一个变量是否能安全地赋值给另外一个变量

A strong criterion for when it *should* be safe is:

- every value from `second_type` is also in the set of values of `first_type`; and
- every function from `first_type` is also in the set of functions of `second_type`.

```python
a = 1.1 # type float
a = 1 # type int , safe, 因为int的set更小， 但是function set更多

b = 1 # type: int
b = 1.1 # type: float, unsafe
b >> 2 # 这个会出错，因为float不支持这个操作

# 所以int是float的subtype， 记为 int <: float
# List[int]是 List[float]的subtype吗？ 不是。 


```

Assigning `a_value` to `a_variable` is OK if the type of `a_value` is consistent with the type of `a_variable`

generic type takes a concrete type and return a concrete type

wikipedia :

[Covariance and Contravariance](https://en.wikipedia.org/wiki/Covariance_and_contravariance_(computer_science))

