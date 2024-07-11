import requests
import json
import os
import time

queries = {
    "ammo.json": """
    {
        items(lang: en, type: ammo) {
            id
            name
            image512pxLink
        }
    }
    """,
    "backpack.json": """
    {
        items(lang: en, type: backpack) {
            id
            name
            image512pxLink
        }
    }
    """,
    "headphones.json": """
    {
        items(lang: en, type: headphones) {
            id
            name
            image512pxLink
        }
    }
    """,
    "helmet.json": """
    {
        items(lang: en, type: helmet) {
            id
            name
            image512pxLink
        }
    }
    """,
    "rigs.json": """
    {
        items(lang: en, type: rig) {
            id
            name
            image512pxLink
        }
    }
    """,
    "glasses.json": """
    {
        items(lang: en, type: glasses) {
            id
            name
            image512pxLink
        }
    }
    """,
     "guns.json": """
    {
        items(lang: en, type: gun) {
            id
            name
            image512pxLink
        }
    }
    """,
    "armor.json": """
    {
        items(lang: en, type: armor) {
            id
            name
            image512pxLink
        }
    }
    """,
}

def run_query(query):
    headers = {"Content-Type": "application/json"}
    response = requests.post('https://api.tarkov.dev/graphql', headers=headers, json={'query': query})
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, query))

def save_json(data, filename):
    directory = './item_jsons'
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, filename)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def refresh_jsons():
    for filename, query in queries.items():
        print(f"Fetching data for {filename}...")
        data = run_query(query)
        print(f"Saving data to {filename}...")
        save_json(data, filename)
        print(f"Data for {filename} saved successfully.")
        time.sleep(0.5)

if __name__ == "__main__":
    refresh_jsons()
