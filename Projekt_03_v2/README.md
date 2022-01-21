# Engeto_Scraper

Engeto projekt 3
#
Třetí projekt na Python Akademii od Engeta.
#
# Popis projektu
Tento projekt slouží k extrahování výsledků z parlamentních voleb v [roce 2017](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).


#
# Instalace knihoven
Knihovny, které jsou použity v kódu jsou uložené v souboru (requirements.txt) . Pro instalaci doporučuji použít nové virtální prostředí a s nainstalovaným manažerem spustit následovně:

$ pip3 --version # ověříme si verzi

$ pip3 install - r requirements.txt # nainstalujeme knihovny

# Spuštění projektu
Spuštění souboru Electionscrapy.py v rámci příkazového řádku požaduje dva povinné argumenty.

python "odkaz na uzemni celky" "název souboru"
Následně se vám stáhnou výsledky jako soubor s příponou .csv.

# Ukázka projektu pro Okres: Benešov
Spustíme program a do terminálu napíšeme: python Electionscrapy.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101' 'Benesov_2017'
Poté pokud je vše v pořádku dojde ke stahování a ukládání dat do námo pojmenovaného cvs souboru, v našem případě Pribram_2017.
Vystup:     Zbiram data z... "obce"
            Slozka Benesov_2017.csv vytvorena.








































