"""
Papildināt programmu ar ciklu, kurā sarakstā esošiem uzvārdiem tiktu 
pievienots klāt doktora nosaukums - Dr.
"""

"""
saraksts1=["Kalniņš", "Opmanis", "Vēzis", "Almane"]
saraksts2=[]

for uzvards in saraksts1:
    doktors="Dr. "+uzvards
    saraksts2.append(doktors)

print(saraksts2)
"""    

saraksts1=["Kalniņš", "Opmanis", "Vezis", "Almane"]
saraksts2=[]
def pievienot_dokt(uzvards):
    return "Dr. "+uzvards

saraksts2=list(map(pievienot_dokt, saraksts1))
print(saraksts2)
    
