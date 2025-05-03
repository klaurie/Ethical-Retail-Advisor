import logo from './ERA_logo.png';
import './App.css';
import SearchBar from './components/SearchBar'; // Import the SearchBar component

function App() {
  // This function will handle search queries from the SearchBar
  const handleSearch = (searchQuery) => {
    console.log("Searching for:", searchQuery);
    // Here you would typically:
    // 1. Call an API to get search results
    // 2. Update state with those results
    // 3. Display the results in the UI
  };

  return (
    <div className="App">
      <header className="App-header">
        <div className="logo-container">
          <img src={logo} alt="Ethical Retail Advisor Logo" className="app-logo" />
          <h1>Ethical Retail Advisor</h1>
        </div>
        <SearchBar onSearch={handleSearch} /> {/* Add the SearchBar component */}
      </header>
    </div>
  );
}

export default App;
