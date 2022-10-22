our_list = [1,2,3,4,5,6,7]
our_dict = {
    "a": 2,
    "b": 5,
    "c": 8,
    "d": 12,
    "e": 357,
    "f": 12
}
our_tuple = (357, 12, 12, 8, 5, 2, 2)

#-------------------------------------------------------
## Ful je glupo napisano navodilo, nevem kaj narest ali kaj je cilj naloge

#print(our_list)
tempval = our_list[4]
our_list.remove(4)
#print(our_list)

#print(our_dict)
our_dict["d"] = tempval ##katero vrednost. To ki jo je blo potrebno odstranit?? (nimamo je več)
#print(our_dict)

NovTuple = tuple(our_dict.values())
#print(NovTuple)

print(our_tuple == NovTuple)

"""Iz sledečega lista our_list odstranite vrednost, 
ki se nahaja na indexu 4. Vrednost dodajte v dictionary 
pod ključ d. Nato iz dictionary our_dict pridobite vse vrednosti. 
Te vrednosti shranite v nov tuple in novonastali tuple primerjajte 
ali je enak podanemu tuple-u our_tuple."""