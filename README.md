![Screenshot 2021-10-02 at 17 16 23](https://user-images.githubusercontent.com/5929502/135720335-5b1a2ca0-6165-4945-a440-48c8ded62e60.png)

python -m venv venv
source ./venv/bin/activate

pip install SpeechRecognition
pip install multi-rake

chmod a+x cgi-bin/result.py

python3 -m http.server --cgi

go to http://localhost:8000

---

### Client repo
https://github.com/seaone/audiofile-to-text-client
