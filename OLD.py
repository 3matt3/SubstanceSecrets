import requests
from bs4 import BeautifulSoup


def getInfo(drug):
    try:
        msg = str(drug)
        url2 = 'https://drugs.tripsit.me/'+msg
        html = requests.get(url2)
        info = BeautifulSoup(html.text, 'html.parser')

        basic = info.find(id='grid')
        basicc = basic.find_all('p',class_='layoutPosition')
        basic3 = str(basicc)
        basic3 = basic3.split('>')[1]
        summary = basic3.split('<')[0]
        summary = summary+'\n\nIf you would like more information, visit: '+url2
        return str(summary)

    except:
        return('fail')

#getInfo('heroin')

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
def get_dosage(drug):
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
        if 'Common' not in dosages:
            return 'fail'
        else:
            print(dosages)
            return dosages
    except:
        return 'fail'

get_dosage('cocaine')

    #roa = dosages[0]
    #threshhold = dosages[4]+'mg'
    #light = dosages[4]+'-'+dosages[8]+'mg'
    #common = dosages[8]+[]


    #for x in dosages:
    #    if x is int:

    #dosages = str([x for x in dosages if str(dosages).isdigit()])
 



#get_dosage('etizolam')

# Working
def get_duration(drug):
    url2 = 'https://drugs.tripsit.me/'+drug
    html = requests.get(url2)
    info = BeautifulSoup(html.text, 'html.parser')
    duration = info.find(id='grid',)
    duration2 = duration.find(id='flexDuration layoutPosition')
    duration3 = str(info.find_all('td', class_='table'))
    #duration = duration.find(id='flexDuration layoutPosition')
    #duration = duration.find_all('td',class_='td_width')
    
    print(duration3)
    return str(duration)

#get_duration('etizolam')



#   //  functions to do  //  
#onset = ''
#dose = ''
#interactions = ''
#lightDose = ''
#commonDose = ''
#strongDose = ''
   