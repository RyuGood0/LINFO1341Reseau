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
- Packet certificats : 1434

#

- Upload start: 1875
- Upload end: 7032

#

- Download start: 7352
- Download end: 10021

# Questions énoncées

- IP : 46.105.132.156

## DNS

### Combien de noms de domaines sont résolus et quand ?

- drive.shadow.tech

- Standard query 0xbc80 A drive.shadow.tech OPT -> Standard query response 0xbc80 A drive.shadow.tech A 46.105.132.157 A 46.105.132.156 OPT
- Standard query 0x3b8d AAAA drive.shadow.tech OPT -> Standard query response 0x3b8d AAAA drive.shadow.tech SOA candy.ns.cloudflare.com OPT

### Quels sont les serveurs autoritatifs pour ces noms de domaines ? Sont-ils gérés par des entreprises différentes ?

- candy.ns.cloudflare.com

### À quelles entreprises appartiennent les noms de domaines résolus ? Il y en a-t-il d’autres que celle qui détient l’application ?

### Quels sont les types de requête DNS effectuées ?

- Toutes les deux récursives

### Lorsqu’une requête DNS souhaite obtenir une adresse IP, quelle est sa famille ? Il y a-t-il une version IP préférée par l’application ?

- 2 requêtes sont envoyées, une pour ipv4 et une pour ipv6, mais seul la ipv4 reçoit une réponse, donc la communication se fait dessus

### Les requêtes contiennent elles des records additionnels ? Le cas échéant, à quoi servent-ils ?

### Observez-vous des comportements DNS inattendus ?

## Couche transport

### Quels sont les protocoles de transports utilisés pour chaque fonctionnalité ?

- À part pour les requêtes DNS, tous les protocoles de transport sont du TCP

### Il y a-t-il plusieurs connexions vers un même nom de domaine ? Si oui, pouvez-vous l’expliquer ?

- shadow drive est un sous-domaine de shadow.tech, mais shadow.tech redirige vers une IPv6: 2606:4700:10::6816:1e7e alors que shadow drive redirige vers une IPv4: 46.105.132.156

- 2606:4700:10::6816:1e7e est un serveur Cloudflare, alors qu'un whois sur 46.105.132.156 donne: "RIPE Network Coordination Centre"

### Si vous observez du trafic QUIC, quels sont les versions utilisées ? Pouvez-vous identifier des extensions négociées dans le handshake ?

- Aucun trafic QUIC

### Lorsque vous observez du trafic UDP, identifiez-vous d’autres protocoles que QUIC et DNS ? Expliquez comment ils sont utilisés par l’application.

## Chiffrement et sécurité

### L’utilisation du DNS est-elle sécurisée ? Comment ?

### Quelles versions de TLS sont utilisées ? Précisez les protocoles de transport sécurisés par ces versions.

- TLSv1.3

### Quel est la durée de vie des certificats utilisés ? Par qui sont-ils certifiés ?

4 Certificats:
- 12 ans (utcTime: 2018-11-02 00:00:00 (UTC) -> utcTime: 2030-12-31 23:59:59 (UTC)): "(id-at-commonName=USERTrust RSA Certification Authority,id-at-organizationName=The USERTRUST Network,id-at-localityName=Jersey City id-at-stateOrProvinceName=New Jersey,id-at-countryName=US)"
- 10 ans (utcTime: 2019-03-12 00:00:00 (UTC) -> utcTime: 2028-12-31 23:59:59 (UTC)): "(id-at-commonName=AAA Certificate Services,id-at-organizationName=Comodo CA Limited,id-at-localityName=Salford,id-at-stateOrProvinceName=Greater Manchester,id-at-countryName=GB)"
- 24 ans (utcTime: 2004-01-01 00:00:00 (UTC) -> utcTime: 2028-12-31 23:59:59 (UTC)): "(id-at-commonName=AAA Certificate Services,id-at-organizationName=Comodo CA Limited,id-at-localityName=Salford,id-at-stateOrProvinceName=Greater Manchester,id-at-countryName=GB)"
- 1 an (utcTime: 2023-10-30 00:00:00 (UTC) -> utcTime: 2024-10-29 23:59:59 (UTC)): "(id-at-commonName=Sectigo RSA Extended Validation Secure Server CA,id-at-organizationName=Sectigo Limited,id-at-localityName=Salford,id-at-stateOrProvinceName=Greater Manchester,id-at-countryName=GB)"

### Lorsque vous pouvez observer l’établissement du chiffrement, quels sont les algorithmes de chiffrement utilisés ?

- rsa_pss_rsae_sha256 pour les certificats
- Cipher suite: TLS_AES_128_GCM_SHA256 pour le chiffrement TLS sur le site
- Cipher suite: TLS_AES_256_GCM_SHA384 pour le chiffrement TLS sur l'app

### Si vous observez du trafic UDP, semble-t-il chiffré ? Comment est-il sécurisé ?

## Application

### Quels comportements observer-vous lors du transfert de nouveaux fichiers comparé à la modification de fichiers existant ? Quel impact a la modification par plusieurs utilisateurs par rapport à un seul ?

### Quel est le volume de données échangées par l’application pour chacune de ces fonctionnalités ? Utilisez une base appropriée permettant la comparaison (par ex. par minute).

### Il y a-t-il des serveurs relais utilisés pour interagir avec un utilisateur ou les applications communiquent-elles directement ? Observez-vous autre chose lorsque deux utilisateurs sont sur le même réseau Wi-Fi ?

### Est-ce qu’interagir avec un utilisateur se trouvant dans le même réseau Wi-Fi ou Ethernet a un impact sur la façon dont le trafic applicatif est transporté ? Il y a-t-il des serveurs relais ?