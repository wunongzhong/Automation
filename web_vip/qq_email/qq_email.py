#coding=utf-8
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from log.log import log


message = MIMEMultipart()
# message.attach(MIMEText(open(r'..\test\test_report.html','rb').read(),_subtype='html',_charset='utf-8'))
message.attach(MIMEText(open(r'..\test\demo_03.py','rb').read(),_subtype='plain',_charset='utf-8'))
# message.attach(MIMEText('<html><body><img src="cid:imageid" alt="imageid"></body></html>', 'html', 'utf-8'))
att1=MIMEText(open(r'..\test\demo_03.py',"rb").read(),"base64","utf-8")
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="demo_03.py"'
message.attach(att1)

#发送图片
# file = open("20180819062117.jpg", "rb")
# img_data = file.read()
# file.close()
# img = MIMEImage(img_data)
# img.add_header('Content-ID', 'imageid')
# message.attach(img)

message["From"]=Header("来不及说爱你<766903532@qq.com>","utf-8")
message["To"]=Header("各位领导","utf-8")
message["Subject"]=Header("python 发送带附件邮件","utf-8")

try:
    smtpobj=smtplib.SMTP_SSL(host="smtp.qq.com")
    # 连接smtp服务器
    smtpobj.connect(host="smtp.qq.com", port="465")
    # 用户登录,用户名即为发送者地址，密码不是账号的密码，是授权码
    smtpobj.login(user="766903532@qq.com", password="qihhrmosedrlbfcc")
    sender = "766903532@qq.com"
    receiver = ['508419907@qq.com','673301542@qq.com']
    smtpobj.sendmail(sender,receiver,message.as_string())
    log.info("邮件发送成功")
except smtplib.SMTPException:
    log.info("邮件发送失败")