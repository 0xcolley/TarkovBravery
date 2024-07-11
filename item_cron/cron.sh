#!/bin/bash

# Define the directory containing the Python scripts
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Run the Python script to refresh JSON files
echo "Running refresh_jsons.py..."
python3 "$DIR/refresh_jsons.py"
echo "JSON refresh completed."
sleep 1

# Clear the tables in the database
echo "Clearing tables..."
mysql -u place1 -p 'place2' -e "
USE your_database;
TRUNCATE TABLE PrimaryWeapons;
TRUNCATE TABLE Rigs;
TRUNCATE TABLE Ammo_300;
TRUNCATE TABLE Ammo_338;
TRUNCATE TABLE Ammo_357;
TRUNCATE TABLE Ammo_366;
TRUNCATE TABLE Ammo_45;
TRUNCATE TABLE Ammo_127x55mm;
TRUNCATE TABLE Ammo_1270;
TRUNCATE TABLE Ammo_2070;
TRUNCATE TABLE Ammo_20x1mm;
TRUNCATE TABLE Ammo_2375mm;
TRUNCATE TABLE Ammo_4630mm;
TRUNCATE TABLE Ammo_40mm;
TRUNCATE TABLE Ammo_4046mm;
TRUNCATE TABLE Ammo_545x39mm;
TRUNCATE TABLE Ammo_5728mm;
TRUNCATE TABLE Ammo_6851mm;
TRUNCATE TABLE Ammo_762x25mm;
TRUNCATE TABLE Ammo_762x39mm;
TRUNCATE TABLE Ammo_762x54mmR;
TRUNCATE TABLE Ammo_9x18mm;
TRUNCATE TABLE Ammo_9x19mm;
TRUNCATE TABLE Ammo_9x39mm;
"
echo "Tables cleared."

echo "Running generator scripts..."
for script in "$DIR/Generators"/*.py; do
    echo "Running $(basename "$script")..."
    python3 "$script"
    sleep 0.5
done

echo "DONE"
