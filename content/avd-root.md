Title: Install Xposed on AVD
Date: 2018-09-29
Category: Android,AVD,emulator,Xposed

Install Xposed on AVD
==

在avd上获取root权限，安装xposed framework

### 模拟器准备工作：


- ./sdkmanager "system-images;android-22;google_apis;x86"
- ./avdmanager create avd -n test -k "system-images;android-22;google_apis;x86" 安装后发现没有挂载sdcard， 后来在android studio中修改上了
- cp ~/Library/Android/sdk/system-images/android-22/google_apis/x86/system.img ~/.android/avd/test.avd/system-qemu.img 拷贝之后，模拟器对system的修改就会被保存下载
- ./emulator -avd test -port 5557 -writable-system  这里需要指明解锁system

### 开始root：

参考https://stackoverflow.com/questions/5095234/how-to-get-root-access-on-android-emulator


- adb install supersu.apk
- unzip flashable.zip
- adb root; adb remount
- cd flashable/your_emu_arch/; adb push su.pie /system/bin/su
- adb shell; su root; chmod 06755 /system/bin/su
- su --install; su --daemon&; setenforce 0
- in emulator, open opensu and update bin, click normal button; reboot

### 安装xposed：

下载xpose installer.apk， 在app中操作即可。


### 已知问题：

1. [xpose-installer 下载框架的时候闪退](https://github.com/htwenning/htwenning.github.io/issues/3)


