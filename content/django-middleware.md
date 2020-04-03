Title: Django Middleware Exception Handling
Date: 2020-02-23
Category: Django, Python, Middleware

Django Middleware Exception Handling
==

** TL;DR **

> django在处理middleware的时候就是装饰了handler，每一层middleware都会被convert_exception_to_response来处理异常，所以出错了直接会返回报错的信息。

---

之前在一次面试的时候，问我如果你写了一个middleware，如果请求过来的时候报错了，那么请求在返回的时候还会执行这个middleware吗？
当时我只在一家公司写过3个月的django，所以我对这个问题还没有比较清晰的认识，我就说要看django的实现。


实际上django在实现middleware的时候还是非常简单的。
```python
def load_middleware(self):
    handler = convert_exception_to_response(self._get_response)
    for middleware_path in reversed(settings.MIDDLEWARE):
        middleware = import_string(middleware_path)
    try:
        mw_instance = middleware(handler)
    except MiddlewareNotUsed as exc:
        pass   
    if mw_instance is None:
       raise ImproperlyConfigured(
       'Middleware factory %s returned None.' % middleware_path
)

```

所以如果你在handle之前出错了还没有处理的话，那么这个调用链就断了。
这个写法就像是在一个函数前面加了很多的装饰器一样。

```python
@middleware0
@middleware1
@yourmiddleware
@middleware2
def handle(request):
    return response
```

处理错误的方法就是上面的convert_exception_to_response

```python
def convert_exception_to_response(get_response):
    @wraps(get_response)
    def inner(request):
        try:
            response = get_response(request)
        except Exception as exc:
            response = response_for_exception(request, exc)
        return response
    return inner

```

一个简单的middleware

```python
def simple_middleware(get_response):
    def middleware(request):
        print("before middleware")
        response = get_response(request)
        print("after middleware")
        return response
    return middleware
```

    
