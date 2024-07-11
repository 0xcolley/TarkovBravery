// src/KitForm.js
import React, { useState } from 'react';
import axios from 'axios';
import '../styles/kitform.css'; // Import the CSS file

const KitForm = () => {
  const [kit, setKit] = useState(null);
  const [loading, setLoading] = useState(false);

  const fetchKit = async () => {
    setLoading(true);
    try {
      const response = await axios.get('https://urchin-app-yn8i5.ondigitalocean.app/api/get_kit');
      setKit(response.data);
    } catch (error) {
      console.error('Error fetching the kit:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="kit-form">
      <button className="cta-button" onClick={fetchKit} disabled={loading}>
        {loading ? 'Generating...' : 'Generate Kit'}
      </button>
      {kit && (
        <div className="kit-details">
          <h3>Your Kit</h3>
          <div className="loadout-container">
            <div className="loadout-item">
              {kit.helmet && <img src={kit.helmet.image} alt={kit.helmet.name} />}
              {kit.helmet && <p>{kit.helmet.name}</p>}
            </div>
            <div className="loadout-item">
              {kit.glasses && <img src={kit.glasses.image} alt={kit.glasses.name} />}
              {kit.glasses && <p>{kit.glasses.name}</p>}
            </div>
            <div className="loadout-item">
              {kit.headphones && <img src={kit.headphones.image} alt={kit.headphones.name} />}
              {kit.headphones && <p>{kit.headphones.name}</p>}
            </div>
            <div className="loadout-item">
              {kit.rig && <img src={kit.rig.image} alt={kit.rig.name} />}
              {kit.rig && <p>{kit.rig.name}</p>}
            </div>
            <div className="loadout-item">
              {kit.armor && <img src={kit.armor.image} alt={kit.armor.name} />}
              {kit.armor && <p>{kit.armor.name}</p>}
            </div>
            <div className="loadout-item">
              {kit.gun && <img src={kit.gun.image} alt={kit.gun.name} />}
              {kit.gun && <p>{kit.gun.name}</p>}
            </div>
            <div className="loadout-item">
              {kit.ammo && <img src={kit.ammo.image} alt={kit.ammo.name} />}
              {kit.ammo && <p>{kit.ammo.name}</p>}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default KitForm;
