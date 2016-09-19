#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class CtedsGroupQuit_group(object):
    
    url = "http://open.aliwap.cn:8000/cteds/group/quit_group"

    # �˳�Ȧ�ӣ������˳�
    def test_1(self):
        param = {"gid":"55","uid":"4412"}
        pic = ""
        times = ""
        result = {"status": 10000, "data": {"is_lost": 0, "ret": 0}}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # �˳�Ȧ�ӣ������Ѽ���Ȧ��
    def test_2(self):
        param = {"gid":"55","uid":"4412"}
        pic = ""
        times = ""
        result = {"status":"1004","msg":"������Ȧ����"}
        CtedsGroupQuit_group().Implementation(param, pic, times, result)
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # �˳�Ȧ�ӣ��ѹر�Ȧ��
    def test_3(self):
        param = {"gid":"2","uid":"4412"}
        pic = ""
        times = ""
        result = {"status":"1004","msg":"Ȧ���ѹر�"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # �˳�Ȧ�ӣ�Ȧ�Ӳ�����
    def test_4(self):
        param = {"gid":"123456","uid":"4412"}
        pic = ""
        times = ""
        result = {"status": "1003", "message": "Ȧ�Ӳ�����"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # �˳�Ȧ�ӣ�Ȧ��idΪ��
    def test_5(self):
        param = {"gid":"","uid":"4412"}
        pic = ""
        times = ""
        result = {"status": "1004", "message": "��������"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # �˳�Ȧ�ӣ��û�idΪ��
    def test_6(self):
        param = {"gid":"55","uid":""}
        pic = ""
        times = ""
        result = {"status": "1004", "message": "��������"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # �˳�Ȧ�ӣ��û�idΪ�˺�
    def test_7(self):
        param = {"gid":"55","uid":"18067951267"}
        pic = ""
        times = ""
        result = {"status": 10003, "message": "����������û������ڡ�"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
