import React, { useState } from 'react';

function CreatePaperForm() {
  const [uid, setUid] = useState('');
  const [title, setTitle] = useState('');
  const [abstract, setAbstract] = useState('');
  const [flSubject, setFlSubject] = useState('');
  const [slSubject, setSlSubject] = useState('');
  const [message, setMessage] = useState('');
  const [submitUsed, setSubmitUsed] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('http://localhost:8000/api/paper_creation/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Token ${localStorage.getItem('token')}`,
        },
        body: JSON.stringify({
          uid,
          title,
          abstract,
          fl_subject: flSubject,
          sl_subject: slSubject,
        }),
      });

      if (response.ok) {
        setMessage('پژوهش با موفقیت اضافه شد');
        setSubmitUsed(true);
      } else {
        setMessage('عملیات ناموفق بود');
      }
    } catch (error) {
      console.error('Error:', error);
      setMessage('عملیات ناموفق بود');
    }
  };
  const handleUpdateList = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/updatelist/', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Token ${localStorage.getItem('token')}`,
        },
      });

      if (response.ok) {
        setMessage('لیست به‌روزرسانی شد');
      } else {
        setMessage('عملیات ناموفق بود');
      }
    } catch (error) {
      console.error('Error:', error);
      setMessage('عملیات ناموفق بود');
    }
  };
  return (
    <div>
      <h1>اضافه کردن پژوهش</h1>
      <form onSubmit={handleSubmit}>
      <input
          type="text"
          placeholder="uid"
          value={uid}
          onChange={(e) => setUid(e.target.value)}
        />
        <input
          type="text"
          placeholder="عنوان"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <textarea
          placeholder="چکیده"
          value={abstract}
          onChange={(e) => setAbstract(e.target.value)}
        />
        <input
          type="text"
          placeholder="موضوع سطح اول"
          value={flSubject}
          onChange={(e) => setFlSubject(e.target.value)}
        />
        <input
          type="text"
          placeholder="موضوع سطح دوم"
          value={slSubject}
          onChange={(e) => setSlSubject(e.target.value)}
        />
        <button type="submit">ثبت</button>
      </form>
      {submitUsed && (
        <button onClick={handleUpdateList}>به‌روزرسانی لیست</button>
      )}
      <p>{message}</p>
    </div>
  );
}

export default CreatePaperForm;