Title: a little awk
Date: 2018-07-11 18:28
Category: Linux

a little awk
===

参考:
https://gregable.com/2010/09/why-you-should-know-just-little-awk.html

- 默认使用空格分割
- 使用$符号选取字段
- NF是字段数, NR行号
- 可以使用if进行判断语句
- print 打印后面的内容
- 可以把字段存入变量，不用声明, 也不用考虑单位


例子：
```bash
docker images | awk '{print $1}'
docker images | awk '{if($1 == "<none>"){print $3}}' | xargs docker rmi
docker images | awk '{print "tag: ", $2}'
docker images | awk '{a += $NF; print "total: ", a}'
```