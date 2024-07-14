import React, { useEffect, useState } from 'react';
import api from '../api';
import PlantCard from './PlantCard';
import PlantModal from './PlantModal';
import '../style/PlantList.css';

const PlantList = () => {
  const [plants, setPlants] = useState([]);
  const [selectedPlant, setSelectedPlant] = useState(null);

  useEffect(() => {
    // Fetch plants data from Django API
    api.get('/plants/')
      .then(response => {
        setPlants(response.data);
      })
      .catch(error => {
        console.error('Error fetching plants:', error);
      });
  }, []);

  const handleCardClick = (plant) => {
    setSelectedPlant(plant);
  };

  const handleCloseModal = () => {
    setSelectedPlant(null);
  };

  return (
    <div className="plant-list-container">
      <h2 className="plant-list-title">Currently Available</h2>
      <div className="plant-list">
        {plants.map(plant => (
          <PlantCard key={plant.id} plant={plant} onClick={handleCardClick} />
        ))}
      </div>
      {selectedPlant && (
        <PlantModal plant={selectedPlant} onClose={handleCloseModal} />
      )}
    </div>
  );
};

export default PlantList;
