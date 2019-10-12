## rack ##
# https://en.wikipedia.org/wiki/Rack_(web_server_interface)

```ruby
# helloWorld.ru
# The application that has the call method defined.
class HelloWorld
  # Call method that would return the HTTP status code, the content type and the content.
  def call (env)
    [200, {"Content-Type" => "text/html; charset=utf-8"}, ["Hello World"]]
  end
end
```

## WSGI
# https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface

```python
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    yield b'Hello, World\n'
```


ASGI
# https://asgi.readthedocs.io/en/latest/specs/main.html

```python
coroutine application(scope, receive, send)
```