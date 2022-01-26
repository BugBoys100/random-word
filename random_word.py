# by BugBoys100


from os import name, system
from requests import post, get
from json import dumps, loads
import random
from larousse_api import larousse
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System

import json

with open('settings.json') as json_data:
    data_dict = json.load(json_data)

lien = data_dict['lien_webhook']
nom_webhook = data_dict['nom_webhook']
avatar_webhook = data_dict['avatar_webhook']


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


Anime.Fade(Center.Center(banner), Colors.red_to_yellow, Colorate.Vertical, enter=True)


# Test si webhook déjà rentré
if lien == 'TON URL WEBHOOK':
    print(Colorate.Diagonal(Colors.red_to_yellow, Center.XCenter(text)))
    lien = Write.Input("URL du webhook -> ", Colors.red_to_yellow, interval=0.005)

if not lien.startswith('https://discord.com/api/webhooks'):
    print('URL du webhook invalide')
    system("pause")
    exit()

else:

    nombre = int(Write.Input("Nombre de mots -> ", Colors.red_to_yellow, interval=0.005))

    mots_a_trouver = []
    mots_larousse = []
    mots_defs = dict()
    # choix du mot


    for i in range(nombre):
        mot_a_trouver = random.choice(open('liste_francais.txt').readlines())
        mot_a_trouver = mot_a_trouver[:len(mot_a_trouver)-1]
        mots_a_trouver.append(mot_a_trouver)


        mot_larousse = mot_a_trouver
    
        larousse_def = larousse.get_definitions(mot_a_trouver)[0]
        if larousse_def.startswith('1. '): larousse_def = larousse_def[3:]
        if not larousse_def:
            larousse_def = 'aucune définition'
        # if larousse_def.find('\n') > 1:
        #         larousse_def = larousse_def[:larousse_def.index('\n')] + '  \n  ' + larousse_def[larousse_def.index('\n')+1:]
        mots_larousse.append(larousse_def)

    resultat = ''
    # Infos sur le webhook
    
    resp = get(lien)
    if resp.status_code in [200, 204]:
        webhook = loads(resp.text)['name']
        infos = f'\nRéussi ! les mots qui ont étés envoyés à {webhook} sont :\n'

    for i in range(nombre):
        resultat = resultat + \
            f' \n- **__{mots_a_trouver[i].capitalize()}__** : \n```{mots_larousse[i]}```\n'


    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }

    # Tests des entrées Avatar / Pseudo
    if nom_webhook == 'LE NOM QUE TU VEUX DU WEBHOOK':
        nom_webhook = 'Choix des mots by Bug Boys heheh'
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
                        'url': avatar_webhook,
                }
            }]}

    post(lien, data=dumps(embed).encode("utf-8"), headers=headers)
    
    if infos:
        print(infos)
    else:
        print(f'\nRéussi ! les mots qui ont étés envoyés sont :\n')
    for i in range(len(mots_a_trouver)):
        print('  - ', mots_a_trouver[i].capitalize())
    print('\n')
    system('pause')
    exit()
