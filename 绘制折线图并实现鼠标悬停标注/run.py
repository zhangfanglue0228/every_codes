import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca()
x = np.arange(0, 2 * np.pi, 0.01)
y = np.sin(x)
sinCurve, = plt.plot(x, y,  # 绘图数据
                     picker=3)  # 鼠标距离曲线3像素可识别
annot = ax.annotate("",
                    xy=(0, 0),  # 标注箭头位置
                    xytext=(-50, 50),  # 标注文本位置偏移量
                    textcoords="offset pixels",  # 偏移量单位（像素）
                    bbox={'boxstyle': "round",  # 圆角
                          'fc': "r"},  # 红色背景
                    arrowprops={'arrowstyle': "->"})  # 箭头形状
annot.set_visible(False)


def onMotion(event):
    # 获取鼠标位置和标注可见性
    x = event.xdata
    y = event.ydata
    visible = annot.get_visible()

    if event.inaxes == ax:
        # 测试鼠标事件是否发生在曲线上
        contain, _ = sinCurve.contains(event)
        if contain:
            # 设置标注的重点和文本位置，设置标注可见
            annot.set_visible(True)  # 设置标注可见
            annot.xy = (x, y)
            annot.set_text(str(y))  # 设置标注文本
        else:
            # 鼠标不在曲线附近，设置标注为不可见
            if visible:
                annot.set_visible(False)
        event.canvas.draw_idle()


def onEnter(event):
    # 鼠标进入时修改轴的颜色
    event.inaxes.patch.set_facecolor('yellow')
    event.canvas.draw_idle()


def onLeave(event):
    # 鼠标离开时恢复轴的颜色
    event.inaxes.patch.set_facecolor('white')
    event.canvas.draw_idle()


# 绑定鼠标事件和对应函数
fig.canvas.mpl_connect('motion_notify_event', onMotion)
fig.canvas.mpl_connect('axes_enter_event', onEnter)
fig.canvas.mpl_connect('axes_leave_event', onLeave)
plt.show()
