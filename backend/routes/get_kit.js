const express = require('express');
const { connection } = require('../db.js');

const router = express.Router();

router.get('/get_kit', async (req, res) => {
    try {
        const [helmet] = await queryDatabase('SELECT * FROM Helmets ORDER BY RAND() LIMIT 1');
        
        let glasses = null;
        let headphones = null;

        if (!helmet.is_facewear && helmet.can_glasses) {
            [glasses] = await queryDatabase('SELECT * FROM Glasses ORDER BY RAND() LIMIT 1');
        }

        if (helmet.can_headset) {
            [headphones] = await queryDatabase('SELECT * FROM Headphones ORDER BY RAND() LIMIT 1');
        }

        const [guns] = await queryDatabase('SELECT * FROM PrimaryWeapons ORDER BY RAND() LIMIT 1');

        let armor = null;
        let rig = null;

        let random = Math.random();
        if (random > 0.8) {
            // armor no rig
            [armor] = await queryDatabase('SELECT * FROM Armor ORDER BY RAND() LIMIT 1');
        } else if (random > 0.6) {
            // rig no armor
            [rig] = await queryDatabase('SELECT * FROM Rigs WHERE plate_carrier = false ORDER BY RAND() LIMIT 1');
        } else if (random > 0.4) {
            // plate carrier no armor
            [rig] = await queryDatabase('SELECT * FROM Rigs WHERE plate_carrier = true ORDER BY RAND() LIMIT 1');
        } else if (random > 0.2) {
            // armor and rig (only non-plate carrier rigs)
            [armor] = await queryDatabase('SELECT * FROM Armor ORDER BY RAND() LIMIT 1');
            [rig] = await queryDatabase('SELECT * FROM Rigs WHERE plate_carrier = false ORDER BY RAND() LIMIT 1');
        } // no armor no rig

        const ammoTable = guns.ammo_type;
        const [ammo] = await queryDatabase(`SELECT * FROM ${ammoTable} ORDER BY RAND() LIMIT 1`);

        res.json({
            headphones,
            glasses,
            helmet,
            armor,
            rig,
            gun: guns,
            ammo
        });
    } catch (error) {
        console.error('Error fetching kit:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

function queryDatabase(sql) {
    return new Promise((resolve, reject) => {
        connection.query(sql, (error, results) => {
            if (error) {
                return reject(error);
            }
            resolve(results);
        });
    });
}

module.exports = router;
