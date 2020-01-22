Title: Async in Python and Javascript
Date: 2020-01-21
Category: Async, Python, Javascript

Async in Python and Javascript
==

[Django 3.0](https://docs.djangoproject.com/en/3.0/releases/3.0/)于2019-12-2日发布，一个新功能是支持了ASGI

Darphne是目前一个支持ASGI的服务器，但是我在[Channels](https://github.com/django/channels/tree/master/loadtesting/2016-09-06) 里面的benchmark看到:
> Daphne is not as efficient as its WSGI counterpart. When considering only latency, Daphne can have 10 times the latency when under the same traffic load as gunincorn. When considering only throughput, Daphne can have 40-50% of the total throughput of gunicorn while still being at 2 times latency.

**所以django的asgi可以期待，但是目前还不能用于产品环境。**

习惯了Django开发的，可能会对asyncio这个不太了解，但是Channels里面又提供了很多async的函数，为了方便用户开发，提供了async_to_sync方法，这样就可以在sync函数中调用async函数了。

但是在javascript里面，就算函数用async装饰了，还是可以直接像常规函数一样调用，所以他们的机制是不一样的。下面就对此做个比较。

**TL;DR**

Python使用的yield从函数内部中跳出; Javascript使用Promise。

---

### 以async_to_sync为例

它实际上是一个class，
构造方法传入一个coroutine, 然后覆写了__call__方法实现:

- get or create a loop

        if not (self.main_event_loop and self.main_event_loop.is_running()):
            loop = asyncio.new_event_loop()
            loop_executor = ThreadPoolExecutor(max_workers=1)
        else:
            pass

- create future

        call_result = Future()

- run coroutine in loop

        if new_loop:
            loop_executor = ThreadPoolExecutor(max_workers=1)
            loop_future = loop_executor.submit(
                self._run_event_loop,
                loop,
                self.main_wrap(
                    args, kwargs, call_result, source_thread, sys.exc_info()
                ),
            )
        else:
            self.main_event_loop.call_soon_threadsafe(
                self.main_event_loop.create_task,
                self.main_wrap(
                    args, kwargs, call_result, source_thread, sys.exc_info()
                ),
            )

- get result

        return call_result.result()

### Javascript Promise

Promise class构造函数接收一个function(resolve, reject)函数，
同步的逻辑写在刚才的函数以及promise对象的then方法接收的回调中。

example：hello方法实现一些逻辑后调用resolve，并传入参数（'hello'），那么在then的回调中会以这个参数执行。

```javascript
function hello(){
    return new Promise(function(resolve, reject){
        setTimeout(()=>{
            resolve('hello')
        }, 2000)
    })
}

hello().then(response=> console.log(response))
```

这样的好处在于可以把then串联起来，以避免过多的缩进。

async/await关键词的引入，使得写法更加简明易懂。

下面的代码和上面的等效：

```javascript
function sleep(milliseconds) {
  return new Promise(resolve => setTimeout(resolve, milliseconds))
}
async function hello(){
    await sleep(2000)
    return 'hello'
}
response = await hello()
console.log(response)
```

可以把async修饰理解为在原来的函数(origin_function)进行了一层包装：

```javascript
new Promise((resolve, reject)=>{
    try{
        var response = origin_function();
        resolve(response)
    }catch(e){
        reject(e)
    }
})
```

## Conclusion

Python中大量的是同步的代码，所以在实现的时候是在该线程中创建一个loop来管理coroutine;
Javascript中主要是异步的代码，所以用Promise来把异步操作串起来。