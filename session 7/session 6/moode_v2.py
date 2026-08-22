
datas = [
    {"name": "ali", "score": 4, "reason": "alpha"},
    {"name": "ahamd", "score": 2, "reason": "beta"},
    {"name": "reza", "score": 1, "reason": "delta"},
    {"name": "mohammad", "score": 5, "reason": "alpha"},
    {"name": "mahdi", "score": 3, "reason": "beta"},
]

def get_mood_status(score: int):
    if score == 5:
        status = "excellent"
    elif score == 4:
        status = "good"
    elif score ==3:
        status = "normal"
    elif score < 3:
        status = "needs attention"
    return status

num_needs_attention = 0
sum_mood=0
for data in datas:
    user_status = get_mood_status(data["score"])
    sum_mood=data["score"]+sum_mood
    data["status"] = user_status
    print(data["name"], user_status, data)

    if data["status"] == "needs attention":
        num_needs_attention+=1

print("tedad_needs_attiontion: ", num_needs_attention)

#Gozaresh nahaie
tedad_kol_afrad=len(datas)
miangin_mood=sum_mood/len(datas)
def status_koli(miangin_mood):
    if miangin_mood == 5:
        status_koli = "excellent"
    elif miangin_mood >= 4 and miangin_mood<5:
        status_koli = "good"
    elif miangin_mood < 4 and miangin_mood >= 3:
        status_koli = "normal"
    elif miangin_mood < 3:
        status_koli = "needs attention"
    return status_koli

status_koli_class=status_koli(miangin_mood)

Gozaresh_nahaie={
    "tedad_kol_afrad: ": tedad_kol_afrad,
   "miangin_mood: ": miangin_mood,
   "tedad_needs_attiontion: ": num_needs_attention,
   "vaziat_koli_class: ": status_koli_class
   }

print(Gozaresh_nahaie)