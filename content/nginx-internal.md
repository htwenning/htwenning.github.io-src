Title: Nginx Internal (protect your static resource)
Date: 2018-08-31
Category: Nginx, python

Nginx Internal (protect your static resource)
==


1. nginx internal
在location中使用internal标志，限制当前location仅对内部访问


2. 在服务端的response headers中添加x-accel头，并指向internal位置， nginx会访问指定位置
官方文档：https://www.nginx.com/resources/wiki/start/topics/examples/x-accel/

nginx配置实例：

```nginx
server {
    listen       5000;
	location /protected {
		internal;
	    alias /Users/wenning/protected;
	}
	location /doc {
	    proxy_pass http://localhost:8888;
	}
}
```

python服务端实例， 这里以sanic为例：

```python
@app.route("/doc/<file>")
async def projected(request, file):
    return response.raw(body=b'', headers={
        'X-Accel-Redirect': '/protected/{}'.format(file)
    })
```
