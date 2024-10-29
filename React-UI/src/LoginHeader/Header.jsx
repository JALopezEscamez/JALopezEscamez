import React from 'react';
import './Header.css';

const Header = ({ onLoginClick }) => {
  return (
    <header>
      <div className="kolling-logo">
        <img src="/images/kollingLogo.png" alt="Kolling Institute Logo" />
      </div>
      <div className="nav-container">
        <nav>
          <ul className="nav-links">
            <li><a href="https://github.com/r5n-labs/vscode-react-javascript-snippets/blob/master/docs/Snippets.md">Home</a></li>
            <li><a href="https://kollinginstitute.org.au/menieres-disease-neuroscience-group">Research</a></li>
            <li><a href="#">About</a></li>
            <li><a href="https://northfoundation.org.au/menieresdiseaseresearch/">Support Us</a></li>
            <li><a href="#">Contact Us</a></li>
          </ul>
        </nav>
      </div>
      <div class="header-right">
      <button onClick={onLoginClick} className="login-signup-btn">Login/Signup</button>
      </div>
      
    </header>
  );
}

export default Header;
