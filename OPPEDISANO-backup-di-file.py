"""
=========================================================================================
Programma:                Backup file Cartella 

Descrizione:              Faccio il backup di una cartella tramite metodi e importazioni

Autore:                   Gianluca Oppedisano
Data Di Pubblicazione:    30/01/2023
Relase:                   v1.0
=========================================================================================
"""

import os                                                                                           #Importo clausole per lettura directory
import shutil

def backup_di_file():                                                                               #Creo metodo per backup
    
    src_dir = input("Inserire la directory sorgente da backuppare: ")                               #Chiedo all'utente la directory sorgente e destinataria
    print()

    dst_dir = input("Inserire la directory destinataria per il backup: ")
    print()
                                                                                     
    file_type = input("Inserire l'estensione del file da salvare (esempio: '.txt'): ")              #Chiedere all'utente la tipologia di file da salvare

    print()

    
    if not os.path.isdir(dst_dir):                                                                  #Verificare l'esistenza della directory di backup
        
        os.makedirs(dst_dir)
        print("La directory di backup non esisteva, è stata creata.")
   
    
    for dirpath, dirnames, filenames in os.walk(src_dir):                                           #Effettuare il backup dei file richiesti
        
        for filename in filenames:
            
            if filename.endswith(file_type):
                
                src_file = os.path.join(dirpath, filename)
                dst_file = os.path.join(dst_dir, filename)
                shutil.copy(src_file, dst_file)
                
                print(f"Il file {filename} è stato copiato nella directory di backup.")             #Comunico che il backup è stato eseguito

                print ()
    
    print("Backup riuscito e completato.")                                                          #Comunico fine operazione



    if not os.path.isdir(src_dir):                                                                  #Verifico che la directory inserita esista
        
        print("La directory sorgente non esiste. Backup non eseguito.")
        print()
        return

"""
=======================================================================================================================================================================
"""

print("Questo programma permettere fare un backup di alcuni file all'interno di una cartella. ")

print()

while True:
    print (backup_di_file())                                                                        #Invoco metodo

    end = input("Se si vuole terminare il programma digitare si altrimenti, no: ")                  #Chiedo se si vogliono fare altre istanze

    print()

    if (end == "si"):                                                                               #Verifico condizione e nel caso termino il programma 
        break
    
