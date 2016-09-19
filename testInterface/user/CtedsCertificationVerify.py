#coding=gbk
from tools.MySQL import *
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class CtedsCertificationVerify(object):
    
    url = "http://open.aliwap.cn:8000/cteds/certification/verify"
    siteid = "1"

    # ʵ����֤��ˣ���˽��Ϊ��
    def test_1(self):
        param = {"id":"1588","form_status":"","note":""}
        param["siteid"] = self.siteid
        pic = {}
        times = {}
        result = {}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ʵ����֤��ˣ���˽��ͨ��
    def test_2(self):
        param = {"id":"1588","form_status":"success","note":""}
        param["siteid"] = self.siteid
        pic = {}
        times = {}
        result = {"status": 10000}
        MySQL().ExecNonQuery("edusohodb", "UPDATE user SET approvalStatus = 'approving' WHERE id = "+param["id"])
        MySQL().ExecNonQuery("edusohodb", "UPDATE user_approval SET status = 'approving' WHERE userId = "+param["id"])
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ʵ����֤��ˣ���˽��ʧ��
    def test_3(self):
        param = {"id":"1588","form_status":"fail","note":""}
        param["siteid"] = self.siteid
        pic = {}
        times = {}
        result = {}
        MySQL().ExecNonQuery("edusohodb", "UPDATE user SET approvalStatus = 'approving' WHERE id = "+param["id"])
        MySQL().ExecNonQuery("edusohodb", "UPDATE user_approval SET status = 'approving' WHERE userId = "+param["id"])
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ʵ����֤��ˣ����ύʧ�ܣ��޸ĳɹ�
    def test_4(self):
        param = {"id":"1588","form_status":"fail","note":""}
        param["siteid"] = self.siteid
        pic = {}
        times = {}
        result = {}
        MySQL().ExecNonQuery("edusohodb", "UPDATE user SET approvalStatus = 'approving' WHERE id = "+param["id"])
        MySQL().ExecNonQuery("edusohodb", "UPDATE user_approval SET status = 'approving' WHERE userId = "+param["id"])
        detailedData = CtedsCertificationVerify().Implementation(param, pic, times, result)
        param = {"id":"1588","form_status":"success","note":""}
        param["siteid"] = self.siteid
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    