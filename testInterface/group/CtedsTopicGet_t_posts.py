#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class CtedsTopicGet_t_posts(object):
    
    url = "http://open.aliwap.cn:8000/cteds/topic/get_t_posts"

    # ��ȡ������������ȡ
    def test_1(self):
        param = {"tid":"237","page":"1","num":"6"}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ��ȡ������ʡ�Բ���
    def test_2(self):
        param = {"tid":"237","page":"","num":""}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
