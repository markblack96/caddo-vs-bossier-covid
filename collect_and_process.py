import requests
import pandas as pd


# request data
url = 'https://ldh.la.gov/assets/oph/Coronavirus/data/LA_COVID_TESTBYDAY_PARISH_PUBLICUSE.xlsx'
r = requests.get(url)

# open data with pandas
state_data = pd.read_excel(r.content)

# isolate caddo and bossier
caddo_data = state_data[state_data['Parish'] == 'Caddo']
bossier_data = state_data[state_data['Parish'] == 'Bossier']

# isolate just the data we want and save it to json
caddo_json = caddo_data[['Lab Collection Date', 'Daily Test Count', 'Daily Positive Test Count', 'Daily Case Count', 'datetime']].reset_index(drop=True).to_json(orient='records')

bossier_json = bossier_data[['Lab Collection Date', 'Daily Test Count', 'Daily Positive Test Count', 'Daily Case Count', 'datetime']].reset_index(drop=True).to_json(orient='records')


for data in [caddo_data, bossier_data]:
    descriptive_stats = {}
    descriptive_stats['Parish'] = str(data['Parish'].iloc[0])
    descriptive_stats['Total Tests'] = int(data['Daily Test Count'].sum())
    descriptive_stats['Total Cases'] = int(data['Daily Case Count'].sum())
    descriptive_stats['Latest Data'] = str(data['Lab Collection Date'].max().ctime())
    with open(f"data/{descriptive_stats['Parish'].lower()}Descrip.json", 'w') as f:
        f.write(json.dumps(descriptive_stats))

# save the data
with open('data/caddo.json', 'w') as f:
    f.write(caddo_json)
    f.close()

with open('data/bossier.json', 'w') as f:
    f.write(bossier_json)
    f.close()