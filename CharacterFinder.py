with open("TXT_FILE_PATH", "r") as document:
    text = document.read()

tokens = text.split()

keywords = ['enrique', 'carlota']


class CharacterFinder:

    def __init__(self):

        try:
            import pandas
        
        except:
            print('Unicodedata library is not installed, try pip install pandas')

    def process_tokens(self, tokens, keyword_list):

        keyword_found = False
        keywords_seen = [] 
        relationship_counts = {}
        relationship_list = []

        for i, token in enumerate(tokens):
        
            if token in keyword_list:

                keyword_found = True
                keywords_seen.append(token)
                
                for j in range(i+1, min(i+21, len(tokens))):

                    next_token = tokens[j]
                    
                    if next_token in keyword_list:

                        relationship_list.append((token, next_token))
                        key = (token, next_token)

                        if key in relationship_counts:

                            relationship_counts[key] += 1

                        else:

                            relationship_counts[key] = 1

                        print(f"Detected relationship: {token} - {next_token}")

        for relationship, count in relationship_counts.items():

            print(f"Relationship: {relationship}, Count: {count}")
                
        return keyword_found, keywords_seen, relationship_counts, relationship_list


finder = CharacterFinder()
keyword_found, keywords_seen, relationship_counts, relationship_list = finder.process_tokens(tokens, keywords)

