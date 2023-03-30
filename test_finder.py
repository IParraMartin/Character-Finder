from CharacterFinder import CharacterFinder

#OPEN TXT FILE
with open('FILE_PATH_HERE', "r") as document:
    text = document.read()


#SPLIT TOKENS AND SELECT KEYWORDS FOR RELATIONS
tokens = text.split()
keywords = ['NAME_1', 'NAME_2', 'NAME_3']


# FIND RELATIONSHIPS AND COUNT
finder = CharacterFinder()
finder.process_tokens(tokens, keywords)


#EXTRACT DATA FOR GEPHI (SOURCE, TARGER, AND WEIGHTS)
relationship_data = finder.get_csv()