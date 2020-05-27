# 0:由8升容器向3升容器倒啤酒
# 1:由8升容器向5升容器倒啤酒
# 2:由3升容器向8升容器倒啤酒
# 3:由3升容器向5升容器倒啤酒
# 4:由5升容器向8升容器倒啤酒
# 5:由5升容器向3升容器倒啤酒


original_state = [8, 0, 0]
final_state = [4, 4, 0]


def can_pour(state, way):
    if way == 0:
        if (state[2] == 3) or (state[0] == 0):
            return False
        else:
            return True
    if way == 1:
        if (state[1] == 5) or (state[0] == 0):
            return False
        else:
            return True
    if way == 2:
        if (state[0] == 8) or (state[2] == 0):
            return False
        else:
            return True
    if way == 3:
        if (state[1] == 5) or (state[2] == 0):
            return False
        else:
            return True
    if way == 4:
        if (state[0] == 8) or (state[1] == 0):
            return False
        else:
            return True
    if way == 5:
        if (state[2] == 3) or (state[1] == 0):
            return False
        else:
            return True


def pour(state, way):
    temp_state = state[:]
    if way == 0:
        if temp_state[0] > 3 - temp_state[2]:
            temp_state[0] -= 3 - temp_state[2]
            temp_state[2] = 3
        else:
            temp_state[2] += temp_state[0]
            temp_state[0] = 0
    if way == 1:
        if temp_state[0] > 5 - temp_state[1]:
            temp_state[0] -= 5 - temp_state[1]
            temp_state[1] = 5
        else:
            temp_state[1] += temp_state[0]
            temp_state[0] = 0
    if way == 2:
        if temp_state[2] > 8 - temp_state[0]:
            temp_state[2] -= 8 - temp_state[1]
            temp_state[0] = 8
        else:
            temp_state[0] += temp_state[2]
            temp_state[2] = 0
    if way == 3:
        if temp_state[2] > 5 - temp_state[1]:
            temp_state[2] -= 5 - temp_state[1]
            temp_state[1] = 5
        else:
            temp_state[1] += temp_state[2]
            temp_state[2] = 0
    if way == 4:
        if temp_state[1] > 8 - temp_state[0]:
            temp_state[1] -= 8 - temp_state[1]
            temp_state[0] = 8
        else:
            temp_state[0] += temp_state[1]
            temp_state[1] = 0
    if way == 5:
        if temp_state[1] > 3 - temp_state[2]:
            temp_state[1] -= 3 - temp_state[2]
            temp_state[2] = 3
        else:
            temp_state[2] += temp_state[1]
            temp_state[1] = 0
    return temp_state


def change_2_str(state):
    return "".join((str(i) for i in state))


def BFS(state):
    queue = []
    queue.append(state)
    step = {change_2_str(state): 0}
    parent = {change_2_str(state): None}
    seen = set()
    seen.add(change_2_str(state))
    while len(queue) > 0:
        before_state = queue.pop(0)
        if change_2_str(before_state) == "440":
            return step[change_2_str(before_state)], parent

        for i in range(6):
            if can_pour(before_state, i):
                after_state = pour(before_state, i)
                if change_2_str(after_state) not in seen:
                    seen.add(change_2_str(after_state))
                    step[change_2_str(after_state)] = step[change_2_str(before_state)] + 1
                    parent[change_2_str(after_state)] = change_2_str(before_state)
                    queue.append(after_state)
    return -1


def get_print_parent(parent):
    key = "440"
    process = []
    process.append(key)
    while parent[key]:
        process.insert(0, parent[key])
        key = parent[key]
    print(*process, sep=" ---> ")


def main():
    step_num, parent = BFS(original_state)
    print("step:%d" % step_num)
    get_print_parent(parent)


if __name__ == "__main__":
    main()
