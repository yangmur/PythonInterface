#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *


class CtedsUserRegister(object):
    
    url = "http://open.aliwap.cn:8000/cteds/user/register"
    
    # ע�ᣬ���ֻ���ע��
    def test_1(self):
        param = {"phone":"13486119817","type":"1","password":"123456"}
        pic = ""
        times = ""
        result = {"ret":"0"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ע�ᣬ��ע���ֻ���ע��
    def test_2(self):
        param = {"phone":"13486119817","type":"1","password":"123456"}
        pic = ""
        times = ""
        result = {"ret":"1","msg":"�ֻ�����ע��"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ע�ᣬ�Ǵ������ֻ���ע��
    def test_3(self):
        param = {"phone":"1111����11111","type":"1","password":"123456"}
        pic = ""
        times = ""
        result = {"ret":"1","msg":"�ֻ��Ÿ�ʽ����"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ע�ᣬ����Ϊ��
    def test_4(self):
        param = {"phone":"13486119819","type":"1","password":""}
        pic = ""
        times = ""
        result = {"ret":"1","msg":"�ֻ�����ע��"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    