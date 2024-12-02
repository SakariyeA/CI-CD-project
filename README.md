CI/CD

Det finns en sajt som publicerar data (namn) på kunder som skall kontaktas inom kort…
Det är en webapplikation (HTML+Javascript) som läser data från en fil data.json och det är VI som producerar den filen
Vi ska produktionssätta denna sajt och bygga en PIPELINE för Data kontroll


UPPGIFTEN

- skapa ett enhetstest som alltid ”funkar”
- skapa en Githib action PIPELINE
- den ska köra enhetstest och BRYTA ifall enhetstestet inte går bra (verifiera genom att göra så testet FAILAR)
- den ska produktionssätta en Githib Pages site så sajten ovan funkar!

- Skapa en csvtojson.py som gör om profiles1.csv till en JSON fil
- Skapa tester som
– verifierar att CSV-filen innehåller 12 kolumner
– verifierar att CSV-filen innehåller 900+ rader
– verifierar att JSON-filen innehåller alla properties den ska
– verifierar att JSON-filen innehåller 900+ rader
- i min pipeline körs
- generate.py
- csvtojson.py
- testerna
- deploy index.html + script.js + data.json till Github Pages
