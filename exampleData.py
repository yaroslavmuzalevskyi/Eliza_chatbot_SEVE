from nltk.corpus import wordnet

issues = [
    {
        "name": "PHD",
        "reply": "Go to PDH office Mon-Fri",
    },
    {
        "name": "home",
        "reply": "You will sooner get expelled than get your contract renewed",
    },
    {
        "name": "enrol",
        "reply": "If you wish to enrol for the first time, go to admissions.uni.lu",
    },
    {
        "name": "Reenrolment",
        "reply": "If you wish to get reenrolled, go to admissions.uni.lu",
    },
]

def get_synonyms(word):
    synonyms = set()
    for synset in wordnet.synsets(word):
        for lemma in synset.lemmas():
            synonyms.add(lemma.name().lower())
    return synonyms

def check_keywords(user_input):
    user_words = set(user_input.lower().split())
    
    user_synonyms = set(user_words)
    for word in user_words:
        user_synonyms.update(get_synonyms(word))
    
    for issue in issues:
        issue_name = issue["name"].lower()
        issue_synonyms = get_synonyms(issue_name)

        if issue_name in user_synonyms or user_synonyms.intersection(issue_synonyms):
            print(issue["reply"])
            return
    print("No matching issue found.")

def main():
    user_input = input("Enter your query: ").strip()
    check_keywords(user_input)



       
main()
