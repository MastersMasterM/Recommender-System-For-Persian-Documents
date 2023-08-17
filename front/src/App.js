import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Link, useParams } from 'react-router-dom';
import './App.css';

const App = () => {
  const [items, setItems] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:8000/get/get_paper/');
        const data = await response.json();
        setItems(data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <Router>
      <div className="app">
        <div className="list-container">
          <h1>لیست مقالات</h1>
          <ul>
            {items.map((item) => (
              <li key={item.id}>
                <Link to={`/paper/${item.id}`}>{item.title}</Link>
              </li>
            ))}
          </ul>
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
      <h3>چکیده:</h3>
      <p>{paper.abstract}</p>
      <h3>موضوع سطح اول</h3>
      <p>{paper.fl_subject}</p>
      <h3>موضوع سطح دوم</h3>
      <p>{paper.sl_subject}</p>
      <h3>مقالات مشابه</h3>
      <ul>
        {paper.recommended_papers.map((recommendedPaper) => (
          <li key={recommendedPaper.id}>
            <Link to={`/paper/${recommendedPaper.id}`}>{recommendedPaper.title}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default App;