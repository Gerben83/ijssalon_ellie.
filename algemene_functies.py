
def mijn_functie_1(argument):
   
    print(pow(argument, 2)) 

mijn_functie_1(2)
mijn_functie_1(4)
mijn_functie_1(10)
mijn_functie_1(12)

def mijn_functie_2(argument):
   
    waarden_dict = {
        12.3: [15, 9, 36, 4],
        12.2: [14, 10, 24, 6],
        10.5: [15, 5, 50, 2],
        100.20: [120, 80, 2000, 5]
    }
    
    return waarden_dict.get(argument,)

print(mijn_functie_2(12.3))   
print(mijn_functie_2(12.2))   
print(mijn_functie_2(10.5))   
print(mijn_functie_2(100.20)) 
print(mijn_functie_2(99.9))   