import React from 'react';
import SearchBar from './SearchBar'; 
import logo from '../era-logo.png'; 

export default function MainHeader({ onSearch }) {
  return (
    <header className="App-main-header">
      <div className="header-content">
        <div className="logo-title-container">
          <img src={logo} alt="Ethical Retail Advisor Logo" className="app-logo" />
          <span className="main-title-style">Ethical Retail Advisor</span>
        </div>
        <SearchBar 
          onSearch={onSearch} 
        />
      </div>
    </header>
  );
}

