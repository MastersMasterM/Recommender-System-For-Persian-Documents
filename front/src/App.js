import React, { useState, useEffect } from 'react';

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
    <div>
      <h1>لیست مقالات</h1>
      <ul>
        {items.map((item) => (
          <li key={item.id}>
            <a href="">{item.title}</a>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default App;