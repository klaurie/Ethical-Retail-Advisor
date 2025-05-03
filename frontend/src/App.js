/**
 * App.js - Main Application Component
 * 
 * This component serves as the entry point for the Ethical Retail Advisor application.
 * It handles the main application state, search functionality, and rendering of results.
 * 
 * Key features:
 * - Manages search results, loading states, and error handling
 * - Connects with backend API via the searchCompany service
 * - Formats ethics data for display in the EthicalCard component
 * - Provides responsive UI with conditional rendering based on search state
 */
import React, { useState } from 'react';
import logo from './ERA_logo.png';
import './App.css';
import SearchBar from './components/SearchBar';
import EthicalCard from './components/EthicalResponse';
import { searchCompany } from './services/api';

function App() {
  // Initialize state variables
  const [searchResult, setSearchResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // This function will handle search queries from the SearchBar
  const handleSearch = async (searchQuery) => {
    try {
      setLoading(true);
      setError(null);
      
      // Search with ethics evaluation included
      const result = await searchCompany(searchQuery, true);
      setSearchResult(result);
    } catch (err) {
      setError('Failed to search: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

    // Format ethics data for the EthicalCard component
    const formatEthicsData = (result) => {
      if (!result || !result.ethics_score) return null;
      
      const categories = result.ethics_score.categories || {};
      
      // Extract breakdown points from categories
      const breakdown = Object.entries(categories).map(
        ([category, [score, reason]]) => `${category}: ${score}/10 - ${reason}`
      );
      return {
        brand: result.name,
        rating: result.ethics_score.overall_score,
        sources: ['EthicalConsumer', 'GoodOnYou'], // Example sources
        breakdown,
        alternatives: ['Alternative 1', 'Alternative 2'] // Example alternatives
      };
    };

  return (
    <div className="App">
      <header className="App-header">
        <div className="logo-container">
          <img src={logo} alt="Ethical Retail Advisor Logo" className="app-logo" />
          <h1>Ethical Retail Advisor</h1>
        </div>
        <SearchBar onSearch={handleSearch} /> 
        {loading && <p>Searching...</p>}
        {error && <p className="error">{error}</p>}
        
        {searchResult && (
          <div className="results">
            <h2>Search Results</h2>
            {searchResult.ethics_score ? (
              <EthicalCard {...formatEthicsData(searchResult)} />
            ) : (
              <p>Found: {searchResult.name}</p>
            )}
          </div>
        )}
      </header>
    </div>
  );
}

export default App;
