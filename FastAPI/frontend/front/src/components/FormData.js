
import React, { useEffect, useState } from 'react';
import axios from 'axios';


const FormData = () => {
  const [userList, setUserList] = useState([]);
  const [name, setName] = useState('');
  const [city, setCity] = useState('');

  useEffect(() => {
    axios.get('http://localhost:8000')
      .then(res => {
        setUserList(res.data);
      })
      .catch(error => {
        console.error('Error fetching user data:', error);
      });
  }, []);  

  const addUserhandler = () => {
    axios.post('http://localhost:8000/formdata', { name, city })
      .then(res => {
        console.log(res.data);
        
      })
      .catch(error => {
        console.error('Error adding user:', error);
      });
  };

  return (
    <>
      <div>
        <label>Name:</label>
        <input
          type='text'
          placeholder='Enter your name'
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <label>City:</label>
        <input
          type='text'
          placeholder='Enter city'
          value={city}
          onChange={(e) => setCity(e.target.value)}
        />
        <button type='button' onClick={addUserhandler}>Store</button>
        

        <ul>
          {userList.map(user => (
            <li key={user.id}>
              {user.name}, {user.city}
            </li>
          ))}
        </ul>
      </div>
    </>
  );
};

export default FormData;


 