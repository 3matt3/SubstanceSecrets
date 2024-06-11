from scraper import getInfo, get_durations
import datetime

# Make function to dose with timestamps
# sTORE DATA
# Send warning for high doses and bad combos
# Finish Scraping and parsing info


usage = []
    

def help():
    print(' \nThe comands available are: \n\n!help \n!info (drug) \n!dose (drug)')


print('-----------------------------\n\n')
print('Welcome to Substance Secrets. \n\nAn app with a focus on harm reduction by allowing recreational drug users the ability to track their usage, aswell as search for info such as safe dosages for each substance and will give warnings if you are taking high doses.')

print('\n\n-----------------------------\n\n')
print('To get a summary of a drug, type   !info drug   \n')
print('To view the rest of our commands and functions, enter: !help \n')

drugs_consumed = []


command = input(': ')

if command == '!help':
    help()

if command == '!dose':
    drug = input('What drug did you take?')
    dosage = input('\nHow many milligrams (mg) of '+drug+' have you consumed?\n\n')
    route = input('What ROA (Route of Administratiion) did you use? e.g snort')
    time = datetime.datetime.now()
    dosetime = str(dosage+'taken at '+time+' via Inhalation')

    drugs_consumed.append(drug)
    usage.append(dosetime)
    print(dosetime)

if command.startswith('!'):

    command = str(command.split('!')[1])
    drug = str(command.split(' ')[1])

    if command == 'info':
       summary = getInfo(drug)
       print(summary+'\n')

    elif command == 'duration':
        cmd = get_durations(drug)
        print(cmd+'\n')

    

    




#print(drug)
