import json
from random import randint


class JsonParser:

    def zoek_meme(self):
        # TODO de aanvraag via de reddit JSON doen en niet het lokale bestand.
        with open('testdata.json') as test_data:
            data = json.load(test_data)
        afbeelding = ""

        # Geeft een willekeurig getal tussen de 0 en de lengte van de array met alle posts
        index = randint(0, len(data["data"]["children"])) - 1
        while afbeelding == "":
            try:
                # Test of er een afbeelding bij deze post zit. Zo niet verhoog de index met 1 en probeer nogmaals
                afbeelding = data["data"]["children"][index]["data"]["preview"]["images"][0]["source"]["url"]
                return afbeelding
            except KeyError:
                index += 1
