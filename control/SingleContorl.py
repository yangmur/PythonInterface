#coding=gbk
import os, time
import glob
import json
import importlib
from tools.WriteFile import *
from tools.ReadFile import *
from testInterface.user.CtedsUserCheckMobile import *
from testInterface.user.CtedsUserRegister import *
from testInterface.user.CtedsUserLogin import *
from testInterface.user.CtedsUserInfo import *
from testInterface.user.CtedsUserReset import *
from testInterface.user.CtedsUserCertification import *
from testInterface.user.CtedsUserSendCode import *
from testInterface.user.CtedsCertificationList import *
from testInterface.user.CtedsCertificationVerify import *
from testInterface.user.CtedsCertificationInfo import *
from testInterface.banner.AdBannerGet_banner_list import *
from testInterface.banner.AdBannerPost_banner_list import *
from testInterface.model_test.NewsLists import *
from testInterface.model_test.NewsListsCount import *
from testInterface.model_test.NewsShow import *
from testInterface.model_test.NewsInsert import *
from testInterface.model_test.NewsDelete import *
from testInterface.model_test.NewsUpdate import *
from testInterface.group.CtedsGroupGet_info import *
from testInterface.group.CtedsGroupJoin_group import *
from testInterface.group.CtedsGroupQuit_group import *
from testInterface.group.CtedsTopicT_list import *
from testInterface.group.CtedsTopicGet_t_list import *
from testInterface.group.CtedsTopicT_add import *
from testInterface.group.CtedsTopicGet_t_posts import *
from testInterface.group.CtedsTopicAdd_t_post import *
from testInterface.development.CtedsDevelopmentGet import *

#��¼���ݳ�ʼ��
total = 0 #�ܴ���
success = 0 #�ɹ�����,ֻ��ִ��ͨ��
fail = 0
maxTime = 0  #����ִ���ʱ��,ֻ��ִ��ͨ������ʱ��
minTime = 99999 #����ִ�����ʱ��,ֻ��ִ��ͨ������ʱ��
totalExecutionTime = 0 #������ʱ��

if __name__ == '__main__':
    #�������Լ�¼�ļ���
    FolderPath = WriteFile().Createfolder()    
    #���ò�����
    detailedData = CtedsTopicT_add().test_7()
    WriteFile().WriteXls(FolderPath, detailedData)
    