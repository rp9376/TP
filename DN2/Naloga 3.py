d = {
    "mačka": "Micka",
    "pes": "Fido",
    "volk": "Rex",
    "medved": "Žan",
    "slon": "Jan",
    "žirafa": "Helga",
    "lev": "Gašper",
    "tiger": "Anže",
    "papagaj": "Črt",
    "ribica": "Elena",
    "krokodil": "Kasper",
    "zajec": "Lars",
    "kamela": "Manca" 
}

for key, value in d.items():
    if (("r" in value) or ("R" in value)):
        print(key)


"""
Iz danega dictionary-ja d izpišite vse ključe, 
katerih vrednost vsebuje črko r ali veliko tiskano črko R.
"""
