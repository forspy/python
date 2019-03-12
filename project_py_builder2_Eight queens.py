# 八皇后问题的游戏规则：1.有n个皇后就是n*n的棋盘2.每个皇后不能在同一行列对角线3.默认从上往下依次放
# 使用元组或列表表示
# state[0]=3 表示第一个皇后在第三列
# conflict函数接收既有皇后的位置，并确定下一个皇后的位置是否会导致冲突
def conflicts(state, nextX):  # nextX表示列
    nextY = len(state)
    for i in range(nextY):  # nextY表示行
        if abs(state[i] - nextX) in (0, nextY - i):
            # 1.当位于同一列时abs(state[i] - nextX)==0 表达式为真
            # 2.nextY - i表示行之差如果等于列之差abs(state[i] - nextX)就可视为在对角线上
            return True
    return False  # 表示没有发生冲突


if 2 in (0, 3):  # 测试，注意2 不在这个元组里
    print('ok')


# def queens(num=8, state=()):  # num为皇后的总数，state是一个元组，包含已经放好的皇后的位置比如state[0]=1 state[1]=3 state[2]=0 即(1,3,0)
#     if len(state) == num - 1:  # 表示如果是当前最后一个皇后还没有放置
#         for posX in range(num):  # 0-(num-1)
#             if not conflicts(state, posX):
#                 yield posX
#     else:
#         for posX in range(num):
#             if not conflicts(state, posX):
#                 for result in queens(num, state + (posX,)):
#                     yield (posX,) + result

def queens(num=8, state=()):
    for posX in range(num):
        if not conflicts(state, posX):
            if len(state) == num - 1:  # 如果是最后一个皇后
                yield (posX,)  # 返回所有元组
            else:
                for result in queens(num, state + (posX,)):
                    yield (posX,) + result


for i in range(3):  # 测试
    print('测试', i)

print('测试', list(queens(4)))
print('有{}种解'.format(len(list(queens(6)))))  # 6皇后为什么解反而少了？


# 可视化显示
def prettyprint(solution):
    def line(posX, length=len(solution)):
        return '. ' * posX + 'X ' + '. ' * (length - posX - 1)

    for posX in solution:
        print(line(posX))


import random

prettyprint(random.choice(list(queens(8))))  # 随机输出一个
# 核心的问题就是回溯尝试
