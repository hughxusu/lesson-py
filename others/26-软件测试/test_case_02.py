import unittest

class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):   # 所有test运行前运行一次
        print('\n')
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):  # 所有test运行后运行一次
        print("tearDownClass")

    def setUp(self):
        print('\n')
        print('setUp')

    def tearDown(self):
        print('tearDown')

    def test_01(self):
        print('case 01')

    def test_02(self):
        print('case 02')

if __name__ == '__main__':
    unittest.main()