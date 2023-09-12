import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Link, useParams } from 'react-router-dom';
import './App.css';

const App = () => {
  const [items, setItems] = useState([]);
  const [query, setQuery] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(`http://localhost:8000/get/get_paper/?query=${query}`);
        const data = await response.json();
        setItems(data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, [query]);

  const handleSearch = (e) => {
    e.preventDefault();
    setQuery(e.target.elements.search.value);
  };

  return (
    <Router>
      <div className="app">
        <div className="search-container">
          <h1>جست و جوی عنوان پایان‌نامه</h1>
          <form onSubmit={handleSearch}>
            <input type="text" name="search" placeholder="عنوان و یا کلمه در عنوان" />
            <button type="submit">جست و جو</button>
          </form>
        </div>

        <div className="list-container">
          <h1>لیست پایان‌نامه‌ها</h1>
          {items.length === 0 ? (
            <p>موردی یافت نشد</p>
          ) : (
            <ul>
              {items.map((item) => (
                <li key={item.id}>
                  <Link to={`/paper/${item.id}`}>{item.title}</Link>
                </li>
              ))}
            </ul>
          )}
        </div>

        <Routes>
          <Route path="/paper/:id" element={<PaperDetail />} />
        </Routes>
      </div>
    </Router>
  );
};

const PaperDetail = () => {
  const [paper, setPaper] = useState(null);
  const { id } = useParams();

  useEffect(() => {
    const fetchPaper = async () => {
      try {
        const response = await fetch(`http://localhost:8000/get/get_paper/${id}/`);
        const data = await response.json();
        setPaper(data);
      } catch (error) {
        console.error('Error fetching paper:', error);
      }
    };

    fetchPaper();
  }, [id]);

  if (!paper) {
    return (
      <div className="paper-detail">
        <div>Loading...</div>
      </div>
    );
  }

  return (
    <div className="paper-detail">
      <h2>{paper.title}</h2>
      <h3>چکیده</h3>
      <p>{paper.abstract}</p>
      <h3>موضوع سطح اول</h3>
      <p>{paper.fl_subject}</p>
      <h3>موضوع سطح دوم</h3>
      <p>{paper.sl_subject}</p>
      <h3>پایان‌نامه‌های مشابه</h3>
      <ul>
        {paper.recommended_papers.slice(1).map((recommendedPaper) => (
          <li key={recommendedPaper.id}>
            <Link to={`/paper/${recommendedPaper.id}`}>{recommendedPaper.title}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default App;
