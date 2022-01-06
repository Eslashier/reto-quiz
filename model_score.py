import pickle

class Score:
    def __init__(self, user, score,):
        self.user = user
        self.score = score

    def update(user,score): #Funcion para actualizar o escribir puntuaciones
        hscores = pickle.load( open( "scores.p", "rb" ) )
        x=0 #Contador para recorrer hscores
        cx = 0 #variable de control, si es 1 se reescribe la variable score del respectivo usuario, si es 0 se registra una nueva entrada

        while x<len(hscores): #loop para recorrer estructura hscores
                   
            if user == hscores[x].user: #condicional para buscar el usuario, si coincide se asigna a cx valor 1 y se rompe el loop.
                cx = 1
                break

            x += 1 #Sino se cumple la condición aumenta el contador

        if cx == 1: #Si el usuario existe
            hscores[x].score = hscores[x].score + score #Se le suma a la variable score el puntaje obtenido en el juego actual
            print("Tu puntaje actual es de", hscores[x].score) #Se escribe en pantalla el puntaje historico del usuario
            pickle.dump( hscores, open( "scores.p", "wb" ) ) #Se reescribe el archivo scores.p con la información actualizada
            input("Presione enter para volver")
        else: #Si el usuario no existe
            userscore = Score(user,score) #Se crea un nuevo objeto con las propiedades de Score
            hscores.append(userscore) #Se anexa el nuevo objeto a la estructura
            pickle.dump( hscores, open( "scores.p", "wb" ) ) #Se reescribe el archivo scores.p con la información añadida
            input("Presione enter para volver")

    def historic():

        #hscores = [Score("andres",5), 
        #    ]  #Estructura de prueba, y para iniciar archivo
        #pickle.dump( hscores, open( "scores.p", "wb" ) ) #Iniciar archivo de datos
        
        hscores = pickle.load( open( "scores.p", "rb" ) ) #Cargar datos
        
        x=0 #Contador para recorrer hscores

        print ("Nombre de usuario".ljust(40) + "Puntuacion") #Se imprime encabezado
        while x<len(hscores):
            print("     "+hscores[x].user,"".ljust(30) + str(hscores[x].score), "pts") #Se imprime el nombre de usuario y la puntuación
            x += 1

        input("Presione enter para volver")


