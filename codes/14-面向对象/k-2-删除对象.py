class Camera:
    def __init__(self):
        print('1. 使用电脑的摄像头')

    def __del__(self):
        print('4. 关闭电脑的摄像头')
    
my_new_camera = Camera()
print('2. 采集图像')
del my_new_camera
print('3. 处理图像')