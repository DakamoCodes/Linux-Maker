
#This will allow me to use the OS to get WSL installed

import os

print('This Linux maker was made by Goerge Dakamo\nCheck out his github: https://github.com/DakamoCodes')

#Works like:
#distro = input('Enter the name of the image you want:')
#question = input('Do you want to start up the Distro?:')

distro, question = input('Enter the name of the image you want:'), input('Do you want to start up the Distro?:')

#This will execute the code to PowerShell

os.system('''
wsl --install {distro}
wsl --unregister {distro}
''')

#Works like: if question == 'yes' or 'y':

if question in ['yes', 'y']:
	
	#This will run the distro from PowerShell
	
	os.system(distro)
	
elif question in ['no', 'n']:
	
    print('You can go to {distro} anytime by searching {distro} in the start menu')
	
else:
    print('Couldn\'t understand function but you can go to {distro} anytime by searching {distro} in the start menu')
