from numpy import array, zeros
import random
lista=[]
tablou= zeros((9,9), int)
n=9
exista=0
lista_pozitii=[]
scor=0
for i in range(0,n):
    for j in range (0,n):
        tablou[i][j]=random.randint(1,4)
print ("Tablou dupa completare : ")
print (tablou)
def cautare_formatiuni_colt(tablou,lista):
    for i in range(0,n):
        for j in range (0,n):
            if j<n-2:
                for k in range(j,j+3):
                    lista.append(tablou[i][k])
                if len(set(lista))==1:
                    print ("colt")
                    print ("tablou[",i,"][",j,"]")
                    lista_pozitii.append(i)
                    lista_pozitii.append(j)
                    if i<n-2:
                        lista.append(tablou[i + 1][j])
                        lista.append(tablou[i + 2][j])
                        lista_pozitii.append(i+2)
                        lista_pozitii.append(j)
                        print ("lista=", lista)
                        print ("lista_pozitii=", lista_pozitii)
                        if len(set(lista)) == 1:
                            return lista_pozitii
                        else:
                            lista.pop()
                            lista.pop()
                            lista_pozitii.pop()
                            lista_pozitii.pop()
                    if i<n-2:
                        lista.append(tablou[i + 1][j+2])
                        lista.append(tablou[i + 2][j+2])
                        lista_pozitii.append(i + 2)
                        lista_pozitii.append(j+2)
                        print ("lista=", lista)
                        print ("lista_pozitii=", lista_pozitii)
                        if len(set(lista)) == 1:
                            return lista_pozitii
                        else:
                            lista.pop()
                            lista.pop()
                            lista_pozitii.pop()
                            lista_pozitii.pop()
                    if i>1:
                        lista.append(tablou[i-1][j])
                        lista.append(tablou[i-2][j])
                        lista_pozitii.append(i-2)
                        lista_pozitii.append(j)
                        print ("lista=", lista)
                        print ("lista_pozitii=", lista_pozitii)
                        if len(set(lista))==1:
                            return lista_pozitii
                        else:
                            lista.pop()
                            lista.pop()
                            lista_pozitii.pop()
                            lista_pozitii.pop()
                    if i>1:
                        lista.append(tablou[i-1][j+2])
                        lista.append(tablou[i-2][j+2])
                        lista_pozitii.append(i-2)
                        lista_pozitii.append(j+2)
                        print ("lista=", lista)
                        print ("lista_pozitii=",lista_pozitii)
                        if len(set(lista))==1:
                            return lista_pozitii
                        else:
                            lista.pop()
                            lista.pop()
                            lista_pozitii.pop()
                            lista_pozitii.pop()
                del lista[:]
                del lista_pozitii[:]
    return 0
def cautare_formatiuni_T_linie(tablou,lista):
    for i in range(0, n):
        for j in range(0, n):
            if j < n - 2:
                for k in range(j, j + 3):
                    lista.append(tablou[i][k])
                if len(set(lista)) == 1:
                    print ("T_linie")
                    print ("tablou[", i, "][", j, "]")
                    lista_pozitii.append(i)
                    lista_pozitii.append(j)
                    if i>1:
                        lista.append(tablou[i-1][j+1])
                        lista.append(tablou[i-2][j+1])
                        lista_pozitii.append(i - 2)
                        lista_pozitii.append(j + 1)
                        print ("lista=", lista)
                        print ("lista_pozitii=", lista_pozitii)
                        if len(set(lista))==1:
                            return lista_pozitii
                        else:
                            lista.pop()
                            lista.pop()
                            lista_pozitii.pop()
                            lista_pozitii.pop()
                    if i<n-2:
                        lista.append(tablou[i + 1][j + 1])
                        lista.append(tablou[i + 2][j + 1])
                        lista_pozitii.append(i+2)
                        lista_pozitii.append(j+1)
                        print ("lista=", lista)
                        print ("lista_pozitii=", lista_pozitii)
                        if len(set(lista)) == 1:
                            return lista_pozitii
                        else:
                            lista.pop()
                            lista.pop()
                            lista_pozitii.pop()
                            lista_pozitii.pop()
                del lista[:]
                del lista_pozitii[:]
    return 0
def cautare_formatiuni_T_coloana(tablou,lista):
    for i in range(0, n):
        for j in range(0, n):
            if i < n - 2:
                for k in range(i, i + 3):
                    lista.append(tablou[k][j])
                if len(set(lista)) == 1:
                    print ("T_coloana")
                    print ("tablou[", i, "][", j, "]")
                    lista_pozitii.append(i)
                    lista_pozitii.append(j)
                    if j>1:
                        lista.append(tablou[i+1][j-1])
                        lista.append(tablou[i+1][j-2])
                        lista_pozitii.append(i+1)
                        lista_pozitii.append(j-2)
                        print ("lista=", lista)
                        print ("lista_pozitii=", lista_pozitii)
                        if len(set(lista))==1:
                            return lista_pozitii
                        else:
                            lista.pop()
                            lista.pop()
                            lista_pozitii.pop()
                            lista_pozitii.pop()
                    if j<n-2:
                        lista.append(tablou[i + 1][j + 1])
                        lista.append(tablou[i + 1][j + 2])
                        lista_pozitii.append(i+1)
                        lista_pozitii.append(j+2)
                        print ("lista=", lista)
                        print ("lista_pozitii=", lista_pozitii)
                        if len(set(lista)) == 1:
                            return lista_pozitii
                        else:
                            lista.pop()
                            lista.pop()
                            lista_pozitii.pop()
                            lista_pozitii.pop()
                del lista[:]
                del lista_pozitii[:]
    return 0
def cautare_formatiuni_linie5(tablou,lista):
    for i in range(0,n):
        for j in range (0,n):
            if j<n-4:
                for k in range(j,j+5):
                    lista.append(tablou[i][k])
                if len(set(lista))==1:
                    print ("linie5")
                    print ("tablou[",i,"][",j,"]")
                    print ("lista=", lista)
                    lista_pozitii.append(i)
                    lista_pozitii.append(j)
                    lista_pozitii.append(i)
                    lista_pozitii.append(j + 4)
                    print ("lista_pozitii=", lista_pozitii)
                    return lista_pozitii
                del lista[:]
            del lista_pozitii[:]
    return 0
def cautare_formatiuni_linie4(tablou,lista):
    for i in range(0,n):
        for j in range (0,n):
            if j<n-3:
                for k in range(j,j+4):
                    lista.append(tablou[i][k])
                if len(set(lista))==1:
                    print ("linie4")
                    print ("tablou[",i,"][",j,"]")
                    print ("lista=", lista)
                    lista_pozitii.append(i)
                    lista_pozitii.append(j)
                    lista_pozitii.append(i)
                    lista_pozitii.append(j + 3)
                    print ("lista_pozitii=", lista_pozitii)
                    return lista_pozitii
                del lista[:]
            del lista_pozitii[:]
    return 0
def cautare_formatiuni_linie3(tablou,lista):
    for i in range(0,n):
        for j in range (0,n):
            if j<n-2:
                for k in range(j,j+3):
                    lista.append(tablou[i][k])
                if len(set(lista))==1:
                    print ("linie3")
                    print ("tablou[",i,"][",j,"]")
                    print ("lista=", lista)
                    lista_pozitii.append(i)
                    lista_pozitii.append(j)
                    lista_pozitii.append(i)
                    lista_pozitii.append(j + 2)
                    print ("lista_pozitii=", lista_pozitii)
                    return lista_pozitii
                del lista[:]
            del lista_pozitii[:]
    return 0
def cautare_formatiuni_coloana5(tablou,lista):
    for i in range(0, n):
        for j in range(0, n):
            if i < n - 4:
                for k in range(i, i + 5):
                    lista.append(tablou[k][j])
                if len(set(lista)) == 1:
                    print ("coloana5")
                    print ("tablou[", i, "][", j, "]")
                    print ("lista=", lista)
                    lista_pozitii.append(i)
                    lista_pozitii.append(j)
                    lista_pozitii.append(i+4)
                    lista_pozitii.append(j)
                    print ("lista_pozitii=", lista_pozitii)
                    return lista_pozitii
                del lista[:]
            del lista_pozitii[:]
    return 0
def cautare_formatiuni_coloana4(tablou,lista):
    for i in range(0, n):
        for j in range(0, n):
            if i < n - 3:
                for k in range(i, i + 4):
                    lista.append(tablou[k][j])
                if len(set(lista)) == 1:
                    print ("coloana4")
                    print ("tablou[", i, "][", j, "]")
                    print ("lista=", lista)
                    lista_pozitii.append(i)
                    lista_pozitii.append(j)
                    lista_pozitii.append(i + 3)
                    lista_pozitii.append(j)
                    print ("lista_pozitii=", lista_pozitii)
                    return lista_pozitii
                del lista[:]
            del lista_pozitii[:]
    return 0
def cautare_formatiuni_coloana3(tablou,lista):
    for i in range(0, n):
        for j in range(0, n):
            if i < n - 2:
                for k in range(i, i + 3):
                    lista.append(tablou[k][j])
                if len(set(lista)) == 1:
                    print ("coloana3")
                    print ("tablou[", i, "][", j, "]")
                    print ("lista=", lista)
                    lista_pozitii.append(i)
                    lista_pozitii.append(j)
                    lista_pozitii.append(i + 2)
                    lista_pozitii.append(j)
                    print ("lista_pozitii=", lista_pozitii)
                    return lista_pozitii
                del lista[:]
            del lista_pozitii[:]
    return 0
def eliminare_formatiuni_linie(tablou,lista,lista_pozitii):
    if len(lista_pozitii)==4:
        a=lista_pozitii[0]
        b=lista_pozitii[1]
        c=lista_pozitii[2]
        d=lista_pozitii[3]
        for i in range(b,b+3):
            tablou[a][i]=0
            if(c<=a):
                for j in range(c,a+1):
                    tablou[j][d]=0
            if(c>a):
                for j in range(a,c+1):
                    tablou[j][d]=0
    print ("Tablou inlocuit cu zerouri:")
    print (tablou)
def eliminare_formatiuni_coloana(tablou,lista,lista_pozitii):
    if len(lista_pozitii)==4:
        a = lista_pozitii[0]
        b = lista_pozitii[1]
        c = lista_pozitii[2]
        d = lista_pozitii[3]
        for i in range(a,a+3):
            tablou[i][b]=0
            if(d<=b):
                for j in range(d,b+1):
                    tablou[c][j]=0
            if(c>a):
                for j in range(b,d+1):
                    tablou[c][j]=0
    print ("Tablou inlocuit cu zerouri:")
    print (tablou)
def eliminare_formatiuni_linie_completa(tablou,lista,lista_pozitii):
    if len(lista_pozitii)==4:
        a = lista_pozitii[0]
        b = lista_pozitii[1]
        c = lista_pozitii[2]
        d = lista_pozitii[3]
        if(a==c):
            for i in range(b,d+1):
                tablou[a][i]=0
    print ("Tablou inlocuit cu zerouri:")
    print (tablou)
def eliminare_formatiuni_coloana_completa(tablou,lista,lista_pozitii):
    if len(lista_pozitii)==4:
        a = lista_pozitii[0]
        b = lista_pozitii[1]
        c = lista_pozitii[2]
        d = lista_pozitii[3]
        if(b==d):
            for i in range(a,c+1):
                tablou[i][b]=0
    print ("Tablou inlocuit cu zerouri:")
    print (tablou)
def recompletare_tablou_linie(tablou,lista,lista_pozitii):
    bool=1
    if len(lista_pozitii)==4:
        a = lista_pozitii[0]
        b = lista_pozitii[1]
        c = lista_pozitii[2]
        d = lista_pozitii[3]
    while bool==1:
        bool=0
        if a>c and c>0:
            for i in range(a,0,-1):
                for j in range(b,b+3):
                    if tablou[i][j]==0:
                        if i==a:
                            bool=1
                        tablou[i][j]=tablou[i-1][j]
                        tablou[i-1][j]=0
        if a<c and a>0:
            for i in range(c,0,-1):
                for j in range(b,b+3):
                    if tablou[i][j]==0:
                        if i==c:
                            bool=1
                        tablou[i][j]=tablou[i-1][j]
                        tablou[i-1][j]=0
    for i in range(0,n):
        for j in range(0,n):
            if tablou[i][j]==0:
                tablou[i][j]=random.randint(1,4)
    print ("Tablou dupa recompletare:")
    print (tablou)
def recompletare_tablou_coloana(tablou,lista,lista_pozitii):
    bool=1
    if len(lista_pozitii)==4:
        a = lista_pozitii[0]
        b = lista_pozitii[1]
        c = lista_pozitii[2]
        d = lista_pozitii[3]
        while bool==1:
            bool=0
            if (b<d):
                for i in range(c+1,1,-1):
                    for j in range(b,d+1):
                        if tablou[i][j]==0:
                            if j==d:
                                bool=1
                            tablou[i][j]=tablou[i-1][j]
                            tablou[i-1][j]=0
            if (b>d):
                for i in range(c+1,1,-1):
                    for j in range(b,d,-1):
                        if tablou[i][j]==0:
                            #if j==b:
                             #   bool=1
                            tablou[i][j]=tablou[i-1][j]
                            tablou[i-1][j]=0
    for i in range(0,n):
        for j in range(0,n):
            if tablou[i][j]==0:
                tablou[i][j]=random.randint(1,4)
    print ("Tablou dupa recompletare:")
    print (tablou)
def recompletare_tablou_linie_completa(tablou,lista,lista_pozitii):
    if len(lista_pozitii)==4:
        a = lista_pozitii[0]
        b = lista_pozitii[1]
        c = lista_pozitii[2]
        d = lista_pozitii[3]
        if a==c:
            for i in range(a,0,-1):
                for j in range(b,d+1):
                    tablou[i][j]=tablou[i-1][j]
                    tablou[i-1][j]=0
    for i in range(0,n):
        for j in range(0,n):
            if tablou[i][j]==0:
                tablou[i][j]=random.randint(1,4)
    print ("Tablou dupa recompletare:")
    print (tablou)
def recompletare_tablou_coloana_completa(tablou,lista,lista_pozitii):
    bool=1
    if len(lista_pozitii)==4:
        a = lista_pozitii[0]
        b = lista_pozitii[1]
        c = lista_pozitii[2]
        d = lista_pozitii[3]
        if (b==d)and (a>0):
            while bool==1:
                bool=0
                for i in range(c,0,-1):
                    tablou[i][b]=tablou[i-1][b]
                    tablou[i-1][b]=0
                    if tablou[c][b]==0:
                        bool=1
    for i in range(0,n):
        for j in range(0,n):
            if tablou[i][j]==0:
                tablou[i][j]=random.randint(1,4)
    print ("Tablou dupa recompletare:")
    print (tablou)
bool=1
while bool==1:
    bool=0
    if (cautare_formatiuni_linie5(tablou,lista)!=0):
        bool=1
        scor=scor+60
        eliminare_formatiuni_linie_completa(tablou, lista, lista_pozitii)
        recompletare_tablou_linie_completa(tablou, lista, lista_pozitii)
    else:
        if (cautare_formatiuni_coloana5(tablou,lista)!=0):
            bool=1
            scor=scor+60
            eliminare_formatiuni_coloana_completa(tablou, lista, lista_pozitii)
            recompletare_tablou_coloana_completa(tablou, lista, lista_pozitii)
        else:
            if(cautare_formatiuni_colt(tablou,lista)!=0):
                bool=1
                scor=scor+40
                eliminare_formatiuni_linie(tablou,lista,lista_pozitii)
                recompletare_tablou_linie(tablou, lista, lista_pozitii)
            else:
                if(cautare_formatiuni_T_linie(tablou,lista)!=0):
                    bool=1
                    scor=scor+30
                    eliminare_formatiuni_linie(tablou, lista, lista_pozitii)
                    recompletare_tablou_linie(tablou, lista, lista_pozitii)
                else:
                    if(cautare_formatiuni_T_coloana(tablou,lista)!=0):
                        bool=1
                        scor=scor+30
                        eliminare_formatiuni_coloana(tablou, lista, lista_pozitii)
                        recompletare_tablou_coloana(tablou, lista, lista_pozitii)
                    else:
                        if(cautare_formatiuni_linie4(tablou,lista)):
                            bool=1
                            scor=scor+20
                            eliminare_formatiuni_linie_completa(tablou, lista, lista_pozitii)
                            recompletare_tablou_linie_completa(tablou, lista, lista_pozitii)
                        else:
                            if(cautare_formatiuni_coloana4(tablou,lista)):
                                bool=1
                                scor=scor+20
                                eliminare_formatiuni_coloana_completa(tablou, lista, lista_pozitii)
                                recompletare_tablou_coloana_completa(tablou, lista, lista_pozitii)
                            else:
                                if(cautare_formatiuni_linie3(tablou,lista)):
                                    bool=1
                                    scor=scor+10
                                    eliminare_formatiuni_linie_completa(tablou, lista, lista_pozitii)
                                    recompletare_tablou_linie_completa(tablou, lista, lista_pozitii)
                                else:
                                    if(cautare_formatiuni_coloana3(tablou,lista)):
                                        bool=1
                                        scor=scor+10
                                        eliminare_formatiuni_coloana_completa(tablou, lista, lista_pozitii)
                                        recompletare_tablou_coloana_completa(tablou, lista, lista_pozitii)
for i in range(0,n):
    for j in range(0,n):
        aux = 0
        nr = 1
        if (i > 0) and (i < n - 1) and (j > 0) and (j < n - 1):
            if nr == 1 and bool == 0:
                nr = nr + 1
                aux = tablou[i][j]
                tablou[i][j] = tablou[i - 1][j]
                tablou[i - 1][j] = aux
                print ("mutare: a[",i,"][",j,"]->a[",i-1,"][",j,"]")
                if (cautare_formatiuni_linie5(tablou, lista) != 0):
                    scor = scor + 60
                    eliminare_formatiuni_linie_completa(tablou, lista, lista_pozitii)
                    recompletare_tablou_linie_completa(tablou, lista, lista_pozitii)
                else:
                    if (cautare_formatiuni_coloana5(tablou, lista) != 0):
                        bool=1
                        scor = scor + 60
                        eliminare_formatiuni_coloana_completa(tablou, lista, lista_pozitii)
                        recompletare_tablou_coloana_completa(tablou, lista, lista_pozitii)
                    else:
                        if (cautare_formatiuni_colt(tablou, lista) != 0):
                            bool = 1
                            scor = scor + 40
                            eliminare_formatiuni_linie(tablou, lista, lista_pozitii)
                            recompletare_tablou_linie(tablou, lista, lista_pozitii)
                        else:
                            if (cautare_formatiuni_T_linie(tablou, lista) != 0):
                                bool = 1
                                scor = scor + 30
                                eliminare_formatiuni_linie(tablou, lista, lista_pozitii)
                                recompletare_tablou_linie(tablou, lista, lista_pozitii)
                            else:
                                if (cautare_formatiuni_T_coloana(tablou, lista) != 0):
                                    bool = 1
                                    scor = scor + 30
                                    eliminare_formatiuni_coloana(tablou, lista, lista_pozitii)
                                    recompletare_tablou_coloana(tablou, lista, lista_pozitii)
                                else:
                                    if (cautare_formatiuni_linie4(tablou, lista)!=0):
                                        bool = 1
                                        scor = scor + 20
                                        eliminare_formatiuni_linie_completa(tablou, lista, lista_pozitii)
                                        recompletare_tablou_linie_completa(tablou, lista, lista_pozitii)
                                    else:
                                        if (cautare_formatiuni_coloana4(tablou, lista)!=0):
                                            bool = 1
                                            scor = scor + 20
                                            eliminare_formatiuni_coloana_completa(tablou, lista, lista_pozitii)
                                            recompletare_tablou_coloana_completa(tablou, lista, lista_pozitii)
                                        else:
                                            if (cautare_formatiuni_linie3(tablou, lista)!=0):
                                                bool = 1
                                                scor = scor + 10
                                                eliminare_formatiuni_linie_completa(tablou, lista, lista_pozitii)
                                                recompletare_tablou_linie_completa(tablou, lista, lista_pozitii)
                                            else:
                                                if (cautare_formatiuni_coloana3(tablou, lista)!=0):
                                                    bool = 1
                                                    scor = scor + 10
                                                    eliminare_formatiuni_coloana_completa(tablou, lista, lista_pozitii)
                                                    recompletare_tablou_coloana_completa(tablou, lista, lista_pozitii)
                    if bool == 0:
                        tablou[i - 1][j] = tablou[i][j]
                        tablou[i][j] = aux
                        aux = 0

print ("Scorul final este:")
print (scor)