#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class CtedsCertificationInfo(object):

    url = "http://open.aliwap.cn:8000/cteds/certification/info"

    # ʵ����֤��ϸ���������
    def test_1(self):
        param = {"id":"1588"}
        pic = {}
        times = {}
        result = {"status": 10000}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ʵ����֤��ϸ��idΪ��
    def test_2(self):
        param = {"id":""}
        pic = {}
        times = {}
        result = {"status": 10000}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    