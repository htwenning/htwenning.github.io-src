Title: tail recursion
Date: 2020-02-25
Category: algorithm

Tail Recursion
===

TL;DR

> 尾递归(Tail Recursion)可以使用一个栈来改为循环遍历；如果不是尾递归，可以使用两个栈来实现.

----

那中序遍历二叉树为例：

```python
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.value)
    inorder(root.right)
```

注意到上面的函数最后调用了函数本身，所以这个就是tail recursion。那么可以非常方便地使用一个stack来把这个递归改为遍历。

> python可以使用list来实现stack

```python
def iterative_inorder(root):
    s = []
    while root or len(s) > 0:
        while root:
            s.append(root.left)
            root = root.left
        root = s.pop()
        print(root.value)
        root = root.right
```

总结一下，就是创建一个stack，然后一个while循环，循环里面第一部分是实现尾递归调用前面的逻辑(如下，往左子树遍历，到头打印)

```
while root:
    s.append(root.left)
    root = root.left
root = s.pop()
print(root.value)
```

最后增加一个递归函数变量传递：
> root = root.right

---

**那么非尾递归怎么办？**

比如后序遍历

```python
def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.value)
```

因为在最后一个递归调用后面还有逻辑处理(print)，相当于遍历完全了再来一段逻辑，那么可以再使用一个stack来实现

```python
def iterative_postorder_two_stacks_ver(root):
    if not root:
        return
    s1 = [root]
    s2 = []
    while len(s1) > 0:
        root = s1.pop()
        if root.left:
            s1.append(root.left)
        if root.right:
            s1.append(root.right)
        s2.append(root)
    while len(s2) > 0:
        root = s2.pop()
        print(root.value)
```

上面就是巧妙地应用了stack的LIFO特性，简洁地实现了postorder traversal

我掌握的理论少，所以描述起来还是不够准确细腻。应该再多写几个例子，就会清楚许多。
