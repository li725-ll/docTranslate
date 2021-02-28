import wx, response
from wx import adv
import pyperclip
import pyautogui
import sentence
import function


class TaskBarIcon(wx.adv.TaskBarIcon):  # 系统托盘
    ID_Play = wx.NewIdRef()
    ID_About = wx.NewIdRef()
    ID_Closeshow = wx.NewIdRef()
    
    def __init__(self, frame):
        super(TaskBarIcon, self).__init__(iconType=adv.TBI_DOCK)
        self.frame = frame
        self.SetIcon(wx.Icon(name='images/ico/tubiao.ico', type=wx.BITMAP_TYPE_ICO), '翻译程序')  # wx.ico为ico图标文件
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarLeftDClick)  # 定义左键双击即左键双击恢复窗口
        self.Bind(wx.EVT_MENU, self.OnPlay, id=self.ID_Play)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=self.ID_About)
        self.Bind(wx.EVT_MENU, self.OnCloseshow, id=self.ID_Closeshow)
    
    def OnTaskBarLeftDClick(self, event):
        if self.frame.IsIconized():  # 判断窗口是否是系统托盘(图标化)
            self.frame.Iconize(False)  # 恢复窗口（如果True，则图标化窗口；如果False，显示并恢复它）
        if not self.frame.IsShown():  # 判断窗口是否隐藏
            self.frame.Show(True)  # 显示窗口
        self.frame.Raise()  # 将窗口提升到顶层
        
    def OnPlay(self, event):
        function.music_play()
    
    def OnAbout(self, event):
        wx.MessageBox('基于百度翻译API的翻译程序', '关于')
    
    def OnCloseshow(self, event):
        self.Destroy()
        self.frame.Destroy()
    
    # 托盘图标右键菜单
    def CreatePopupMenu(self):  # 重写TaskBarIcon的CreatePopupMenu方法
        # 文档地址 https://docs.wxpython.org/wx.adv.TaskBarIcon.html?highlight=createpopupmenu#wx.adv.TaskBarIcon.CreatePopupMenu
        menu = wx.Menu(title="菜单", style=wx.MENU_TEAROFF)
        menu.Append(self.ID_Play, '播放')
        menu.Append(self.ID_About, '关于')
        menu.Append(self.ID_Closeshow, '退出')
        return menu


class FanYiWindow(wx.TipWindow):
    def __init__(self, parent, text):
        super(FanYiWindow, self).__init__(parent, text, maxLength=100)


class MainFrame(wx.Frame):  # 主窗口
    def __init__(self, image):
        super(MainFrame, self).__init__(parent=None, title='百度翻译', id=wx.ID_ANY, size=(400, 300),
                                        style=wx.DEFAULT_FRAME_STYLE, )
        self.setting_exit_id = wx.NewIdRef()  # 创建id
        self.setting_copy_id = wx.NewIdRef()
        self.setting_play_id = wx.NewIdRef()
        self.about_id = wx.NewIdRef()
        self.help_id = wx.NewIdRef()
        self.hot_key = wx.NewIdRef()
        
        self.mark = False
        self.task_bar_icon = TaskBarIcon(self)  # 创建系统托盘
        self.CreateStatusBar(number=1, style=wx.STB_DEFAULT_STYLE, id=0, name="status_bar")  # 创建状态栏
        self.StatusBar.SetStatusText(text="作者：LMX; 博客：https://blog.csdn.net/hskjshs?spm=1011.2124.3001.5343", i=0)  # 设置状态栏
        self.SetIcon(wx.Icon('images/ico/tubiao.ico', wx.BITMAP_TYPE_ICO))  # 设置图标
        menu_bar = wx.MenuBar(style=wx.SIMPLE_BORDER)  # 创建菜单栏
        self.SetMenuBar(menu_bar)  # 设置菜单栏
        self.RegisterHotKey(self.hot_key, wx.MOD_ALT, 0)
        temp = image.ConvertToBitmap()
        self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)
     
        # 菜单设置
        menu_setting = wx.Menu(style=wx.MENU_TEAROFF)
        menu_setting.Append(self.setting_play_id, '播放')
        menu_setting.Append(self.setting_copy_id, '复制')
        menu_setting.Append(self.setting_exit_id, '退出')
        
        menu_setting.SetHelpString(self.setting_exit_id, '退出程序')
        menu_setting.SetHelpString(self.setting_copy_id, '复制翻译结果到剪贴板')
        menu_setting.SetHelpString(self.setting_play_id, '播放每日一句音频')
        menu_bar.Append(menu_setting, title='设置')
        # 菜单关于
        menu_about = wx.Menu(style=wx.MENU_TEAROFF)
        menu_about.Append(self.about_id, '关于')
        menu_bar.Append(menu_about, title='关于')
        # 菜单帮助
        menu_help = wx.Menu(style=wx.MENU_TEAROFF)
        menu_help.Append(self.help_id, '帮助')
        menu_bar.Append(menu_help, title='帮助')
        # 绑定事件
        self.Bind(wx.EVT_CLOSE, self.Close)
        self.Bind(wx.EVT_ICONIZE, self.OnIconfiy)
        self.Bind(wx.EVT_HOTKEY, self.hotkey_down, id=self.hot_key)
        # 绑定菜单事件
        self.Bind(wx.EVT_MENU, self.play, self.setting_play_id)
        self.Bind(wx.EVT_MENU, self.copy,self.setting_copy_id)
        self.Bind(wx.EVT_MENU, self.CloseFram, self.setting_exit_id)
        self.Bind(wx.EVT_MENU, self.help,self.help_id)
        self.Bind(wx.EVT_MENU, self.about, self.about_id)
    
    # 设置功能
    def play(self, event):
        function.music_play()
    
    def OnIconfiy(self, event):  # 最小化
        self.Hide()
        
    def Close(self, force=False):
        self.Hide()
        
    def CloseFram(self,event):  # 关闭程序
        self.task_bar_icon.Destroy()
        self.Destroy()
        
    def copy(self, event):
        #pyperclip.paste()
        answer = wx.MessageBox('是否将翻译结果复制到剪贴板', '复制', wx.CANCEL)
        if answer == 4:
            self.mark = True
        else:
            self.mark = False
            
    def about(self, event):
        wx.MessageBox('基于百度翻译API的翻译程序', '关于')
        
    def help(self, event):
        message = """使用说明：
                    鼠标选中内容，
                    按ALT键显示翻译窗口。
        """
        wx.MessageBox(message, '帮助', style=wx.OK)

    def hotkey_down(self, event):
        pyautogui.hotkey('ctrl','c')
        shuchu = response.fanyi(pyperclip.paste())
        if self.mark:
            pyperclip.copy(shuchu)
        FanYiWindow(self, shuchu[1:])


class app(wx.App):
    def OnInit(self):
        image = wx.Image("images/index/index.jpg", wx.BITMAP_TYPE_JPEG)
        self.main_window = MainFrame(image)
        self.main_window.SetMaxSize((540,800))  # 固定窗口大小
        self.main_window.SetMinSize((540,800))
        self.main_window.Center()
        self.main_window.Show()
        
        return True


def run():
    sentence.load_sentence()  # 加载资源
    function.load_image()
    function.load_music()
    appA = app()
    appA.MainLoop()
   
    
run()