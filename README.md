# 基于翻译api的翻译程序

#### 介绍
利用开放的百度翻译api和金山词霸api制作的翻译程序。
## 功能
1. 具有选中翻译功能（选中按alt键，这项功能使用的是百度翻译的api）
2. 选中单词播放读音功能（选中按shift，这项功能使用的是金山词霸的api）
3. 软件主页显示每日一句（来自金山词霸的每日一句，也可以进行音频播放。设置——>播放）
4. 此软件在运行时可最小化到拖盘（退出可使用托盘图标右键或设置——>退出）
## 使用
安装好依赖包，直接在python中运行translate.py即可 。

**主要依赖包：** 
1. wxpython
2. autogui
3. pypercilp
4. requests
## 注意
api的appid及密钥的获取可自己去百度注册（免费）