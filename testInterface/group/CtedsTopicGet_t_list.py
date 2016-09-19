#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class CtedsTopicGet_t_list(object):
    
    url = "http://open.aliwap.cn:8000/cteds/topic/get_t_info"

    # ������Ϣ��������ȡ
    def test_1(self):
        param = {"tid":"233"}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ������Ϣ������idΪ��
    def test_2(self):
        param = {"tid":""}
        pic = ""
        times = ""
        result = {"status":"1004","msg":"��������"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ������Ϣ�������ѱ�ɾ��
    def test_3(self):
        param = {"tid":"234"}
        pic = ""
        times = ""
        result = {"status":"1004","msg":"������ɾ��"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ������Ϣ�����Ӳ�����
    def test_4(self):
        param = {"tid":"123456"}
        pic = ""
        times = ""
        result = {"status":"1004","msg":"���Ӳ�����"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    