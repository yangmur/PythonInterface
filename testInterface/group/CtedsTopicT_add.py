#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class CtedsTopicT_add(object):
    
    url = "http://open.aliwap.cn:8000/cteds/topic/t_add"

    # �������ӣ���������
    def test_1(self):
        param = {"uid":"4412","name":"�ӿڲ���","gid":"55","message":"asdjksakjdjk"}
        pic = {"pic":"F:\\aaa.jpg"}
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # �������ӣ���������4����
    def test_2(self):
        param = {"uid":"4412","name":"11","gid":"55","message":"asdjksakjdjk"}
        pic = {"pic":"F:\\aaa.jpg"}
        times = ""
        result = {"status": 1004, "message": "���ⳤ�Ȳ���"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # �������ӣ��������25����
    def test_3(self):
        param = {"uid":"4412","name":"�ӿڲ��Խӿڲ��Խӿڲ��Խӿڲ��Խӿڲ��Խӿڲ��Խӿڲ���","gid":"55","message":"asdjksakjdjk"}
        pic = {"pic":"F:\\aaa.jpg"}
        times = ""
        result = {"status": 1004, "message": "���ⳤ�Ȳ���"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # �������ӣ����ݳ���С��10����
    def test_4(self):
        param = {"uid":"4412","name":"�ӿڲ���4","gid":"55","message":"��������������"}
        pic = {"pic":"F:\\aaa.jpg"}
        times = ""
        result = {"status": 1004, "message": "���ݳ��Ȳ���"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # �������ӣ����ݳ��ȴ���700����
    def test_5(self):
        message = ""
        for i in range(150):
            message = message + "���Գ���700��"
        param = {"uid":"4412","name":"�ӿڲ���5","gid":"55","message":"asdjksakjdjk"}
        param["message"] = message
        pic = {"pic":"F:\\aaa.jpg"}
        times = ""
        result = {"status": 1004, "message": "���ݳ��Ȳ���"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # �������ӣ�ͼƬ����
    def test_6(self):
        param = {"uid":"4412","name":"�ӿڲ���6","gid":"55","message":"asdjksakjdjk"}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # �������ӣ��û�id����
    def test_7(self):
        param = {"uid":"13486119817","name":"�ӿڲ���7","gid":"55","message":"asdjksakjdjk"}
        pic = {"pic":"F:\\aaa.jpg"}
        times = ""
        result = {"status": 1004, "message": "�û�δ��¼�򲻴���"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # �������ӣ��û�����ֵ
    def test_8(self):
        param = {"uid":"","name":"�ӿڲ���8","gid":"55","message":"asdjksakjdjk"}
        pic = {"pic":"F:\\aaa.jpg"}
        times = ""
        result = {"status": 1004, "message": "�û�δ��¼�򲻴���"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    