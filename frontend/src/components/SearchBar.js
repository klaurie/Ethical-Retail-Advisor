/**
 * SearchBar Component
 * 
 * A reusable search input component that captures user queries and triggers search functionality.
 * 
 * Features:
 * - Manages its own input state
 * - Handles form submission
 * - Prevents default form submission behavior
 * - Passes search query to parent component via callbaack
 */
import React, { useState } from 'react';

export default function SearchBar({ onSearch }) {
    // Creates and initializes the query state variable
    const [query, setQuery] = useState('');
    
    const handleSubmit = (e) => {
        e.preventDefault(); // Prevents page reload on form submission
        onSearch(query); // Executes the search with current query text
    };
    
    return (
        <form className="search-bar" onSubmit={handleSubmit}>
            <input
                type="search"
                value={query}
                onChange={(e) => setQuery(e.target.value)} // Updates query state when user types
                placeholder="Search products..."
                aria-label="Search"
            />
            <button type="submit" aria-label="Submit search">
                Search
            </button>
        </form>
    );
}