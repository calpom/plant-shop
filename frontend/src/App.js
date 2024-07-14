import React from 'react';
import PlantList from './components/PlantList';
import Header from './components/Header';
import '@fortawesome/fontawesome-free/css/all.min.css';

function App() {
  return (
    <div className="App">
      <Header />
      <PlantList />
    </div>
  );
}

export default App;
