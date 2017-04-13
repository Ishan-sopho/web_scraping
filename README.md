# web_scraping
note: this code is written in windows and in python 2.7. you are required to install python 2.7 on your desktop.

india legal wiki assignment-
1. clone the repository
2. install beautiful soup on your desktop, run the following command in the terminal: pip install beautifulsoup4
3. run indialegalwiki.py

the python script extracts judgements from supreme court website, starting from the
link: http://judis.nic.in/supremecourt/imgst.aspx?filename=00001
the scripts keeps extracting until it finds a url without a judgement, then it goes into an infinite loop
checking the url everyday at 5 p.m. to see if new judgements have been uploaded.

all the judgements are stored in the folder JUDGEMENTS, that is created in the same folder as indialegalwiki.py
