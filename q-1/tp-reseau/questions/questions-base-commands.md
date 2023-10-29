Comment savoir le nom de l'appareil sur lequel je suis dans Cisco IOS ?
```
c'est ecrit a gauche du mode de configuration dans la console.

ex:

nom_appareil>
nom_appareil#
nom_appareil(config)#
```

comment savoir quelles sont les commandes possible dans le mode de configuration actuel sous Cisco IOS ?
```
? dans la console
```

Comment savoir les commandes possible qui commence par x dans le mode de configuration actuel sous Cisco IOS ?
```
x?
```

Comment savoir quels parametres je dois mettre apres ma commande sous Cisco IOS ?
```
command ?
```

Quels sont les quatres principaux modes de configuration dans Cisco IOS ?
```
> : Utilisateur standard
# : Utilisateur privilégié
(config)# : configuration globale
(config-int)# : configuration d'une interface
```

Comment passer du mode "Utilisateur standard" au mode "Utilisateur privilégié" dans Cisco IOS ?
```
> enable
#
```

Comment passer du mode "Utilisateur privilégié" au mode "Configuration globale" dans Cisco IOS ?
```
# configure terminal
(config)#
```

Comment afficher la configuration actuelle dans cisco IOS ?
```
# show running-config
```

Comment modifier la date, l'heure, les minutes et les secondes, ... de l'horloge interne sous cisco IOS ?
```
# clock set hh:mm:ss MONTH dd yyyy
```

Comment sauvegarder la configuration actuelle dans la NVRAM sous cisco IOS ?
```
# copy running-config startup-config
```

Comment changer le nom de l'appareil dans cisco IOS ?
```
(config)# hostname {new_name}
```

Comment ajouter un mot de passe "non-chiffree" pour le mode privilégié dans cisco IOS ?
```
(config)# enable password {password}
```

Comment ajouter un mot de passe "chiffree" pour le mode privilégié dans cisco IOS ?
```
(config)# enable secret {password}
```

Comment activer le chiffrement automatique des mots de passe dans le fichier de configuration sous cisco IOS ?
```
(config)# service password-encryption
```

Comment changer la banniere de connexion sous cisco IOS ?
```
(config)# banner motd "{new_banner}"
```

Comment ajouter un mot de passe sur l'acces par port console sous cisco IOS ?
```
(config)# line console 0
(config-line)# password {password}
(config-line)# login
```

Comment obtenir des informations sur le matériel et la version d'un appareil cisco IOS ?
```
> show version

! La commande est dans tous les modes de configuration !
```

Comment afficher l'horloge interne d'un appareil sous cisco IOS ?
```
> show clock

! La commande est dans tous les modes de configuration !
```