class Ratio(object):
    def __init__(self, value=0):
        self.__value = value    

    @property
    def percent(self):
        return self.__value * 100
      
    @percent.setter 
    def percent(self, value):
        if value > 100:
            self.__value = 1
        elif value < 0:
            self.__value = 0
        else:
            self.__value = value / 100
               
ratio = Ratio()
print(f'当前百分比为: {ratio.percent}%')
ratio.percent = 44
print(f'当前百分比为: {ratio.percent}%')
ratio.percent = 120
print(f'当前百分比为: {ratio.percent}%')
