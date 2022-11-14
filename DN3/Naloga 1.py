#    2704999505231  #Totaly not my EMSO

from datetime import datetime, timedelta

def emso_leta_preracun():
    emso = input("Vnesi svoj EMSO: ")

    emso = emso.strip()     #Cut away any whitespaces
    
    if emso.isnumeric():    #check if there is only characters
       pass                 #woah thats something new for me
    else:
        print("Error\nYou enetered a character")
        exit()              #close the program

    #print(emso[4:7])
    BirthYear = emso[4:7]        #strip out las 3 numbers ofbirth year 
    if BirthYear[0] == '9':      #Magic
        BirthYear = '1' + BirthYear     # 999 -> 1999  || 900 -> 1900
    else:
        BirthYear = '2' + BirthYear     # 000 -> 2000  || 899 -> 2899

    BirthMonth = emso[2:4]              # get month of birth from emso
    BirthDay = emso[0:2]                # get day of birth from emso

    date = datetime(year=int(BirthYear), month=int(BirthMonth), day=int(BirthDay))  #Make a date format from emso

    if int(emso[9]) < 5:    #Check for genter
        isMan = 1
    else:
        isMan = 0

    Birthdate = datetime(year=int(BirthYear), month=int(BirthMonth), day=int(BirthDay))

    today = date.today()            #get todays date
    year = today.strftime("%Y")     #get todays year

    
    if today > datetime(year=int(year), month=int(BirthMonth), day=int(BirthDay)):  #Check if birthday already happened this year
        hadBD = 1    
    else:
        hadBD = 0

    #IZPIS

    print("\nDanes je: " + today.strftime("%d/%m/%Y"))
    if isMan == 1:
        print("Ste Moški")
    else:
        print("Ste Ženska")
    print("Rojeni ste: " + Birthdate.strftime("%d/%m/%Y"))
    if hadBD == 1:
        print("Stari ste " + str(int(year) - int(BirthYear)) + " let")
    else:
        print("Stari ste " + str(int(year) - int(BirthYear) - 1) + " let")


emso_leta_preracun()
 