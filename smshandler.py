import os
from datetime import datetime as dt
date = "{}.{}.{}_{}_{}".format(
    dt.today().year,
    dt.today().month,
    dt.today().day,
    dt.today().hour,
    dt.today().minute)
sender = ''
smsTo = ['']
root = 'C:\\Users\\user\\Documents\\smshandler\\'
incoming = os.path.join(root,'incoming')
outgoing = os.path.join(root,'outgoing')
files = {}

def getTheLatestSms(path=incoming):
    try:
        for ent in os.scandir(incoming):
            if ent.is_file():
                files.update({ent.stat().st_ctime:ent.name})    
        return files[sorted(files)[-1]]
    except:

        exit()


def delAllSms(path=incoming):
    try:
        for ent in os.scandir(incoming):
            if ent.is_file():
                os.unlink(ent)    
    except:
        exit()


pathToSms = os.path.join(incoming,getTheLatestSms())

with open(pathToSms,'r') as f:
    sms = f.read().split('\n\n')
    for header in sms[0].split('\n'):
        try:
            header_name, value = header.split(': ')
            if header_name.strip().lower() == 'from' and sender.strip().lower() == value:
                for number in smsTo:
                    text = 'To: {}\nAlphabet: UTF\n\n{}'.format(number, sms[1])
                    with open(os.path.join(outgoing,'cod_to_{}_{}.sms'.format(number,date)),'w') as outGoingFile:
                        outGoingFile.write(text)
                break
        except Exception as e:
            continue

delAllSms()
