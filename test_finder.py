from CharacterFinder import CharacterFinder

with open("/Users/inigoparra/Desktop/tokens.txt", "r") as document:
    text = document.read()

tokens = text.split()
keywords = ['enrique', 'carlota', 'sab', 'martina']

finder = CharacterFinder()
keyword_found, keywords_seen, relationship_counts, relationship_list = finder.process_tokens(tokens, keywords)


finder.get_csv()