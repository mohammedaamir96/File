import webbrowser
f=open("helloworld.html",'w')
message="""<html>
<head>
<body>
<style>
table, th, td {
   border: 1px solid black;
}
</style>
<table style="width:50%">
 <tr>
    <th>filename</th>
    <th>type</th>
    <th>size</th>
    <th>Date & Time</th>
  </tr>
  </body>
  </head>
  </html>"""
f.write(message)
f.close()
a='file:///C:/Users/Aamir/PycharmProjects/Email Code/venv/Date and Time/' + 'helloworld.html'
webbrowser.open_new_tab(a)