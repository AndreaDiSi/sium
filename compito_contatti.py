 #Descrizione: Realizza un piccolo programma che gestisce una lista di contatti. 
 # Ogni contatto deve contenere id, nome, cognome, data di nascita, numero di telefono e indirizzo email.

import random


#chiedo le informazioni e le metto in un dizionario

#MENU:

lista = []  

while True:
    print("Ciao Utente, scegli un opzione!")
    print("Crea Contatto: 1")
    print("Visualizza Contatti: 2")
    print("Cerca contatto tramite nome: 3")
    print("Cancella contatto tramite id: 4")
    print("Uscire dal menu: 'finito' ")
    scelta_menu = input("Inserire numero: ")

    

    if scelta_menu == '1':
        
        nome = input("Aggiungi il NOME del tuo contatto: ")
        if nome.isnumeric():
            print("non ci possono essere numeri nel nome, riprova! ")
            exit()

        cognome = input("Aggiungi il COGNOME del tuo contatto: ")
        if cognome.isnumeric():
                    print("non ci possono essere numeri nel cognome, riprova! ")
                    exit()

        nascita = input("Aggiungi la DATA DI NASCITA numerica del tuo contatto: ")

        num_tel = input("Aggiungi il NUMERO DI TELEFONO del tuo contatto: ")
        if not num_tel.isnumeric():
                    print(" non sapevo che i numeri di telefono avessero le lettere, riprova!")
                    exit()

        email = input("Aggiungi l' INDIRIZZO EMAIL del tuo contatto: ")
        if "@" not in email:
                    print(" non hai inserito un indirizzo email valido")
                    exit()

        if "." not in email:
                    print(" non hai inserito un indirizzo email valido")
                    exit()      

        #inizio scrittura file
        file_write = open("compito_contatti.txt" , "w")

        Contatto = {'Nome' : nome, 'Cognome' : cognome , 'Data di nascita' : nascita, 'Numero di telefono' : num_tel , 'Email' : email}
        file_write.write(str(Contatto)
        id = random.randint(0,100000)
        lista.append(Contatto)

#mettendo la lista fuori, si resetta solo quando esco dal while, altrimenti salva tutto.

    #visualizzazione contatto
    if scelta_menu == '2':
        print(lista)
    
    #cercare contatto per nome cognome o id
    if scelta_menu == '3':
        ricerca_contatto = input("inserisci il nome, cognome o id: ")
        
        if ricerca_contatto in Contatto.values():
            print("--------------------------")
            print(f"ID : {id}")
            print("--------------------------")
            print(Contatto)    
        else: print("non c'e nessun contatto che abbia questo Nome/Cognome/ID")

    #cancellare contatto dato un id in input.
    if scelta_menu == '4':
        cancella_contatto = int(input(" inserisci l'ID del contatto per cancellarlo: "))
        if cancella_contatto == id:
            del Contatto['Nome']
            del Contatto['Cognome']
            del Contatto['Data di nascita']
            del Contatto['Numero di telefono']
            del Contatto['Email']
            

            #uscita dal while
    if scelta_menu == 'finito':
        break





#visualizzare contatto
 

            
    





























#if scelta_menu >= 5:
       #break 




















'''id  = input("Aggiungi l'ID del il tuo contatto: ")

nome = input("Aggiungi il NOME del tuo contatto: ")
if nome.isnumeric():
    print("non ci possono essere numeri nel nome, riprova! ")
    exit()

cognome = input("Aggiungi il COGNOME del tuo contatto: ")
if cognome.isnumeric():
    print("non ci possono essere numeri nel cognome, riprova! ")
    exit()

nascita = input("Aggiungi la DATA DI NASCITA numerica del tuo contatto: ")

num_tel = input("Aggiungi il NUMERO DI TELEFONO del tuo contatto: ")
if not num_tel.isnumeric():
    print(" non sapevo che i numeri di telefono avessero le lettere, riprova!")
    exit()

email = input("Aggiungi l' INDIRIZZO EMAIL del tuo contatto: ")
if "@" not in email:
    print(" non hai inserito un indirizzo email valido")
    exit()

if "." not in email:
    print(" non hai inserito un indirizzo email valido")
    exit()    

contatto = {'ID' : id , 'Nome' : nome, 'Cognome' : cognome , 'Data di nascita' : nascita, 'Numero di telefono' : num_tel , 'Email' : email}

for k in contatto:
    print(k, contatto[k])'''

    





#def visualizza():





#def cerca():





#def cancella():
