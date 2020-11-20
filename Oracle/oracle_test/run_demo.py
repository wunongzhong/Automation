#coding=utf-8
'''
1.安装对应的cx_oracle库
2.在python安装目录下找到Lib，site-packages文件夹，放入对应的Oracle执行文件：
oci.dll、oraocci11.dll、oraociei11.dll  注意版本
3、查看服务器端编码
Select userenv('language') from dual;
我实际查到的结果为： AMERICAN_AMERICA.UTF8（每人查到的可能不一样）
4、执行语句 select * from V$NLS_PARAMETERS
查看第一行中PARAMETER项中为NLS_LANGUAGE对应的VALUE项中是否和第一步得到的值一样。
如果不是，需要设置环境变量。
5、设置环境变量
计算机-->属性--> 高级系统设置--> 环境变量 -->系统环境变量-->新建
设置变量名：NLS_LANG
变量值：第1步查到的值，AMERICAN_AMERICA.UTF8(以你第一步查到的为准)
'''

from oracle_test import method_demo
from oracle_test.log_demo import log
log = log()

#单表判断
def liucheng(data):
    log.info('{}表比对开始'.format(data))
    method_demo.find_shuju(data)
    log.info('{}表比对结束'.format(data))

def running():
    with open('test.txt','r') as files:
        for file in files:
            file = file.replace('\n','')
            liucheng(file)

if __name__ == '__main__':
    running()