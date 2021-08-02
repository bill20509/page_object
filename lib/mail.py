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
        self.to_address = ['maxbill20509@gmail.com']

        today = str(datetime.date.today()).replace("-", "_")
        self.Subject = "[Auto Test Report] {} report({})".format(title, today)
        self.contents = """
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<!-- saved from url=(0081)https://wiki.perfectcorp.com/trac/youperfect/wiki/Photo_Quality_Memory_Limitation -->
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge">
 <title>Photo_Quality_Memory_Limitation - youperfect - Trac</title><link rel="start" href="https://wiki.perfectcorp.com/trac/youperfect/wiki"><link rel="search" href="https://wiki.perfectcorp.com/trac/youperfect/search"><link rel="help" href="https://wiki.perfectcorp.com/trac/youperfect/wiki/TracGuide"><link rel="stylesheet" href="./Photo_Quality_Memory_Limitation - youperfect - Trac_files/trac.min.css" type="text/css"><link rel="stylesheet" href="./Photo_Quality_Memory_Limitation - youperfect - Trac_files/tracnav.min.css" type="text/css"><link rel="stylesheet" href="./Photo_Quality_Memory_Limitation - youperfect - Trac_files/jquery-ui.min.css" type="text/css"><link rel="stylesheet" href="./Photo_Quality_Memory_Limitation - youperfect - Trac_files/wiki.css" type="text/css"><link rel="stylesheet" href="./Photo_Quality_Memory_Limitation - youperfect - Trac_files/code.min.css" type="text/css"><link rel="stylesheet" href="./Photo_Quality_Memory_Limitation - youperfect - Trac_files/borland.min.css"><link rel="stylesheet" href="./Photo_Quality_Memory_Limitation - youperfect - Trac_files/wysiwyg-min.css" type="text/css"><link rel="icon" href="https://wiki.perfectcorp.com/tracdocs/trac.ico" type="image/x-icon"><link rel="shortcut icon" href="https://wiki.perfectcorp.com/tracdocs/trac.ico" type="image/x-icon"><link rel="alternate" href="https://wiki.perfectcorp.com/trac/youperfect/wiki/Photo_Quality_Memory_Limitation?format=txt" title="Plain Text" type="text/x-trac-wiki"><link rel="alternate" href="https://wiki.perfectcorp.com/trac/youperfect/wiki/Photo_Quality_Memory_Limitation?format=html" title="HTML" type="text/x-trac-wiki"><style type="text/css">
</style>
 <script type="text/javascript" src="./Photo_Quality_Memory_Limitation - youperfect - Trac_files/jquery-1.8.0.min.js.下載"></script>
 <script type="text/javascript" src="./Photo_Quality_Memory_Limitation - youperfect - Trac_files/jquery-ui-1.8.23.min.js.下載"></script>
 <script type="text/javascript" src="./Photo_Quality_Memory_Limitation - youperfect - Trac_files/trac.min.js.下載"></script>
</head>
<body>




 <div class="wikipage">
</li></ul><h3 id="Photooutputsize">Photo output size<a href="https://wiki.perfectcorp.com/trac/youperfect/wiki/Photo_Quality_Memory_Limitation#Photooutputsize" class="anchor" title="Link to this section"> ¶</a></h3>
<p>
GPU texture size :
</p>
<p>
If Android version is above Marshmallow(23), the max photo size will be 6144. Otherwise, the max photo size is 4096.<br>As saving photo with smart HD pro quality, if buf max length(width or height) * 1.3 is not bigger than source max length(width or height), we will up-scale to same aspect ratio of original file.
</p>
<p>
Memory limitation :
</p>
<ul><li>Before 5.33
</li></ul><table class="wiki">
<tbody><tr><td>Memory</td><td>&lt; 800 MB</td><td>≥ 800MB
</td></tr><tr><td>Max length</td><td>1. High (1024)<br>2. Normal (800)</td><td>1. Smart HD Pro(4096 or 6144) / Ultra high(3200) (Min value between GPU texture)<br>2. High (1600)<br>3. Normal (800)
</td></tr><tr><td>Note</td><td></td><td>Pop-up warning dialog when select to ultra high if memory ≤ 1.5 GB
</td></tr></tbody></table>
<ul><li>After 5.33
</li></ul><table class="wiki">
<tbody><tr><td>Memory</td><td>&lt; 800 MB</td><td>≥ 800MB &amp;&amp;  &lt; 2.0GB</td><td>≥ 2.0 GB
</td></tr><tr><td>Max length</td><td>1. High (1024)<br>2. Normal (800)</td><td>1. Ultra high(biggest 3200) (Min value between GPU texture)<br>2. High (1600)<br>3. Normal (800)</td><td>1. Smart HD Pro(4096 or 6144) (Min value between GPU texture)<br>* Smart HD only support <strong>OS ≥ 5.0</strong><br>2. Ultra high(biggest 3200) (Min value between GPU texture)<br>3. High (1600)<br>4. Normal (800)
</td></tr><tr><td>Note</td><td></td><td>Pop-up warning dialog when select to ultra high if memory ≤ 1.5 GB</td><td>If Android version is above Marshmallow(23), the max photo size will be 6144. Otherwise, the max photo size is 4096.
</td></tr></tbody></table>
<ul><li>After 5.35 (Normal is removed from quality. Request by Dennis)
</li></ul><table class="wiki">
<tbody><tr><td>Memory</td><td>&lt; 800 MB</td><td>≥ 800MB &amp;&amp;  &lt; 2.0GB</td><td>≥ 2.0 GB
</td></tr><tr><td>Max length</td><td>High (1024)</td><td>1. Ultra high(biggest 3200) (Min value between GPU texture)<br>2. High (1600)</td><td>1. Smart HD Pro(4096 or 6144) (Min value between GPU texture)<br>* Smart HD only support <strong>OS ≥ 5.0</strong><br>2. Ultra high(biggest 3200) (Min value between GPU texture)<br>3. High (1600)
</td></tr><tr><td>Note</td><td></td><td>Pop-up warning dialog when select to ultra high if memory ≤ 1.5 GB</td><td>If Android version is above Marshmallow(23), the max photo size will be 6144. Otherwise, the max photo size is 4096.
</td></tr></tbody></table>
<p>
<br> * Ultra high option black list:
</p>
<ul><li>("Sony Ericsson", "MT15i")
</li><li>("samsung", "SCH-I699I")
</li><li>("HUAWEI", "HUAWEI G520-0000")
</li><li>("FIH", "SH530U")
</li><li>("samsung", "GT-I9500")
</li><li>("YuLong", "Coolpad8198T")
</li></ul></div>
   </div>
  <script type="text/javascript">
   addHeadingLinks(document.getElementById("searchable"), "Link to this section");
  </script>
</div>
<script type="text/javascript">
$(function() {
  $( "a#edit" ).button({ icons: {primary:'ui-icon-pencil'} });
  $( "a#attach" ).button({ icons: {primary:'ui-icon-circle-arrow-n'} });
  $( "a#delete_version" ).button({ icons: {primary:'ui-icon-trash'} });
  $( "a#delete_page" ).button({ icons: {primary:'ui-icon-trash'} });     
  $("input[type='submit']").button();
});   
</script>
        """
        # self.contents = """
        #     Hi all,
        #
        #     Here is {} {} report
        #
        #     {}
        #
        #     Attached files are log and fail case
        #
        #
        #     Best Regards
        # """.format(title, today, report)
        # 設定附件（可設多個）
        self.attachments = attached_files
    def send(self):
        # 開始組合信件內容
        mail = MIMEMultipart()
        mail['From'] = self.from_address
        mail['To'] = ', '.join(self.to_address)
        mail['Subject'] = self.Subject
        # 將信件內文加到email中
        mail.attach(MIMEText(self.contents, 'html'))
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


attached_list = [r"../src/deeplink_testcase/camera/effect_frame/deeplink_fashion_android.yml"]
# for test_case in attached_list:
#     with open(test_case, 'r') as f:
#         test_info = yaml.load(f.read(), Loader=yaml.FullLoader)
#         print(test_info)
report = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""
mail = AutoMail(report, "hello", attached_list)
mail.send()








