# -*- coding: utf-8 -*-

from JDmiaosha.db_helper import DBHelp
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_email():
    """
    发送电子邮件
    :return:
    """
    db_pro = DBHelp("miaosha")
    db_user = DBHelp("user")
    all_user = db_user.find_many()
    for user in all_user:
        pros = user.get("proinfo")
        user_w = ""
        for p in pros:
            user_pros = db_pro.find_many({"wname":{"$regex":p}})
            if user_pros:
                for i,item in enumerate(user_pros):
                    wname = item.get("wname")
                    wareId = item.get("wareId")
                    jdPrice = item.get("jdPrice")
                    miaoShaPrice = item.get("miaoShaPrice")
                    startTimeShow = item.get("startTimeShow")
                    miaoSha = item.get("miaoSha")
                    user_w += "%s:商品名称:%s,商品价格:%s,秒杀价:%s,开始时间:%s,是否已秒完:%s,商品链接:%s\n" %(i+1,wname,jdPrice,miaoShaPrice,startTimeShow,
                              "手慢可就没有了哦" if miaoSha else "不好意思,来晚了,已秒光","https://item.jd.com/%s.html" % wareId)
        if len(user_w) != 0:
            user_addr = user.get("user_addr")

            # 第三方 SMTP 服务
            mail_host = "smtp.qq.com"
            mail_user = "840181989@qq.com"
            mail_pass = "ehcimqjijlipbbbeaa"

            sender = '840181989@qq.com'
            receivers = user_addr

            message = MIMEText(user_w,'plain','utf-8')
            message['From'] = Header("京东秒杀", 'utf-8')
            message['To'] = Header(user_addr, 'utf-8')

            subject = '您订阅的商品来了'
            message['Subject'] = Header(subject, 'utf-8')

            try:
                smtpObj = smtplib.SMTP_SSL(mail_host, 465)
                smtpObj.login(mail_user, mail_pass)
                smtpObj.sendmail(sender, receivers, message.as_string())
                smtpObj.quit()
                print("邮件发送成功")
            except smtplib.SMTPException as e:
                print(e)

if __name__ == '__main__':
    send_email()
