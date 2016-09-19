#coding=gbk
from tools.MySQL import *
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *
from testInterface.user.CtedsUserLogin import *

class CtedsUserCertification(object):
    
    url = "http://open.aliwap.cn:8000/cteds/user/certification"
    siteid = "1"

    # ʵ����֤��δ�ύ���˺�
    def test_1(self):
        param = {"truename":"aaa","idcard":"330106198706022014","uid":"","siteid":""}
        param["siteid"] = self.siteid
        param["uid"], self.header["token"] = self.init()
        pic = {"faceImg":"F:\\aaa.jpg","backImg":"F:\\aaa.jpg"}
        times = ""
        result = {"status": 10000, "data": {"correct": {"message": "ʵ����֤�ύ�ɹ���", "code": "200"}}}
        MySQL().ExecNonQuery("edusohodb", "UPDATE user SET approvalStatus = 'unapprove' WHERE id ="+ param["uid"])
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ʵ����֤��������˺�
    def test_2(self):
        param = {"truename":"bbb","idcard":"330106198706022014","uid":"","siteid":""}
        param["siteid"] = self.siteid
        param["uid"], self.header["token"] = self.init()
        self.init()
        pic = {"faceImg":"F:\\aaa.jpg","backImg":"F:\\aaa.jpg"}
        times = ""
        result = {"status": "10005", "message": "�û���ͨ��ʵ����֤���������"}
        MySQL().ExecNonQuery("edusohodb", "UPDATE user SET approvalStatus = 'approving' WHERE id ="+ param["uid"])
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ʵ����֤�����ʧ���˺�
    def test_3  (self):
        param = {"truename":"bbb","idcard":"330106198706022014","uid":"","siteid":""}
        param["siteid"] = self.siteid
        param["uid"], self.header["token"] = self.init()
        self.init()
        pic = {"faceImg":"F:\\aaa.jpg","backImg":"F:\\aaa.jpg"}
        times = ""
        result = {"status": 10000, "data": {"correct": {"message": "ʵ����֤�ύ�ɹ���", "code": "200"}}}
        MySQL().ExecNonQuery("edusohodb", "UPDATE user SET approvalStatus = 'approve_fail' WHERE id ="+ param["uid"])
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ʵ����֤�����ͨ���˺�
    def test_4  (self):
        param = {"truename":"bbb","idcard":"330106198706022014","uid":"","siteid":""}
        param["siteid"] = self.siteid
        param["uid"], self.header["token"] = self.init()
        self.init()
        pic = {"faceImg":"F:\\aaa.jpg","backImg":"F:\\aaa.jpg"}
        times = ""
        result = rs= {"status": "10005", "message": "�û���ͨ��ʵ����֤���������"}
        MySQL().ExecNonQuery("edusohodb", "UPDATE user SET approvalStatus = 'approved' WHERE id ="+ param["uid"])
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ʵ����֤����ʵ����Ϊ��
    def test_5  (self):
        param = {"truename":"","idcard":"330106198706022014","uid":"","siteid":""}
        param["siteid"] = self.siteid
        param["uid"], self.header["token"] = self.init()
        self.init()
        pic = {"faceImg":"F:\\aaa.jpg","backImg":"F:\\aaa.jpg"}
        times = ""
        result = {"status": "10005", "message": "�û���ͨ��ʵ����֤���������"}
        MySQL().ExecNonQuery("edusohodb", "UPDATE user SET approvalStatus = 'unapprove' WHERE id ="+ param["uid"])
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ʵ����֤�����֤Ϊ��
    def test_6  (self):
        param = {"truename":"bbbb","idcard":"","uid":"","siteid":""}
        param["siteid"] = self.siteid
        param["uid"], self.header["token"] = self.init()
        self.init()
        pic = {"faceImg":"F:\\aaa.jpg","backImg":"F:\\aaa.jpg"}
        times = ""
        result = {"status": "10005", "message": "�û���ͨ��ʵ����֤���������"}
        MySQL().ExecNonQuery("edusohodb", "UPDATE user SET approvalStatus = 'unapprove' WHERE id ="+ param["uid"])
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ʵ����֤�����֤ͼƬΪ��
    def test_7  (self):
        param = {"truename":"bbb","idcard":"330106198706022014","uid":"","siteid":""}
        param["siteid"] = self.siteid
        param["uid"], self.header["token"] = self.init()
        self.init()
        pic = {}
        times = ""
        result = {"status": "10006", "message": "���֤ɨ��������ϴ���������"}
        MySQL().ExecNonQuery("edusohodb", "UPDATE user SET approvalStatus = 'unapprove' WHERE id ="+ param["uid"])
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    def init(self):
        param = {"username":"18067951267","password":"123456"}
        pic = ""
        times = ""
        result = Post().post(CtedsUserLogin.url, MakeParams().makeParams(param, pic, times), self.header, "multipart/form-data")
        return result["data"]["user"]["id"], result["data"]["token"]
