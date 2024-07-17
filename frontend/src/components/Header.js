import React from 'react';
import '../style/Header.css';

const Header = () => {
  return (
    <header className="header">
      <div className="header-title">The Plant Shop</div>
      <div className="header-right">
        <input type="text" className="search-bar" placeholder="Search..." />
        <button className="search-button">
          <i className="fas fa-search"></i>
        </button>
        <button className="heart-button">
          <i className="fas fa-heart"></i>
        </button>
        <button className="cart-button">
          <i className="fas fa-shopping-cart"></i>
        </button>
      </div>
    </header>
  );
};

export default Header;
