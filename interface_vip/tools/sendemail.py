import smtplib
from email.header import Header
from email.mime import text
from email.mime.text import MIMEText

from requestcommon.configcommon import emailhost, ports, senders, password, receivers,msgto
from tools.log import logger


class sendmail:
    def send_mail(self, path):
        logger.info("测试报告邮件开始发送流程。。。。。。。。。。。。。")

        logger.info("测试报告邮件读取生成html报告页面")
        try:
            logger.info("测试报告邮件开始打开html文档。。。")
            f = open(path, 'rb')
            logger.info("测试报告邮件开始读取html文档。。。")
            mail_body = f.read()

            f.close()
            logger.info("测试报告邮件读取邮件发送配置。。。")
            host = emailhost
            # 设置发件服务器地址
            port = ports
            # 设置发件服务器端口号。注意，这里有SSL和非SSL两种形式，现在一般是SSL方式
            sender = senders
            # 设置发件邮箱，一定要自己注册的邮箱
            pwd = password
            # 设置发件邮箱的授权码密码，根据163邮箱提示，登录第三方邮件客户端需要授权码
            receiver = receivers
            # 设置邮件接收人，可以是QQ邮箱
            # 设置邮件正文，这里是支持HTML的
            msg = MIMEText(mail_body, "HTML", "utf-8")
            # 设置正文为符合邮件格式的HTML内容
            msg['subject'] = '自动化测试报告'
            # 设置邮件标题
            msg['from'] = sender
            # 设置发送人
            msg['to'] = msgto
            # 设置接收人

            s = smtplib.SMTP_SSL(host, port)
            # 注意！如果是使用SSL端口，这里就要改为SMTP_SSL
            logger.info("测试报告邮件登录smtp。。。")
            s.login(sender, pwd)
            # 登陆邮箱
            logger.info("测试报告邮件开始发邮件。。。")
            s.sendmail(sender, receiver.split(","), msg.as_string())
            # 发送邮件！
            print('Done.sent email success')
            logger.info("测试报告邮件发送成功。。")
        except Exception as e:
            print('Error.sent email fail')
            logger.info("测试报告邮件发送失败。。原因：s%", e)
