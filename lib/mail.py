import smtplib
from lib import ycp_utility
from email.mime.multipart import MIMEMultipart  # email內容載體
from email.mime.text import MIMEText  # 用於製作文字內文
from email.mime.base import MIMEBase  # 用於承載附檔
from email import encoders  # 用於附檔編碼
from pathlib import Path
from string import Template
import datetime
import ssl
import yaml


def attach_html(path, var):
    return Template(Path(path).read_text(encoding="utf8")).substitute(var)


def attach_device_info(mail_htmls):
    info = ycp_utility.get_hardware_info()
    mail_htmls.append(attach_html(r"../src/report_template/device_info.html", {"device_brand": info["device_brand"],
                                                                               "device_model": info["device_model"],
                                                                               "device_api": info["device_api"],
                                                                               "device_memory": format(info["device_memory"], '.2f')
                                                                               }))


class AutoMail:
    def __init__(self, title, content_html, attached_files):
        # 寄件者使用的Gmail帳戶資訊
        self.gmail_user = 'pfautomail@gmail.com'
        self.gmail_password = 'PerfectCorp24725102'
        self.from_address = self.gmail_user

        # 設定信件內容與收件人資訊
        self.to_address = ['maxbill20509@gmail.com']

        today = str(datetime.date.today()).replace("-", "_")
        self.Subject = "[Auto Test Report] {} report({})".format(title, today)
        self.html = content_html
        self.attachments = attached_files

    def send(self):
        # 開始組合信件內容
        mail = MIMEMultipart()
        mail['From'] = self.from_address
        mail['To'] = ', '.join(self.to_address)
        mail['Subject'] = self.Subject
        # 將信件內文加到email中
        mail.attach(MIMEText(self.html, 'html'))
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

# mail_htmls = []
# var_list = {}
# mail_htmls.append(attach_html(r"../src/report_template/preview_limit_report.html", {"title": "Output Limit", "result": "Pass"}))
# attach_device_info(mail_htmls)
# mail_htmls.append(attach_html(r"../src/report_template/output_limit_spec.html"))
# mail = AutoMail("Output_Limit", mail_htmls, attached_list)
# mail.send()








