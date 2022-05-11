import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '1x6tot01@gmail.com'
receivers = ['2659612923@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 第三方 SMTP 服务
mail_host="smtp.gmail.com"  #设置服务器
mail_user="1x6tot01@gmail.com"    #用户名
mail_pass="Mry[937364497]"   #口令

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("Existo", 'utf-8')  # 发送者
message['To'] = Header("me", 'utf-8')  # 接收者

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    # smtpObj = smtplib.SMTP()
    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtpObj.ehlo()
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")

except smtplib.SMTPException:
    print("Error: 无法发送邮件")
