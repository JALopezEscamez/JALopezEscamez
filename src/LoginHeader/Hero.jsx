import React from 'react';
import { useNavigate } from 'react-router-dom'; // Import the useNavigate hook
import Carousel from './Carousel';
import './Carousel.css';

const Hero = () => {
  const navigate = useNavigate(); // Create a navigate function

  const handleLoginClick = () => {
    navigate('/login'); // Navigate to the login page
  };

  return (
    <section className="hero">
      <h1>MÉNIÈRE'S DISEASE ATLAS</h1>
      <div className="hero-content">
        <img 
          src="/images/MD-Atlas-logo.png" 
          alt="Meniere's Disease Atlas" 
          className="hero-image" // Add a class for styling
        />
        <p className="hero-description">
          Explore comprehensive data and insights on Ménière's Disease. Our atlas serves as a valuable resource for understanding the complexities of this condition, providing research findings, treatment options, and support resources for patients and healthcare professionals.
        </p>
      </div>
      <Carousel />
    </section>
  );
}

export default Hero;
