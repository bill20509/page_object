import smtplib
from email.mime.multipart import MIMEMultipart  # email內容載體
from email.mime.text import MIMEText  # 用於製作文字內文
from email.mime.base import MIMEBase  # 用於承載附檔
from email import encoders  # 用於附檔編碼
import datetime
import ssl
import yaml

class AutoMail:
    def __init__(self, title, report, attached_files):
        # 寄件者使用的Gmail帳戶資訊
        self.gmail_user = 'pfautomail@gmail.com'
        self.gmail_password = 'PerfectCorp24725102'
        self.from_address = self.gmail_user

        # 設定信件內容與收件人資訊
        self.to_address = ['bill_zhong@perfectcorp.com', 'billzhongtest1@gmail.com']

        today = str(datetime.date.today()).replace("-", "_")
        self.Subject = "[Auto Test Report] {} report({})".format(title, today)
        self.contents = """
            Hi all,
           
            Here is {} {} report
           
            {}
            
            Attached files are log and fail case
            
           
            Best Regards
        """.format(title, today, report)
        # 設定附件（可設多個）
        self.attachments = attached_files
    def send(self):
        # 開始組合信件內容
        mail = MIMEMultipart()
        mail['From'] = self.from_address
        mail['To'] = ', '.join(self.to_address)
        mail['Subject'] = self.Subject
        # 將信件內文加到email中
        mail.attach(MIMEText(self.contents))
        # 將附加檔案們加到email中
        for file in self.attachments:
            with open(file, 'rb') as fp:
                add_file = MIMEBase('application', "octet-stream")
                add_file.set_payload(fp.read())
            # encoders.encode_base64(add_file)
            today = str(datetime.date.today()).replace("-", "_")
            add_file.add_header('Content-Disposition', 'attachment', filename=file + ".log")
            mail.attach(add_file)

        # 設定smtp伺服器並寄發信件
        smtpserver = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtpserver.ehlo()
        smtpserver.login(self.gmail_user, self.gmail_password)
        smtpserver.sendmail(self.from_address, self.to_address, mail.as_string())
        smtpserver.quit()

# attached_list = [r"../src/deeplink_testcase/camera/effect_frame/deeplink_fashion_android.yml"]
# for test_case in attached_list:
#     with open(test_case, 'r') as f:
#         test_info = yaml.load(f.read(), Loader=yaml.FullLoader)
#         print(test_info)
# mail = AutoMail("hello this report", attached_list)
# mail.send()








