import requests
import smtplib
from email.mime.text import MIMEText
from email.header import Header

false = False
true = True

# SMTP config
mail_user = "existo@163.com"  # username
mail_pass = "DZSDYGWPKWZYFBOU"  # token

sender = 'existo@163.com'
receivers = ['2659612923@qq.com']

# set authorization & data
userAuthorization = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJFeGlzdG8iLCJvcGVuSWQiOiJvb3JvRTVzM1A4SHVwUVNKMDhfclptbjIzMkNBIiwiaXNzIjoiYXBpLmppZWxvbmcuY28iLCJhdWQiOiJjbGllbnQuamllbG9uZy5jbyIsImlhdCI6MTY1MjE5MTQwMiwiZXhwIjoxNjUyNDUwNjAyfQ.L8CEGZXdUUodO9Ql75XhsdxsYAF-fMWxdNnCw5MQEzs'
userData = {
    "Id": 0,
    "ThreadId": 43364841,
    "Number": "1",
    "Signature": "叶鹏",
    "RecordValues": [],
    "DateTarget": "",
    "IsNeedManualAudit": false,
    "MinuteTarget": -1,
    "IsNameNumberComfirm": false
}


def sendEmail(sendingType, msg):
    try:
        # if failed
        if sendingType == 'Fail':
            msg = '填报失败'

        # message content
        message = MIMEText(msg, 'plain', 'utf-8')
        message['From'] = Header(sender, 'utf-8')  # 发送者
        # message['To'] = Header("me", 'utf-8')  # 接收者

        subject = '20级计算机类3班晚点名结果'
        message['Subject'] = Header(subject, 'utf-8')

        # sending process
        smtp = smtplib.SMTP_SSL("smtp.163.com", 994)
        smtp.login(mail_user, mail_pass)
        smtp.sendmail(sender, receivers, message.as_string())
        print("Message sent successfully!")

    except:
        print('Something went wrong...')


def checkIn(url):
    try:
        # set headers
        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
            'Content-Type': 'application/json',
            'Connection': 'keep-alive',
            'Host': 'h-api.jielong.co',
            'Authorization': userAuthorization
        }

        # set data
        data = userData

        r = requests.post(url=url, headers=headers, json=data)
        # print(r.json())
        sendEmail('Success', r.json()['Data'])
        print("check in successfully!")

    except:
        sendEmail('Fail', '填报失败')
        print("Error! check in failed!")


def main():
    url = 'https://h-api.jielong.co/api/Thread/EditCheckInRecord'
    checkIn(url)


if __name__ == '__main__':
    main()
