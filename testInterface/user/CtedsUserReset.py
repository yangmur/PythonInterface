#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *


class CtedsUserReset(object):
    
    url = "http://open.aliwap.cn:8000/cteds/user/reset"

    # �������룬�������
    def test_1(self):
        param = {"phone":"18067951267","password":"123456"}
        pic = ""
        times = ""
        result = {"status": 10000, "data": {"is_lost": 0, "ret": 0}}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # �������룬����Ϊ��
    def test_2(self):
        param = {"phone":"18067951267","password":""}
        pic = ""
        times = ""
        result = {"status": 10000, "data": {"msg": "��������ȷ", "is_lost": 0, "ret": 1}}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # �������룬�ֻ��������
    def test_3(self):
        param = {"phone":"4412","password":"123456"}
        pic = ""
        times = ""
        result = {"status": 10000, "data": {"msg": "δע�����ֻ���", "is_lost": 0, "ret": 1}}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    