import converter
import pathlib
import argparse

#All Args are optional, but ygopro and dragonshield must be populated for the automated process
#If not a Formular will start
argParser = argparse.ArgumentParser(description= 'A simple Converter from the Dragonshield CSV to YDK or a general CSV with translatet Names', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
argParser.add_argument('-d', '--dragonshield', action='store', help='Path to exported Dragonshield CSV')
argParser.add_argument('-y', '--ygopro', action='store', help='Path to exported YGOPro JSON')
argParser.add_argument('-l', '--language', action='store' , help='language setting', default='en')
argParser.add_argument('-t', '--importType', action='store' , help='Choose between a and b (Deck or Collection)', default='a')
argParser.add_argument('-o', '--output', action='store' , help='Choose a Outputfolder', default='')


args=vars(argParser.parse_args())


if args['dragonshield'] is None and args['ygopro'] is None:


    language= input('Language Code (en, de, etc): ')
    #Removing \\ from windowspaths
    ygoJson= input('YGOProJson path: ').replace('\\\\', '\\')

    dragonChoice= input('Choose a Dragonshield Exporttype: \na. Deck \nb. Collection\n')
    dragonPath= input('Path to Dragonshield CSV: ').replace('\\\\', '\\')
    output= input('Outputpath: ').replace('\\\\', '\\')

    coll= converter.Collection(language,output)
    coll.ygoproimport(ygoJson)

    if dragonChoice=='a':
        coll.dragonDeck(dragonPath)
        coll.exportYDK()
    else:
        coll.dragonCollection(dragonPath)
        coll.exportDBCSV()
else:

    coll= converter.Collection(args['language'],args['output'])
    coll.ygoproimport(args['ygopro'])

    if args['importType']=='a':
        coll.dragonDeck(args['dragonshield'])
        coll.exportYDK()
    else:
        coll.dragonCollection(args['dragonshield'])
        coll.exportDBCSV()