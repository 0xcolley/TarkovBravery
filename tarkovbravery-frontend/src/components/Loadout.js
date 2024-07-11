import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './Loadout.css';

const Loadout = () => {
    const [loadout, setLoadout] = useState({
        armor: null,
        rig: null,
        helmet: null,
        gun: null,
        ammo: null,
        headphones: null,
        glasses: null,
    });

    useEffect(() => {
        axios.get('http://your-backend-api/api/get_kit')
            .then(response => {
                setLoadout(response.data);
            })
            .catch(error => {
                console.error("Error fetching loadout:", error);
            });
    }, []);

    return (
        <div className="loadout-container">
            <div className="loadout-item">{loadout.helmet && <img src={loadout.helmet.image} alt={loadout.helmet.name} />}</div>
            <div className="loadout-item">{loadout.glasses && <img src={loadout.glasses.image} alt={loadout.glasses.name} />}</div>
            <div className="loadout-item">{loadout.headphones && <img src={loadout.headphones.image} alt={loadout.headphones.name} />}</div>
            <div className="loadout-item">{loadout.rig && <img src={loadout.rig.image} alt={loadout.rig.name} />}</div>
            <div className="loadout-item">{loadout.armor && <img src={loadout.armor.image} alt={loadout.armor.name} />}</div>
            <div className="loadout-item">{loadout.gun && <img src={loadout.gun.image} alt={loadout.gun.name} />}</div>
            <div className="loadout-item">{loadout.ammo && <img src={loadout.ammo.image} alt={loadout.ammo.name} />}</div>
        </div>
    );
};

export default Loadout;