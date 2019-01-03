Title: Profile in Python
Date: 2018-09-11
Category: Python, profile, pyflame, py-spy

Profile in Python
==

在不改变代码的情况下（比如在生产环境遇到的问题），profile python进程，曾经一个好的选择是pyflame。

现在又发现一个不错的工具： py-spy

- [pyflame](https://github.com/uber/pyflame)
- [py-spy](https://github.com/benfred/py-spy)


pyflame利用ptrace来采样函数调用，然后可以使用 flame graph打印svg显示火焰图。
在一些相对老的系统要配置好还是挺麻烦的。

py-spy使用rust编写， 通过读进程内存来采样，可以直接使用pip安装！

> py-spy --pid 12345

>py-spy --flame profile.svg --pid 12345
