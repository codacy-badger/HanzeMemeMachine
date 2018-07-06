import json
from random import randint

import requests


class JsonParser:

    # vraagt de verbinding aan bij reddit
    def verbinden(self):
        response = requests.get("https://www.reddit.com/r/Hanzememes/.json?count=25&after=t3_10omtd/",
                                headers={"User-Agent": "Hanze Meme Machine v0.1 (by /u/disort)"})
        data = response.json()
        return data

    def zoek_meme(self):
        json_data = self.verbinden()
        afbeelding = ""

        # Geeft een willekeurig getal tussen de 0 en de lengte van de array met alle posts
        index = randint(0, len(json_data["data"]["children"])) - 1
        while afbeelding == "":
            try:
                # Test of er een afbeelding bij deze post zit. Zo niet verhoog de index met 1 en probeer nogmaals
                afbeelding = json_data["data"]["children"][index]["data"]["preview"]["images"][0]["source"]["url"]
                return afbeelding
            except KeyError:
                index += 1
