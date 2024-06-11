
# Start with CLI
# Make a GUI
# Make into a webapp usable on mobile too
# Standalone mobile app
# All criss pltform
def help():
    print(' The comands available are: \n!help \n!info (drug) \n!dose (drug)')


print('-----------------------------\n\n')
print('Welcome to Substance Secrets. \n\nAn app with a focus on harm reduction by allowing recreational drug users the ability to track their usage, aswell as search for info such as safe dosages for each substance and will give warnings if you are taking high doses.')

print('\n\n-----------------------------\n\n')
print('To get a summary of a drug, type   !info drug   \n')
print('To view the rest of our commands and functions, enter: !help \n')


commmands = "!info drug","!duration drug"
command = input('')


if command not in commmands:
    print('Not a command, try again')