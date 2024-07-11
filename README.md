# Tarkov Bravery
Tarkov Bravery was a fun side project inspired by Ultimate Bravery (https://www.ultimate-bravery.net/) with the Tarkov spin on it. The basic idea is that you click the button, get a randomized loadout, and buy it on the flea market then use it. </br>

Feel free to deploy it yourself or use it at https://www.tarkovbravery.xyz (https://tarkov-bravery-frontend.vercel.app/ backup)

# Tech Stack
- MySQL 8 DB
- Python Automatic Scraping w/ Cron Job for Updating
- Express.js Backend
- React.js Frontend

# General Notes
- Some modifications have been made to the db to reflect proper loadouts in the game.
- The cron job is unable to scrape helmet/headset/glasses compatability. That was done manually.
