import random
import copy

print('')
print('RETO TÉCNICO CON PYTHON')

npr = 5
nre = 4
global pts
pts = 5
#npr = int(input("Escribe el numero de preguntas: "))
#nre = int(input("Escribe el numero de respuestas por pregunta: "))

preguntaNivel1 = []
respuestasNivel1= []
preguntaNivel2 = []
respuestasNivel2= []
preguntaNivel3 = []
respuestasNivel3= []
preguntaNivel4 = []
respuestasNivel4= []
preguntaNivel5 = []
respuestasNivel5= []

def ingresoPreguntas_Respuestas(preguntaNivel, respuestasNivel, niv):
    print(f'\nIngeso de preguntas & respuestas - NIVEL {niv}\n')
    for i in range(npr):
        pregunta = input(f'Ingresar pregunta {i+1}: ')
        #for j in range(nre-1):            
        #    respuestaIncorrecta = input(f'Ingresar respuesta incorrecta {j+1}: ')
        respuestaIncorrecta1 = input('Ingresar respuesta incorrecta 1: ')
        respuestaIncorrecta2 = input('Ingresar respuesta incorrecta 2: ')
        respuestaIncorrecta3 = input('Ingresar respuesta incorrecta 3: ')
        respuestaCorrecta = input('Ingresar respuests correcta: ')  
        print('')      
        preguntaNivel.append([pregunta])
        respuestasNivel.append([respuestaIncorrecta1, respuestaIncorrecta2, respuestaIncorrecta3, respuestaCorrecta])

def verPreguntas(preguntaNivel, respuestasNivel, niv):
    print(f'\n MENÚ VER PREGUNTAS NIVEL {niv}\n')
    opcion = 1
    while opcion != 0:
        for i in range(len(preguntaNivel)):
            print(f'\nPregunta {i+1}: {preguntaNivel[i]}')        
            print(f'Respuestas pregunta {i+1}: {respuestasNivel[i]}\n')
        print('\n 0. Regresar')
        opcion = int(input(' \n Escribe el numero cero (0) para regresar: '))

def irNivel(preguntaNivel, respuestasNivel, niv):
    print(f'\nDIFICULTAD NIVEL {niv}\n')
    respuestasNivelOrig = copy.deepcopy(respuestasNivel)
    respuestasNivelSelect = list(respuestasNivel)
    for _ in range(8):   
        p = random.randint(0, 4)  
    random.shuffle(respuestasNivelSelect[p-1])
    opcion = 5
    while opcion != 0:
        print(f'\nPregunta: {preguntaNivel[p-1][0]}\n')        
        print(f'1. Respuesta 1: {respuestasNivelSelect[p-1][0]}')
        print(f'2. Respuesta 2: {respuestasNivelSelect[p-1][1]}')
        print(f'3. Respuesta 3: {respuestasNivelSelect[p-1][2]}')
        print(f'4. Respuesta 4: {respuestasNivelSelect[p-1][3]}\n')

        print('0. Salir\n')
        global pts
        opcion = int(input("Escribe el numero de la opción de la respuesta correcta: "))
        print('')
        if respuestasNivelOrig[p-1][3] == respuestasNivelSelect[p-1][opcion-1]:            
            niv = niv + 1  
            print(f'\nNivel superado, tu acomulado de puntos es: {pts}\n')          
            if niv == 2:
                pts = pts + 10
                irNivel(preguntaNivel2, respuestasNivel2, 2)
            elif niv == 3: 
                pts = pts + 15               
                irNivel(preguntaNivel3, respuestasNivel3, 3)
            elif niv == 4: 
                pts = pts + 20              
                irNivel(preguntaNivel4, respuestasNivel4, 4)
            elif niv == 5:
                pts = pts + 25                                
                irNivel(preguntaNivel5, respuestasNivel5, 5)
            elif niv == 6:
                print('JUEGO COMPLETADO - FELICIDADES')                    
            else:
                break            
            break

        else:
            print('Respuesta incorrecta')

def menuConfigurar(opcion):
    while opcion != 0:
        print('')
        print('             MENÚ CONFIGURAR\n')
        print('1. Ingresar preguntas & respuestas - Nivel 1')
        print('2. Ingresar preguntas & respuestas - Nivel 2')
        print('3. Ingresar preguntas & respuestas - Nivel 3')
        print('4. Ingresar preguntas & respuestas - Nivel 4')
        print('5. Ingresar preguntas & respuestas - Nivel 5\n')
        
        print('6. Ver preguntas & respuestas - Nivel 1')
        print('7. Ver preguntas & respuestas - Nivel 2')
        print('8. Ver preguntas & respuestas - Nivel 3')
        print('9. Ver preguntas & respuestas - Nivel 4')
        print('10. Ver preguntas & respuestas - Nivel 5\n')

        print('0. Regresar\n')

        opcion = int(input("Escribe el numero de la opción: "))

        print('')
        if opcion == 1:
            ingresoPreguntas_Respuestas(preguntaNivel1, respuestasNivel1, 1)   
        elif opcion == 2:
            ingresoPreguntas_Respuestas(preguntaNivel2, respuestasNivel2, 2)    
        elif opcion == 3:
            ingresoPreguntas_Respuestas(preguntaNivel3, respuestasNivel3, 3)    
        elif opcion == 4:
            ingresoPreguntas_Respuestas(preguntaNivel4, respuestasNivel4, 4)    
        elif opcion == 5:
            ingresoPreguntas_Respuestas(preguntaNivel5, respuestasNivel5, 5)
                     
        elif opcion == 6:
            verPreguntas(preguntaNivel1, respuestasNivel1, 1)            
        elif opcion == 7:
            verPreguntas(preguntaNivel2, respuestasNivel2, 2)                     
        elif opcion == 8:
            verPreguntas(preguntaNivel3, respuestasNivel3, 3)                      
        elif opcion == 9:
            verPreguntas(preguntaNivel4, respuestasNivel4, 4)          
        elif opcion == 10:
            verPreguntas(preguntaNivel5, respuestasNivel5, 5)          
        else:
            print('\nEscribe una opción de nivel VALIDA entre 0 y 10 ')

def menuIniciarJuego():       
    opcion = 6
    while opcion != 0:
        print(' \nMENÚ INICIAR JUEGO\n')
        print('  1. Nivel 1')
        print('  2. Nivel 2')
        print('  3. Nivel 3')
        print('  4. Nivel 4')
        print('  5. Nivel 5\n')
        print('  0. Salir\n')
        opcion = int(input("Escribe el numero de la opción: "))
        if opcion == 1:
            irNivel(preguntaNivel1, respuestasNivel1, 1)
            False 
        elif opcion == 2:
            irNivel(preguntaNivel2, respuestasNivel2, 2)
            False   
        elif opcion == 3:
            irNivel(preguntaNivel3, respuestasNivel3, 3)
            False 
        elif opcion == 4:
            irNivel(preguntaNivel4, respuestasNivel4, 4)
            False
        elif opcion == 5:
            irNivel(preguntaNivel5, respuestasNivel5, 5)
            False       
        else:
            print('\nEscribe la opción de nivel VALIDA entre 1 y 5 ')        
        break
    
def menuPrincipal():    
    opcion = 3
    while opcion != 0:
        print('')
        print('    MENÚ PRINCIPAL\n')
        print('1. Configurar juego')
        print('2. Iniciar Juego\n')
        print('0. Salir\n')
        opcion = int(input("Escribe el numero de la opción: "))
        print('')

        if opcion == 1:
            menuConfigurar(opcion)    
        if opcion == 2:
            menuIniciarJuego()

menuPrincipal()
