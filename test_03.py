import unittest
from login_tes import userlogin


class Test_login(unittest.TestCase):
    lis = [('登录失败', 'adin', '12456'), ('用户名不能为空', 'admin', '123456'), ('密码不能为空', 'admin', '')]

    @parameterized.expand(lis)
    def test_login(self, expect, username, password):
        self.assertEqual(expect, userlogin(username, password))

    # def test_login1(self):
    #     print('开始执行用例1')
    #     self.assertEqual('登录失败',userlogin('adin' , '12456'))

    # def test_login2(self):
    #     print('开始执行用例2')
    #     self.assertEqual('用户名不能为空',userlogin('d', '123456'))

    # def test_login3(self):
    #     print('开始执行用例3')
    #     self.assertEqual('密码不能为空',userlogin('admin',' '))

    # def test_login4(self):
    #     print('开始执行用例4')
    #     self.assertEqual('用户名错误',userlogin('ad', '123456'))