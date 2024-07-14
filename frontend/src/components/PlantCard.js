import React from 'react';
import '../style/PlantCard.css';

const PlantCard = ({ plant, onClick }) => {
  return (
    <div className="plant-card" onClick={() => onClick(plant)}>
      <div className="plant-card-header">
        <span className="plant-name">{plant.name}</span>
        <span className="plant-price">${plant.price}</span>
      </div>
      <img src={plant.image_url} alt={plant.name} className="plant-image" />
    </div>
  );
};

export default PlantCard;
