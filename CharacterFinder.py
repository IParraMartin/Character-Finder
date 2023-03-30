import pandas

with open("FILE_PATH_HERE", "r") as document:
    text = document.read()

tokens = text.split()
keywords = ['enrique', 'carlota', 'sab', 'martina']

class CharacterFinder:

    def __init__(self):

        try:
            import pandas
            
        except:
            print('Pandas library is not installed, try pip install pandas')


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

        for relationship, count in relationship_counts.items():
            
            print(f"Relationship: {relationship}, Count: {count}")

        return keyword_found, keywords_seen, relationship_counts, relationship_list
    

    def get_csv(self):

        relationship_data = [(r[0], r[1], count/100) for r, count in relationship_counts.items()]
        df = pandas.DataFrame(relationship_data, columns=['Source', 'Target', 'Weight'])
        df.to_csv('relationships.csv')


finder = CharacterFinder()
keyword_found, keywords_seen, relationship_counts, relationship_list = finder.process_tokens(tokens, keywords)


