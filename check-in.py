import requests
import smtplib
from email.mime.text import MIMEText
from email.header import Header

false = False
true = True

# SMTP config
mail_user = ""  # username
mail_pass = ""  # token

sender = ''
receivers = []

# set authorization & data
userAuthorization = ''
userData = {
    "Id": 0,
    "ThreadId": ,
    "Number": "1",
    "Signature": "",
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

        subject = ''
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
