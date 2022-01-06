from model_questions import Question
from model_score import Score
import os
import random
import pickle

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear') # Función para limpiar pantalla

questions = pickle.load( open( "questions.p", "rb" ) ) # Se cargan las preguntas desde el archivo save.p

class Quiz:
        
    def run():
        difficulty = 0 #Se inicializa la variable de puntuación del usuario
        while difficulty < 5 : #Loop que usa la puntuación como nivel, en la estructura el nivel 0 es el 1, el 1 es el 2, etc.

            while True:
                question = random.choice(questions) #Se selecciona de forma aleatoria la pregunta que cumpla la condicion del nivel
                if question.level == difficulty:
                    break
            print("Pregunta de nivel ",difficulty + 1) #Se imprime el nivel actual de la pregunta
            print(question.question) #Se imprime la pregunta
            user_answer = input(question.choices) #Se imprime las respuestas
            user_answer = user_answer.lower() #Control de entrada, todos los elementos escritos se devuelven en minusculas para las estructuras de control siguientes

            while user_answer not in ["a","b","c","d"]: #Loop como estructura de control en caso de que el usuario no ingrese la respuesta a, b, c, o d.
                print("Por favor ingrese una respuesta valida (a,b,c,d)")  #Se solicita nuevamente al usuario ingresar una respuesta 
                user_answer = input()
                user_answer = user_answer.lower()

            if user_answer in question.correct: #Si la respuesta dada coincide con la guardada el puntaje aumenta en 1
                clearConsole()
                print("¡Respuesta correcta!")
                difficulty += 1

                if difficulty == 5: #Si la puntuación alcanza el maximo de 5 se rompe el loop injicial.
                    score = 1000*difficulty
                    print("¡FELICITACIONES HAS GANADO! \n Tu puntaje es :",score, "pts") #Se imprime la puntuación de la partida.
                    user = input("Por favor ingrese su nick o iniciales\n") #Se solicita el nombre de usuario
                    Score.update(user,score) #Se llama la funcion para actualizar o agregar usuario y puntaje.
                    break

                else:
                    score = 1000*difficulty
                    print("Tu puntaje es:",score, "pts") #Cada vez que se responde de forma correcta se muestra el puntaje de la partida actual
                    print("La siguiente pregunta será de nivel ",difficulty+1) #Cada vez que se responde de forma correcta se muestra el puntaje de la partida actual
                    print("Desea continuar (s/n):") #Se pregunta si el usuario desea continuar o retirarse de la partida.
                    control = input()
                    control = control.lower()

                    while control not in ["s","n"]: #Estructura de control en caso de que el usuario no ingrese s o n
                        print("Por favor ingrese S para continuar N para terminar") #Se solicita nuevamente al usuario ingresar una respuesta 
                        control = input()
                        control = control.lower()

                    if control == "n": #Si el usuario no desea continuar en partida
                        print("Tu puntaje final es ", score, "pts") #Se imprime la puntuación de la partida actual finalizada
                        print("Has llegado al nivel", difficulty) #Se imprime el nivel alcanzado
                        user = input("Por favor ingrese su nick o iniciales\n") #Se solicita el nombre de usuario
                        Score.update(user,score) #Se llama la funcion para actualizar o agregar usuario y puntaje.
                        break

                clearConsole()

            else: #Si la respuesta es incorrecta.
                clearConsole()
                score = 0  #Puntuación de la partida actual es 0
                print("Respuesta incorrecta, ", question.answer)
                print("Juego finalizado")
                print("Tu puntaje es ", score, "pts") #Se imprime la puntuación de la partida actual finalizada
                user = input("Por favor ingrese su nick o iniciales\n") #Se solicita el nombre de usuario
                Score.update(user,score) #Se llama la funcion para actualizar o agregar usuario y puntaje.
                break

      
