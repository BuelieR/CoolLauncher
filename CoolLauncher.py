import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
import runtime_libs.DataGet as DataGet

class mainWindows:
    def __init__(self) -> None:
        self.lang = DataGet.DataGet("lang").get_launcher_data()["url"]
        self.mainWindows = tk.Tk()
        self.mainWindows.title(
            DataGet.DataGet(
                "mainWindows.title"
            ).get_launcher_data(
                f"runtime_res/lang/{self.lang}.json"
            )["url"]
        )

        # 注册自定义字体
        try:
            import os
            from tkinter import font
            font_path = os.path.join(os.path.dirname(__file__), "runtime_res", "font", "XiangLiFangHeiTi.ttf")
            if os.path.exists(font_path):
                font.Font(family="XiangLiFangHeiTi", file=font_path, size=12, weight="bold")
        except Exception as e:
            pass

        #启动时居中显示
        self.center_window(960, 540)

    def center_window(self, width:int=1280, height:int=720):
        #获取屏幕尺寸
        screenwidth = self.mainWindows.winfo_screenwidth()
        screenheight = self.mainWindows.winfo_screenheight()

        #计算窗口居中显示的参数
        size = '%dx%d+%d+%d' % (
            width, height, (screenwidth - width) / 2, 
            (screenheight - height) / 2
        )

        #设置窗口居中显示
        self.mainWindows.geometry(size)

    def ttk_style(self):
        pass

    def left_menu(self):
        #左侧边栏
        left_menu = tk.Frame(
            self.mainWindows, 
            width=200, height=540, 
            bg="#f0f0f0"
        )
        # 显示用户信息
        user_info = tk.Label(
            left_menu, 
            text="用户：" + 
            DataGet.DataGet("user").get_launcher_data()["url"]["name"], 
            bg="#f0f0f0")
        user_info.pack(pady=20)


        left_menu.place(x=0, y=0)

    def startGame(self):
        self.style = ttk.Style()
        # 设置按钮样式为原生Win10样式，保留大小设置
        self.style.configure(
            "Custom.TButton", 
            padding=(30, 15),  # 使用padding来控制按钮大小
            font=('XiangLiFangHeiTi', 16, 'bold')
        )
        
        start_btn = tk.ttk.Button(
            self.mainWindows,
            text=f"{DataGet.DataGet(
                "mainWindows.start_btn"
            ).get_launcher_data(
                f"runtime_res/lang/{self.lang}.json"
            )["url"]}",
            style="Custom.TButton",
        )
        
        start_btn.place(relx=1, rely=1, anchor="se")# 最下居右

    def showWindows(self):
        self.mainWindows.mainloop()

if __name__ == "__main__":
    app = mainWindows()
    app.left_menu()
    app.startGame()
    app.showWindows()