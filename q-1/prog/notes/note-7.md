# Prise de notes - prog - N07

### Programmation événementielle.

- Programme événementiel : Programme en attente qui attend des 'événements' pour y répondre ou effectuer des actions en conséquence.

- Événement : Changement d'état dans l'environnement.

### Gestion des événements


### Gestion d'events
```
Event dispatcher:
|-- Recevoir un événement --> dispatcher l'événement --| <- Boucle d'événements
|------<------- Attendre -------<--------|

Event source : le moyen de déclencher un événement
Dispatch : appeler la fonction d'un événement.
Event handler : fonction qui s'exécute quand il y a un événement x.
```

> Utiliser un `input()` qui met en pause le programme n'est pas de la programmation événementielle mais séquentielle !
