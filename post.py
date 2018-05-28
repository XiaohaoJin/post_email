# coding = 'utf-8'
# 环境：发件人邮箱需要开启SMTP协议

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def how_to_send():
    account = "1234589@qq.com"
    account_password = "**********"   #授权密码，非登录密码
    recevier = ['987654321@qq.com', '098765432@qq.com']

    msg = MIMEText('content', 'plain', 'utf-8')
    msg['Subject'] = 'title'
    msg['From'] = '{}'.format(account)
    msg['To'] = ','.join(recevier)
    send_emile = smtplib.SMTP_SSL('smtp.qq.com', 465)   # SMTP服务器

    send_emile.login(account,account_password)
    send_emile.sendmail(account, recevier, msg.as_string())
    send_emile.quit()

if __name__ == '__main__':
    how_to_send()