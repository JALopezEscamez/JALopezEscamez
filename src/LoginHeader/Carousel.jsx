import React, { useState } from 'react';
import './Carousel.css';

const Carousel = () => {
  const images = [
    '/images/MD-logo.png',
    '/images/Prosper.png',
    '/images/dna.jpeg'
  ];
  
  const [currentImage, setCurrentImage] = useState(0);

  const handleNext = () => {
    setCurrentImage((currentImage + 1) % images.length);
  }

  const handlePrev = () => {
    setCurrentImage((currentImage - 1 + images.length) % images.length);
  }

  return (
    <div className="carousel">
      <button className="prev" onClick={handlePrev}>&#8249;</button>
      <img src={images[currentImage]} alt="Meniere's Disease Atlas" />
      <button className="next" onClick={handleNext}>&#8250;</button>
    </div>
  );
}

export default Carousel;
