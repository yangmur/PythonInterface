#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class NewsUpdate(object):
    
    url = "http://open.aliwap.cn:8000/news/update"

    # �޸����ţ��������
    def test_1(self):
        param = {"id":"24", "title":"���Բ���12","username":"18067951267","content":"���Բ���","keywords":"����","description":"test"}
        pic = {"thumb":"F:\\aaa.jpg"}
        times = ""
        result = {"status": 10000, "data": 1}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # �޸����ţ���ɾ������
    def test_2(self):
        param = {"id":"27", "title":"���Բ���13","username":"18067951267","content":"���Բ���","keywords":"����","description":"test"}
        pic = {"thumb":"F:\\aaa.jpg"}
        times = ""
        result = {"status": 10000, "data": 1}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # �޸����ţ�ʡ��δ�޸��ֶ�
    def test_3(self):
        param = {"id":"29", "title":"���Բ���13"}
        pic = {}
        times = ""
        result = {"status": "1004", "message": "��������"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    