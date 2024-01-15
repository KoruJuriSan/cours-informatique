# Cryptologie

## Sciences

- Cryptographie: Crée des codes.
- Cryptanalyse: Décodage/Décryptage.
- Cryptologie: Cryptographie & Cryptanalyse.
- Stéganographie: Cacher des messages dans d'autres choses.

## Cryptographie
- Création de chiffrements.

### Termes
- Cryptographe: Personne qui crée des algorithmes de cryptographie.
- Ciphertext ou cryptogramme: Un message chiffré.
- Texte brut: Un message non chiffré.
- Hachage: Transforme un message en hash, illisible et normalement non-inverse.
- Cryptage: N'existe pas, abus de langage.

### Symétrique vs Asymétrique
- Symétrique: Une seule clé privée pour les deux parties.
- Asymétrique: Une clé privée, que seul le destinataire a, une clé publique disponible pour tout le monde. La clé privée décode les messages chiffrés par la clé publique et pas l'inverse.

Exemples d'algorithmes asymétriques: AES et RSA.

### RSA |!| Vulgarisation |!|
du cote prive:
    - choisit deux nombre premier au hasard 'p' et 'q'
    - on calcul 'n' = p * q (cle publique et prive partie I)
    - on calcul le 'totient de n' = (p-1) * (q-1)
    - on choisit e tel que 1 < e < 'totient de n' et est premier avec 'totient de n' (cle publique partie II)
    - on choisit d tel que (d*e) % 'totient de n' = 1 (cle prive partie II)

cote publique:
    - m = message sous forme numerique (0 < m < n)
    - C ≡ m^e % n (message chiffree)

cote prive:
    - m ≡ C^d % n
    - m = message dechiffree sous forme numerique


## Cryptanalyse
- Étude de l'analyse et du décryptage des codes.

## Stéganographie
- Cacher l'existence d'un contenu secret dans un média.
- Seule une personne avertie peut lire le véritable sens du contenu.

## Hashing vs Chiffrement

- Le chiffrement a pour but de pouvoir être déchiffré à un moment ou un autre.
- Le hachage est comme le chiffrement sans retour arrière, pas de déchiffrement possible.
