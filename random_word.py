# by BugBoys100


from os import system
from requests import post
from json import dumps
import random
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System


lien = 'TON URL WEBHOOK'
nom_webhook = 'LE NOM QUE TU VEUX DU WEBHOOK'
avatar_webhook = 'AVATAR QUE TU VEUX DU WEBHOOK'

text = r'''
            _____                 _                                         _     
            |  __ \               | |                                       | |    
            | |__) |__ _ _ __   __| | ___  _ __ ___   __      _____  _ __ __| |___ 
            |  _  // _` | '_ \ / _` |/ _ \| '_ ` _ \  \ \ /\ / / _ \| '__/ _` / __|
            | | \ \ (_| | | | | (_| | (_) | | | | | |  \ V  V / (_) | | | (_| \__ \
            |_|  \_\__,_|_| |_|\__,_|\___/|_| |_| |_|   \_/\_/ \___/|_|  \__,_|___/
                                                                                    
                                                                        
'''[1:]


banner = r"""
                                    `OooOOo.                     o                
                                    o     `o                   O                 
                                    O      O                   o                 
                                    o     .O                   o                 
                                    OOooOO'  .oOoO' 'OoOo. .oOoO  .oOo. `oOOoOO. 
                                    o    o   O   o   o   O o   O  O   o  O  o  o 
                                    O     O  o   O   O   o O   o  o   O  o  O  O 
                                    O      o `OoO'o  o   O `OoO'o `OoO'  O  o  o 
                                                                                
                                                                                
                                        o          `O                   o       
                                        O           o                  O        
                                        o           O                  o        
                                        O           O                  o        
                                        o     o     o .oOo. `OoOo. .oOoO        
                                        O     O     O O   o  o     o   O        
                                        `o   O o   O' o   O  O     O   o        
                                        `OoO' `OoO'  `OoO'  o     `OoO'o       
                                              
"""[1:]

system('color a')
print("\n"*5)


print(banner)


# Test si webhook déjà rentré
if lien == 'TON URL WEBHOOK':
    lien = str(input('URL du webhook : '))

if not lien.startswith('https://discord.com/api/webhooks'):
    print('URL du webhook invalide')
    system("pause")
    exit()

else:
    system('cls')
    print(text)



    nombre = int(input('Nombre de mots : '))

    mots_a_trouver = []
    mots_larousse = []
    # choix du mot


    for _ in range(nombre):
        # mot_a_trouver = 'sachez'
        mot_a_trouver = random.choice(open('liste_francais.txt').readlines())
        mot_a_trouver = mot_a_trouver[:len(mot_a_trouver)-1]
        mots_a_trouver.append(mot_a_trouver)

        mot_larousse = mot_a_trouver
        for i in range(mot_larousse.count(' ')):
            # web search
            if mot_larousse.index(' '):
                mot_larousse = mot_larousse[:mot_larousse.index(
                    ' ')] + '%20' + mot_larousse[mot_larousse.index(' ')+1:]

        mots_larousse.append(mot_larousse)
        


    resultat = ''

    for i in range(nombre):
        resultat = resultat + \
            f'- [{mots_a_trouver[i].capitalize()}](https://www.larousse.fr/dictionnaires/francais/{mots_larousse[i]})\n'


    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }

    # Tests des entrées Avatar / Pseudo
    if nom_webhook == 'LE NOM QUE TU VEUX DU WEBHOOK':
        nom_webhook = 'Choix des mots Bug Boys heheh'
    if avatar_webhook == 'AVATAR QUE TU VEUX DU WEBHOOK':
        avatar_webhook = 'https://i.imgur.com/wxf30FQ.jpg'


    embed = {
        "username": f'{nom_webhook}',
        "avatar_url": f"{avatar_webhook}",
        "embeds": [
            {
                    "color": 0xFF0000,
                    "title": f'Nombre de mots : {nombre}',
                    'description': f' {resultat}',
                    "author": {
                        "name": "Choix de mots",
                        'icon-url': 'https://i.imgur.com/wxf30FQ.jpg'
                    },
                "footer": {
                        "text": "by Bug Boys#9702"
                    },
                'thumbnail': {
                        'url': 'https://i.imgur.com/wxf30FQ.jpg',
                    }
            }]}

    post(lien, data=dumps(embed).encode("utf-8"), headers=headers)


    print(f'Réussi ! les mots qui ont étés envoyés sont :\n')
    for i in range(len(mots_a_trouver)):
        print('  - ',mots_a_trouver[i].capitalize())
    print('\n')
    system('pause')
    exit()