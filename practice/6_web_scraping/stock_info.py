"""
There is a list of most active Stocks on Yahoo Finance https://finance.yahoo.com/most-active.
You need to compose several sheets based on data about companies from this list.
To fetch data from webpage you can use requests lib. To parse html you can use beautiful soup lib or lxml.
Sheets which are needed:
1. 5 stocks with most youngest CEOs and print sheet to output. You can find CEO info in Profile tab of concrete stock.
    Sheet's fields: Name, Code, Country, Employees, CEO Name, CEO Year Born.
2. 10 stocks with best 52-Week Change. 52-Week Change placed on Statistics tab.
    Sheet's fields: Name, Code, 52-Week Change, Total Cash
3. 10 largest holds of Blackrock Inc. You can find related info on the Holders tab.
    Blackrock Inc is an investment management corporation.
    Sheet's fields: Name, Code, Shares, Date Reported, % Out, Value.
    All fields except first two should be taken from Holders tab.

    https://blog.jovian.ai/web-scraping-yahoo-finance-using-python-7c4612fab70c


Example for the first sheet (you need to use same sheet format):
==================================== 5 stocks with most youngest CEOs =====================================
| Name        | Code | Country       | Employees | CEO Name                             | CEO Year Born |
---------------------------------------------------------------------------------------------------------
| Pfizer Inc. | PFE  | United States | 78500     | Dr. Albert Bourla D.V.M., DVM, Ph.D. | 1962          |
...

About sheet format:
- sheet title should be aligned to center
- all columns should be aligned to the left
- empty line after sheet

Write at least 2 tests on your choose.
Links:
    - requests docs: https://docs.python-requests.org/en/latest/
    - beautiful soup docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    - lxml docs: https://lxml.de/
"""
countries = ['AFGHANISTAN', 'ALAND ISLANDS', 'ALBANIA', 'ALGERIA', 'AMERICAN SAMOA', 'ANDORRA', 'ANGOLA', 'ANGUILLA', 'ANTARCTICA', 'ANTIGUA AND BARBUDA', 'ARGENTINA', 'ARMENIA', 'ARUBA', 'AUSTRALIA', 'AUSTRIA', 'AZERBAIJAN', 'BAHAMAS', 'BAHRAIN', 'BANGLADESH', 'BARBADOS', 'BELARUS', 'BELGIUM', 'BELIZE', 'BENIN', 'BERMUDA', 'BHUTAN', 'BOLIVIA, PLURINATIONAL STATE OF', 'BONAIRE, SINT EUSTATIUS AND SABA', 'BOSNIA AND HERZEGOVINA', 'BOTSWANA', 'BOUVET ISLAND', 'BRAZIL', 'BRITISH INDIAN OCEAN TERRITORY', 'BRUNEI DARUSSALAM', 'BULGARIA', 'BURKINA FASO', 'BURUNDI', 'CAMBODIA', 'CAMEROON', 'CANADA', 'CAPE VERDE', 'CAYMAN ISLANDS', 'CENTRAL AFRICAN REPUBLIC', 'CHAD', 'CHILE', 'CHINA', 'CHRISTMAS ISLAND', 'COCOS (KEELING) ISLANDS', 'COLOMBIA', 'COMOROS', 'CONGO', 'CONGO, THE DEMOCRATIC REPUBLIC OF THE', 'COOK ISLANDS', 'COSTA RICA', "CÔTE D'IVOIRE", 'CROATIA', 'CUBA', 'CURAÇAO', 'CYPRUS', 'CZECH REPUBLIC', 'DENMARK', 'DJIBOUTI', 'DOMINICA', 'DOMINICAN REPUBLIC', 'ECUADOR', 'EGYPT', 'EL SALVADOR', 'EQUATORIAL GUINEA', 'ERITREA', 'ESTONIA', 'ETHIOPIA', 'FALKLAND ISLANDS (MALVINAS)', 'FAROE ISLANDS', 'FIJI', 'FINLAND', 'FRANCE', 'FRENCH GUIANA', 'FRENCH POLYNESIA', 'FRENCH SOUTHERN TERRITORIES', 'GABON', 'GAMBIA', 'GEORGIA', 'GERMANY', 'GHANA', 'GIBRALTAR', 'GREECE', 'GREENLAND', 'GRENADA', 'GUADELOUPE', 'GUAM', 'GUATEMALA', 'GUERNSEY', 'GUINEA', 'GUINEA-BISSAU', 'GUYANA', 'HAITI', 'HEARD ISLAND AND MCDONALD ISLANDS', 'HOLY SEE (VATICAN CITY STATE)', 'HONDURAS', 'HONG KONG', 'HUNGARY', 'ICELAND', 'INDIA', 'INDONESIA', 'IRAN, ISLAMIC REPUBLIC OF', 'IRAQ', 'IRELAND', 'ISLE OF MAN', 'ISRAEL', 'ITALY', 'JAMAICA', 'JAPAN', 'JERSEY', 'JORDAN', 'KAZAKHSTAN', 'KENYA', 'KIRIBATI', "KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF", 'KOREA, REPUBLIC OF', 'KUWAIT', 'KYRGYZSTAN', "LAO PEOPLE'S DEMOCRATIC REPUBLIC", 'LATVIA', 'LEBANON', 'LESOTHO', 'LIBERIA', 'LIBYA', 'LIECHTENSTEIN', 'LITHUANIA', 'LUXEMBOURG', 'MACAO', 'MACEDONIA, REPUBLIC OF', 'MADAGASCAR', 'MALAWI', 'MALAYSIA', 'MALDIVES', 'MALI', 'MALTA', 'MARSHALL ISLANDS', 'MARTINIQUE', 'MAURITANIA', 'MAURITIUS', 'MAYOTTE', 'MEXICO', 'MICRONESIA, FEDERATED STATES OF', 'MOLDOVA, REPUBLIC OF', 'MONACO', 'MONGOLIA', 'MONTENEGRO', 'MONTSERRAT', 'MOROCCO', 'MOZAMBIQUE', 'MYANMAR', 'NAMIBIA', 'NAURU', 'NEPAL', 'NETHERLANDS', 'NEW CALEDONIA', 'NEW ZEALAND', 'NICARAGUA', 'NIGER', 'NIGERIA', 'NIUE', 'NORFOLK ISLAND', 'NORTHERN MARIANA ISLANDS', 'NORWAY', 'OMAN', 'PAKISTAN', 'PALAU', 'PALESTINIAN TERRITORY, OCCUPIED', 'PANAMA', 'PAPUA NEW GUINEA', 'PARAGUAY', 'PERU', 'PHILIPPINES', 'PITCAIRN', 'POLAND', 'PORTUGAL', 'PUERTO RICO', 'QATAR', 'RÉUNION', 'ROMANIA', 'RUSSIAN FEDERATION', 'RWANDA', 'SAINT BARTHÉLEMY', 'SAINT HELENA, ASCENSION AND TRISTAN DA CUNHA', 'SAINT KITTS AND NEVIS', 'SAINT LUCIA', 'SAINT MARTIN (FRENCH PART)', 'SAINT PIERRE AND MIQUELON', 'SAINT VINCENT AND THE GRENADINES', 'SAMOA', 'SAN MARINO', 'SAO TOME AND PRINCIPE', 'SAUDI ARABIA', 'SENEGAL', 'SERBIA', 'SEYCHELLES', 'SIERRA LEONE', 'SINGAPORE', 'SINT MAARTEN (DUTCH PART)', 'SLOVAKIA', 'SLOVENIA', 'SOLOMON ISLANDS', 'SOMALIA', 'SOUTH AFRICA', 'SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS', 'SPAIN', 'SRI LANKA', 'SUDAN', 'SURINAME', 'SOUTH SUDAN', 'SVALBARD AND JAN MAYEN', 'SWAZILAND', 'SWEDEN', 'SWITZERLAND', 'SYRIAN ARAB REPUBLIC', 'TAIWAN, PROVINCE OF CHINA', 'TAJIKISTAN', 'TANZANIA, UNITED REPUBLIC OF', 'THAILAND', 'TIMOR-LESTE', 'TOGO', 'TOKELAU', 'TONGA', 'TRINIDAD AND TOBAGO', 'TUNISIA', 'TURKEY', 'TURKMENISTAN', 'TURKS AND CAICOS ISLANDS', 'TUVALU', 'UGANDA', 'UKRAINE', 'UNITED ARAB EMIRATES', 'UNITED KINGDOM', 'UNITED STATES', 'UNITED STATES MINOR OUTLYING ISLANDS', 'URUGUAY', 'UZBEKISTAN', 'VANUATU', 'VENEZUELA, BOLIVARIAN REPUBLIC OF', 'VIET NAM', 'VIRGIN ISLANDS, BRITISH', 'VIRGIN ISLANDS, U.S.', 'WALLIS AND FUTUNA', 'YEMEN', 'ZAMBIA', 'ZIMBABWE']
import requests
from bs4 import BeautifulSoup
from operator import itemgetter

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
def get_yougest_Ceo(listD):
    return sorted(listD, key = lambda i: (i['CEO_BD']),reverse=True)[0:5]
def get_blackrock_largest(listD):
    return sorted(listD, key = lambda i: (i['BR']),reverse=True)[0:10]

def get_Summary(soap):
    company_summary = {}
    #top_companies = {}

    company_soup = BeautifulSoup(company_page.content, 'html.parser')
    profile_content = company_soup.find('p', class_="D(ib) W(47.727%) Pend(40px)").strings
    name = company_soup.find_all("h1", class_="D(ib) Fz(18px)")

    company_summary['Name'] = str(name[0].text)
    company_summary['Code'] = str(link).split('=')[-1]

    # Contry
    for strings in profile_content:
        if strings.upper() in countries:
            company_summary['Country'] = strings
    # Employees
    employes_tag_p = company_soup.find('p', class_='D(ib) Va(t)')
    span = employes_tag_p.find_all('span', class_='Fw(600)')
    company_summary['Employees'] = span[2].text
    nav_div = company_soup.find_all('li', attrs={'data-test': 'COMPANY_PROFILE'})
    nav_div_holders = company_soup.find_all('li', attrs={'data-test': 'HOLDERS'})
    #FIRST I NEED TO CREATE CEO PROFILE REQUEST, AND SEND IT TO GET_CEO_INFO
    #print(nav_div[0].a['href'])

    ceo_page = requests.get('https://finance.yahoo.com' + nav_div[0].a['href'], headers=headers)
    holders_page = requests.get('https://finance.yahoo.com' + nav_div_holders[0].a['href'], headers=headers)

    ceo_soup = BeautifulSoup(ceo_page.content, 'html.parser')
    company_summary = get_Ceo(ceo_soup,company_summary)

    holders_soup = BeautifulSoup(holders_page.content, 'html.parser')
    company_summary = get_blackrock(holders_soup, company_summary)

    return company_summary

def get_blackrock(soap, info):
    rows = soap.find_all("tr", class_="BdT Bdc($seperatorColor) Bgc($hoverBgColor):h Whs(nw) H(36px)")
    try:
        for element in range(len(rows)):
            if rows[element].text.find('Blackrock Inc.') != -1:
                #company_dict['CEO'] = td[element].text
                #print(names[element].text)
                #print(rows[element].text)
                childrens = rows[element].find_all("td", class_="Ta(end) Pstart(10px)")
                shares = int(str(childrens[0].text).replace(',', ''))
                date_reported = str(childrens[1].text)
                out = str(childrens[2].text)
                value =  int(str(childrens[3].text).replace(',', ''))
                info['BR'] = value
                info['BR_out'] = out
                info['BR_shares'] = shares
                info['BR_date_reported'] = date_reported
                #Sheet's fields: Name, Code, Shares, Date Reported, % Out, Value.
                # print(td[element].text,"Pos:",ceo[element].text,company_dict['Name'],"BD:",company_dict['CEO_BD'])
                break
            else:
                pass

    except IndexError:
        print("No se encontró nada en", link)

    if 'BR' not in info:
        info['BR'] = 0
        info['BR_out'] = 0
        info['BR_shares'] = 0
        info['BR_date_reported'] = ''
    return info

def get_Ceo(soap,company_dict):
    td = soap.find_all("td", class_="Ta(start)")
    ceo = soap.find_all("td", class_="Ta(start) W(45%)")
    ceo_bd = soap.find_all("td", class_="Ta(end)")

    for i in ceo_bd:
        if i.text.isnumeric():
            #print(i.text)
            company_dict['CEO_BD'] = int(i.text)
            break

    # Collect CEO name and junk
    try:
        for element in range(len(td)):
            if ceo[element].text.find('CEO') != -1 or ceo[element].text.find('Chief Exec. Officer') != -1:
                company_dict['CEO']= td[element].text
                #print(td[element].text,"Pos:",ceo[element].text,company_dict['Name'],"BD:",company_dict['CEO_BD'])
                break
            else:
                pass
    except IndexError:
        print("No se encontró nada en", link)
    if 'CEO_BD' not in company_dict:
        company_dict['CEO_BD'] = 0
    return company_dict

url = "https://finance.yahoo.com/most-active"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

code_tables = soup.find_all("a", class_="Fw(600) C($linkColor)")

# Find all links to profile
profile_links = soup.find_all("a", href=True)
href = []
for table in code_tables:
    href.append(table['href'])
country = []
profile_href = []
list_companies = []

for link in href:
    print(link)
    #Name, Code, Country, Employees, CEO Name, CEO Year Born.
    top_companies = {}
    # Make request to link
    company_page = requests.get('https://finance.yahoo.com' + link)
    company_soup = BeautifulSoup(company_page.content, 'html.parser')
    company_summary = get_Summary(company_soup)
    list_companies.append(company_summary)


import pandas as pd
#print(list_companies)
yougest_Ceos = get_yougest_Ceo(list_companies)
blackrock_largest_holds = get_blackrock_largest(list_companies)
print(yougest_Ceos)
print(blackrock_largest_holds)

print()
print("======================= 5 stocks with most youngest CEOs ========================")


from rich.console import Console
from rich.table import Table
console = Console()
table_ceo = Table(show_header=True, header_style="bold magenta")
#Name, Code, Country, Employees, CEO Name, CEO Year Born.
table_ceo.add_column("Name")
table_ceo.add_column("Code")
table_ceo.add_column("Country")
table_ceo.add_column("Employees")
table_ceo.add_column("CEO Name", justify="right")
table_ceo.add_column("CEO Year Born", justify="right")
for ceo_info in yougest_Ceos:
    table_ceo.add_row(
        str(ceo_info['Name']), str(ceo_info['Code']),  str(ceo_info['Country']),  str(ceo_info['Employees']), str(ceo_info['CEO']), str(ceo_info['CEO_BD'])
    )

console.print(table_ceo)
print("======================= 10 largest holds of Blackrock Inc. ========================")
table_br = Table(show_header=True, header_style="bold magenta")
#Name, Code, Shares, Date Reported, % Out, Value.
table_br.add_column("Name")
table_br.add_column("Code")
table_br.add_column("Shares")
table_br.add_column("Date Reported")
table_br.add_column("% Out", justify="right")
table_br.add_column("Value", justify="right")
for br_info in blackrock_largest_holds:
    table_br.add_row(
        str(br_info['Name']), str(br_info['Code']),  str(br_info['BR_shares']),  str(br_info['BR_date_reported']), str(br_info['BR_out']), str(br_info['BR'])
    )

console.print(table_br)

'''
ESTRATEGIA:

YA TENGO LOS URL A TODOS LOS PERFILES
YA PUEDO ACCEDER AL PAIS
DATOS A ENCONTRAR: Name, Code, Country, Employees, CEO Name, CEO Year Born.

'''