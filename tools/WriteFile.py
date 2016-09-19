#coding=gbk
import time
import os
import xlrd
from xlwt import *
from xlutils.copy import copy
import sys
#stdi,stdo,stde=sys.stdin,sys.stdout,sys.stderr
#reload(sys)
#sys.stdin,sys.stdout,sys.stderr=stdi,stdo,stde
#sys.setdefaultencoding('gb2312')

class WriteFile():
    
    def Createfolder(self):
        #global path
        foldername = time.strftime("%Y%m%d %H%M%S", time.localtime())
        path = os.path.dirname(os.getcwd())+"\\result\\"+foldername
        #print path
        if not os.path.exists(path):
            os.makedirs(path)   
        return path
    
    def WriteTxt(self, path, Total, Sucess, Fail, TotalExecutionTime, MaxTime, MinTime):
        f = open((path+"\\InformationCenter.txt"), "w")
        f.write("�˴β���ִ����ɣ�����\n")
        f.write("������ʱ�䣺"+str(TotalExecutionTime)+"��\n")
        if Total>0:
            avgTime = TotalExecutionTime/Total
        else:
            avgTime = 0
        f.write("ƽ��ÿ����������ʱ�䣺"+str(avgTime)+"��\n")
        f.write("��ִ�в��ԣ�"+str(Total)+"��\n")
        f.write("ִ�гɹ���"+str(Sucess)+"��\n")
        f.write("ִ��ʧ�ܣ�"+str(Fail)+"��\n")
        f.write("�������ʱ�䣺"+str(MaxTime)+"��\n")
        f.write("��С����ʱ�䣺"+str(MinTime)+"��\n")
        f.close()
        
    def WriteXls(self, path, data):
        filepath = path+"\\Detailed.xls"
        if not os.path.exists(filepath):
            #print "����xls"
            f = Workbook()
            sheet = f.add_sheet("sheet1")
            f.save(filepath)
            wb = xlrd.open_workbook(filepath,formatting_info=True)
            ws = copy(wb)
            sheet = ws.get_sheet(0)
            sheet.write(0,0,"Id")
            sheet.write(0,1,"Name")
            sheet.write(0,2,"StartTime")
            sheet.write(0,3,"EndTime")
            sheet.write(0,4,"ExecutionTime")
            sheet.write(0,5,"Result")
            sheet.write(0,6,"ErrorMessage")
            os.remove(filepath)
            ws.save(filepath)  
    
        #print "׷��xls"
        wb = xlrd.open_workbook(filepath,formatting_info=True)
        ws = copy(wb)
        sheet = ws.get_sheet(0)
        nrows = wb.sheet_by_index(0).nrows #ͳ�Ƶ�ǰ�����ж�����
        sheet.write(data["Id"],0,data["Id"])
        sheet.write(data["Id"],1,data["filename"])
        sheet.write(data["Id"],2,data["starttime"])
        sheet.write(data["Id"],3,data["endtime"])
        sheet.write(data["Id"],4,data["executiontime"])
        sheet.write(data["Id"],5,data["result"])
        sheet.write(data["Id"],6,str(data["errormessage"]))
        os.remove(filepath)
        ws.save(filepath)
    

#if __name__ == "__main__":
    #Createfolder()
    #WriteTxt("100","1","1sad")
    #data = {"filename":"1111", "starttime":"asdas", "endtime":"djaskd", "result":"true"}
    #WriteXls(data)

