Title: Proxy Golang
Date: 2020-03-27
Category: Golang, Proxy

Proxy Golang
===

go的便捷性提升来自三个要素：

1. go module
2. github private repo free
3. goproxy.io

从1.11开始支持go module， 让项目不再依赖gopath, 之前的所有过渡方案都可以舍弃了;
github免费了私有项目，作为稳定和使用广泛的git仓库，私有免费之后，可以让开发避免本地依赖，舍弃 require replace;
goproxy.io提供了免费的代理，让build无需翻墙。

```bash
go env -w GO111MODULE=on
go env -w GOPROXY=https://goproxy.io,direct

# 设置不走 proxy 的私有仓库，多个用逗号相隔（可选）
go env -w GOPRIVATE=github.com/n-wen/*

# github 使用ssh替换https
git config --global url."git@github.com:".insteadOf "https://github.com/"
```

*发布的私有module可以使用git tag来标记版本*

*Reference:*

- [goproxy.io](https://goproxy.io/zh/)
- [How to `go get` private repos using SSH key auth instead of password auth](https://gist.github.com/dmitshur/6927554)
- [Publishing Go Modules](https://blog.golang.org/publishing-go-modules)