# Structure
captures est le dossier avec les captures wireshark
keys sont les clés des captures
LINFO1115-synthese.pdf est le fichier test pour upload/download

# Infos captures:

## Flags util

- `dns`
- `tcp.flags.syn==1 && tcp.flags.ack==0` pour client hello
- `tcp.flags.syn==1 && tcp.flags.ack==1` pour server hello
- `tls`

## ShadowWIFI-Login-Upload-Download

- Premier packet avec shawdow: 218
- Packet auth: 779
- Premier packet shadow drive: 1412
- Packet drive download: 7312

# Questions énoncées

## DNS

### Combien de noms de domaines sont résolus et quand ?

### Quels sont les serveurs autoritatifs pour ces noms de domaines ? Sont-ils gérés par des entreprises différentes ?

### À quelles entreprises appartiennent les noms de domaines résolus ? Il y en a-t-il d’autres que celle qui détient l’application ?

### Quels sont les types de requête DNS effectuées ?

### Lorsqu’une requête DNS souhaite obtenir une adresse IP, quelle est sa famille ? Il y a-t-il une version IP préférée par l’application ?

### Les requêtes contiennent elles des records additionnels ? Le cas échéant, à quoi servent-ils ?

### Observez-vous des comportements DNS inattendus ?

## Couche transport

### Quels sont les protocoles de transports utilisés pour chaque fonctionnalité ?

### Il y a-t-il plusieurs connexions vers un même nom de domaine ? Si oui, pouvez-vous l’expliquer ?

### Si vous observez du trafic QUIC, quels sont les versions utilisées ? Pouvez-vous identifier des extensions négociées dans le handshake ?

### Lorsque vous observez du trafic UDP, identifiez-vous d’autres protocoles que QUIC et DNS ? Expliquez comment ils sont utilisés par l’application.

## Chiffrement et sécurité

### L’utilisation du DNS est-elle sécurisée ? Comment ?

### Quelles versions de TLS sont utilisées ? Précisez les protocoles de transport sécurisés par ces versions.

### Quel est la durée de vie des certificats utilisés ? Par qui sont-ils certifiés ?

### Lorsque vous pouvez observer l’établissement du chiffrement, quels sont les algorithmes de chiffrement utilisés ?

### Si vous observez du trafic UDP, semble-t-il chiffré ? Comment est-il sécurisé ?

## Application

### Quels comportements observer-vous lors du transfert de nouveaux fichiers comparé à la modification de fichiers existant ? Quel impact a la modification par plusieurs utilisateurs par rapport à un seul ?

### Quel est le volume de données échangées par l’application pour chacune de ces fonctionnalités ? Utilisez une base appropriée permettant la comparaison (par ex. par minute).

### Il y a-t-il des serveurs relais utilisés pour interagir avec un utilisateur ou les applications communiquent-elles directement ? Observez-vous autre chose lorsque deux utilisateurs sont sur le même réseau Wi-Fi ?

### Est-ce qu’interagir avec un utilisateur se trouvant dans le même réseau Wi-Fi ou Ethernet a un impact sur la façon dont le trafic applicatif est transporté ? Il y a-t-il des serveurs relais ?