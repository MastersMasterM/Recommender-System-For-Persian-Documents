import React, { useState } from 'react';
import CreatePaperForm from './CreatePaperForm';
import './App.css';

function App() {
  const [signupName, setSignupName] = useState('');
  const [signupEmail, setSignupEmail] = useState('');
  const [signupPassword, setSignupPassword] = useState('');
  const [signupMessage, setSignupMessage] = useState('');

  const [loginEmail, setLoginEmail] = useState('');
  const [loginPassword, setLoginPassword] = useState('');
  const [loginMessage, setLoginMessage] = useState('');

  const [showSignup, setShowSignup] = useState(false); // State variable to track signup form visibility
  const [showCreatePaperForm, setShowCreatePaperForm] = useState(false); 

  const handleSignup = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('http://localhost:8000/api/user/create/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          name: signupName,
          email: signupEmail,
          password: signupPassword,
        }),
      });

      if (response.ok) {
        setSignupMessage('ثبت نام با موفقیت انجام شد');
      } else {
        setSignupMessage('ثبت نام ناموفق بود');
      }
    } catch (error) {
      console.error('Error:', error);
      setSignupMessage('ثبت نام ناموفق بود');
    }
  };

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('http://localhost:8000/api/user/token/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: loginEmail,
          password: loginPassword,
        }),
      });

      if (response.ok) {
        const data = await response.json();
        const token = data.token;
        localStorage.setItem('token', token);
        setLoginMessage('ورود موفقیت آمیز بود');
  
        // Redirect to the create paper page
        setShowSignup(false); // Reset signup form visibility
        setShowCreatePaperForm(true);
      } else {
        setLoginMessage('ورود ناموفق بود');
      }
    } catch (error) {
      console.error('Error:', error);
      setLoginMessage('ورود ناموفق بود');
    }
  };

  const toggleSignupForm = () => {
    setShowSignup(!showSignup);
  };

  return (
    <div>
      <h1>ورود</h1>
      <form onSubmit={handleLogin}>
        <input
          type="email"
          placeholder="Email"
          value={loginEmail}
          onChange={(e) => setLoginEmail(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          value={loginPassword}
          onChange={(e) => setLoginPassword(e.target.value)}
        />
        <button type="submit">ورود</button>
      </form>
      <p>{loginMessage}</p>

      
      {!showSignup && (
        <button onClick={toggleSignupForm}>نمایش فرم ثبت‌ نام</button>
      )}
      
      {showSignup && (
      <><h1>ثبت نام</h1><form onSubmit={handleSignup}>
          <input
            type="text"
            placeholder="نام"
            value={signupName}
            onChange={(e) => setSignupName(e.target.value)} />
          <input
            type="email"
            placeholder="Email"
            value={signupEmail}
            onChange={(e) => setSignupEmail(e.target.value)} />
          <input
            type="password"
            placeholder="Password"
            value={signupPassword}
            onChange={(e) => setSignupPassword(e.target.value)} />
          <button type="submit">ثبت نام</button>
        </form></>
      )}
      <p>{signupMessage}</p>
      {showCreatePaperForm && <CreatePaperForm />}
    </div>
  );
}

export default App;