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
        "name": "Enrolment",
        "reply": "If you wish to enrol for the first time, go to admissions.uni.lu",
    },
    {
        "name": "Reenrolment",
        "reply": "If you wish to get reenrolled, go to admissions.uni.lu",
    },
]

def get_input():
    user_input = input().lower().strip()
    check_keywords(user_input)

def check_keywords(user_input):
    user_words = set(user_input.split())

    for issue in issues:
        synonyms = set()
        
        synonyms.add(issue["name"].lower())

        for synset in wordnet.synsets(issue["name"]):
            for lemma in synset.lemmas():
                synonyms.add(lemma.name().lower())
        
        if user_words.intersection(synonyms):
            print(issue.get("reply", "No reply available"))
            return
    
    print("No recognized keywords found.")
    print(synonyms)

       


get_input()
