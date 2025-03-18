import firebase_admin
import matplotlib.pyplot as plt
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("firebaseKeyFinal.json")
firebase_admin.initialize_app(cred, {'databaseURL':'https://connecttojvacode-default-rtdb.europe-west1.firebasedatabase.app/'})
ref = db.reference('/CleanData')#reference the root node of the databaset

#pulls collums
def get_FullName():
    ref = db.reference('/CleanData/Full Name')
    Full_Name = ref.get()
    return Full_Name

Name = get_FullName()


def get_Age():
    ref = db.reference('/CleanData/Age')
    Age = ref.get()
    return Age
def get_Nationality():
    ref = db.reference('/CleanData/Nationality')
    Nationality = ref.get()
    return Nationality

def get_Club():
    ref = db.reference('/CleanData/Club Name')
    Club = ref.get()
    return Club

def get_Overall():
    ref = db.reference('/CleanData/Overall')
    Overall = ref.get()
    return Overall

def get_Value():
    ref = db.reference('/CleanData/Value')
    Value = ref.get()
    return Value

def get_Position():
    ref = db.reference('/CleanData/Position')
    Position = ref.get()
    return Position

def get_Pace():
    ref = db.reference('/CleanData/Pace')
    Pace = ref.get()
    return Pace

def get_Shooting():
    ref = db.reference('/CleanData/Shooting')
    Shooting = ref.get()
    return Shooting

def get_Passing():
    ref = db.reference('/CleanData/Passing')
    Passing = ref.get()
    return Passing

def get_Dribbling():
    ref = db.reference('/CleanData/Dribbling')
    Dribbling = ref.get()
    return Dribbling

def get_Defending():
    ref = db.reference('/CleanData/Defending')
    Defending = ref.get()
    return Defending

def get_Physicality():
    ref = db.reference('/CleanData/Physicality')
    Physicality = ref.get()
    return Physicality


def get_Foot():
    ref = db.reference('/CleanData/Foot')
    Foot = ref.get()
    return Foot

def get_Wage():
    ref = db.reference('/CleanData/Wage')
    Wage = ref.get()
    return Wage

Name = get_FullName()
Age = get_Age()
Club = get_Club()
Nationality = get_Nationality()
Overall = get_Overall()
Value = get_Value()
Position = get_Position()
Pac = get_Pace()
Sho = get_Shooting()
Pas = get_Passing()
Dri = get_Dribbling()
Def = get_Defending()
Phy = get_Physicality()
Foot = get_Foot()
Wage = get_Wage()



#graph1
cubratings = []
Clubratings1 = []
x = 0
players = 0
clubschecked = []
TeamKey = []
TeamVal = []
 
print("start")
for x in range(18538):
    club = Club[x]
    if club not in clubschecked:
        A = club
        clubschecked.append(A)
#print(clubschecked)

for i in range(len(clubschecked)):
    Clubratings1 = []
    for x in range(18538):
        A = clubschecked[i]
        if Club[x] == A:
            Clubratings1.append((Overall[x]))
            players = players + 1
    #print(A)
    TeamKey.append(A)
    #print(Clubratings1)
    players = len(Clubratings1)
    Average = round((sum(Clubratings1))/players)
    TeamVal.append(Average)
    #print(Average)  

print(TeamKey)
print(TeamVal)

Teams = TeamKey
AvOvr = TeamVal

plt.bar(Teams, AvOvr)
plt.title('Clubs in fifas Average Overall Rating')
plt.xlabel('Club Names')
plt.xticks(rotation=90)
plt.ylabel('Average Overall Rating')
#plt.show()

#graph2
Countrykey = []
Countrykey2 = []

Nationalityschecked = []
nationfoot = []
Lefties = []
Righties = []
print("start")
for x in range(18538):
    Nation = Nationality[x]
    if Nation not in Nationalityschecked:
        A = Nation
        Nationalityschecked.append(A)
print(Nationalityschecked)

for i in range(len(Nationalityschecked)):
    nationfoot = []
    for x in range(18538):
        A = Nationalityschecked[i]
        if Nationality[x] == A:
            nationfoot.append((Foot[x]))
    Countrykey.append(A + " Left")
    Lefties.append(nationfoot.count("Left"))
for i in range(len(Nationalityschecked)):
    nationfoot = []
    for x in range(18538):
        A = Nationalityschecked[i]
        if Nationality[x] == A:
            nationfoot.append((Foot[x]))
    Countrykey2.append(A + " Right")
    Righties.append(nationfoot.count("Right"))
print(Countrykey2)
print(Righties)
print(Lefties)
FootRandL = Righties + Lefties
print(FootRandL)
FootRandLPer = []
for i in range (len(FootRandL)):
    total = sum(FootRandL)
    percent = (FootRandL[i]/total)*100
    FootRandLPer.append(percent)
Countrykeys3 = Countrykey2 + Countrykey
    
print(FootRandLPer)
print(sum(FootRandLPer))


labels = Countrykeys3
sizes = FootRandLPer
print(len(labels))
print(len(sizes))


labels = tuple(Countrykeys3)
fig, ax = plt.subplots()
#ax.title('Comparing left and right foot data from nations')
ax.pie(sizes, labels=labels, rotatelabels= 270,labeldistance=0.7)
plt.show()
