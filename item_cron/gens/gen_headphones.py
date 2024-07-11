import json
import os

def load_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def generate_sql_insert(json_file_path):
    data = load_json(json_file_path)
    items = data['data']['items']
    
    sql_insert_statements = []
    for item in items:
        name = item['name'].replace("'", "")
        image = item['image512pxLink']
        sql_insert_statements.append(f"INSERT INTO Headphones (name, image) VALUES ('{name}', '{image}');")
    
    return sql_insert_statements

def save_sql_to_file(sql_statements, filename):
    with open(filename, 'w') as file:
        for statement in sql_statements:
            file.write(statement + '\n')

def main():
    json_file_path = './item_jsons/headphones.json'
    sql_file_path = './out/headphones.sql'
    
    print(f"Generating SQL insert statements from {json_file_path}...")
    sql_statements = generate_sql_insert(json_file_path)
    
    print(f"Saving SQL insert statements to {sql_file_path}...")
    if os.path.exists(sql_file_path):
        os.remove(sql_file_path)
    save_sql_to_file(sql_statements, sql_file_path)
    
    print(f"SQL insert statements saved successfully to {sql_file_path}.")

if __name__ == "__main__":
    main()
