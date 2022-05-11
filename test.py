import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_user = "existo@163.com"    #用户名
mail_pass = "DZSDYGWPKWZYFBOU"   #口令

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("Existo", 'utf-8')  # 发送者
message['To'] = Header("me", 'utf-8')  # 接收者

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtp = smtplib.SMTP_SSL("smtp.163.com", 994)
    smtp.login(mail_user, mail_pass)
    smtp.sendmail(mail_user, ['2659612923@qq.com', '1257743935@qq.com'], message.as_string())
    print("发送成功!")
except:
    print('Something went wrong...')
