from nltk.corpus import wordnet
import json
import random

with open("data.json", "r") as file:
    content = file.read()
    content = json.loads(content)

ISSUES=content["issues"]
BASIC_REPLIES=content["basic_replies"]



def get_synonyms(word):
    synonyms = set()
    for synset in wordnet.synsets(word):
        for lemma in synset.lemmas():
            synonyms.add(lemma.name().lower())
    return synonyms

def get_matched_issues(user_input):
    user_words = set(user_input.lower().split())
    
    user_synonyms = set(user_words)
    for word in user_words:
        user_synonyms.update(get_synonyms(word))

    matched_issues = []
    
    for issue in ISSUES:
        issue_name = issue["name"].lower()
        issue_synonyms = issue["keywords"]

        if issue_name in user_synonyms or user_synonyms.intersection(issue_synonyms):
            matched_issues.append(issue["name"])
            print(issue["reply"])
    
    return matched_issues

def main():
    user_input = input("Enter your query: ").strip()
    matched_issues=get_matched_issues(user_input)

    # if there is no match between the keywords and 
    if(len(matched_issues)==0):
        reply = random.choice(BASIC_REPLIES["not_understand"])
        print(reply)
        main()
    #if there was only one match 
    elif(len(matched_issues)==1):
        issue = next((item for item in ISSUES if item["name"] == matched_issues[0]), None)
        reply = issue["reply"]
        print(f"Your selected issue is {issue['name']}\n////\n{issue['reply']}\n////")


        print(random.choice(BASIC_REPLIES["more_help"]))
        user_input = int(input("Enter your choice (1-yes, 2-no): ").strip())
        if(user_input==1):
            main()
        else:
            print(random.choice(BASIC_REPLIES["goodbye"]))
            return

    else:
        print("Choose a specific issue you need help with:")
        i=0
        for matched_issue in matched_issues:
            i=i+1
            issue = next((item for item in ISSUES if item["name"] == matched_issue), None)
            print(f"{i}. {issue['name']}")
        
        user_input = int(input("Enter your issue number: ").strip())
        issue = next((item for item in ISSUES if item["name"] == matched_issues[user_input-1]), None)
        print(f"Your selected issue is {issue['name']}\n////\n{issue['reply']}\n////")

        print(random.choice(BASIC_REPLIES["more_help"]))
        user_input = int(input("Enter your choice (1-yes, 2-no): ").strip())
        if(user_input==1):
            main()
        else:
            print(random.choice(BASIC_REPLIES["goodbye"]))
            return


       
main()
