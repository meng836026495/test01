def assert_login(self,r,status_code=200,msg="操作成功！"):
    # 断言状态响应码是否为200
    self.assertEqual(status_code,r.status_code)

    # 断言返回success
    self.assertTrue(r.json().get("success"))

    # 断言msg
    self.assertEqual(msg,r.json().get("message"))

    # 断言code
    self.assertEqual(10000,r.json().get("code"))