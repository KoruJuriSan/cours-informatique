Quelle est ce peripherique reseau (francais et anglais) ?

![Image du switch](image/questions-switch_commands/1698421610122.png)
```
Switch / Commutateur
```

Comment donner une addresse ip a un switch / commutateur sous cisco IOS ?
```
(config)# interface vlan 1
(config-if)# ip address {addr} {submask}
(config-if)# no shutdown
```

Comment avoir une listes des interfaces d'un switch sous cisco IOS ?
```
show ip interface brief
```