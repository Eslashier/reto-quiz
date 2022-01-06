from model_questions import Question
from model_score import Score
from model_quiz import Quiz
import sys 
import os
import pickle

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear') #Funcion para limpiar consola.



def main():

    clearConsole()
    print("*********************************")
    print("******Bienvenido a QuizRush******")
    print("*********************************")

    menu = input("Por favor seleccione una opcion: \n 1. Nuevo  juego \n 2. Ver historico de puntuaciones\n e. Salir\n")  #Menu inicial

    while menu not in ["1","2","3","e"]: #Estructura de control en caso de que el usuario no ingrese s o n
                        print("Por favor ingrese S para continuar N para terminar") #Se solicita nuevamente al usuario ingresar una respuesta 
                        menu = input()
                        menu = menu.lower()

    if menu == "1": #Se inicia el juego
        clearConsole()
        Quiz.run()
        main()

    elif menu == "2": #Se pueden ver los puntajes historicos
        clearConsole()
        Score.historic()
        main()

    elif menu == "3": # Opcion para guardar el set de preguntas en el archivo questions.p
        
        """
        questions = [Question(0, "¿Cuál es el libro más vendido de todos los tiempos?", "El libro más vendido es la biblia", "a)Don Quijote\nb)El Señor de los Anillos\nc)La Biblia\nd)Harry Potter y la piedra filosofal\n:", "c"), 
                    Question(0, "¿Cuál es el nombre de la actual Reina de Inglaterra? ", "La actual reina de inglaterra se llama Isabel", "a)Isabel\nb)Margarita\nc)Ana\nd)Victoria\n:", "a"),
                    Question(0, "¿Cuántos corazones tiene un pulpo?", "Los pulpos tienen 3 corazones", "a)2\nb)1\nc)4\nd)3\n:", "d"),
                    Question(0, "¿Cuántos huesos tiene el cuerpo humano?", "El cuerpo humano tiene 206 huesos", "a)189\nb)206\nc)210\nd)294\n:", "b"),
                    Question(0, "¿Cuál es el país más pequeño del mundo?", "El país más pequeño del mundo es el Vaticano", "a)El Vaticano\nb)Maldivas\nc)San Marino\nd)Nauru\n:", "a"),
                    Question(1,"¿Cuál es la primera película de Disney?", "La primera película de Disney es Blancanieves", "a)Blancanieves\nb)Dumbo\nc)Pinocho\nd)Bambi\n:", "a"),
                    Question(1,"¿Cuáles colores tiene la bandera de Italia?", "Los colores de la bandera de Italia son verde/blanco/rojo", "a)Negro Amarillo Rojo\nb)Verde Blanco Rojo\nc)Verde Amarillo Azul\nd)Amarillo Azul Blanco\n:", "b"),
                    Question(1,"¿De qué está hecho el sake japonés?", "El sake japonés está hecho de arroz", "a)Manzanas\nb)Trigo\nc)Maíz\nd)Arroz\n:", "d"),
                    Question(1,"¿Cuál es el río más largo del mundo?", "El río más largo del mundo es el Nilo", "a)Amazonas\nb)Nilo\nc)Misisipi\nd)Bravo\n:", "b"),
                    Question(1,"¿Quién pintó la Mona Lisa?", "La Mona Lisa fue pintada por Leonardo da Vinci", "a)Leonardo da Vinci\nb)Miguel Ángel\nc)Vincent van Gogh\nd)Sandro Botticelli\n:", "a"),
                    Question(2,"¿Cuál es el animal más grande del mundo?", "El animal más grande del mundo es la ballena azul", "a)Tiburón\nb)Rinoceronte\nc)Ballena azul\nd)Anaconda\n:", "c"),
                    Question(2,"¿Cuántas zonas horarias tiene Rusia?", "Rusia tiene once zonas horarias", "a)Cinco\nb)Once\nc)Siete\nd)Quince\n:", "b"),
                    Question(2,"¿Cuántos anillos olímpicos son?", "Son cinco anillos olímpicos", "a)Siete\nb)Cinco\nc)Cuatro\nd)Seis\n:", "b"),
                    Question(2,"¿Cuál es el planeta más pequeño de nuestro sistema solar?", "El planeta más pequeño del sistema solar es Mercurio", "a)Venus\nb)Tierra\nc)Mercurio\nd)Saturno\n:", "c"),
                    Question(2,"¿Cuál es la capital de Dinamarca?", "2 + 2 is 4", "a)Copenhague\nb)Estocolmo\nc)Reikiavik\nd)Oslo\n:", "a"),
                    Question(3,"¿Cuál fue el primer animal en la luna?", "El primer animal en la luna fue un perro", "a)Mandril\nb)Gato\nc)Ratón\nd)Perro\n:", "d"),
                    Question(3,"¿Cuántas teclas tiene un piano clásico?", "Un piano clásico tiene 88 teclas", "a)61\nb)49\nc)88\nd)37\n:", "c"),
                    Question(3,"¿Qué fuerza atrae todo hacia la tierra?", "La fuerza que atrae todo hacia la tierra es la gravedad", "a)Electromagnetismo\nb)Atracción\nc)Gravedad\nd)Nuclear\n:", "c"),
                    Question(3,"¿A qué le teme la acrofobia?", "La acrofibia es una fobia a las alturas", "a)Alturas\nb)Arañas\nc)Tormentas\nd)Sangre\n:", "a"),
                    Question(3,"¿Cuántas semanas tiene un año?", "Un año tiene 52 semanas", "a)56\nb)52\nc)51\nd)54\n:", "b"),
                    Question(4,"¿Cuándo se inventaron los LEGO?", "Los LEGO fueron inventados en 1958", "a)1958\nb)1944\nc)1963\nd)1951\n:", "a"),
                    Question(4,"¿Quién diseñó la Torre Eiffel?", "Gustave Eiffel diseño la Torre Eiffel", "a)Antoine Eiffel\nb)Belmont Eiffel\nc)Gustave Eiffel\nd)Dean Eiffel\n:", "c"),
                    Question(4,"¿Cómo se llama la luna más grande de Saturno?", "La luna más grande de Saturno se llama Titán", "a)Calipso\nb)Titán\nc)Pan\nd)Helena\n:", "b"),
                    Question(4,"¿Cuántos dientes permanentes tienen los perros?", "Los perros tienen 42 dientes permanentes", "a)40\nb)39\nc)35\nd)42\n:", "d"),
                    Question(4,"¿Cuál es el único continente donde no se encuentran especies de hormigas?", "El único continente donde no se encuentran hormigas es la Antártida", "a)Oceanía\nb)Antártida\nc)África\nd)Europa\n:", "b"),
                    ]
        

        pickle.dump( questions, open( "questions.p", "wb" ) ) #Guardar preguntas
        clearConsole()
        print("Se guardaron las preguntas en el archivo questions.p")
        """
        main()

    elif menu == "e": #salir del programa
        clearConsole()
        sys.exit("Programa terminado")

main()


        

    

    