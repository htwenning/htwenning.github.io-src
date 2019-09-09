Title: a little docker-compose
Date: 2018-07-12
Category: Linux, Docker

a little docker-compose
==

docker-compose 可以快速给一个临时的linux开发环境

docker-compose run service_name

--rm参数可以在退出的时候删除这个container


**例子：**

在项目下面创建 docker-compose.yml, 内容如下
（cap_add和secutiry_opt用来保证container中可以正常使用gdb）

```yml
version: '3'
services:
  app:
    image: "python:3.6"
    volumes:
      - .:/app
    ports:
      - "5000:5000"
    cap_add:
      - ALL
    security_opt:
      - seccomp:unconfined
    command: bash
```

启动并attach bash:

> docker-compose run app

如果上面指定了ports那么需要带上 --service-ports 参数才能把服务的ports暴露给host

> docker-compose run --service-ports app

退出后container也就挂掉了，通过docker ps -a 查看container_id, 后面再启动：

> docker start [container_id]

> docker attach [container_id]

或者执行一个新的bash命令

> docker exec -it [container_id] bash

tips：

- 根据需要可以commit镜像
- 可以写Dockerfile和更多的service, 利用docker-compose up启动
- docker-compose up用来启动一堆服务，没有交互式的概念

**参考：**

- https://docs.docker.com/compose/
