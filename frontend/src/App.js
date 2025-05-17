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

import FeatureColumns from './components/FeatureColumns'; // Import the new component

import sustainabilityIcon from './imgs/leaf_icon.png';
import laborRightsIcon from './imgs/people_icon.png';
import transparencyIcon from './imgs/coin_icon.png';

import './App.css';

import MainHeader from './components/MainHeader';
import EthicalCard from './components/EthicalResponse';
import { searchCompany } from './Services'; // Import the searchCompany function from Services.js

function App() {
  // Initialize state variables
  const [searchResult, setSearchResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [currentQuery, setCurrentQuery] = useState(""); // Store the current search query
    const [showIntro, setShowIntro] = useState(true); // Assuming you still have this

  const featureItemsData = [
    {
      imageSrc: sustainabilityIcon,
      imageAlt: 'Leaf icon representing sustainability',
      text: 'Sustainability' // This matches the text from your image
    },
    {
      imageSrc: laborRightsIcon,
      imageAlt: 'People icon representing labor rights',
      text: 'Labor Rights'
    },
    {
      imageSrc: transparencyIcon,
      imageAlt: 'Dollar sign icon representing transparency',
      text: 'Transparency'
    }
  ];

  // This function will handle search queries from the SearchBar
  const handleSearch = async (searchQuery) => {
    try {
      setCurrentQuery(searchQuery); // Set the current query for display
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
      <MainHeader 
        onSearch={handleSearch} 
        searchBarPlaceholder="Search for a company (e.g. Starbucks)"
      />
      <main className="App-page-content">
        <FeatureColumns items={featureItemsData} />
        {loading && <p>Searching...</p>}
        {error && <p className="error">{error}</p>}
        
               {searchResult && (
          <div className="results" style={{marginTop: '20px', width: '80%', maxWidth: '800px'}}>
            <h2>Results for: "{currentQuery}"</h2>
            
            <p><strong>Company (from backend lookup):</strong> {searchResult.name} (ID: {searchResult.company_id})</p>

            {/* Display LLM General Info */}
            {searchResult.llm_response && (
              <div className="llm-response" style={{ border: '1px solid #eee', padding: '15px', margin: '20px 0', backgroundColor: '#fdfdfd' }}>
                <h3>General Information from Assistant:</h3>
                <pre style={{ 
                  whiteSpace: 'pre-wrap', 
                  textAlign: 'left', 
                  backgroundColor: '#f0f0f0', 
                  padding: '10px', 
                  borderRadius: '4px',
                  fontFamily: 'monospace',
                  fontSize: '0.9em',
                  lineHeight: '1.5',
                  maxHeight: '500px', // Keep it from being too long
                  overflowY: 'auto'   // Add scroll for long content
                }}>
                  {searchResult.llm_response}
                </pre>
              </div>
            )}
          </div>
        )}
        </main>
    </div>
  );
}

export default App;
