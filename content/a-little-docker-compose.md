Title: a little docker-compose
Date: 2018-07-12
Category: Linux, Docker

a little docker-compose
==

docker-compose 可以快速给一个临时的linux开发环境

docker-compose run service_name

--rm参数可以在推出的时候删除这个container


**例子：**

在项目下面创建 docker-compose.yml, 内容如下

```yml
version: '3'
services:
  app:
    image: "python:3.6"
    volumes:
      - .:/app
    command: bash
```

启动并attach bash:

> docker-compose run app

推出后container stop，通过docker ps -a 查看container_id, 后面再启动：

> docker start [container_id]; docker attach [container_id]

tips：

- 根据需要可以commit镜像
- 可以写Dockerfile和更多的service, 利用docker-compose up启动

**参考：**

- https://docs.docker.com/compose/
