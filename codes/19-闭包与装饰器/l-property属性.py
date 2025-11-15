class Ratio(object):
    def __init__(self):
        self.__value = 0

    @property
    def percent(self):
        return self.__value * 100
      
    @property
    def is_half_percent(self): # 可以添加一系列辅助属性
      	return self.__value >= 0.5
    
    @percent.setter
    def percent(self, value):
        if value > 100:
            self.__value = 1
        elif value < 0:
            self.__value = 0
        else:
            self.__value = value / 100
               
ratio = Ratio()
print(ratio.percent)
ratio.percent = 44
print(ratio.percent)
ratio.percent = 120
print(ratio.percent)