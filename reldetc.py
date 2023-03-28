with open("/Users/inigoparra/Desktop/paper-516/sab-clean.txt", "r") as f:
    text = f.read()

def process_tokens(tokens, keyword_list):

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
            
    return keyword_found, keywords_seen, relationship_counts, relationship_list


keywords = ['sab', 'carlota', 'enrique', 'teresa', 'luis', 'martina', 'jardín', 'naturaleza', 'bosque']
tokens = text.split()

keyword_found, keywords_seen, relationship_counts, relationship_list = process_tokens(tokens, keywords)

for relationship, count in relationship_counts.items():
    print(f"Relationship: {relationship}, Count: {count}")
