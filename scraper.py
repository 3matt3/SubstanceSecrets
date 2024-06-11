import requests

from bs4 import BeautifulSoup

# FIX THIS SHIT ASS FUNCTION
def getInfo(drug):
    try:

        input = drug
        url = "https://tripsit.me/factsheets/"+input
        html = requests.get(url)
        info = BeautifulSoup(html.text, 'html.parser')

    except:
        return('fail')

# FIX     
def getDose(drug):
    try:
        drug = str(drug)
        url = 'https://psychonautwiki.org/wiki/'+drug+'/Summary'
        html = requests.get(url)
        info = BeautifulSoup(html.text, 'html.parser')
        
        soup = info.get_text()
        soupf = soup.format()
        soupy = soupf.splitlines()
        soupy[:] = [x for x in soupy if x]

        dosages = soupy[9:24]

        roa = dosages[0]
        threshold = dosages[4]
        light = dosages[6:8]
        common = dosages[8:10]
        strong = dosages[10:12]
        heavy = dosages[12]
        msg = str('roa')+'\n\n'+'Threshold: '+str(threshold)+(dosages[13])+'\n'+'Light: '+str(light)+'\nCommon: '+str(common)+'Strong: '+str(strong)+'\nHeavy: '+str(heavy)


        #if 'Common' not in dosages:
        #    return('Fail')
       # print(msg)
        return msg

        print(soupy[:])
   
    except:
        return('Fail')

# WORKING
def get_durations(drug):
    try:

        drug = str(drug)
        url = 'https://psychonautwiki.org/wiki/'+drug+'/Summary'
        html = requests.get(url)
        info = BeautifulSoup(html.text, 'html.parser')

        soup = info.get_text()
        soupp = soup.format()
        soupp = soup.splitlines()
        soupp[:] = [x for x in soupp if x]

        dosages = soupp[9:24]

        duration = soupp[26:32]
        total = str(duration[0])
        onset = str(duration[1])
        comeup = str(duration[2])
        peak = str(duration[3])
        offset = str(duration[4])
        afterglow = str(duration[-1])
        durations = total,onset,comeup,peak,offset,afterglow
        reply = durations[0]+'\n'+durations[1]+'\n'+durations[2]+'\n'+durations[3]+'\n'+durations[4]+'\n'+durations[5]
        print(reply)
        return(reply)
    except:
        return('fail')

get_durations('cocaine')