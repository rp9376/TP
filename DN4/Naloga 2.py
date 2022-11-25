import numpy as np

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

polje=[346,782,26,367,256774,235]

def func(polje):
    print("Najmanjsi: "+ str(min(polje)))
    print("Najvecji: " + str(max(polje)))
    print("povrprecje: " + str(np.average(polje)))
    print("najblizji povprecju: " + str(find_nearest(polje, np.average(polje))))


func(polje)