#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class CtedsTopicAdd_t_post(object):
    
    url = "http://open.aliwap.cn:8000/cteds/topic/add_t_post"

    # ������������ȡ
    def test_1(self):
        param = {"tid":"241","uid":"4412","content":"hdjsajkkdjalksakd"}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ��������������Ϊ��
    def test_2(self):
        param = {"tid":"237","uid":"4412","content":""}
        pic = ""
        times = ""
        result = {"status":"1004","message":"���ݳ��ȴ���"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ��������������С��10����
    def test_3(self):
        param = {"tid":"237","uid":"4412","content":"aaaaa"}
        pic = ""
        times = ""
        result = {"status":"1004","message":"���ݳ��ȴ���"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ����������ɾ��״̬
    def test_4(self):
        param = {"tid":"242","uid":"4412","content":"hdjsajkkdjalksakd"}
        pic = ""
        times = ""
        result = {"status":"1004","message":"�ظ���������ɾ���򲻴���"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # �������������ݴ���700����
    def test_5(self):
        content = ""
        for i in range(150):
            content = content + "���Գ���700��"
        param = {"tid":"242","uid":"4412","content":"hdjsajkkdjalksakd"}
        param["content"] = content
        pic = ""
        times = ""
        result = {"status":"1004","message":"���ݳ��ȴ���"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    