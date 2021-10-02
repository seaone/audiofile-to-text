python -m venv venv
source ./venv/bin/activate

pip install SpeechRecognition
pip install multi-rake

chmod a+x cgi-bin/result.py

python3 -m http.server --cgi

go to http://localhost:8000
