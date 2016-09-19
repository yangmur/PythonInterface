#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class CtedsDevelopmentGet(object):
    
    url = "http://open.aliwap.cn:8000/cteds/development/get"
    
    # ��ȡ����ָ����Ϣ    ���������
    def test_1(self):
        param = {"county_id":"2"}
        pic = ""
        times = ""
        result = {}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ��ȡ����ָ����Ϣ    ��idΪ��
    def test_2(self):
        param = {"county_id":""}
        pic = ""
        times = ""
        result = {"status": 10000, "data": {"status": 11000}}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData