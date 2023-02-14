"""
=========================================================================================
Programma:                Backup file Cartella 

Descrizione:              Faccio il backup di una cartella tramite metodi e importazioni

Autore:                   Gianluca Oppedisano
Data Di Pubblicazione:    12/02/2023
Relase:                   v2.0
=========================================================================================
"""

import os                                                                                               #Importo clausole per lettura directory
import shutil

def backup_di_file():                                                                                   #Creo metodo per backup

    print("Digitare 1 se si desidera utilizzare la directory corrente, dove risiede il file.")
    print("Digitare 2 se si vuole immettere manualmente la directory.")

    print()

    sel = int(input("Inserimento: "))

    print()

    if (sel == 1):                                                                                      #Verifico che cosa l'utente desidera fare 

        temp_dir = os.getcwd()                                                                          #Prendo la directory nella quale il file viene eseguito

        print ("Ora, la directory selezionata è: ", temp_dir)                                           #Comunico la directory in cui ci si trova

        print()


        src_dir = os.getcwd() + '\\' + input("Inserire il nome della cartella da backuppare: ")         #Chiedo all'utente la directory sorgente 
        print()

        if not os.path.isdir(src_dir):                                                                  #Verifico che la directory inserita esista
            
            return print("La directory sorgente non esiste. Backup non eseguito.")
 
        dst_dir = os.getcwd() + '\\' + input("Inserire il nome della cartella destinazione: ")          #Chiedo all'utente la directory destinazione
        print()

        files = os.listdir(src_dir)                                                                     #Leggo file ed estensioni all'interno della cartella
    
    else:

        src_dir = input("Inserire la directory sorgente da backuppare: ")                               #Chiedo all'utente la directory sorgente 
        print()

        if not os.path.isdir(src_dir):                                                                  #Verifico che la directory inserita esista
            
           return print("La directory sorgente non esiste. Backup non eseguito.")

        dst_dir = input("Inserire la directory destinataria per il backup: ")                           #Chiedo all'utente la directory destinazione
        print()

        files = os.listdir(src_dir)                                                                     #Leggo file ed estensioni all'interno della cartella
                                                                           
    
    
    
    file_type = input("Inserire l'estensione del file da salvare (esempio: '.txt'): ")                  #Chiedere all'utente la tipologia di file da salvare

    print()



    file_found = False                                                                                  #Variabile d'uscita e di appoggio

    for file in files:                                                                                  #Verifico che ci siano i file con estensione inserita all'interno della cartella

        if file.endswith(file_type):                                                                    #Verifico file all'interno della cartella
            file_found = True
            break

    if file_found:

        print(f"Un file con estensione {file_type} è stato trovato in {src_dir}.")                      #Comunico che il programma ha trovato i file con estenseione designata
    else:

        return print(f"Non è stato trovato nessun file con estensione {file_type} in {src_dir}.")       #Comunico che il programma non ha trovato i file con estenseione designata


    if not os.path.isdir(dst_dir):                                                                      #Verificare l'esistenza della directory di backup
        
        os.makedirs(dst_dir)

        print()

        print("La directory di backup non esisteva, è stata creata.")
   
    print ()
    
    for dirpath, dirnames, filenames in os.walk(src_dir):                                               #Effettuare il backup dei file richiesti
        
        for filename in filenames:
            
            if filename.endswith(file_type):
                
                src_file = os.path.join(dirpath, filename)
                dst_file = os.path.join(dst_dir, filename)
                shutil.copy(src_file, dst_file)
                
                print(f"Il file {filename} è stato copiato nella directory di backup.")                 #Comunico che il backup è stato eseguito

                print ()
    
    print("Backup riuscito e completato.")                                                              #Comunico fine operazione



"""
=======================================================================================================================================================================
"""



print("Questo programma permettere fare un backup di alcuni file all'interno di una cartella. ")

print()

while True:
    
    backup_di_file()                                                                                #Invoco metodo
    
    print()                                                                      

    end = input("Se si vuole terminare il programma digitare si altrimenti, no: ")                  #Chiedo se si vogliono fare altre istanze

    print()

    if (end == "si"):                                                                               #Verifico condizione e nel caso termino il programma 
        break
    
