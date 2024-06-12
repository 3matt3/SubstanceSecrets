from scraper import get_info, get_durations, get_dose
import datetime
import json

# History function to display all times you have dosed
# sTORE DATA
# Send warning for high doses and bad combos
# Finish Scraping and parsing info

# 
print('-----------------------------\n')
print('Welcome to Substance Secrets. \n\nAn app with a focus on harm reduction by allowing recreational drug users the ability to track their usage,\nas well as the ability to easily find info for any substance')


print('\n-----------------------------\n')
print('To get a summary of a drug, type   !info drug   \n')
print('To view the rest of our commands and functions, enter: !help \n')

drugs_consumed = []
drugs_consumed_txt = []


while True:

    with open('history.json') as f:
        data = json.load(f)
        drugs_consumed.append(data)
    f.close()

    command = input(': ')

    if command == '!help':
        print('\n\n')
        print('-------------------------------------------\n')
        print('The currently available commands are: \n')
        print('!help   - Displays all the available commands')
        print('!info (drug)   - Gives you a short summary of the drug')
        print('!duration (drug)   - Displays the duration info for the drug')
        print('!dosage (drug)   - Displays the dosage range for the drug')
        print('!dose (drug)   - Allows you to enter your drug consumption with timestamps to log your drug usage')
        print('!history   - Gives you a summary of your drug consumption')
        print('\n-------------------------------------------\n')

    if command == '!exit':
        break


    if command.startswith('!'):

        command2 = str(command.split('!')[1])
        try:
         
            drug = str(command.split(' ')[1])
        except:
            drug = '' 
        cmd = command2.split(' ')[0]


        if cmd == 'info':
            summary = get_info(drug)
            print(summary+'\n')

        elif cmd == 'duration':
            print('\n')
            text = get_durations(drug)
        
        elif cmd == 'dosage':
            print('\n')
            doses = get_dose(drug)

        elif cmd == 'dose':
            dosage = input('\nHow many milligrams (mg) of '+drug+' have you taken? \n')
            route = input('How did you take '+drug+' ? (Oral,Snorted,Smoked,IV etc) \n')
            time = datetime.datetime.now()
            info = {'drug': drug, 'dosage': dosage, 'roa': route,'time': str(time)}

            msg = str(dosage+' mg of '+drug+' taken via '+route+' at: '+str(time))

            drugs_consumed.append(info)
            drugs_consumed_txt.append(msg)

            with open('history.json', 'w') as f:
                json.dump(drugs_consumed, f, indent=4)

            print(msg)

            print('\n\n')   
            print(drugs_consumed)
            #print(drugs_consumed_txt)

        elif cmd == 'history':
            print(str(drugs_consumed))
        

    
