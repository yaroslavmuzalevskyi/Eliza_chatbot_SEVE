from nltk.corpus import wordnet
import json
import random
from termcolor import colored

with open("data.json", "r") as file:
    content = file.read()
    content = json.loads(content)

ISSUES = content["issues"]
BASIC_REPLIES = content["basic_replies"]

farewells = ["bye", "goodbye", "see you", "farewell", "later", "ciao", "adios", "see ya", "thanks", "thank you"]

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
    
    return matched_issues

def main():
    user_input = input(colored("Enter your query: ","yellow")).strip()
    
    # End conversation if a farewell word is detected in the input
    if any(farewell in user_input.lower() for farewell in farewells):
        print(colored(random.choice(BASIC_REPLIES["goodbye"]), "cyan"))
        return

    matched_issues = get_matched_issues(user_input)

    if len(matched_issues) == 0:
        reply = random.choice(BASIC_REPLIES["not_understand"])
        print(reply)
        main()
    elif len(matched_issues) == 1:
        issue = next((item for item in ISSUES if item["name"].lower() == matched_issues[0].lower()), None)
        reply = random.choice(issue["reply"])
        print(f"\nYour selected issue is {colored(str(issue['name']), 'yellow')}\n\n{colored(reply,'cyan')}\n")
        print(random.choice(BASIC_REPLIES["more_help"]))
        main()
    elif len(matched_issues) >= 2:
        print(colored("Choose a specific issue you need help with:", "green"))
        for i, matched_issue in enumerate(matched_issues, start=1):
            print(colored(str(f"{i}. {matched_issue}"), "light_green"))
        user_choice = int(input(colored("Enter your issue number: ", "green")).strip())
        issue = next((item for item in ISSUES if item["name"].lower() == matched_issues[user_choice-1].lower()), None)
        reply = random.choice(issue["reply"])
        print(f"\nYour selected issue is {colored(str(issue['name']), 'yellow')}\n\n{colored(reply, 'cyan')}\n")
        print(random.choice(BASIC_REPLIES["more_help"]))
        main()

main()
