# What is this?
Because the format of the Dragonshield export is non standart a converter is needed.
This Python programm can convert decks in to the ydk format or convert a collection into a format I use in my DB.
If you want to transalte the collection from englisch into another language this tool is also usefull.

# How does it Work?
It takes the JSON from the YGOProDeck API and compares it to the Dragonshioeld CSV.
The YGOProDeck API can create this JSON in multiple languages, so it is also possible to translate the englisch names.
The comparison either works with the set_code (GEIM-EN001) or over the englisch name.

# Usage
This scrtipt is written with Python 3.9. It only uses standard packages, so no pip install needed.
It either can be used with commandlineargs or called without them and fill out a formular.
```
main.py [-h] [-d DRAGONSHIELD] [-y YGOPRO] [-l LANGUAGE] [-t IMPORTTYPE] [-o OUTPUT]

A simple Converter from the Dragonshield CSV to YDK or a general CSV with translatet Names

optional arguments:
  -h, --help            show this help message and exit
  -d DRAGONSHIELD, --dragonshield DRAGONSHIELD
                        Path to exported Dragonshield CSV (default: None)
  -y YGOPRO, --ygopro YGOPRO
                        Path to exported YGOPro JSON (default: None)
  -l LANGUAGE, --language LANGUAGE
                        language setting (default: en)
  -t IMPORTTYPE, --importType IMPORTTYPE
                        Choose between a and b (Deck or Collection) (default: a)
  -o OUTPUT, --output OUTPUT
                        Choose a Outputfolder (default: )

```

# Future Versions?
I might change the schame of my DB and so the CSV from this programm would also change.
If there is intrest in some specific schema for other sites I would be open to implemetn it. Just create an issue with the schema of the CSV you need.
I want to build a mapping for the rarity codes from Dragonshield, but I dont know all the options yet.

Propably there will be a version where you can convert a ydk to a dragonshield deck.
If there is a need for a converter from a file of another site to the Dragonshield format just ask in a issue.

# MY CSV Format

```
'ID', 'Name', 'Name_en', 'Set_Code','Quantity','Rarity'
```

This CSV is mostly only needed if your collection is not in englisch.
