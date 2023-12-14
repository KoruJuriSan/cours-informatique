
# Prise de note - cours - N04

### Communication et protocoles reseau

- Emetteur: source d'un message, personne ou peripherique qui envoie un message.
- Recepteur: destinataire d'un message.
- Support de transmission: par ou le message va passer.

Source du message => Encodage => Emetteur => Support de transmission => Recepteur => Decodage => Destination du message

P
- Protocoles: Regles de structure d'un message
- message doit etre encapsule
- Trame reseau: un packet de donees encapsule

#### Taille messages

- Une message trop grand est decoupe en plusieurs plus petit messages.

#### dif

monodiffusion: un seul emetteur, un seul destinataire (unicast).
broadcast: un seul emetteur, tout le reseau destinataire.

#### Protocols

il y a des protocols libre et d'autre proprietaires.

TCP/IP: liste de protocols libre d'utilisation que tout le monde utilise.

Chaque Trame a un protocols definit par couche

Modele/Couche TCP/IP:

```
1. Application
2. Transport
3. Internet
4. Acces reseaux
```

!! Certain protocoles de certaine couche sont dependant d'un protocols d'une autre !!

#### TCP/IP Transport

protocols:

1. TCP: lent mais securise
2. UDP: rapide mais peu securise

#### TCP/IP Acces internet

- IP (Internet Protocol): addresse des paquets
- NAT (Network Address Translation): converti l'IP d'un reseau prive par une addresse publique.
- ICMP (Internet COntrol Message Protocol): permet de signaler des erreurs liees aux transmissions de paquets
- RIP (Routing Information Protocol): routage dynamique
- OSPF (Open Shortest Path First): permet de faire du routage dynamique
- EIGRP (Enchanced Interior Gateway Routing Protocol): permet de faire du routage dynamique, PRORIETAIRE
- BGP (): permet de faire du routage dynamique niveau d'internet.

#### TCP/IP Reseau

- ARP (Address Resolution Protocol): permet de lier l'addresse MAC et IP