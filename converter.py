import json
import csv
import io 
import codecs
import re

class Collection:

    # depending on the language setting while exporting from YGOPro the JSON is build slightly different
    # because of that there is some duplication of code with a slight change

    def __init__(self,lan='en',outputPath=''):
        self.ygoproLan=lan
        self.outputPath=outputPath
        # check if / or \ is at the end and adds it if not exist
        # depends on path given
        if self.outputPath!='':
            if self.outputPath[-1]!='\\' and re.search('.:\\+',self.outputPath):
                self.outputPath=self.outputPath+'\\'
            elif self.outputPath[-1]!='/':
                self.outputPath=self.outputPath+'/'

    def ygoproimport(self,filename):
        with open(filename, 'r') as f:
            self.ygopro = json.load(f)

    def dragonCollection(self,filename):
        with open(filename, newline='', encoding='utf-16-le') as file:

            dragonshield=[{}]
            csvfile= csv.reader(file, delimiter=',',quotechar='"')
            next(csvfile) # fisrt two lines have to be skipped
            next(csvfile) 
            for row in csvfile:
                dragonshield.append(
                    {
                        'name_en': row[3],
                        'set_code': row[4],
                        'card_number': row[6],
                        'quantity': row[1],
                        'rarity': row[7]
                    }    
                )

        dragonshield.remove({})
        self.dragonCol=dragonshield

    def dragonDeck(self,filename):
        with open(filename, newline='', encoding='utf-16-le') as file:

            dragonshield=[{}]
            csvfile= csv.reader(file, delimiter=',',quotechar='"')
            next(csvfile)
            next(csvfile)
            for row in csvfile:
                dragonshield.append(
                    {
                        'card_type': row[0],
                        'quantity': int(row[1]),
                        'name_en': row[2]
                    }
                )

        dragonshield.remove({})
        self.dragonDeck=dragonshield

    def exportDBCSV(self):
        db=[['ID', 'Name', 'Name_en', 'Set_Code','Quantity','Rarity']]
        
        # matches are found over the set_code (GEIM-EN001)
        # rarity is not Mapped - maybe in a newer version (don't have all variations fro dragonshield)
        for x in self.ygopro['data']:
            if 'card_sets' in x:
                for y in x['card_sets']:
                    for z in self.dragonCol:
                        if y['set_code']==z['card_number']:
                            if self.ygoproLan!='en':
                                db.append(
                                    [
                                        
                                        x['id'],
                                        x['name'],
                                        x['name_en'], 
                                        y['set_code'],
                                        z['quantity'],
                                        z['rarity']
                                    
                                    ]
                                )
                            else:
                                db.append(
                                    [
                                        
                                        x['id'],
                                        x['name'],
                                        x['name'], 
                                        y['set_code'],
                                        z['quantity'],
                                        z['rarity']
                                    
                                    ]
                                )
        
        self.outputPath=self.outputPath+'db.csv'
        with open(self.outputPath, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(db)
        
    def exportYDK(self):
        ydk=[['#create by Renton'],['#main']]

        # matches are found over the name
        # if a match is found the id will be written - how often depends on the quanitety from dragonshield CSV

        if self.ygoproLan!='en':
            for x in self.ygopro['data']:
                for z in self.dragonDeck:
                    if z['name_en']==x['name_en'] and z['card_type'] not in ('Extra Deck', 'Side Deck'):
                        for i in range(z['quantity']):
                            ydk.append(
                                [
                                    x['id']
                                ]
                            )
                        
            ydk.append(['#extra'])
            for x in self.ygopro['data']:
                for z in self.dragonDeck:
                    if z['name_en']==x['name'] and z['card_type'] in ('Extra Deck'):
                        for i in range(z['quantity']):
                            ydk.append(
                                [
                                    x['id']
                                ]
                            )
                            
            ydk.append(['!side'])                        
            for x in self.ygopro['data']:
                for z in self.dragonDeck:                        
                    if z['name_en']==x['name'] and z['card_type'] in ('Side Deck'):
                        for i in range(z['quantity']):
                            ydk.append(
                                [
                                    x['id']
                                ]
                            )
        else:
            for x in self.ygopro['data']:
                for z in self.dragonDeck:
                    if z['name_en']==x['name'] and z['card_type'] not in ('Extra Deck', 'Side Deck'):
                        for i in range(z['quantity']):
                            ydk.append(
                                [
                                    x['id']
                                ]
                            )
                        
            ydk.append(['#extra'])
            for x in self.ygopro['data']:
                for z in self.dragonDeck:
                    if z['name_en']==x['name'] and z['card_type'] in ('Extra Deck'):
                        for i in range(z['quantity']):
                            ydk.append(
                                [
                                    x['id']
                                ]
                            )
                            
            ydk.append(['!side'])                        
            for x in self.ygopro['data']:
                for z in self.dragonDeck:                        
                    if z['name_en']==x['name'] and z['card_type'] in ('Side Deck'):
                        for i in range(z['quantity']):
                            ydk.append(
                                [
                                    x['id']
                                ]
                            )

        self.outputPath=self.outputPath+'deck.ydk'
        with open(self.outputPath, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(ydk)