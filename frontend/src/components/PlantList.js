import React, { useEffect, useState } from 'react';
import api from '../api';
import PlantCard from './PlantCard';
import '../style/PlantList.css';

const PlantList = () => {
  const [plants, setPlants] = useState([]);

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

  return (
    <div className="plant-list-container">
      <h2 className="plant-list-title">Currently Available</h2>
      <div className="plant-list">
        {plants.map(plant => (
          <PlantCard key={plant.id} plant={plant} />
        ))}
      </div>
    </div>
  );
};

export default PlantList;
