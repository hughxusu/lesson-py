class Ratio(object):
    def __init__(self, value=0):
        self.__value = value    

    @property
    def percent(self):
        return self.__value * 100
           
ratio = Ratio(0.44)
print(f'当前百分比为: {ratio.percent}%')