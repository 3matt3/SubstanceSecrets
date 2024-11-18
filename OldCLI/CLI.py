from scraper import get_info, get_durations, get_dose
import datetime
import json
import uuid

# Push data to a SQLite database, both the usage history and cache the information about the drug when a search command is used,
# to save time by using cached data (if it has already been searched for) instead of scraping the info again

# Make user/session classes / objects, Send warning for high doses and bad combos, 
# Methods:
# User.dose(drug) User.history(drug=all, date=today) User.total(drug)
# Drug.dosages() drug.durations() drug.info() drug.history(User,Time) 
# Function to add all doses of drug to show their total usage
# Simple GUI with command line and display

print(
"""
//////////////////////////////////////////////////////////////////////////////////
//                                                                              //
//                                                                              //
//    _________       ___.              __                                      //
//   /   _____/ __ __ \_ |__    _______/  |_ _____     ____    ____    ____     //
//   \_____  \ |  |  \ | __ \  /  ___/\   __\\__  \   /    \ _/ ___\ _/ __ \    //
//   /        \|  |  / | \_\ \ \___ \  |  |   / __ \_|   |  \\  \___ \  ___/    //
//  /_______  /|____/  |___  //____  > |__|  (____  /|___|  / \___  > \___  >   //
//    ______\/_            \/      \/            _\/      \/      \/      \/    //
//   /   _____/  ____    ____  _______   ____  _/  |_   ______                  //
//   \_____  \ _/ __ \ _/ ___\ \_  __ \_/ __ \ \   __\ /  ___/                  //
//   /        \\  ___/ \  \___  |  | \/\  ___/  |  |   \___ \                   //
//  /_______  / \___  > \___  > |__|    \___  > |__|  /____  >                  //
//          \/      \/      \/              \/             \/                   //
//                                                                              //
//                                                                              //
//////////////////////////////////////////////////////////////////////////////////
"""
)

print('\n\nA project with a strong focus on harm reduction, by allowing recreational drug users the ability to track their usage,\nas well as to easily find info for any substance')
print('\n-----------------------------\n')
#print('To get a summary of a drug, type   !info drug   \n')
print('To view our commands and functions, enter: !help \n')

drugs_consumed = []
drugs_consumed_txt = []
session_usage = []
session_use_msg = []
#user = ''
#global session 

        

#class Session:
#    def __init__(self):
#        id = uuid.uuid1()
#        session = id
#    def closeSession(self):
#       pass

   # username = self.user
    #uuid = id
    
class User:


    def __init__(self, username=None, id=None):
        self.username = username
        self.id = uuid.uuid4()


# 
#    def save():     // Not rly needed as it already saves to json when the command is inputted
#        '''Backs up the usage history to history.json'''
#        print('Saving...')

    def exit():
        '''Updates the database when the user exits the program'''
        # Push the current session data (drugs_consumed) to SQLite DB. *preffered
        # or update the database based on the json file.
        print('exit...')


def loadData():
    try:
        with open('history.json') as f:
            data = json.load(f)
            drugs_consumed.extend(data)
        f.close()
    except:
        print('FAILED TO OPEN HISTORY')
        pass
    try:
        with open('data.json') as h:
            data = json.load(h)
            drugs_consumed_txt.extend(data)
        h.close()
    except:
        print('FAILED TO OPEN HISTORY DATA')
        pass

def test():
    print(str(drugs_consumed_txt))
#username = input('what is your username? : ')
#print(f'Hello {username}! Enter a command')
#loadData()
# Main Menu Logic // Keeps repeating input until exit command //
while True:
    #username = ''
    #if len(username) == 0:
     #   username = input('what is your username? : ')
     #   client = Session(user=username)
     #   username = User


    


    command = input(': ')

    if command == '!help':
        print("""\n
//////////////////////////////////////////////\n
The currently available commands are: \n
!help   - Displays all the available commands
!info (drug)   - Gives you a short summary of the drug
!duration (drug)   - Displays the duration info for the drug
!dosage (drug)   - Displays the dosage range for the drug
!dose (drug)   - Allows you to enter your drug consumption with timestamps to log your drug usage
!history   - Gives you a summary of your drug consumption\n
//////////////////////////////////////////////\n
""")
        
    if command == '!exit' or command == '!q':
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

        elif cmd == 'test':
            test()
        elif cmd == 'load':
            loadData()

        elif cmd == 'dose':
            dosage = str(input('\nHow many milligrams (mg) of '+drug+' have you taken? \n'))
            route = input('How did you take '+drug+' ? (Oral,Snorted,Smoked,IV etc) \n')
            time = datetime.datetime.now()
            info = {'drug': drug, 'dosage': dosage, 'roa': route,'time': str(time)}
            msg = str(dosage+' mg of '+drug+' taken via '+route+' at: '+str(time))
            drugs_consumed.append(info)
            drugs_consumed_txt.append(msg)
            session_usage.append(info)
            session_use_msg.append(msg)


            with open('history.json', 'w') as f:
                json.dump(drugs_consumed, f)   
            f.close()
            with open('data.json', 'w') as h:
                json.dump(drugs_consumed_txt, h)
            h.close()

            print('\n')
            print(msg)
            print('\n\n') 

        elif cmd == 'history':
            print('\n')
            print('//////////////////////////////////////////////\n')
            for x in drugs_consumed_txt:
                print(x)
            print('\n//////////////////////////////////////////////\n')
            print('\n')

                

        

    
