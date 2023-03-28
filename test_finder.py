from CharacterFinder import CharacterFinder

with open("TXT_FILE_PATH", "r") as document:
    text = document.read()

tokens = text.split()
keywords = ['enrique', 'carlota']

finder = CharacterFinder()
keyword_found, keywords_seen, relationship_counts, relationship_list = finder.process_tokens(tokens, keywords)


