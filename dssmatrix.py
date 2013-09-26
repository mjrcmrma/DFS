__author__="Manuel"
__date__ ="$Sep 19, 2013 12:43:00 PM$"

import random
from copy import copy, deepcopy

if __name__ == "__main__":
    global ciclo
    global r_ancla
    global c_ancla
    ciclo = 0
    r_ancla = 0
    c_ancla = 0
    def generar_matriz():
        global matriz 
        global matriz2
        global matriz3
        matriz = [[random.randrange(1,30) for x in xrange(10)] for y in xrange(10)]
        matriz3 = [[0 for x in xrange(10)] for y in xrange(10)]
        matriz2 = deepcopy(matriz)
        print "Original: "
        for i in matriz:
            print i
        matriz[0][0] = 0
        matriz[9][9] = 0
        ordenar_copiar()

    def ordenar_copiar():
        i = 0
        print "Ordenada: "
        while ( i < 10):
            matriz2[i].sort(reverse = True)
            print matriz2[i]
            i = i +1
        promediar_mayores(matriz2)
    
    def promediar_mayores(matriz2):
        i = 0
        global suma
        suma = 0
        while ( i < 10):
            suma = matriz2[0][1] + suma
            i = i + 1
        suma = suma / 10
        print "Promedio: %d" % suma
        for i in matriz:
            print i
        remplazar(suma)
    
    def remplazar(suma):
        global diferencia 
        diferencia = 0
        global fin
        fin = 0
        while (diferencia <= suma and fin == 0):
            for i in range(0, len(matriz2)):
                for j in range(0, len(matriz2)):
                    if ((matriz[i][j] == (suma + diferencia)) or (matriz[i][j] == (suma - diferencia))):
                        matriz[i][j] = 0
                    matriz3[i][j] = 0
            diferencia = diferencia + 1
        print "Reemplazada: "
        for i in matriz:
            print i
        fin = buscar_camino(0,0,matriz3)

    def buscar_camino(r_ancla, c_ancla, matriz3):
        fin = 0
        if(r_ancla == 9 and c_ancla == 9):
            fin = 1
            print "\nLo encontre"
        if (c_ancla < 9 and fin == 0):
            if(matriz[r_ancla][c_ancla + 1] == 0 and matriz3[r_ancla][c_ancla + 1] == 0):
                matriz3[r_ancla][c_ancla + 1] = 1
                fin = buscar_camino(r_ancla,c_ancla + 1, matriz3)
        if (c_ancla > 0 and fin == 0):
            if(matriz[r_ancla][c_ancla - 1] == 0 and matriz3[r_ancla][c_ancla - 1] == 0):
                matriz3[r_ancla][c_ancla - 1] = 1
                fin = buscar_camino(r_ancla,c_ancla - 1, matriz3)
        if (r_ancla < 9 and fin == 0):
            if(matriz[r_ancla + 1][c_ancla] == 0 and matriz3[r_ancla + 1][c_ancla]== 0):
                matriz3[r_ancla + 1][c_ancla] = 1
                fin = buscar_camino(r_ancla + 1, c_ancla, matriz3);
        if(r_ancla > 0 and fin == 0):
            if(matriz[r_ancla - 1][c_ancla] == 0 and matriz3[r_ancla - 1][c_ancla] == 0):
                matriz3[r_ancla - 1][c_ancla] = 1
                fin = buscar_camino(r_ancla - 1,c_ancla, matriz3);
        if(fin == 1):
            print "\n%d,%d" % (r_ancla,c_ancla)
        
        return fin;
                
    generar_matriz()
                    