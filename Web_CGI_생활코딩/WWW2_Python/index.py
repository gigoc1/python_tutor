#!/usr/bin/python3
print("Content-Type: text/html")
print()
import cgi, os
form = cgi.FieldStorage()
files=os.listdir('data')
listStr=''
for item in files:
  listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
if 'id' in form:
  pageId = form["id"].value
  description=open('data/'+pageId).read()
else:
  pageId = 'Welcome'
  description = 'Web is world wide web'
print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {listStr}
  </ol>
  <a href="creat.py">creat</a>
  <form action="process_create.py"method="post">
  <p><input type="text" name="title" placeholder="title"></p>
  <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
  <p><input type="submit"></p>
  </form>

  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=listStr))