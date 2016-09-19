#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class NewsInsert(object):  
    url = "http://open.aliwap.cn:8000/news/insert"

    # ������ţ��������
    def test_1(self):
        param = {"title":"���Բ���11","username":"18067951267","content":"���Բ���","keywords":"����","description":"test"}
        pic = {"thumb":"F:\\aaa.jpg"}
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ������ţ��������������д�ͼƬ
#     def test_2(self):
#         content = "����  &lt;/p&gt;&lt;p style=&quot;text-align: center;&quot;&gt;&lt;img alt=&quot;\&quot; src=&quot;http://news.edianshang.com/uploadfile/2016/0511/20160511092607215.jpg&quot;/&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;����"
#         param = {"title":"���Բ���12","username":"18067951267","keywords":"����","description":"test"}
#         param["content"] = content 
#         pic = {"thumb":"F:\\aaa.jpg"}
#         times = ""
#         result = {"status":"10000"}
#         detailedData = NewsInsert().Implementation(param, pic, times, result)
#         return detailedData

    # ������ţ�����100������
    def test_3(self):
        title = ""
        for i in range(50):
            title = title + "����"
        param = {"title":"���Բ���11","username":"18067951267","content":"���Բ���","keywords":"����","description":"test"}
        param["title"] = title 
        pic = {"thumb":"F:\\aaa.jpg"}
        times = ""
        result = {"status": "10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ������ţ�����60������,����Χ
    def test_4(self):
        title = ""
        for i in range(30):
            title = title + "����"
        param = {"title":"���Բ���11","username":"18067951267","content":"���Բ���","keywords":"����","description":"test"}
        param["title"] = title 
        pic = {"thumb":"F:\\aaa.jpg"}
        times = ""
        result = {"status": "1004", "message": "[title] This value is too long. It should have 60 characters or less."}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ������ţ���������Ϊ��
    def test_5(self):
        param = {"title":"���Բ���11","username":"18067951267","content":"","keywords":"����","description":"test"}
        pic = {"thumb":"F:\\aaa.jpg"}
        times = ""
        result = {"status": "1004", "message": "[content] ���ݲ���Ϊ��"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ������ţ�����ʹ�ÿո�
    def test_6(self):
        param = {"title":"          ","username":"18067951267","content":"���Բ���","keywords":"����","description":"test"}
        pic = {"thumb":"F:\\aaa.jpg"}
        times = ""
        result = {"status": "1004", "message": "[title] This value should not be null."}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ������ţ��ؼ���Ϊ��
    def test_7(self):
        param = {"title":"���Բ���11","username":"18067951267","content":"���Բ���","keywords":"","description":"test"}
        pic = {"thumb":"F:\\aaa.jpg"}
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ������ţ��ؼ���100��
    def test_8(self):
        keywords = "aaa"
        for i in range(12):
            keywords = keywords+"��"+"".join(random.sample('0123456789abcdef', random.randint(1,5)))
        param = {"title":"���Բ���11","username":"18067951267","content":"���Բ���","keywords":"����","description":"test"}
        param["keywords"] = keywords
        pic = {"thumb":"F:\\aaa.jpg"}
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
     
    # ������ţ������ؼ���15����
    def test_9(self):
        param = {"title":"���Բ���11","username":"18067951267","content":"���Բ���","keywords":"aaasssdddfffggg","description":"test"}
        pic = {"thumb":"F:\\aaa.jpg"}
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ������ţ�ժҪ����Ϊ��
    def test_10(self):
        param = {"title":"���Բ���11","username":"18067951267","content":"���Բ���","keywords":"����","description":""}
        pic = {"thumb":"F:\\aaa.jpg"}
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ������ţ�ժҪ����250�ַ�
    def test_11(self):
        description = ""
        for i in range(250):
            description = description+"".join(random.sample('0123456789abcdef', 1))
        param = {"title":"���Բ���11","username":"18067951267","content":"���Բ���","keywords":"����","description":""}
        param["description"] = description
        pic = {"thumb":"F:\\aaa.jpg"}
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ������ţ�ժҪ����251�ַ�,�������
    def test_12(self):
        description = ""
        for i in range(271):
            description = description+"".join(random.sample('0123456789abcdef', 1))
        param = {"title":"���Բ���11","username":"18067951267","content":"���Բ���","keywords":"����","description":""}
        param["description"] = description
        pic = {"thumb":"F:\\aaa.jpg"}
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # ������ţ�����ͼƬ
    def test_13(self):
        param = {"title":"���Բ���11","username":"18067951267","content":"���Բ���","keywords":"����","description":"test"}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    