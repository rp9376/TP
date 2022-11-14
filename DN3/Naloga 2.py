
data = {"prices": [41970, 40721, 41197, 41137, 43033],
       "volume": [49135346712, 50768369805, 47472016405, 34809039137, 38700661463]}

def najvecja_vrednost(podatki):
    seznam = []
    final = []

    for x in data:      #goes trough keys from "data"
        seznam = data[x]            #copies values from cartain key to array 
        seznam.sort()               #sorts values 
        final.append(seznam[-1])    #puts value (biggest) into a seperate array
        print('V "' + x + '" je najvecja vrezdnost: ' + str(seznam[-1]))
        seznam.clear()              #clears array for values from next key

    print(final)

najvecja_vrednost(data)