import json

DATA_FILE = "mood_entries.json"


def load_entries():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_entries(datas):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(datas, file, ensure_ascii=False, indent=2)


entries = load_entries()
    
new_entry = {
    "name": "مینا",
    "score": 5,
    "reason": "فهمیدن تابع"
}
new_entry_2 = {
    "name": "Ali",
    "score": 4,
    "reason": "تمرین پایتون"
}
new_entry_3 = {
    "name": "Ali",
    "score": 4,
    "reason": "تمرین پایتون"
}
new_entry_4 = {
    "name": "Ali",
    "score": 4,
    "reason": "تمرین پایتون"
}
invalid_entry = {
    "name": "Reza",
    "score": 8,
    "reason": "test"
}
def validate_score (score):
    if score>=1 and score<=5:
        return True
    else:
        return False

if validate_score(new_entry["score"]) == True:
    entries.append(new_entry)
if validate_score(new_entry_2["score"]) == True:
    entries.append(new_entry_2)
if validate_score(new_entry_3["score"]) == True:
    entries.append(new_entry_3)
if validate_score(new_entry_4["score"]) == True:
    entries.append(new_entry_4)
if validate_score(invalid_entry["score"]) == True:
    entries.append(invalid_entry)
save_entries(entries)

print(f"Saved {len(entries)} entries.")

scores=[]
for i in entries:
    scores.append(i["score"])
print("scores: ", scores)

def calculate_average(entries):
    return sum(scores)/len(scores)

print("Average score: ", calculate_average(entries))
