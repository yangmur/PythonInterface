#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class CtedsUserLogin(object):    
    url = "http://open.aliwap.cn:8000/cteds/user/login"

    # ��¼���˺ź����붼��ȷ
    def test_1(self):
        param = {"username":"18067951267","password":"123456"}
        pic = ""
        times = ""
        result = {"status": 10000}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData

    # ��¼���˺Ų�����
    def test_2(self):
        param = {"username":"1806795126","password":"123456"}
        pic = ""
        times = ""
        result = {"message": "�ʺŻ����벻��ȷ", "name": "username_error"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ��¼���������
    def test_3(self):
        param = {"username":"18067951267","password":"12345"}
        pic = ""
        times = ""
        result = {"message": "�ʺ����벻��ȷ", "name": "password_error"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ��¼������Ϊ��
    def test_4(self):
        param = {"username":"18067951267","password":""}
        pic = ""
        times = ""
        result = {"message": "�ʺ����벻��ȷ", "name": "password_error"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ��¼���˺�Ϊ��
    def test_5(self):
        param = {"username":"","password":"123456"}
        pic = ""
        times = ""
        result = {"message": "�ʺ����벻��ȷ", "name": "password_error"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData