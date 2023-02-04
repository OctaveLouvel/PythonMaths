def PGCD(a, b):

  #Déclaration des valeurs de suivi
  r = 1

  #Revoie si l'un des deux nombres est 0
  if a == 0 or b == 0:
    return 

  #Algorithme d'Euclide
  while True:
    r = a % b
    if r == 0:
      return b
    a = b
    b = r

def euBizout(a, b):

  #Déclaration des valeurs de suivis 
  r, f, C, m = 1, 0, [], False
  #r: reste; f: nombres d'itérations ; C: tableau contenant les coef; m: condition pour l'inversement entre a et b

  #Revoie si l'un des deux nombres est 0
  if a == 0:
    return "0 n'est pas valable"
  elif b == 0:
    return "0 n'est pas valable"
   elif a < b:
      #On inverse les valeurs de a et b pour avoir des résultats corrects
    ab = a
    a = b
    b = ab
    m = True
  elif PGCD(a,b) != 1:
    return "Non Premiers entre eux"
  print("Premiers entres eux")

  #Algorithme d'Euclide
  while r != 0:
    r = a % b
    c = (a - r) / b
    a = b
    b = r
    #On stocke les valeur des coeficients
    if r != 0 and c != 0:
      C.append(c)
      f = f + 1

  #On déclare les valeurs qui vont nous aider à remonter l'algo. v: on garde le nombre d'iterations pour le réutiliser à la fin; X et Y: tableau contenant toute les étapes pour remonter jusqu'aux réponses
  v = f - 2
  X, Y = [], []
  #On initialise X et Y
  X.append(-C[f - 1])
  Y.append(C[f - 1] * C[f - 2] + 1)

  #On remonte l'agorithme d'Euclide avec une formule de suite conjecturée
  for i in range(v):
    Y.append(Y[i] * (-C[f - 3]) + X[i])
    X.append(Y[i])
    f = f - 1

  #On retourne la réponse sous forme de tableau et on inverse X et Y si besoin 
  if m:
    R = [Y[v], X[v]]
  elif not m:
    R = [X[v], Y[v]]
  return R

#euBizout renvoie un tableau de valeur qu'on affiche (on peut aussi le faire depuis la console)
print(euBizout(0, 5))