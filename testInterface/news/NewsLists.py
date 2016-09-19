#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class NewsLists(object):
    
    url = "http://open.aliwap.cn:8000/news/lists"
    
    # �����б�������ȡ
    def test_1(self):
        param = {"start":"1","type":"1","isid":"","offset":"12"}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # �����б���ȡ������б�Χ
    def test_2(self):
        param = {"start":"1000","type":"1","isid":"","offset":"1006"}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # �����б�ʡ�Խ����ֶ�ֵ
    def test_3(self):
        param = {"start":"1","type":"1","isid":"","offset":""}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # �����б�ʡ�Կ�ʼ�ֶ�ֵ
    def test_4(self):
        param = {"start":"","type":"1","isid":"","offset":"6"}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # �����б���������
    def test_5(self):
        param = {"start":"1","type":"1","isid":"11","offset":"6"}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # �����б����Ͳ����ڻ�ȡ��
    def test_6(self):
        param = {"start":"1","type":"10","isid":"","offset":"6"}
        pic = ""
        times = ""
        result = {"status":"1004","message":"��������"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    