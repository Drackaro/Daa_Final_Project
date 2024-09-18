def main():
    # Leer el número de edificios
    n = int(input())
    
    # Leer las cadenas que representan las clases programadas en cada edificio y los profesores en cada edificio
    c = input().strip()  # `c` es el array de clases programadas en cada edificio
    p = input().strip()  # `p` es el array de los profesores en cada edificio
    
    # Crear una lista de listas para categorizar los edificios según su desajuste
    g = [[] for _ in range(6)]
    #  g  | p[i]| c[i]
    # [0] |  C  |  -
    # [1] |  M  |  C
    # [2] |  -  |  M
    # [3] |  M  |  -
    # [4] |  C  |  M
    # [5] |  -  |  C

    # Iterar sobre cada edificio
    for i in range(n):
        # Si el profesor y la clase coinciden, no es necesario hacer nada
        if p[i] == c[i]:
            continue
        
        # Clasificar los edificios según el tipo de profesor y la clase que necesitan
        if p[i] == 'C':
            if c[i] == '-':
                g[0].append(i + 1)  # Edificios con profesor de CC y sin clase programada
            else:
                g[4].append(i + 1)  # Edificios con profesor de CC y clase de Matemáticas
        elif p[i] == 'M':
            if c[i] == '-':
                g[3].append(i + 1)  # Edificios con profesor de Matemáticas y sin clase programada
            else:
                g[1].append(i + 1)  # Edificios con profesor de Matemáticas y clase de CC
        elif p[i] == '-':
            if c[i] == 'C':
                g[5].append(i + 1)  # Edificios sin profesor y clase de CC
            else:
                g[2].append(i + 1)  # Edificios sin profesor y clase de Matemáticas
    
    # Lista para almacenar las operaciones a realizar
    ans = []
    
    # Función para realizar la operación de recoger o dejar a un profesor
    def put(i, ty):
        assert len(g[i]) > 0
        ans.append((g[i].pop(), ty))
    
    # Caso 1: Hay más profesores de M en edificios con clase de CC que viceversa
    if len(g[1]) > len(g[4]):
        put(0, 1)  # Recoger a un profesor de CC de un edificio sin clases
        while len(g[4]): # Mientras queden edificios con profesores de CC pero clase de M
            put(1, 3)  # Ir a un edificio con clase de CC con un profesor de M, para dejar al profesor de CC que se está llevando y recoger el de M
            put(4, 3)  # Ir a un edificio con clase de M con un profesor de CC, para dejar al profesor de M que se está llevando y recoger el de CC
        put(1, 3)  # Dejar al profesor de CC que se está llevando en un edificio donde hay uno de M y recoger al de M
        if len(g[2]):
            put(2, 2)  # Si hay algun edificio vacío y con clases de M se deja al profesor de M que se está llevando
        ans[-1] = (ans[-1][0], 2)  # Actualizar la última operación para indicar que es un DROP (Suprimir un hipotético PICK innecesario)
        
        while len(g[1]): # Si aún quedan profesores de M en edificios con clase de CC
            put(0, 1)  # Recoger a un profesor de CC de un edificio sin clases
            put(1, 3)  # Ir a un edificio con clase de CC con un profesor de M, para dejar al profesor de CC que se está llevando y recoger el de M
            if len(g[2]): 
                put(2, 2) # Si hay algun edificio vacío y con clases de M se deja al profesor de M que se está llevando
            ans[-1] = (ans[-1][0], 2)  # Actualizar la última operación para indicar que es un DROP (Suprimir un hipotético PICK innecesario)
        while len(g[5]): # Si aún quedan edificios vacíos con clase de CC programada
            put(0, 1)  # Recoger a un profesor de CC de un edificio sin clases
            put(5, 2)  # Dejar al profesor de CC en el edificio con clase de CC que está vacío
        while len(g[2]): # Si aún quedan edificios vacíos con clase de M programada
            put(3, 1)  # Recoger a un profesor de M de un edificio sin clases
            put(2, 2)  # Dejar al profesor de M en el edificio con clase de M que está vacío
    
    # Caso 2: Hay más profesores de CC en edificios con clase de M que viceversa.
    elif len(g[1]) < len(g[4]):
        put(3, 1)  # Recoger a un profesor de M de un edificio sin clases
        while len(g[1]): # Mientras queden edificios con profesores de M pero clase de CC
            put(4, 3)  # Ir a un edificio con clase de M con un profesor de CC, para dejar al profesor de M que se está llevando y recoger el de CC
            put(1, 3)  # Ir a un edificio con clase de CC con un profesor de M, para dejar al profesor de CC que se está llevando y recoger el de M
        put(4, 3) # Dejar al profesor de M que se está llevando en un edificio donde hay uno de CC y recoger al de CC
        if len(g[5]):
            put(5, 2)  # Si hay algun edificio vacío y con clases de CC se deja al profesor de CC que se está llevando
        ans[-1] = (ans[-1][0], 2)  # Actualizar la última operación para indicar que es un DROP (Suprimir un hipotético PICK innecesario)
        
        while len(g[4]): # Si aún quedan profesores de CC en edificios con clase de M
            put(3, 1)  # Recoger a un profesor de M de un edificio sin clases
            put(4, 3)  # Ir a un edificio con clase de M con un profesor de CC, para dejar al profesor de M que se está llevando y recoger el de CC
            if len(g[5]):
                put(5, 2)  # Si hay algun edificio vacío y con clases de CC se deja al profesor de CC que se está llevando
            ans[-1] = (ans[-1][0], 2)  # Actualizar la última operación para indicar que es un DROP (Suprimir un hipotético PICK innecesario)
        while len(g[2]): # Si aún quedan edificios vacíos con clase de M programada
            put(3, 1)  # Recoger a un profesor de M de un edificio sin clases
            put(2, 2)  # Dejar al profesor de M en el edificio con clase de M que está vacío
        while len(g[5]): # Si aún quedan edificios vacíos con clase de CC programada
            put(0, 1)  # Recoger a un profesor de CC de un edificio sin clases
            put(5, 2)  # Dejar al profesor de CC en el edificio con clase de CC que está vacío
    
    # Caso 3: Hay la misma cantidad de profesores de M en edificios con clases de CC que viceversa
    else:
        if len(g[1]): #Si hay edificios con profesores de M pero con clases de CC
            if len(g[0]): # Si hay edificios con profesor de CC sin clase programada
                put(0, 1)  # Recoger a un profesor de CC de un edificio sin clases
                while len(g[1]): #Mientras haya edificios con profesores de M pero con clases de CC
                    put(1, 3)  # Ir a un edificio con clase de CC con un profesor de M, para dejar al profesor de CC que se está llevando y recoger el de M
                    put(4, 3)  # Ir a un edificio con clase de M con un profesor de CC, para dejar al profesor de M que se está llevando y recoger el de CC
                if len(g[5]):
                    put(5, 2)  # Si hay algun edificio vacío y con clases de CC se deja al profesor de CC que se está llevando
                ans[-1] = (ans[-1][0], 2)  # Actualizar la última operación para indicar que es un DROP (Suprimir un hipotético PICK innecesario)
            else:
                # Si no hay edificios con profesor de CC sin clase programada
                assert len(g[3])  # Tiene que existir al menos un edificio con profesor de M y sin clase programada, sino el problema no tiene solución
                put(3, 1)  # Recoger a un profesor de M de un edificio sin clases
                while len(g[4]): # Mientras hayan profesores de CC en edificios con clase de M
                    put(4, 3)  # Ir a un edificio con clase de M con un profesor de CC, para dejar al profesor de M que se está llevando y recoger el de CC
                    put(1, 3)  # Ir a un edificio con clase de CC con un profesor de M, para dejar al profesor de CC que se está llevando y recoger el de M
                if len(g[2]):
                    put(2, 2)  # Si hay algun edificio vacío y con clases de M se deja al profesor de M que se está llevando
                ans[-1] = (ans[-1][0], 2)  # Actualizar la última operación para indicar que es un DROP (Suprimir un hipotético PICK innecesario)
        
        while len(g[2]): # Si aún quedan edificios vacíos con clase de M programada
            put(3, 1)  # Recoger a un profesor de M de un edificio sin clases
            put(2, 2)  # Dejar al profesor de M en el edificio con clase de M que está vacío
        while len(g[5]): # Si aún quedan edificios vacíos con clase de CC programada
            put(0, 1)  # Recoger a un profesor de CC de un edificio sin clases
            put(5, 2)  # Dejar al profesor de CC en el edificio con clase de CC que está vacío
    
    # Crear el listado final de comandos
    cmds = []
    for v, c in ans:
        cmds.append(f"DRIVE {v}")  # Agregar el comando DRIVE para ir al edificio v
        if c // 2:
            cmds.append("DROPOFF")  # Si c es par, agregar el comando DROPOFF
        if c % 2:
            cmds.append("PICKUP")  # Si c es impar, agregar el comando PICKUP
    
    # Imprimir el número total de comandos y cada comando
    print(len(cmds))
    for cmd in cmds:
        print(cmd)
 
if __name__ == "__main__":
    main()