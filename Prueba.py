import colorama
import os
import time
import numpy as np
from colorama import Fore

colorama.init(autoreset=True)

def print_maze(maze):
    for row in maze:
        for column in row:
            if column == 1:
                print("#", end='')
            elif column == 0:
                print(" ", end='')
            else:
                print(column, end=' ')
        print()
        

def imprimir_bueno(maze, x, y):
    maze[x][y] = 'X'
    print("El laberinto está de la siguiente forma:")



    for i in maze:
        for j in i:
            if j == 1:
                print("#", end='')
            elif j == 0:
                print(" ", end='')
            elif j == 'X':
                print(Fore.GREEN + "X", end='')
            elif j == 'Y':
                print(Fore.RED + "X", end='')

            else:
                print(j, end=' ')
        print()
    print("\n\n\n\n\n")

def imprimir_malo(maze,x,y):
    maze[x][y] = 'Y'
    print("El laberinto está de la siguiente forma:")



    for i in maze:
        for j in i:
            if j == 1:
                print("#", end='')
            elif j == 0:
                print(" ", end='')
            elif j == 'X':
                print(Fore.GREEN + "X", end='')
            elif j == 'Y':
                print(Fore.RED + "X", end='')

            else:
                print(j, end=' ')
        print()
    print("\n\n\n\n\n")






def resolver_laberinto(maze, start, goal):
    x, y = start
    dir_index = 0  # Comienza mirando hacia la derecha (0, 1)
    visitadas = set()  # donde van a ir los visitados
    
    def backtrack(x, y, dir_index):
        # visitamos la posición actual
        visitadas.add((x, y))
        #print(f"Estamos en la posicion {x,y}")
        imprimir_bueno(maze, x, y)
        time.sleep(0.2)
        os.system('cls')
        
        if (x, y) == goal: #finaliza
            print("¡Salida encontrada en:", x,y)
            return True
        
        for _ in range(4):
            nueva_direccion = (dir_index + 1) % 4
            nx, ny = x + direcciones[nueva_direccion][0], y + direcciones[nueva_direccion][1]
            
            if (nx, ny) not in visitadas and maze[nx][ny] == 0:
                #print(f"Estamos en la posicion {nx,ny}")
                if backtrack(nx, ny, nueva_direccion):
                    return True
            
            dir_index = nueva_direccion  # giramos a la derecha para la próxima iteración
        
        # si llegamos a callejón sin salida, regresamos
        visitadas.remove((x, y))
        imprimir_malo(maze, x,y)
        os.system('cls')
        time.sleep(0.2)
        return False
    
    if not backtrack(x, y, dir_index):
        print("No se encontró una salida en el laberinto.")



def obtener_inicio_final(maze):
    array = np.array(maze)
    inicio = np.argwhere(array == 'S')
    final = np.argwhere(array == 'M')

    

    return inicio, final






matriz = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 'M', 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    ['S', 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]



direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]



inicio, final = obtener_inicio_final(matriz) #obtenemos el inicio y el final (nos devolverá un arreglo)
xInicio, yInicio = inicio[0][0], inicio[0][1] #el arreglo que tenemos lo descomponemos en x y y para tener las variables separadas
xFinal, yFinal = final[0][0], final[0][1]

matriz[xFinal][yFinal] = 0 #borramos la variable M del laberinto y la convertimos en un cero para que se pueda detectar

#creamos las variables como tuplas con las posiciones de inicio y final
start = (xInicio, yInicio)
goal = (xFinal, yFinal)
# Print the maze
print_maze(matriz)
resolver_laberinto(matriz, start, goal)





