#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class AdBannerPost_banner_list(object):
    
    url = "http://open.aliwap.cn:8000/ad/banner/post_banner_list"

    # ��ȡ���    ���������
    def test_1(self):
        param = {"gid":"55","code":"index-banner"}
        pic = ""
        times = ""
        result = {}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ��ȡ���    ��idΪ��
    def test_2(self):
        param = {"code":""}
        pic = ""
        times = ""
        result = {"status": "10004", "message": "���������޷�ƥ�䡿"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData