class Camera:
    def __init__(self):
        print('1. 使用电脑的摄像头')

    def __del__(self):
        print('4. 关闭电脑的摄像头')

    def __str__(self):
        return f'这是一个视频处理程序'
    
my_new_camera = Camera()
print('2. 采集图像')
print('3. 处理图像')