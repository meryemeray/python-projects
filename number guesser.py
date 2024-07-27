import random

obere_schranke = input("Bitte gebe eine obere Schranke fur die Nummer an: ")
counter = 0

if obere_schranke.isdigit:
    oben = int(obere_schranke)
    
    if oben <= 0:
        print("Deine Nummer soll bitte größer als 0 sein.")
        quit()
else:
    print("Bitte nur Zahlen eingeben!")
    quit()
    
computer = random.randint(1, oben)
print("Hehe :3 Willkommen im Spiel!")
while(True):
    benutzer_guess = input("Kannst du raten, welche Nummer ich fur dich ausgewählt habe? ")
    if benutzer_guess.isdigit():
        benutzer_guess = int(benutzer_guess)
    else:
        print("Bitte nur Zahlen eingeben!")
        continue
    
    if benutzer_guess == computer:
        print("Prima! Du hast das in " + str(counter + 1) + " Versuchen geschafft.")
        break
    elif benutzer_guess > computer:
        print("Versuch mal eine kleinere Zahl!")
        counter += 1
    else: 
        print("Versuch mal eine groessere Zahl!")
        counter += 1
