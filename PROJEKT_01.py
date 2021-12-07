# FINALE | Opraveno
# def Textovy_analyzator():

'''
    author = Aleš_Kaňuk
    '''
TEXTS = [

    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is . ,  a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30N and the Union Pacific Railroad,
    which traverse the valley. ''',

    '''At the base of Fossil Butte are the bright 
    red, purple, yellow and gray beds of the Wasatch 
    Formation. Eroded portions of these horizontal 
    beds slope gradually upward from the valley floor 
    and steepen abruptly. Overlying them and extending 
    to the top of the butte are the much steeper 
    buff-to-white beds of the Green River Formation, 
    which are about 300 feet thick.''',

    '''The monument contains 8198 acres and protects 
    a portion of the largest deposit of freshwater fish 
    fossils in the world. The richest fossil fish deposits 
    are found in multiple limestone layers, which lie some 
    100 feet below the top of the butte. The fossils 
    represent several varieties of perch, as well as 
    other freshwater genera and herring similar to those 
    in modern oceans. Other fish such as paddlefish, 
    garpike and stingray are also present.'''
]



odd = 80 * "-"

v_slovo = (0)
V_SLOVA = (0)
M_SLOVA = 0
cisla = 0
suma = 0

# prihlaseni a kontrola
prihlaseni = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}
print("Vytej v text analyzatoru, prosim prihlas se: ")
jmeno = input("Zadej uzivatelske jmeno: ")
heslo = input("Zadej heslo: ")
print(odd)
if prihlaseni.get(jmeno) == (heslo):
    print("Vytej! Vyber si jeden ze 3 textu pro analyzu. ")
else:
    print("Zadane udaje neodpovidaji. Provedte kontrolu vasich udaju a zkuste to znova.")
    quit()

vyber = input("Napis cislo textu ktery chces analyzovat: ")
print(odd)

if vyber.isnumeric():
    vyber = int(vyber)
    vyber -= 1
    if vyber in range(len(TEXTS)+1):
        print(odd)
    else:
        print("Zadana hodnota je mimo rozsah! Zkus to znova.")
        quit()
else:
    print("Zadana hodnota neni cislo! Zkus to znova.")
    quit()
# print("provadime rozbor textu." print(vyber))
textuprava = [nahrada.strip("!\"#$%/:;<=>?@[\\]&'()*+, -.^_`{|}~") for nahrada in (TEXTS[vyber].split())]
uprava = []
for slova in textuprava:
    if slova != "":
        uprava.append(slova)
textuprava = uprava






print("celkovy pocet slov: ", len(textuprava))


# Pocet slov 'Velke' pismeno
for slovo in TEXTS[vyber].split(" "):
    if slovo.istitle():
        v_slovo = v_slovo + 1

    # Pocet slov 'VELKYM'
    elif slovo.isupper():
        V_SLOVA = V_SLOVA + 1

    # Pocet slov 'Malych'
    elif slovo.islower():
        M_SLOVA = M_SLOVA + 1

    elif slovo.strip(",./;'[]-=}{:?\n|><"):
        slovo.isnumeric
        cisla = cisla + 1
        slovo = int(slovo)
        suma = suma + slovo

print("Slov zacinajicich velkym pismenem: ", v_slovo, )
print("Slov psanych velkym pismem: ", V_SLOVA, )
print("Slov psanych pouze malym pismem: ", M_SLOVA)
print("Cisel v textu: ", cisla)
print("Soucet cisel v textu: ", suma)
# 6
print(odd)
odd2 = "+--++-.-.-.-.-.-++--+"
print("Nejcastejsi slova v textu: ")
cista_slova = list()
for slovo in TEXTS[vyber].split():
    cista_slova.append(slovo.strip(",./;'[]<''>? :}{"";").lower())


slova: dict = dict()

for slovo in cista_slova:
    if slovo not in slova:
        slova[slovo] = 1
    else:
        slova[slovo] += + 1

ocislovani: list = sorted(
    list(slova.values()), reverse=True
)[:5]
vysledky = list()
for vyskyt in slova:
    if slova[vyskyt] in ocislovani:
        vysledky.append((slova[vyskyt], vyskyt))

for index, tupl in enumerate(sorted(vysledky, reverse=True), 1):
    print(
        odd2,
        f"|{index}.|{tupl[1]: ^13}|{tupl[0]}x|",
        odd2,
        sep="\n"
    )

# len
#cista_slova = textuprava
#Tohle neni potreba - - -for slovo in TEXTS[vyber].split():
    #cista_slova.append(slovo.strip(",./;'[]<>? '':}{"";").lower())
    # words = ['ahoj', 'hoj', '1', '4', 'west', 'of']

pocet = len(TEXTS[vyber].split())
print(odd)
print("LEN|     OCCURENCES     |NR.")
print(odd)

words_occurrence = {}
for word in textuprava:
    len_w = len(word)
    if len_w not in words_occurrence:
        words_occurrence[len_w] = 0
    words_occurrence[len_w] = words_occurrence[len_w] + 1
for len_w, po in sorted(words_occurrence.items()):
    occurrences = po * '*'
    print(f'{len_w:>3}| {occurrences:<18} | {po}')