import React from 'react';
import KitForm from './KitForm';

const Main = () => {
  return (
    <main className="main">
      <section className="welcome-section">
        <h2>What's up rat?</h2>
        <p>Was the normal beatdown not enough? No? Okay. Click the green button, flea market the gear, and queue up for your favorite map.</p>
      </section>
      <KitForm />
    </main>
  );
};

export default Main;
