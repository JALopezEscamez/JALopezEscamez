import React, { useState } from 'react';
import './Login.css';

const Login = ({ onClose }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [rememberMe, setRememberMe] = useState(false);
  const [isSignUp, setIsSignUp] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (isSignUp) {
      console.log('Signed Up:', { email, password });
    } else {
      console.log('Logged In:', { email, password, rememberMe });
    }
    onClose(); // Close modal after login/signup
  };

  return (
    <div className="modal-overlay">
      <div className="login-container">
        <button className="close-btn" onClick={onClose}>X</button> {/* Close button */}
        
        <form onSubmit={handleSubmit} className="login-form">
          <div className="form-toggle">
            <button onClick={() => setIsSignUp(false)} className={`toggle-btn ${!isSignUp ? 'active' : ''}`}>Login</button>
            <button onClick={() => setIsSignUp(true)} className={`toggle-btn ${isSignUp ? 'active' : ''}`}>Sign Up</button>
          </div>
          
          <h2>{isSignUp ? 'Sign Up' : 'Login'}</h2>
          <div className="input-group">
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              placeholder="Email"
            />
          </div>
          <div className="input-group">
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              placeholder="Password"
            />
          </div>
          {isSignUp && (
            <div className="input-group">
              <input
                type="password"
                required
                placeholder="Confirm Password"
              />
            </div>
          )}
          <div className="remember-me">
            { !isSignUp && (
              <>
                <input
                  type="checkbox"
                  checked={rememberMe}
                  onChange={(e) => setRememberMe(e.target.checked)}
                />
                <label>Remember Me</label>
              </>
            )}
          </div>
          <button type="submit" className="login-btn">{isSignUp ? 'Sign Up' : 'Login'}</button>
          
          <div className="links">
            {!isSignUp ? (
              <>
                <a href="#">Forgot Password?</a>
                <p>Don't have an account? <a onClick={() => setIsSignUp(true)}>Sign Up</a></p>
              </>
            ) : (
              <p>Already have an account? <a onClick={() => setIsSignUp(false)}>Login</a></p>
            )}
            <p><a href="#">Terms and Conditions</a></p>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Login;
