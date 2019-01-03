Title: Emacs with Jetbrain IDE
Date: 2018-08-21
Category: Emacs, Jetbrain, macos

Emacs with Jetbrain IDE
==

为了启动的效率， 使用c/s形式的emacs；
推荐一个配置：https://korewanetadesu.com/emacs-on-os-x.html
下面摘抄一下

启动一个emacs server：

```applescript
tell application "Terminal"
   do shell script "/Applications/Emacs.app/Contents/MacOS/Emacs --daemon"
end tell
```

以一个frame启动一个emacs client：
```applescript
tell application "Terminal"
    try
        do shell script "/Applications/Emacs.app/Contents/MacOS/bin/emacsclient -c -n &"
        tell application "Emacs" to activate
    on error
        do shell script "/Applications/Emacs.app/Contents/MacOS/Emacs"
    end try
end tell
```

下面两个脚本作为后续applescript的基础, 在 server没有响应的时候执行
在终端启动一个gui emacs

emacsc

```bash
#!/bin/sh
set -e
/Applications/Emacs.app/Contents/MacOS/Emacs "$@"
```

在终端启动一个emacs

emacst

```bash
#!/bin/sh
set -e
/Applications/Emacs.app/Contents/MacOS/Emacs -nw "$@"
```

ec

```applescript
set -e
EMACSCLIENT=/Applications/Emacs.app/Contents/MacOS/bin/emacsclient
exec $EMACSCLIENT -c -a emacsc "$@"
```

et

```applescript
set -e
EMACSCLIENT=/Applications/Emacs.app/Contents/MacOS/bin/emacsclient
exec $EMACSCLIENT -t -a emacst "$@"
```

添加一些alias到.bash_profile, 替换系统自带的emacs命令

```bash
alias emacsclient="/Applications/Emacs.app/Contents/MacOS/bin/emacsclient"
alias emacs="ec"
export EDITOR="ec"
```

启动的时候新的frame是不能获得焦点的， 把下面的添加到init.el解决

```elisp
(when (featurep 'ns)
  (defun ns-raise-emacs ()
    "Raise Emacs."
    (ns-do-applescript "tell application \"Emacs\" to activate"))

  (defun ns-raise-emacs-with-frame (frame)
    "Raise Emacs and select the provided frame."
    (with-selected-frame frame
      (when (display-graphic-p)
        (ns-raise-emacs))))

  (add-hook 'after-make-frame-functions 'ns-raise-emacs-with-frame)

  (when (display-graphic-p)
    (ns-raise-emacs)))
```

然后在jetbrain ide比如pycharm里面，

preferences-> Tools-> External Tools-> +新建一个

- Program： ec
- Arguments: $FilePath$
- Working directory: $FileDir$

还可以在keymap设置一个快捷键  比如command+e，

这样可以直接使用emacsclient打开当前的文件