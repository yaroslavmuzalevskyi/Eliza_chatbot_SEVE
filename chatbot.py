import re
from nltk.corpus import wordnet
import json

# def get_user_input():

    # while True:
    #     u_input = input().lower().strip()
    #     synonyms = get_synonyms(u_input)
    #     for word, syn_list in synonyms.items():
    #         if "bye" in syn_list:
    #             return None
    #     return u_input
    
# def read_replies():
#     with open('replies.json') as replies_json:
#         replies = json.loads(replies_json)
#         replies_json.close()
#         print(replies)


# def get_synonyms(u_input):
#     u_input_list = u_input.split()
#     synonyms_dict = {}
    
#     for word in u_input_list:
#         synonyms = set()
#         for syn in wordnet.synsets(word):
#             for lemma in syn.lemmas():
#                 lem_name = re.sub('[^a-zA-Z0-9 \n\.]', ' ', lemma.name())
#                 synonyms.add(lem_name.lower())
#         synonyms_dict[word] = list(synonyms)
    
#     return synonyms_dict


# def main():
#     while True:
#         user_sentence = get_user_input()
#         if user_sentence is None:
#             print("Exiting the program.")
#             break
#         synonyms = get_synonyms(user_sentence)
#         print("\nSynonyms for the words in your sentence:")
#         for word, syns in synonyms.items():
#             print(f"{word}: {', '.join(syns)}")


# main()