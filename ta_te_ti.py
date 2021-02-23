def mostrar_tablero(tablero):
    print('\n\t\t | {} | {} | {} |'.format(tablero[7], tablero[8], tablero[9]))
    print('\t\t | {} | {} | {} |'.format(tablero[4], tablero[5], tablero[6]))
    print('\t\t | {} | {} | {} |\n'.format(tablero[1], tablero[2], tablero[3]))

def ingreso_jugada(tablero,turno):
    jugada = 0
    while True:
        entrada = input('Jugador {}, ingrese su jugada del 1 al 9 (De abajo hacia arriba, de izquierda a derecha): '.format(turno))
        if entrada.isdigit():
            jugada = int(entrada)
            if jugada in range(1,10):
                if tablero[jugada] == ' ':
                    break
                else:
                    print('El lugar que eligió ya está ocupado')
            else:
                print('Ingrese por favor un número dentro del rango')
        else:
            print('Ingrese por favor un número válido')
    return jugada

def jugar(tablero, letra, jugada):
    tablero[jugada] = letra

def ganador(ta, le):
    return ((ta[1] == le and ta[5] == le and ta[9] == le) or
    (ta[3] == le and ta[5] == le and ta[7] == le) or
    (ta[1] == le and ta[2] == le and ta[3] == le) or
    (ta[4] == le and ta[5] == le and ta[6] == le) or
    (ta[7] == le and ta[8] == le and ta[9] == le) or
    (ta[1] == le and ta[4] == le and ta[7] == le) or
    (ta[2] == le and ta[5] == le and ta[8] == le) or
    (ta[3] == le and ta[6] == le and ta[9] == le))

def tablero_completo(tablero):
    for i in range(1, 10):
        if tablero[i] == ' ':
            return False
    return True

print(':::::::::::::::::::::::::::::::::::::::::::::::::::')
print('::::::::::::Bienvenido al TA TE TI:::::::::::::::::')
print(':::::::::::::::::::::::::::::::::::::::::::::::::::')
tablero_juego = [' '] * 10
turno = '1'
jugando = True

while jugando:
    if turno == '1':
        mostrar_tablero(tablero_juego)
        jugada = ingreso_jugada(tablero_juego, turno)
        jugar(tablero_juego, 'X', jugada)

        if ganador(tablero_juego, 'X'):
            mostrar_tablero(tablero_juego)
            print('Felicitaciones jugador {}, ganaste la partida!'.format(turno))
            jugando = False
        else:
            if tablero_completo(tablero_juego):
                mostrar_tablero(tablero_juego)
                print('Ups... hubo un empate!')
                break
            else:
                turno = '2'

    else:
        mostrar_tablero(tablero_juego)
        jugada = ingreso_jugada(tablero_juego,turno)
        jugar(tablero_juego, 'O', jugada)

        if ganador(tablero_juego, 'O'):
            mostrar_tablero(tablero_juego)
            print('Felicitaciones jugador {}, ganaste la partida!'.format(turno))
            jugando = False
        else:
            if tablero_completo(tablero_juego):
                mostrar_tablero(tablero_juego)
                print('Ups... hubo un empate!')
                break
            else:
                turno = '1'