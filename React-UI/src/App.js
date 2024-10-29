import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; // Import necessary modules for routing
import './App.css';
import Header from './LoginHeader/Header';
import Hero from './LoginHeader/Hero';
import Login from './LoginComponent/Login';

function App() {
  const [isLoginOpen, setIsLoginOpen] = useState(false);

  const toggleLoginModal = () => {
    setIsLoginOpen(!isLoginOpen);
  };
  return (
    <Router> {/* Wrap the application in Router for routing functionality */}
      <div className="App">
        <Header onLoginClick={toggleLoginModal}/>
        {isLoginOpen && <Login onClose={toggleLoginModal} />}
        <Routes> {/* Define your routes here */}
          <Route path="/" element={<Hero />} /> {/* Hero component on the root path */}
          <Route path="/login" element={<Login />} /> {/* Login component on /login path */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
