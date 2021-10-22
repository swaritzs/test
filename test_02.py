import unittest
from login_tes import userlogin

version = 29


class Test_login(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls) ->  None:
    #     print('开始执行测试用例')

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print('测试用例执行完毕')

    # def setUp(self) -> None:
    #     print('初始化方法')

    # def tearDown(self) -> None:
    #     print('清空方法')
    @unittest.skipIf(version <= 30, '大于等于30执行')
    def test_login1(self):
        print('开始执行用例1')
        self.assertEqual('登录失败', userlogin('adin', '12456'))

    def test_login2(self):
        print('开始执行用例2')
        self.assertEqual('用户名不能为空', userlogin('d', '123456'))

    def test_login3(self):
        print('开始执行用例3')
        self.assertEqual('密码不能为空', userlogin('admin', ' '))

    def test_login4(self):
        print('开始执行用例4')
        self.assertEqual('用户名错误', userlogin('ad', '123456'))
