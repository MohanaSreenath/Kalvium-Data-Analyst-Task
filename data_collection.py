import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_election_data(url):
    # Fetch the page content
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve page content: Status code {response.status_code}")

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all tables and inspect
    tables = soup.find_all('table')
    
    # Iterate through tables to find the one with the election results
    party_table = None
    for table in tables:
        if "Party" in table.text:  # Simple check to find the table with "Party" in the text
            party_table = table
            break

    if party_table is None:
        raise Exception("Failed to find the party results table in the HTML content")

    # Extracting party-wise results
    rows = party_table.find_all('tr')[1:]

    # Parsing the data
    data = []
    for row in rows:
        cols = row.find_all('td')
        if len(cols) < 4:
            continue  # Skip rows that don't have the expected number of columns
        party_data = {
            'Party': cols[0].text.strip(),
            'Won': int(cols[1].text.strip()),
            'Leading': int(cols[2].text.strip()),
            'Total': int(cols[3].text.strip())
        }
        data.append(party_data)

    # Creating DataFrame
    df = pd.DataFrame(data)
    return df

def save_data_to_csv(df, filename='party_wise_results.csv'):
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    url = "https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S11.htm"
    df = fetch_election_data(url)
    save_data_to_csv(df)
