#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class NewsDelete(object):
    
    url = "http://open.aliwap.cn:8000/news/delete"

    # ɾ�����ţ��������
    def test_1(self):
        param = {"id":"27"}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ɾ�����ţ���ɾ��
    def test_2(self):
        param = {"id":"27"}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ɾ�����ţ�id������
    def test_3(self):
        param = {"id":"10000"}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ɾ�����ţ�idΪ��
    def test_4(self):
        param = {"id":""}
        pic = ""
        times = ""
        result = {"status": "1004", "message": "��������"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
