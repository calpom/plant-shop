import React from 'react';
import '../style/PlantCard.css';

const PlantCard = ({ plant }) => {
  return (
    <div className="plant-card">
      <div className="plant-card-header">
        <span className="plant-name">{plant.name}</span>
        <span className="plant-price">${plant.price}</span>
      </div>
      <img src={plant.image_url} alt={plant.name} className="plant-image" />
      <div className="plant-description">{plant.description}</div>
    </div>
  );
};

export default PlantCard;
