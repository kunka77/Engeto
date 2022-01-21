import csv
import os.path
import requests
import sys
from bs4 import BeautifulSoup as BS


#start
def click():
    if str(sys.argv[1] and sys.argv[2]):
        url = sys.argv[1]
        filename = sys.argv[2]
        filename += ".csv"
        soup = get_soup(url)
        #Stahuji data voleb
        municipalities = get_municipalities_list(get_municipality_names(soup), get_numbers_and_links(soup))
        try:
            header = get_csv_header(url, municipalities[0][2])
        except (IndexError, TypeError) as err:
            print()
            print("Jejda! Nepodařilo se. Zkontroluj odkaz a nazev slozky ktera se ma vytvorit a zkus to znova. V pripade stale opakujici se chybi nam napis na: random_mail@CZ_volby.cz")
            print("Chyba ! ! !", err)
        else:
            table_data = []
            for municipality in municipalities:  # ukladam do csv
                print("\r", "Zbiram data z...", municipality[1], end="")
                municipality_data = get_municipality_data(url, municipality[2])
                table_data.append(get_table_data(municipality, municipality_data))
            write_csv(header, table_data, filename)

# prvni cast spolecne adresy okresu a mest
def get_main_part_url(url):
    return url.rsplit("/", 1)[0]


def get_parties_list(url, municipality):
    parties_list = []
    soup = get_soup(url)
    print("Spojuji stazeny material...")
    for td in get_td_data(soup, "t1sa1 t1sb2", "t2sa1 t2sb2"):
        parties_list.append(td.get_text())
    return parties_list


# Data o obci, zber
def get_municipality_data(url, municipality):
    url = get_main_part_url(url) + "/" + municipality
    soup = get_soup(url)
    municipality_data = []
    for td in get_td_data(soup,"sa2", "sa3", "sa6", "t1sa2 t1sb3", "t2sa2 t2sb3"):
        municipality_data.append(td.get_text().replace("\xa0", ""))  # /prida cislo, odstrani mezeru z vyskokych cisel
    return municipality_data


# Spojka jmen stran(parties) a headeru
def get_csv_header(url, municipality_url):
    header = ["Kod_obce", "Název_obce", "voličů", "volilo", "platné_hlasy"]
    url = get_main_part_url(url) + "/" + municipality_url
    return header + get_parties_list(url, municipality_url)

def get_soup(url):
    try:
        request = requests.get(url)
        request.raise_for_status()
        return BS(request.text, "html.parser")
    except (requests.exceptions.ConnectionError, requests.exceptions.MissingSchema) as err:
        print()
        print("Jejda! Nepodařilo se. Zkontroluj odkaz a nazev slozky ktera se ma vytvorit a zkus to znova. V pripade stale opakujici se chybi nam napis na :random_mail@CZ_volby.cz")
        print("Chyba ! ! ! ")
        print(err)
        exit()


# najdi znaky
def get_td_data(soup, *args):
    try:
        td_data = soup.find_all("td", headers=args)
        return td_data
    except AttributeError as err:
        print("Chyba ! ! !", err)
        exit()

# Nazvy obci
def get_municipality_names(soup):
    names = []
    for tab_number in range(1,4):
        for td in (get_td_data(soup, f"t{tab_number}sa1 t{tab_number}sb2")):
            names.append(td.get_text())
    return names


# list,tupl a odkaz na obce
def get_numbers_and_links(soup):
    nums_and_links = []
    try:
        for tab_number in range(1,4):
            for td in get_td_data(soup, f"t{tab_number}sa1 t{tab_number}sb1"):
                if td.get_text() != "-":
                    nums_and_links.append((td.get_text(), td.a["href"]))
        return nums_and_links
    except TypeError as err:
        print("Jejda! Nepodařilo se. Zkontroluj odkaz a nazev slozky ktera se ma vytvorit a zkus to znova. V pripade stale opakujici se chybi nam napis na :random_mail@CZ_volby.cz")
        print("Chyba ! ! !:", err)
        exit()


def get_municipalities_list(names, nums_and_links):
    print("Spojuji stazeny material...")
    try:
        municipalities = [[int(num_and_link[0]), name, num_and_link[1]] for name, num_and_link in zip(names, nums_and_links)]
        print(municipalities)
        return municipalities
    except ValueError as err:
        print("Jejda! Nepodařilo se. Zkontroluj odkaz a nazev slozky ktera se ma vytvorit a zkus to znova. V pripade stale opakujici se chybi nam napis na :random_mail@CZ_volby.cz")
        print("Chyba ! ! !:", err)
        exit()



def get_table_data(municipality, municipality_data):
    return municipality[:2] + municipality_data


# Zapisuji data do csv souboru
def write_csv(header, table_data, output_file):
    with open(output_file, "a+", newline="") as file:
        writer = csv.writer(file)
        if not os.path.exists(output_file) or os.path.getsize(output_file) == 0:
            writer.writerow(header)
        writer.writerows(table_data)
    print()
    print(f"Složka {output_file} vytvořena.")


if __name__ == '__main__':
    click()
