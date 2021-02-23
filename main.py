import requests
from bs4 import BeautifulSoup

customised = "False"

customised = input("Please enter True for custom stats, False for standard stats: ")

if customised == "True":
    postcode = (input("Please enter your postcode: ")).upper()
    postcodeArray = postcode.split()

# Get stats on general covid stats
URL = 'https://coronavirus.data.gov.uk/'
results = requests.get(URL)
soup = BeautifulSoup(results.text, "html.parser")
job_elems = soup.find_all('p', class_='sam-body')
caseting = soup.find_all('div', class_='float govuk-heading-m govuk-!-margin-bottom-0 govuk-!-padding-top-0 total-figure2')

# Get stats on local Tings
if customised == "True":
    neURL = 'https://coronavirus.data.gov.uk/search?postcode=' + postcodeArray[0] + '+' + postcodeArray[1]
    neResults = requests.get(neURL)
    neSoup = BeautifulSoup(neResults.text, "html.parser")
    localCases = neSoup.find_all('div', class_='float govuk-heading-m govuk-!-margin-bottom-0 govuk-!-padding-top-0 total-figure2')

# Print out the STATS!

print("---------VACCINE STATISTICS---------")
print ("        "+(job_elems[0]).text)
print ("        "+(job_elems[1]).text)
print("---------TESTING STATISTICS---------")
posCases = (caseting[0]).text
posCases1 = posCases.split('Daily')
print ("   "+posCases1[0] + "Postive Tests Today")
cases = (caseting[9]).text
cases1 = cases.split('Daily')
print ("      "+cases1[0] + "Tests Today")
print("----------DEATH STATISTICS----------")
deathsstats = (caseting[3]).text
deaths1 = deathsstats.split('Daily')
print("      "+deaths1[0] + "Deaths Today")
if customised == "True":
    print("--------" + postcode + " STATISTICS---------")
    posLocalCases = (localCases[0]).text
    posLocalCases1 = posLocalCases.split('Daily')
    print("    "+(posLocalCases1[0]) + "Postive Tests Today")
    deathsLocal = (localCases[3]).text
    deathsLocal1 = deathsLocal.split('Daily')
    print("       "+(deathsLocal1[0]) + "Deaths Today")
    patients = (localCases[6]).text
    patients1 = patients.split('Daily')
    print("  "+(patients1[0]) + "Patients Admitted Today")