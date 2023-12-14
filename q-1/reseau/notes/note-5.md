
# Prise de note - reseau - N05

### Infos

Support = cable

### Exo

Trouver l'adresse reseau, nb d'hotes, plage ip d'host, broadcast addr.

- 122.60.42.50 255.255.255.224
```
- mask range: X.X.X.001yyyyy
- CIDR: /27
- net addr: 122.60.42.32 /27
- broadcast: 122.60.42.63 /27
- nb d'addr: 2^5 = 32
- nb d'hotes: 2^5 -2 = 30
```
---
- 10.20.30.200 255.255.255.248
```
mask range: X.X.X.11001yyy
CIDR: /29
net addr: 10.20.30.200 /29
broadcast: 10.20.30.207 /29
nb d'addr: 2^3 = 8
nb d'hotes: 2^3 -2 = 6
```
---
- 172.76.111.200 /21
```
mask range: X.X.01101yyy.Y
submask: 255.255.248.0
net addr: 172.76.104.0
broadcast: 172.76.111.255
nb d'addr: 2^11 = 1024
nb d'hotes: 2^11 -2 = 1022
```
---
- 192.168.70.45 /23
```
mask range: X.X.0100011y.Y
submask: 255.255.254.0
net addr: 192.168.71.255
broadcast: 192.168.70.0
nb d'addr: 2^9 = 512
nb d'hotes: 2^9 -2 = 510 
```
- 161.98.122.187 /26
```
---
mask range: X.X.X.10yyyyyy
submask: 255.255.255.192
net addr: 161.98.122.128
broadcast: 161.98.122.191
nb d'addr = 2^6 = 64
nb d'hotes = 2^6 -2 = 62
```