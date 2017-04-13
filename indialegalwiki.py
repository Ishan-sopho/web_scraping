import sys, os, urllib, time
from bs4 import BeautifulSoup
import datetime as dt

# defining constants
url = "http://judis.nic.in/supremecourt/imgst.aspx?filename="

# calls url, parses html and stores data in a text file
def store(count, file_path):
    new_name = os.path.join(file_path,str(count)+'.txt')
    if os.path.exists(new_name):
        print "{}.txt exists".format(count)
        return 0
    else:
        request = str(count).zfill(5)
        request_url = url + request

        data = urllib.urlopen(request_url)
        soup = BeautifulSoup(data)
        text = soup.find('textarea')
        if bool(text):
            temp = open(new_name, 'w')
            temp.write(text.contents[0])
            # the next two lines are just for debugging purposes and can be removed later
            temp.write('\n')
            temp.write("extracted from {}\n".format(request_url))
            temp.close()
            print "created {}.txt".format(count)
            time.sleep(1)
            return 0
        else:
            return 1

# check and create folder if necessary and returns file path where text file is to be stored
def create_folder(name):
    new_name = str((name-1)/20*20+1)+"-"+str((name-1)/20*20+20)
    if not os.path.isdir(os.path.join(path, new_name)):
        try:
            os.makedirs(os.path.join(path, new_name))
            print "created folder {}".format(new_name)
        except:
            sys.exit("could not create folder {}".format(new_name))
        return os.path.join(path, new_name)
    else:
        return os.path.join(path, new_name)

# calculates the time difference between now and the next 5 p.m.
# note this is done assuming the programme is run after 5 p.m. in the current day
def pause_1_day():
    nextDay = dt.datetime.now() + dt.timedelta(days=1)
    timestring = nextDay.strftime('%d-%m-%Y') + " 17-00-00"
    newtime = nextDay.strptime(timestring, '%d-%m-%Y %H-%M-%S')
    delay = (newtime - dt.datetime.now()).total_seconds()
    return delay


# check if storage folder exists
if not os.path.isdir("JUDGEMENTS"):
    try:
        os.makedirs("JUDGEMENTS")
        path = os.path.join(os.getcwd(), "JUDGEMENTS")
        print "created folder JUDGEMENTS"
    except:
        sys.exit("could not create folder JUDGEMENTS")
else:
    path = os.path.join(os.getcwd(), "JUDGEMENTS")

i = 1
while True:
    file_path = create_folder(i)
    if not store(i, file_path):
        i += 1
    else:
        print "judgement {} is not available yet it will be checkded again next day at 5 p.m.".format(i)
        time.sleep(pause_1_day())