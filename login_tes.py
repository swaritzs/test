def userlogin(username, password):
    if username is None or username == '':
        return '用户名不能为空'

    if password is None or password == '':
        return '密码不能为空'

    if username == 'admin' and password == '123456':
        return '登录成功'
    elif username != 'admin' and password == '123456':
        return '用户名错误'
    elif username == 'admin' and password != '123456':
        return '密码错误'
    else:
        return '登录失败'