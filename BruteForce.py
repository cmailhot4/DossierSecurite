import time
import sys

def BruteForceFaible():
        return "abcdefghijklmnopqrstuvwxyz"
def BruteForceMoyen():
        return "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def BruteForceFort():
        return "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

force = sys.argv[1]
password = sys.argv[2]
motATrouver = []
motDePasse = []
trouver = False
motTrouver = []

for lettre in password:
 motDePasse.append(lettre)

if force == "faible":
 startTime = time.time()
 for lettre1 in BruteForceFaible():
  if trouver == False:
   for lettre2 in BruteForceFaible():
    if trouver == False:
     for lettre3 in BruteForceFaible():
      if trouver == False:
       for lettre4 in BruteForceFaible():
        if trouver == False:
         for lettre4 in BruteForceFaible():
          if trouver == False:
           for lettre5 in BruteForceFaible():
            motATrouver = [lettre1, lettre2, lettre3, lettre4, lettre5]
            if motATrouver == motDePasse:
             finTime = time.time()
             trouver = True
             motTrouver = motATrouver
 if trouver == True:
  print("Mot de passe:", ''.join(motTrouver))
  print("--- Trouve en %s secondes ---" %(finTime - startTime))
 else:
  print("Echec")
elif force == "moyen":
 startTime = time.time()
 for lettre1 in BruteForceMoyen():
  if trouver == False:
   for lettre2 in BruteForceMoyen():
    if trouver == False:
     for lettre3 in BruteForceMoyen():
      if trouver == False:
       for lettre4 in BruteForceMoyen():
        if trouver == False:
         for lettre4 in BruteForceMoyen():
          if trouver == False:
           for lettre5 in BruteForceMoyen():
            motATrouver = [lettre1, lettre2, lettre3, lettre4, lettre5]
            if motATrouver == motDePasse:
             finTime = time.time()
             trouver = True
             motTrouver = motATrouver
 if trouver == True:
  print("Mot de passe:", ''.join(motTrouver))
  print("--- Trouve en %s secondes ---" %(finTime - startTime))
 else:
  print("echec")
elif force == "fort":
 startTime = time.time()
 for lettre1 in BruteForceFort():
  if trouver == False:
   for lettre2 in BruteForceFort():
    if trouver == False:
     for lettre3 in BruteForceFort():
      if trouver == False:
       for lettre4 in BruteForceFort():
        if trouver == False:
         for lettre4 in BruteForceFort():
          if trouver == False:
           for lettre5 in BruteForceFort():
            motATrouver = [lettre1, lettre2, lettre3, lettre4, lettre5]
            if motATrouver == motDePasse:
             finTime = time.time()
             trouver = True
             motTrouver = motATrouver
 if trouver == True:
  print("Mot de passe:", ''.join(motTrouver))
  print("--- Trouve en %s secondes ---" %(finTime - startTime))
 else:
  print("Echec")
else:
 print("force non valide")
