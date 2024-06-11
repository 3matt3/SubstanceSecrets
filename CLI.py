


def help():
    print(' \nThe comands available are: \n\n!help \n!info (drug) \n!dose (drug)')


print('-----------------------------\n\n')
print('Welcome to Substance Secrets. \n\nAn app with a focus on harm reduction by allowing recreational drug users the ability to track their usage, aswell as search for info such as safe dosages for each substance and will give warnings if you are taking high doses.')

print('\n\n-----------------------------\n\n')
print('To get a summary of a drug, type   !info drug   \n')
print('To view the rest of our commands and functions, enter: !help \n')



command = input(': ')

if command.startswith('!'):

    command = str(command.split('!')[1])
    command = str(command.split(' ')[0])
    #drug = str(command.split(' ')[0])
    
print(drug)

