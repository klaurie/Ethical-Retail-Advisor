/*
*   Serivces.js
*
*   Handle backend API calls
*/

// default backend URL
// TODO: move to env variable
const API_BASE_URL = 'http://localhost:8000';

/**
 * Search for a company with optional ethics evaluation
 * 
 * @param {string} query - The company name to search for
 * @param {boolean} includeEthics - Whether to include ethical evaluation (defaults to false)
 * @returns {Promise} - JSON response with company data and optional ethics score
 */
export const searchCompany = async (query, includeEthics = false) => {
  try {
    // Construct the URL dynamically using template literals
    const response = await fetch(`${API_BASE_URL}/search/text${includeEthics ? '?eval=true' : ''}`, {
      // Configure the request options
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',  // Tell the server we're sending JSON
      },
      body: JSON.stringify({ query }),   // Convert our JavaScript object to JSON string
    });
    
    if (!response.ok) {
      throw new Error(`Error: ${response.status}`);
    }
    
    // Parse and return the JSON response data
    return await response.json();
  } catch (error) {
    console.error('Error searching company:', error);
    throw error;
  }
};

/**
 * Evaluate ethics for a specific company using its ID
 * 
 * @param {string} companyId - The unique identifier for the company
 * @returns {Promise} - JSON response with ethics evaluation data
 */
export const evaluateCompany = async (companyId) => {
  try {
    // Send POST request to the evaluate endpoint
    const response = await fetch(`${API_BASE_URL}/evaluate`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ company_id: companyId }),
    });
    
    if (!response.ok) {
      throw new Error(`Error: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('Error evaluating company:', error);
    throw error;
  }
};