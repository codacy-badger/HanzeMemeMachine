# Hanze Meme Machine
Alle vochtige memes, nu ook in je discord server.
***
De Hanze Meme Machine is een Discord bot geschreven in Python. Het is een open source bot die je gemakkelijk zelf kan hosten of ergens op een VPS kan laten draaien.

## Commando's
Alle commando's zijn niet hoofdletter gevoelig.

* **!HanzeXperience** Plaatst het HanzeXperience logo in de chat waar het commando gedaan is.
* **!Versie** Geeft de huidige versie van Hanze Meme Machine terug in de chat.
* **!Meme** Geeft eem willekeurige meme van HanzeMemes terug in de chat.
* **!Help** Geeft een lijst terug met commando's of uitleg over een commando als je !help opvolgt met een commando

## Gebruik
### 1. Clone de repository
```git
git clone https://github.com/JonkerThing/HanzeMemeMachine.git
```
### 2. Installeer packages
Toegevoegd is ``` requirements.txt ``` dit is een bestand waar alle nodige extra pakketen in staan. je kan ze gemakkelijk in 1x installeren door het volgende commando uit te voeren:
```pip
pip install -r requirements.txt
```
### 3. Maak een config.py bestand aan
In de gekloonde repository mist 1 bestand. Namelijk de ```config.py```. Dit bestand wordt gebruikt om je persoonlijke discord sleutel op te slaan. Dit bestand ziet er als volgt uit:
```Python
import os

# Token voor de reddit bot.
configuratie = {
    # Token voor de reddit bot.
    "discord_api_sleutel": "[Hier komt je persoonlijke discord sleutel]",
    # Versie nummer voor de bot
    "versienummer": "0.1"
}
```
De sleutel die je moet hebben kan je gratis krijgen via [deze pagina](https://discordapp.com/developers/docs/intro)
Maak een nieuwe bot aan en plak de key in je ```config.py```

### 4. Voeg de bot toe aan je server
De volgende stap is om je bot aan de server toe te voegen die je wilt.

### 5. Start de bot!
Je kan nou de bot starten door naar de map te gaan waar je ```HanzeMemeMachine.py``` zich bevindt en deze uit te voeren met
```Python
python HanzeMemeMachine.py
```
***
Om je bot actief te houden moet je script draaien. Als je de computer niet altijd aan wilt hebben staan overweeg dan om het via een RaspberryPi te draaien of via een VPS. 

### Alleen gebruiken. Niks aan het project toevoegen :(
Ook wordt de bot [hier](https://discordapp.com/api/oauth2/authorize?client_id=464745470267228170&permissions=0&scope=bot) gehost. Klik op de link en voeg hem toe
