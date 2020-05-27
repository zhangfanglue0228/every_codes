from operator import attrgetter


class State:
    def __init__(self, m, c, b):
        self.m = m  # 左岸传教士数量
        self.c = c  # 左岸野人数量
        self.b = b  # 船的状态；b = 1: 船在左岸；b = 0: 船在右岸
        self.g = 0  # 节点深度
        self.f = 0  # f = g + h, 启发式函数的值
        self.father = None  # 当前节点的父节点
        self.node = [m, c, b]  # 以列表的形式记录传教士、野人、船的状态，优化输出形式


def safe(s):
    """岸边非法情况判断"""
    if (
        s.m > M
        or s.m < 0
        or s.c > C
        or s.c < 0
        or (s.m != 0 and s.m < s.c)  # 左岸传道士数量小于野人数量
        or (s.m != M and M - s.m < C - s.c)  # 右岸传道士数量小于野人数量
    ):
        return False
    else:
        return True


def h(s):
    """启发函数"""
    return s.m + s.c - K * s.b
    # return M - s.m + C - s.c


def back(new, s):
    """判断new节点与其祖父节点状态是否一致"""
    if s.father is None:
        return False
    return new.node == s.father.node


def open_sort(l):
    """将列表l以其中元素的某一属性进行排序"""
    l.sort(key=attrgetter("f"))  # 指定属性排序的key


def in_list(new, l):
    """扩展节点时在open表和closed表中找原来是否存在相同属性的节点"""
    for item in l:
        if new.node == item.node:
            return True, item
    return False, None


def A_star(s):
    open_list = [s]
    closed_list = []  # 记录已经遍历过的状态
    while open_list:  # open表非空
        get = open_list.pop(0)  # 取出open表第一个元素get，分析get拓展出的状态
        if get.node == goal.node:  # 判断是否为目标节点
            return get
        
        closed_list.append(get)  # 将get加入closed表

        # 以下得到一个get的新子节点new并考虑是否放入openlist
        for i in range(M + 1):  # 上船传教士
            for j in range(C + 1):  # 上船野人
                # 船上非法情况
                if i + j == 0 or i + j > K or (i != 0 and i < j):
                    continue

                if get.b == 1:  # 此时船在左岸，下一状态统计船在右岸的情况
                    new = State(get.m - i, get.c - j, 0)
                else:  # 此时船在右岸，下一状态统计船在左岸的情况
                    new = State(get.m + i, get.c + j, 1)

                if in_list(new, closed_list)[0]:
                    # 若产出的新状态已经出现过
                    continue

                if not safe(new) or back(new, get):
                    # 如果状态不安全或者要拓展的节点与当前节点的父节点状态一致，则跳过该状态。
                    continue
                # 如果要拓展的节点满足以上情况，将它的父亲设为当前节点，计算f，并对open_list排序
                else:
                    new.father = get
                    new.g = get.g + 1  # 与起点的距离
                    new.f = get.g + h(get)  # f = g + h 更新新节点的h值

                    # 如果new在open表中
                    if in_list(new, open_list)[0]:
                        old = in_list(new, open_list)[1]
                        if new.f < old.f:  # new的f < open表相同状态的f，替换为f值小的节点状态
                            open_list.remove(old)
                            open_list.append(new)
                    else:
                        open_list.append(new)
                    open_sort(open_list)
    return False


def printPath(f, M, C, K):
    """递归打印路径"""
    if f.father is None:
        return
    printPath(f.father, M, C, K)
    # print()语句放在递归语句后，实现倒序输出
    tem1 = [M, C, 1]
    tem2 = [f.node, []]
    for i in range(len(f.node)):
        tem2[1].append(tem1[i] - f.node[i])
    tem2.append(str(abs(sum(f.node) - sum(f.father.node)) - 1))
    print(*tem2, sep="   |   ")


if __name__ == "__main__":
    M, C, K = map(int, input("输入传教士、野人、船的容量:").split())
    init = State(M, C, 1)  # 初始节点
    goal = State(0, 0, 0)  # 目标
    print("有%d个传教士，%d个野人，船容量:%d" % (M, C, K))
    final = A_star(init)
    if final:
        print("有解，解为：")
        printPath(final, M, C, K)
    else:
        print("无解！")
