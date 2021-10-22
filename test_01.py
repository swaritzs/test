import unittest
from login_tes import userlogin


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

    def test_login1(self):
        print('开始执行用例1')
        self.assertEqual('登录成功', userlogin('admin', '123456'))

    def test_login2(self):
        print('开始执行用例2')
        self.assertEqual('用户名不能为空', userlogin('', '123456'))

    def test_login3(self):
        print('开始执行用例3')
        self.assertEqual('密码不能为空', userlogin('admin', ''))

    def test_login4(self):
        print('开始执行用例4')
        self.assertEqual('用户名错', userlogin('ad', '123456'))

# if __name__ == '__main__':
#     unittest.main()

# SUITE=unittest.TestSuite()

# runner=unittest.TextTestRunner(verbosity=2)

# SUITE.addTest(Test_login('test_login4'))
# SUITE.addTests([Test_login('test_login1'),Test_login('test_login2')])

# runner.run(SUITE)

















