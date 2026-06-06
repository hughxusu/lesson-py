class Ratio(object):
    def __init__(self, value=0):
        self.__value = value    

    def get_percent(self):
        return self.__value * 100
      
    def set_percent(self, value):
        if value > 100:
            self.__value = 1
        elif value < 0:
            self.__value = 0
        else:
            self.__value = value / 100
        
    def del_percent(self):
        print("删除属性")
        del self.__value

    percent = property(get_percent, set_percent, del_percent)
               
ratio = Ratio()
ratio.percent = 120
print(f'当前百分比为: {ratio.percent}%')
del ratio.percent
