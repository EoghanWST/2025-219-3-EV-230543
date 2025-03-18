import firebase_admin
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


#Team average overall
cubratings = []
Clubratings1 = []
x = 0
players = 0
clubschecked = []
TeamKey = []
TeamVal = []
 
#print("start")
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

#print(len(TeamKey))
#print(TeamVal)
    
   

# Create dictionary using zip
TeamsOverall_dict = dict(zip(TeamKey, TeamVal))
#print(TeamsOverall_dict)




ref = db.reference('/TeamsOvr')#reference the root node of the database
for key,value in TeamsOverall_dict.items():
    #print(key,'---',value)#if key contains . replace with ''
    key = key.replace('.','')
    #print(key)    
    ref.update({key:value})
    
    


PlayerKey = []
PlayerRatings = []
for x in range(18538):
    playerName = (Name[x])
    PlayerRatings.append([Pac[x], Dri[x], Sho[x], Def[x], Pas[x], Phy[x]])
    PlayerKey.append(playerName)
    #print(PlayerRatings)
    #print(PlayerKey)
    
PlayerRatings_dict = dict(zip(PlayerKey, PlayerRatings))
print(PlayerRatings_dict)

ref = db.reference('/PlayerRatings')#reference the root node of the database
for key,value in PlayerRatings_dict.items():
    #print(key,'---',value)#if key contains . replace with ''
    key = key.replace('.','')
    #print(key)    
    ref.update({key:value})



#left foot right foot

Countrykey = []
Countrykey2 = []

Nationalityschecked = []
nationfoot = []
Lefties = []
Righties = []
#print("start")
for x in range(18538):
    Nation = Nationality[x]
    if Nation not in Nationalityschecked:
        A = Nation
        Nationalityschecked.append(A)
#print(Nationalityschecked)

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
    #print(A)
    Countrykey2.append(A + " Right")
    Righties.append(nationfoot.count("Right"))

FootCount_dict = dict(zip(Countrykey, Lefties ))
RFootCount_dict = dict(zip(Countrykey2, Righties ))
FootCount_dict.update(RFootCount_dict)
#print(FootCount_dict)



#print(RFootCount_dict)
#print(LFootCount_dict)
 


ref = db.reference('/FootnationCount')#reference the root node of the database
for key,value in FootCount_dict.items():
    #print(key,'---',value)#if key contains . replace with ''
    key = key.replace('.','')
    #print(key)    
    ref.update({key:value})




# Average player wages

Nationkey3 = []
Averagewage = []
for i in range(len(Nationalityschecked)):
    nationwages = []
    for x in range(18538):
        A = Nationalityschecked[i]
        if Nationality[x] == A:
            nationwages.append((Wage[x]))
    Nationkey3.append(A)
    players = len(nationwages)
    nationtotwage = sum(nationwages)
    Averagewage.append(nationtotwage/players)
print(Nationkey3)
print(Averagewage)



# Create dictionary using zip
Countriesavwage_dict = dict(zip(Nationkey3, Averagewage))
#print(Countriesavwage_dict)



ref = db.reference('/AvNationPlayerWages')#reference the root node of the database
for key,value in Countriesavwage_dict.items():
    #print(key,'---',value)#if key contains . replace with ''
    key = key.replace('.','')
    #print(key)    
    ref.update({key:value})
    
"""
""" 
# Average Nation Player ratings

Nationkey3 = []
AveragRatingN = []
players3 = []
for i in range(len(Nationalityschecked)):
    nationrating = []
    for x in range(18538):
        A = Nationalityschecked[i]
        if Nationality[x] == A:
            nationrating.append((Overall[x]))
    Nationkey3.append(A)
    players = len(nationrating)
    nationtotrat = sum(nationrating)
    AveragRatingN.append(nationtotrat/players)
print(Nationkey3)
print(AveragRatingN)



# Create dictionary using zip
Countriesavrate_dict = dict(zip(Nationkey3, AveragRatingN))
print(Countriesavrate_dict)



ref = db.reference('/AvNationPlayerRatings')#reference the root node of the database
for key,value in Countriesavrate_dict.items():
    #print(key,'---',value)#if key contains . replace with ''
    key = key.replace('.','')
    #print(key)    
    ref.update({key:value})
