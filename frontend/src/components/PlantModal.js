// src/components/PlantModal.js
import React, { useState } from 'react';
import '../style/PlantModal.css';

const PlantModal = ({ plant, onClose }) => {
  const [isFavorited, setIsFavorited] = useState(false);

  if (!plant) return null;

  const handleHeartClick = () => {
    setIsFavorited(!isFavorited);
  };

  return (
    <>
      <div className="overlay" onClick={onClose}></div>
      <div className="modal">
        <div className="modal-content">
          <div className="modal-image">
            <img src={plant.image_url} alt={plant.name} />
          </div>
          <div className="modal-details">
            <div className="modal-header">
              <h2 className="modal-title">{plant.name}</h2>
              <button className="close-button" onClick={onClose}>×</button>
            </div>
            <p className="modal-price">${plant.price}</p>
            <p className="modal-stock">{plant.stock} in stock</p>
            <p className="modal-description">{plant.description}</p>
            <div className="modal-actions">
              <button className="heart-button" onClick={handleHeartClick}>
                <i className={isFavorited ? 'fas fa-heart' : 'far fa-heart'}></i>
              </button>
              <button className="add-to-cart-button">Add to Cart</button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default PlantModal;
