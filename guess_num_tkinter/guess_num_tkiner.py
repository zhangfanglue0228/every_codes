import tkinter as tk
import random
import time

from tkinter.simpledialog import askinteger
from tkinter.messagebox import showerror, showinfo


window = tk.Tk()
window.geometry("280x100+400+300")
window.title("tkinter版猜数游戏")
window.resizable(False, False)
window.attributes('-topmost', 1)  #总是在顶端
window.overrideredirect(True)  # 去除标题栏
window.attributes('-alpha', 0.5)  # 半透明


global game_times
global right_times
global x
global y
game_times = 0
right_times = 0


def start_buttom():
    global min_num
    global max_num
    global time_remain
    global num_guess
    global game_times
    min_num = askinteger("允许范围（最小值）", "最小数", initialvalue=1, minvalue=1)
    max_num = askinteger("允许范围（最大值）", "最大数", initialvalue=10, minvalue=10)
    time_remain = askinteger("允许猜测次数", "次数", initialvalue=1, minvalue=1)
    num_guess = random.randint(min_num, max_num)
    s2.set("剩余次数：" + str(time_remain))
    game_times = game_times + 1
    input_frame["state"] = "normal"


def guess_buttom():
    global min_num
    global max_num
    global time_remain
    global num_guess
    global right_times
    try:
        n = int(input_frame.get())
        time_remain = time_remain - 1
        s2.set("剩余次数：" + str(time_remain))
    except:
        showerror("抱歉", "数据输入错误")
        return
    if n == num_guess:
        right_times = right_times + 1
        s1.set("")
        input_frame["state"] = "disabled"
        s2.set("剩余次数：0")
        showinfo("恭喜！", "猜对了")
        return
    elif n > num_guess:
        showinfo("抱歉", "太大了")
    else:
        showinfo("抱歉", "太小了")

    if time_remain == 0:
        showerror("抱歉", "次数用完，游戏结束了，正确的数是" + str(num_guess))
        s1.set("")
        input_frame["state"] = "disabled"
        return


def closeWindow(event):
    message = "共玩游戏{0}次，猜对{1}次！\n欢迎下次再玩"
    message = message.format(game_times, right_times)
    showinfo("战绩", message)
    window.destroy()


def get_time():
    time_s = time.strftime('%Y-%m-%d %H:%M:%S')
    clock_label['text'] = '当前时间: ' + time_s
    window.after(1000, get_time)


def mouse_press(event):
    global x
    global y
    window.attributes('-alpha', 1)  # 不透明
    x = event.x
    y = event.y


def mouse_motion(event):
    window.attributes('-alpha', 1)  # 不透明
    a_x = window.winfo_x() + event.x - x
    a_y = window.winfo_y() + event.y - y
    window.geometry('+%d+%d' % (a_x, a_y))


def mouse_release(event):
    window.attributes('-alpha', 0.5)  # 半透明


text_label = tk.Label(window, text="请输入一个整数")
text_label.place(x=10, y=10, width=100, height=20)

s1 = tk.StringVar(window, value="")
input_frame = tk.Entry(window, width=10, textvariable=s1, state="disabled")
input_frame.place(x=110, y=10)

s2 = tk.StringVar(window, value="剩余次数：0")
time_label = tk.Label(window, textvariable=s2)
time_label.place(x=190, y=10)

clock_label = tk.Label(window)
clock_label.place(x=45, y=70)

game_button = tk.Button(window, text="start game", command=start_buttom)
game_button.place(x=5, y=40, width=125, height=20)
game_button = tk.Button(window, text="guess", command=guess_buttom)
game_button.place(x=150, y=40, width=125, height=20)


window.bind('<ButtonPress-1>', mouse_press)
window.bind('<B1-Motion>', mouse_motion)
window.bind('<ButtonRelease-1>', mouse_release)


clock_label.bind('<Button-3>', closeWindow)  # 鼠标右击时间关闭窗口
get_time()
window.mainloop()
