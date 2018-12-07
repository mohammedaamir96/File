import os
import signal
import datetime
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os.path, time
path = "C:\\Users\\Aamir\\Desktop\\Date & Time"
filename = os.listdir(path)
c={"1.txt","2.txt","3.txt","4.txt","5.txt","6.txt"}
filename=set(filename)
notpresent=c.difference(filename)
present=c.intersection(filename)
filename=list(filename)
notpresent=list(notpresent)
present=list(present)
d=list()
e=list()
f = notpresent
print(f)
present.sort()
print(present)
for i in present:
    a=''
    a = path
    a = a.__add__("\\")
    a = a.__add__(i)

    d.append(os.path.getsize(a))
    e.append(time.ctime(os.path.getmtime(a)))
print(d)
print(e)
me = "mohammedaamir020@gmail.com"
you = "aakashkumar667@gmail.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "File Details"
msg['From'] = me
msg['To'] = you

html="""
<html>
<head>
<body>
<style>
table, th, td {
   border: 1px solid black;
    border-collapse: collapse;
}
th, td {
    padding: 10px;
    text-align: centre;
}
</style>
<table style="width:50%">
<caption> File Details</caption>
 <tr>
    <th>filename</th>
    <th>size</th>
    <th>Date & Time</th>
    <th>record</th>
  </tr>
  <tr> 
  """
for (j,k,l) in zip(present,d,e):
    html = html + "<tr><td>" + j + "</td><td>" + str(k)+ "</td><td>" + l + "</td>" + "</td><td bgcolor=green> </td></tr>"
for(i) in notpresent:
    html=html + "<tr><td>" + i + "</td><td>" + "null" + "</td><td>" + "null" + "</td>" + "</td><td bgcolor=red> </td></tr>"
html=html + """
</table>
</body>
</head>
</html>
"""
print(html)
part1 = MIMEText(html, 'html')
msg.attach(part1)
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('mohammedaamir020@gmail.com', 'aamir1996')
#mail.sendmail(me, you, msg.as_string())
print("Sucessfully email Sent")