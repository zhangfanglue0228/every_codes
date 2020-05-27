"""
@Author: Zhangfanglue
@Date: 2020-04-15 16:46:47
@Description: 宽度优先搜索解决八数码问题
"""
"""
方向：d:
    0:上 -3
    1:下 +3
    2:左 -1
    3:右 +1

目标状态：'123456780'
"""


move_direction = [-3, 3, -1, 1]  # 方向


def can_move(state, d):
    """判断state状态下，d方向是否可以移动'0'字符"""
    location = 0  # location记录state中'0'的位置
    for s in state:
        if s == "0":
            break
        else:
            location += 1
    if (
        (location < 3 and d == 0)  # '0'在第一行
        or (location > 5 and d == 1)  # '0'在第三行
        or ((location + 3) % 3 == 0 and d == 2)  # '0'在第一列
        or ((location + 1) % 3 == 0 and d == 3)  # '0'在第三列
    ):
        # 返回是否可以移动和'0'的位置
        return False, location
    return True, location


def move(state, location, d):
    list_state = list(state)
    # 转换为list后交换'0'和目标字符的位置
    list_state[location + move_direction[d]], list_state[location] = (
        list_state[location],
        list_state[location + move_direction[d]],
    )
    # 重新恢复为字符串254
    state = "".join(list_state)
    return state


def BFS(before_state, final_state):
    queue = []
    queue.append(before_state)
    step = {before_state: 0}  # 初态步长为0
    seen = set()  # seen集合：存储已出现的状态，判断新状态时候出现
    seen.add(before_state)
    parent = {before_state: None}  # 储存各个状态的前驱状态
    while len(queue) > 0:  # queue不为空时持续搜索
        before_state = queue.pop(0)  # 队列首项pop
        if before_state == final_state:  # 判断状态是否符合期望值
            return step[before_state], parent  # 返回符合时的步长

        for i in range(4):  # 遍历上下左右四个方向移动
            flag, location = can_move(before_state, i)  # 判断移动方向为i时是否可以可以移动
            if flag:
                after_state = move(before_state, location, i)
                if after_state not in seen:  # 如果移动后的状态没有出现过
                    seen.add(after_state)  # 加入seen集合
                    step[after_state] = step[before_state] + 1  # 此状态步长为前态步长+1
                    parent[after_state] = before_state
                    queue.append(after_state)  # 将此状态加入queue
    return False, parent


def get_print_parent(parent, final_state):
    key = final_state
    process = []
    process.append(key)
    while parent[key]:
        process.insert(0, parent[key])
        key = parent[key]
    print(*process, sep=" ---> ")


def main():
    while True:
        original_state = input("Please input original state:")  # 获取初始状态
        final_state = input("Please input final state:")  # 获取目标状态
        step_num, parent = BFS(original_state, final_state)
        if original_state == final_state:
            print("step:0")
        elif step_num:
            print("step:%d" % step_num)
            get_print_parent(parent, final_state)
        elif not step_num:
            print("该种情况没有可以获得目标状态的方法")


if __name__ == "__main__":
    main()
