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
      <img 
        src="/images/MD-Atlas-logo.png" 
        alt="Meniere's Disease Atlas" 
        className="hero-image" // Add a class for styling
      />
      <p className="hero-description">
      Meniere’s Disease (MD) is an inflammatory disorder of the inner ear defined by episodes of vertigo associated with sensorineural hearing loss, tinnitus, and aural fullness. Epidemiological, clinical and molecular research support several mechanisms, including rare genetic variants, leading to autosomal dominant or recessive inheritance, and changes in the immune response.
      </p>
      <Carousel />
    </section>
  );
}

export default Hero;
