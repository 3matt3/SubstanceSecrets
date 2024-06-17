import requests

from bs4 import BeautifulSoup

# FIX THIS SHIT ASS FUNCTION
def get_info(drug):
    try:

        input = str(drug)
        url = "https://tripsit.me/factsheets/"+input
        url2 = 'https://drugs.tripsit.me/'+input
        html = requests.get(url2)
        info = BeautifulSoup(html.text, 'html.parser')

        soup = info.get_text()
        soupf = soup.format()
        soupy = str
        print('//  Under Construction  // ')

    except:
        return('fail')

# WORKING   
def get_dose(drug):
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
        #print(soup)
        #print(dosages)

        unit = str(dosages[13])
        roa = str(dosages[0])
        threshold = str(dosages[4]+unit)    
        light2 = str(dosages[6]+dosages[7]+dosages[8]+' '+unit)
        common2 = str(dosages[8]+dosages[9]+dosages[10]+' '+unit)
        strong2 = str(dosages[10]+dosages[11]+dosages[12]+' '+unit)
        heavy2 = str(dosages[12]+' '+unit+' +')

        msg = roa+'\n\n'+'Threshold: '+threshold+'\n'+'Light: '+light2+'\nCommon: '+common2+'\nStrong: '+strong2+'\nHeavy: '+heavy2

        #if 'Common' not in dosages:
        #    return('Fail')

        #print(dosages)
        print(msg+'\n\n')

        return msg
   
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

        print('\n------ '+drug+' ------')
        print('\n\n'+reply)
        print('\n\n')
        return(reply)
    except:
        return('fail')


#get_info('morphine')