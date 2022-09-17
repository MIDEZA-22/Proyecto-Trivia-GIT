import time

NEGRITA         = '\033[1m'
RESET_NEGRITA   = '\033[0m'
RED             = '\033[31m'
GREEN           = '\033[32m'
MAGENTA         = '\033[35m'
YELLOW          = '\033[33m'
BLUE            = '\033[34m'
RESET_COLOR     = '\033[39m'

puntaje = 0

iniTrivia = True
intentos = 0

promedio = 0

#ENCABEZADO
print(YELLOW + "*************************************************************" + RESET_COLOR)
print(YELLOW + "*** ¿Qué tanto sabes sobre Historia del Perú y Universal? ***" + RESET_COLOR)
print(YELLOW + "*************************************************************" + RESET_COLOR)
time.sleep(1)
print(NEGRITA + RED + "\nINDICACIÓN: Responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta. Ademas, cada respuesta correcta equivale a 1 punto y contarás con varios intentos.\n"+ RESET_COLOR + RESET_NEGRITA)
time.sleep(3)
nombre = input("\n¿Cual es tu nombre?: ")
while not nombre.isalpha():
  nombre = input("Ingresa tu nombre correctamente: ")
print("Bienvenido " + GREEN + NEGRITA + f"{nombre.upper()}" + RESET_NEGRITA + RESET_COLOR + ", tienes" + NEGRITA + RED + f" {puntaje} " + RESET_NEGRITA + RESET_COLOR + "puntos\n")
time.sleep(1)

while iniTrivia == True:
    
    intentos += 1
    puntaje = 0

    print(RED + "\n*********************" + RESET_COLOR)
    print(RED + f"*** INTENTO N° {intentos} ***" + RESET_COLOR)
    print(RED + "*********************\n" + RESET_COLOR)
    input("Presiona 'Enter' para continuar...\n")
    print("\nLoading...")
    time.sleep(1)
    print("Loading...")
    time.sleep(1)
    print("Loading...\n")
    time.sleep(1)

    #PREGUNTA N° 1
    print(YELLOW + "\n*********************** PREGUNTA [1/10] **********************" + RESET_COLOR)
    print(
    """
1. Los Chancas, pueblo que estuvo a punto de derrotar a los Incas, vivieron en lo que ahora es:

    A. Junín
    B. Puno
    C. Apurímac
    D. Lima
    """
    )

    rpta_1 = input("Tu respuesta es la letra: ").upper()

    while rpta_1 not in ("A", "B", "C", "D"):
        rpta_1 = input("Debes responder A, B, C o D. Ingresa nuevamente tu respuesta: ").upper()

    if rpta_1 != "C":
        print(RED + "\n|------------------------------------------------------------|" + RESET_COLOR)
        print(RED + "|------------------- RESPUESTA INCONRRECTA ------------------|" + RESET_COLOR)
        print(RED + "|------------------------------------------------------------|\n" + RESET_COLOR)
        time.sleep(1)
    else:
        puntaje += 1
        print(BLUE + "\n|------------------------------------------------------------|" + RESET_COLOR)
        print(BLUE + "|-------------------- RESPUESTA  CORRECTA -------------------|" + RESET_COLOR)
        print(BLUE + "|------------------------------------------------------------|\n" + RESET_COLOR)
        time.sleep(1)

    #PREGUNTA N° 2
    print(YELLOW + "\n*********************** PREGUNTA [2/10] **********************" + RESET_COLOR)
    print(
    """
2. ¿En qué año llegó Cristóbal Colón al continente Americano?:

    A. 1490
    B. 1492
    C. 1500
    D. 1961
    """
    )

    rpta_2 = input("Tu respuesta es la letra: ").upper()

    while rpta_2 not in ("A", "B", "C", "D"):
        rpta_2 = input("Debes responder A, B, C o D. Ingresa nuevamente tu respuesta: ").upper()

    if rpta_2 != "B":
        print(RED + "\n|------------------------------------------------------------|" + RESET_COLOR)
        print(RED + "|------------------- RESPUESTA INCONRRECTA ------------------|" + RESET_COLOR)
        print(RED + "|------------------------------------------------------------|\n" + RESET_COLOR)
        time.sleep(1)
    else:
        puntaje += 1
        print(BLUE + "\n|------------------------------------------------------------|" + RESET_COLOR)
        print(BLUE + "|-------------------- RESPUESTA  CORRECTA -------------------|" + RESET_COLOR)
        print(BLUE + "|------------------------------------------------------------|\n" + RESET_COLOR)
        time.sleep(1)

    #PREGUNTA N° 3
    print(YELLOW + "\n*********************** PREGUNTA [3/10] **********************" + RESET_COLOR)
    print(
    """
3. ¿Quién fue el primer emperador romano?:

    A. Julio Cesar
    B. Cesar Augusto
    C. Claudio
    D. Trajano
    """
    )

    rpta_3 = input("Tu respuesta es la letra: ").upper()

    while rpta_3 not in ("A", "B", "C", "D"):
        rpta_3 = input("Debes responder A, B, C o D. Ingresa nuevamente tu respuesta: ").upper()

    if rpta_3 != "B":
        print(RED + "\n|------------------------------------------------------------|" + RESET_COLOR)
        print(RED + "|------------------- RESPUESTA INCONRRECTA ------------------|" + RESET_COLOR)
        print(RED + "|------------------------------------------------------------|\n" + RESET_COLOR)
        time.sleep(1)
    else:
        puntaje += 1
        print(BLUE + "\n|------------------------------------------------------------|" + RESET_COLOR)
        print(BLUE + "|-------------------- RESPUESTA  CORRECTA -------------------|" + RESET_COLOR)
        print(BLUE + "|------------------------------------------------------------|\n" + RESET_COLOR)
        time.sleep(1)

    #PREGUNTA N° 4
    print(YELLOW + "\n*********************** PREGUNTA [4/10] **********************" + RESET_COLOR)
    print(
    """
4. ¿En qué país nació Adolfo Hitler?:

    A. Austria
    B. Polonia
    C. Alemania
    D. Rusia
    """
    )

    rpta_4 = input("Tu respuesta es la letra: ").upper()

    while rpta_4 not in ("A", "B", "C", "D"):
        rpta_4 = input("Debes responder A, B, C o D. Ingresa nuevamente tu respuesta: ").upper()

    if rpta_4 != "A":
        print(RED + "\n|------------------------------------------------------------|" + RESET_COLOR)
        print(RED + "|------------------- RESPUESTA INCONRRECTA ------------------|" + RESET_COLOR)
        print(RED + "|------------------------------------------------------------|\n" + RESET_COLOR)
        time.sleep(1)
    else:
        puntaje += 1
        print(BLUE + "\n|------------------------------------------------------------|" + RESET_COLOR)
        print(BLUE + "|-------------------- RESPUESTA  CORRECTA -------------------|" + RESET_COLOR)
        print(BLUE + "|------------------------------------------------------------|\n" + RESET_COLOR)
        time.sleep(1)

    #PREGUNTA N° 5
    print(YELLOW + "\n*********************** PREGUNTA [5/10] **********************" + RESET_COLOR)
    print(
    """
5. ¿Cómo se llamó el primer presidente de Estados Unidos?:

    A. Abraham Lincoln
    B. Thomas Jefferson
    C. George Washington
    D. Donald Trump
    """
    )

    rpta_5 = input("Tu respuesta es la letra: ").upper()

    while rpta_5 not in ("A", "B", "C", "D"):
        rpta_5 = input("Debes responder A, B, C o D. Ingresa nuevamente tu respuesta: ").upper()

    if rpta_5 != "C":
        print(RED + "\n|------------------------------------------------------------|" + RESET_COLOR)
        print(RED + "|------------------- RESPUESTA INCONRRECTA ------------------|" + RESET_COLOR)
        print(RED + "|------------------------------------------------------------|\n" + RESET_COLOR)
        time.sleep(1)
    else:
        puntaje += 1
        print(BLUE + "\n|------------------------------------------------------------|" + RESET_COLOR)
        print(BLUE + "|-------------------- RESPUESTA  CORRECTA -------------------|" + RESET_COLOR)
        print(BLUE + "|------------------------------------------------------------|\n" + RESET_COLOR)
        time.sleep(1)

    #PREGUNTA N° 6
    print(YELLOW + "\n*********************** PREGUNTA [6/10] **********************" + RESET_COLOR)
    print(
    """
6. ¿Cómo se llamó el presidente más joven del Perú?:

    A. Luis Sánchez Cerro
    B. Felipe Santiago Salaverry
    C. Alan García Pérez
    D. Valentin Paniagua
    """
    )

    rpta_6 = input("Tu respuesta es la letra: ").upper()

    while rpta_6 not in ("A", "B", "C", "D"):
        rpta_6 = input("Debes responder A, B, C o D. Ingresa nuevamente tu respuesta: ").upper()

    if rpta_6 != "B":
        print(RED + "\n|------------------------------------------------------------|" + RESET_COLOR)
        print(RED + "|------------------- RESPUESTA INCONRRECTA ------------------|" + RESET_COLOR)
        print(RED + "|------------------------------------------------------------|\n" + RESET_COLOR)
        time.sleep(1)
    else:
        puntaje += 1
        print(BLUE + "\n|------------------------------------------------------------|" + RESET_COLOR)
        print(BLUE + "|-------------------- RESPUESTA  CORRECTA -------------------|" + RESET_COLOR)
        print(BLUE + "|------------------------------------------------------------|\n" + RESET_COLOR)
        time.sleep(1)

    #PREGUNTA N° 7
    print(YELLOW + "\n*********************** PREGUNTA [7/10] **********************" + RESET_COLOR)
    print(
    """
7. La guerra de Las Malvinas se dio entre estos países:

    A. Chile y Argentina
    B. Chile e Inglaterra
    C. Argentina e Inglaterra
    D. Argentina y Chile
    """
    )

    rpta_7 = input("Tu respuesta es la letra: ").upper()

    while rpta_7 not in ("A", "B", "C", "D"):
        rpta_7 = input("Debes responder A, B, C o D. Ingresa nuevamente tu respuesta: ").upper()

    if rpta_7 != "C":
        print(RED + "\n|------------------------------------------------------------|" + RESET_COLOR)
        print(RED + "|------------------- RESPUESTA INCONRRECTA ------------------|" + RESET_COLOR)
        print(RED + "|------------------------------------------------------------|\n" + RESET_COLOR)
        time.sleep(1)
    else:
        puntaje += 1
        print(BLUE + "\n|------------------------------------------------------------|" + RESET_COLOR)
        print(BLUE + "|-------------------- RESPUESTA  CORRECTA -------------------|" + RESET_COLOR)
        print(BLUE + "|------------------------------------------------------------|\n" + RESET_COLOR)
        time.sleep(1)

    #PREGUNTA N° 8
    print(YELLOW + "\n*********************** PREGUNTA [8/10] **********************" + RESET_COLOR)
    print(
    """
8. Potencias que conformaron el Eje en la Segunda Guerra Mundial:

    A. Alemania, Italia y Japón
    B. Alemania, España e Italia
    C. Alemania, Japón y Rusia
    D. Alemania, Francia y Japón
    """
    )

    rpta_8 = input("Tu respuesta es la letra: ").upper()

    while rpta_8 not in ("A", "B", "C", "D"):
        rpta_8 = input("Debes responder A, B, C o D. Ingresa nuevamente tu respuesta: ").upper()

    if rpta_8 != "A":
        print(RED + "\n|------------------------------------------------------------|" + RESET_COLOR)
        print(RED + "|------------------- RESPUESTA INCONRRECTA ------------------|" + RESET_COLOR)
        print(RED + "|------------------------------------------------------------|\n" + RESET_COLOR)
        time.sleep(1)
    else:
        puntaje += 1
        print(BLUE + "\n|------------------------------------------------------------|" + RESET_COLOR)
        print(BLUE + "|-------------------- RESPUESTA  CORRECTA -------------------|" + RESET_COLOR)
        print(BLUE + "|------------------------------------------------------------|\n" + RESET_COLOR)
        time.sleep(1)

    #PREGUNTA N° 9
    print(YELLOW + "\n*********************** PREGUNTA [9/10] **********************" + RESET_COLOR)
    print(
    """
9. ¿En qué gobierno se logró la participación política de la mujer mediante el sufragio en el Perú?:

    A. Fernando Belaunde Terry
    B. Manuel Odría
    C. Juan Velasco Alvarado
    D. Alan García Pérez
    """
    )

    rpta_9 = input("Tu respuesta es la letra: ").upper()

    while rpta_9 not in ("A", "B", "C", "D"):
        rpta_9 = input("Debes responder A, B, C o D. Ingresa nuevamente tu respuesta: ").upper()

    if rpta_9 != "B":
        print(RED + "\n|------------------------------------------------------------|" + RESET_COLOR)
        print(RED + "|------------------- RESPUESTA INCONRRECTA ------------------|" + RESET_COLOR)
        print(RED + "|------------------------------------------------------------|\n" + RESET_COLOR)
        time.sleep(1)
    else:
        puntaje += 1
        print(BLUE + "\n|------------------------------------------------------------|" + RESET_COLOR)
        print(BLUE + "|-------------------- RESPUESTA  CORRECTA -------------------|" + RESET_COLOR)
        print(BLUE + "|------------------------------------------------------------|\n" + RESET_COLOR)
        time.sleep(1)

    #PREGUNTA N° 10
    print(YELLOW + "\n********************** PREGUNTA [10/10] **********************" + RESET_COLOR)
    print(
    """
10. Fecha del atentado contra las Torres Gemelas de Nueva York:

    A. 11 de septiembre de 2000
    B. 11 de septiembre de 2001 
    C. 11 de septiembre de 2002
    D. 11 de septiembre de 2003
    """
    )

    rpta_10 = input("Tu respuesta es la letra: ").upper()

    while rpta_10 not in ("A", "B", "C", "D"):
        rpta_10 = input("Debes responder A, B, C o D. Ingresa nuevamente tu respuesta: ").upper()

    if rpta_10 != "B":
        print(RED + "\n|------------------------------------------------------------|" + RESET_COLOR)
        print(RED + "|------------------- RESPUESTA INCONRRECTA ------------------|" + RESET_COLOR)
        print(RED + "|------------------------------------------------------------|\n" + RESET_COLOR)
        time.sleep(1)
    else:
        puntaje += 1
        print(BLUE + "\n|------------------------------------------------------------|" + RESET_COLOR)
        print(BLUE + "|-------------------- RESPUESTA  CORRECTA -------------------|" + RESET_COLOR)
        print(BLUE + "|------------------------------------------------------------|\n" + RESET_COLOR)
        time.sleep(1) 
  
    if puntaje>=0 and puntaje<4:
        print(GREEN + NEGRITA + "\n>>>>>>>> " + f"{nombre.upper()}" + ", OBTUVISTE" + f" {puntaje} PUNTOS = " + RESET_COLOR + RED + "MALO " + RESET_COLOR + GREEN + ">>>>>>>>\n" + RESET_COLOR + RESET_NEGRITA)
        time.sleep(2)
    elif puntaje>3 and puntaje<8:
        print(GREEN + NEGRITA + "\n>>>>>>>> " + f"{nombre.upper()}" + ", OBTUVISTE" + f" {puntaje} PUNTOS = " + RESET_COLOR + YELLOW + "BUENO " + RESET_COLOR + GREEN + ">>>>>>>>\n" + RESET_COLOR + RESET_NEGRITA)
        time.sleep(2)
    elif puntaje>7 and puntaje<11:
        print(GREEN + NEGRITA + "\n>>>>>>>> " + f"{nombre.upper()}" + ", OBTUVISTE" + f" {puntaje} PUNTOS = " + RESET_COLOR + BLUE + "EXCELENTE " + RESET_COLOR + GREEN + ">>>>>>>>\n" + RESET_COLOR + RESET_NEGRITA)
        time.sleep(2)

    promedio += puntaje
    total = promedio/intentos
  
    print(RED + "\n**********************************************" + RESET_COLOR)
    print(RED + "*** ¿Deseas intentar la trivia nuevamente? ***" + RESET_COLOR)
    print(RED + "**********************************************\n" + RESET_COLOR)

    repTrivia = input("Ingresa 'SI' para repetir, o cualquier tecla para finalizar: ").upper()

    if repTrivia != "SI":
        print("\n\nHasta pronto " + GREEN + NEGRITA + f"{nombre.upper()}, " + RESET_NEGRITA + "en tus " + GREEN + NEGRITA + f"{intentos} " + RESET_NEGRITA + "intentos obtuviste un promedio de: " + GREEN + NEGRITA + f"{round(total,2)} " + RESET_NEGRITA + "puntos")
        iniTrivia = False
    