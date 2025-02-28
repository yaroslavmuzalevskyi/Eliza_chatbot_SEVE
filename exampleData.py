issues = [
    {
        "name": "PHD",
        "reply": "Go to PDH office Mon-Fri",
    },
    {
        "name": "Housing",
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

    for issue in issues:
        if issue["name"].lower() in user_input:
            print(issue.get("reply", "No reply available"))
            return

       


get_input()
