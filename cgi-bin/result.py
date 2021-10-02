#!/usr/bin/env python3

import cgi
import os
import recognize_speech
import extract_keywords
import json

form = cgi.FieldStorage()

text = None
keywords = None
path_to_file = None
lang = form["lang"].value or 'en-Us'

if "file" in form: 
  fileitem = form['file']
  filename = os.path.basename(fileitem.filename)
  path_to_file = os.path.join(os.getcwd(), 'files', filename)
  open(path_to_file, 'wb').write(fileitem.file.read())
  recognized_text = recognize_speech.recognize(path_to_file, lang)
  text = recognized_text

if text != None or text != '':
  keywords = extract_keywords.extract(text, lang)

response = {'success':'true', 'text': text, 'lang': lang, 'keywords': keywords}

print('Content-Type: application/json')
print('Access-Control-Allow-Origin: *')
print()
print(json.dumps(response))