# 来创建一个无穷序列

# 对于一个序列来说，一个索引值对应序列中的一个元素，所以在序列中索引一般是数字（>=0），因此首先需要判定索引的合法性
def check_index(key):
    '''
    键不是整数引发TypeError异常
    键为负数引发IndexError
    '''
    if not isinstance(key, int):
        raise TypeError  # isinstance()来判断一个对象是否是一个已知的类型。 使得返回True
    if key < 0:
        raise IndexError


class ArithmeticSequence:  # 算术序列
    def __init__(self, start=0, step=1):
        '''
        初始化这个算术序列
        :param start: 序列中的第一个值
        :param step: 两个相邻值的差
        '''
        self.start = start
        self.step = step
        self.changed = {}  # changed其实是一个字典

    def __getitem__(self, key):
        '''
        返回一个键对应的值
        :param key:键
        :return: 返回一个值
        '''
        check_index(key)
        try:
            return self.changed[key]  # 如果有这个键值对返回这个值
        except KeyError:  # 没有这个键会抛出错误，则计算这个值，返回
            self.changed[key] = self.start + key * self.step  # 添加这个键值对
            return self.changed[key]

    # 自定义方法 如果不想按照等差序列来构造了，可以尝试自定义修改序列中的值
    def __setitem__(self, key, value):
        check_index(key)
        self.changed[key] = value

    def __delitem__(self, key):
        '''
        删除一个键对应的值
        :param key:
        :return:
        '''
        del self.changed[key]  # 调用del命令

    def __len__(self):
        '''
        要让 len() 函数工作正常，类必须提供一个特殊方法__len__()，它返回元素的个数。
        :return:
        '''
        return len(self.changed)


# 使用这个类实例化一个对象

s = ArithmeticSequence(1, 2)

print(s[4])
s[4] = 2
print(s[4])
del s[4]#删除一个键值对
print(s[4])
print(s[100])
print('键值序列的长度为', len(s))  # 这边len()的长度为什么显示不对，待解决

a = {0: 'bob', 1: 'lucy'}
print(a[0])


