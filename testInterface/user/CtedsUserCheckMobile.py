#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class CtedsUserCheckMobile(object):
    
    url = "http://open.aliwap.cn:8000/cteds/user/check/mobile"

    # �ֻ���У�飬δע���ֻ���
    def test_1(self):
        param = {"phone":"13486119817"}
        pic = ""
        times = ""
        result =  {"status": 10000, "data": {"msg": "", "recode": "1", "is_lost": "0", "ret": "0"}}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # �ֻ���У�飬��ע���ֻ���
    def test_2(self):
        param = {"phone":"11111111111"}
        pic = ""
        times = ""
        result = {"status": "1004", "message": "�����ֻ�����"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # �ֻ���У�飬�ֻ����д�������
    def test_3(self):
        param = {"phone":"1111A111111"}
        pic = ""
        times = ""
        result = {"status": "1004", "message": "�����ֻ�����"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # �ֻ���У�飬�ֻ����д�������
    def test_4(self):
        param = {"phone":"1111��111111"}
        pic = ""
        times = ""
        result = {"status": "1004", "message": "�����ֻ�����"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # �ֻ���У�飬�ֻ���Ϊ��
    def test_5(self):
        param = {"phone":""}
        pic = ""
        times = ""
        result = {"status": "1004", "message": "��������"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    