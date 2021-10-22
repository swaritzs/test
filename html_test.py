import unittest
from HTMLTestRunner import HTMLTestRunner

flname = 'test_report.html'
suite = unittest.TestLoader().discover('.', pattern='test*.py')

with open(flname, 'wb') as f:
    runner = HTMLTestRunner(f, title=('测试报告'), description=('v1.0'))
    runner.run(suite)
