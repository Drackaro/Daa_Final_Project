def main():
    # Leer la cantidad de edificios en el campus
    n = int(input())
    
    # Leer el estado actual de los profesores (b) y las clases asignadas (a)
    b = input().strip()  # Profesores (C: Ciencias de la Computación, M: Matemáticas, -: vacío)
    a = input().strip()  # Clases (C: Ciencias de la Computación, M: Matemáticas, -: vacío)
    
    # Crear 6 grupos para clasificar los edificios según su estado
    g = [[] for _ in range(6)]
    
    # Recorrer cada edificio para clasificarlo según el desajuste entre profesor y clase
    for i in range(n):
        if a[i] == b[i]:
            continue  # Si el profesor ya está en su clase correcta, no hacemos nada
        if a[i] == 'C':
            # Si se necesita un profesor de ciencias de la computación en el edificio
            g[b[i] == '-' and 0 or 4].append(i + 1)
        elif a[i] == 'M':
            # Si se necesita un profesor de matemáticas en el edificio
            g[b[i] == '-' and 3 or 1].append(i + 1)
        elif a[i] == '-':
            # Si no se necesita profesor en este edificio
            g[b[i] == 'C' and 5 or 2].append(i + 1)

    # Lista para almacenar los movimientos que vamos a realizar
    ans = []

    # Función auxiliar para agregar un movimiento (put) de un profesor en un edificio
    def put(i, ty):
        assert len(g[i]) > 0
        ans.append((g[i].pop(), ty))  # Se saca el último profesor del grupo y se añade el tipo de operación

    # Empezamos a balancear el número de profesores en los edificios según el desajuste
    if len(g[1]) > len(g[4]):  # Más profesores de matemáticas necesitan ser colocados
        put(0, 1)  # Mover un profesor de un edificio vacío (g[0])
        while len(g[4]):  # Mientras haya edificios que necesiten profesores de ciencias de la computación
            put(1, 3)  # Llevar profesores de matemáticas donde hacen falta
            put(4, 3)  # Llevar profesores de ciencias de la computación donde hacen falta
        put(1, 3)  # Último ajuste para completar el ciclo
        if len(g[2]):
            put(2, 2)  # Ajustar profesores de ciencias de la computación donde no hace falta
        ans[-1] = (ans[-1][0], 2)  # Última operación es un DROPOFF

        while len(g[1]):  # Repetir el proceso para todos los edificios desajustados
            put(0, 1)
            put(1, 3)
            if len(g[2]):
                put(2, 2)
            ans[-1] = (ans[-1][0], 2)
        while len(g[5]):
            put(0, 1)
            put(5, 2)
        while len(g[2]):
            put(3, 1)
            put(2, 2)

    elif len(g[1]) < len(g[4]):  # Más profesores de ciencias de la computación necesitan ser colocados
        put(3, 1)
        while len(g[1]):
            put(4, 3)
            put(1, 3)
        put(4, 3)
        if len(g[5]):
            put(5, 2)
        ans[-1] = (ans[-1][0], 2)

        while len(g[4]):
            put(3, 1)
            put(4, 3)
            if len(g[5]):
                put(5, 2)
            ans[-1] = (ans[-1][0], 2)
        while len(g[2]):
            put(3, 1)
            put(2, 2)
        while len(g[5]):
            put(0, 1)
            put(5, 2)

    else:  # Caso donde hay el mismo número de profesores desajustados
        if len(g[1]):
            if len(g[0]):
                put(0, 1)
                while len(g[1]):
                    put(1, 3)
                    put(4, 3)
                if len(g[5]):
                    put(5, 2)
                ans[-1] = (ans[-1][0], 2)
            else:
                assert len(g[3])
                put(3, 1)
                while len(g[4]):
                    put(4, 3)
                    put(1, 3)
                if len(g[2]):
                    put(2, 2)
                ans[-1] = (ans[-1][0], 2)

        while len(g[2]):
            put(3, 1)
            put(2, 2)
        while len(g[5]):
            put(0, 1)
            put(5, 2)

    # Generar la lista de comandos según los movimientos realizados
    cmds = []
    for v, c in ans:
        cmds.append(f"DRIVE {v}")
        if c // 2:
            cmds.append("DROPOFF")
        if c % 2:
            cmds.append("PICKUP")
    
    # Imprimir la cantidad de movimientos y los comandos correspondientes
    print(len(cmds))
    for cmd in cmds:
        print(cmd)

# Ejecutar el programa
if __name__ == "__main__":
    main()
