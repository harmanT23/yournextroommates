import React, { useEffect, useState } from 'react';
import './App.css';
import Listings from './components/Listings';
import DataLoading from './components/DataLoading';

function App() {
  const LoadListing = DataLoading(Listings);
  const [appState, setAppState] = useState({
      loading: false,
      listings: null,
  });

  useEffect(() => {
    setAppState({loading: true});
    const apiURL = 'http://127.0.0.1:8000/api/listings/';
    fetch(apiURL)
        .then((data) => data.json())
        .then((listings) => {
          setAppState({loading: false, listings: listings})
        }); 
      }, [setAppState]);
  
  return (
    <div className="App">
      <LoadListing 
          isLoading={appState.loading} 
          listings={appState.listings} 
      />
    </div>
  );
}

export default App