from CharacterFinder import CharacterFinder
import pandas


#OPEN TXT FILE
with open('/Users/inigoparra/Desktop/tokens.txt', "r") as document:
    text = document.read()


#SPLIT TOKENS AND SELECT KEYWORDS FOR RELATIONS
tokens = text.split()
keywords = ['enrique', 'carlota', 'sab', 'martina']


# FIND RELATIONSHIPS AND COUNT
finder = CharacterFinder()
finder.process_tokens(tokens, keywords)


#EXTRACT DATA FOR GEPHI (SOURCE, TARGER, AND WEIGHTS)
relationship_data = finder.get_csv()