Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x="hello"
type(x)
<class 'str'>
x=100
type(x)
<class 'int'>
x=22.13
type(x)
<class 'float'>
x='c'
type(x)
<class 'str'>
x=2j
type(x)
<class 'complex'>
x=["banana","apple"]
type(x)
<class 'list'>
x=("apple","banana","cherry")
type(x)
<class 'tuple'>
x={"apple","banana","cherry"}
type(x)
<class 'set'>
x=range(1:6)
SyntaxError: invalid syntax
x=range(7)
type(x)
<class 'range'>
x={"name":"prachi","age":20}
type(x)
<class 'dict'>
x=frozenset({"banana","apple"})
type(x)
<class 'frozenset'>
x=True
type(x)
<class 'bool'>
x=b"hello"
type(x)
<class 'bytes'>
x=bytearray(5)
type(x)
<class 'bytearray'>
x=memoryview(byte(5))
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    x=memoryview(byte(5))
NameError: name 'byte' is not defined. Did you mean: 'bytes'?
>>> x=memoryview(bytes(5))
>>> type(x)
<class 'memoryview'>
>>> x=None
>>> type(x)
<class 'NoneType'>
>>> 
>>> 
>>> 
>>> l1=["banana","apple"]
>>> l1.append("cherry")
>>> print(l1)
['banana', 'apple', 'cherry']
>>> 
>>> # append in tuple
>>> l1=("banana","apple")
>>> l1.append("cherry")
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    l1.append("cherry")
AttributeError: 'tuple' object has no attribute 'append'
>>> 
>>> 
>>> s=[10,20,30,40]
>>> s
[10, 20, 30, 40]
>>> # tuple
>>> s=(10,20,30,40)
>>> s
(10, 20, 30, 40)
>>> #set
>>> s={10,20,30,40}
>>> s
{40, 10, 20, 30}
>>> #dict
>>> dic={"name":"prachi","age":20}
>>> dic
{'name': 'prachi', 'age': 20}
