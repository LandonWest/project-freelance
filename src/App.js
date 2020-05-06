import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [myGreeting, setMyGreeting] = useState();

  useEffect(() => {
    fetch('/v1/api').then(res => res.json()).then(data => {
      setMyGreeting(data.greeting);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h2>{myGreeting}</h2>
        <img src={logo} className="App-logo" alt="logo" />
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
