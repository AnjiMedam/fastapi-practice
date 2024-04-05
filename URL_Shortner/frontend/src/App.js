// // App.js


import React, { useState } from 'react';
import axios from 'axios';
// import "./InputForm.css"
 
function App() {
  const [originalUrl, setOriginalUrl] = useState('');
  const [shortenedUrl, setShortenedUrl] = useState('');
 
  const handleChange = async (e) => {
    setOriginalUrl(e.target.value);
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
        const response = await axios.post('http://127.0.0.1:8000/shorten/', { original_url: originalUrl });
      setShortenedUrl(response.data.short_link);
    } catch (error) {
      console.error('Error:', error);
    }
  };
 
  return (
    <div>
        <h1 className='text-align: center'>URL SHORTNER</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter URL"
          value={originalUrl}
          onChange={handleChange}
        /><br/>
        <button type="submit">Shorten</button>
        <hr/>
      </form>
      {originalUrl && <p>Original URL: <br/>{originalUrl}</p>}
      <p>Short URL: <br/>{shortenedUrl}</p>
      {/* {shortenedUrl && <p>Shortened URL: {shortenedUrl}</p>} */}
    </div>
  );
}
 
export default App;
 



































// import React, { useState } from 'react';
// import axios from 'axios';

// function App() {
//   const [originalUrl, setOriginalUrl] = useState('');
//   const [shortenedUrl, setShortenedUrl] = useState('');



//   // const handleSubmit = async (e) => {
//   //   e.preventDefault();
//   //   try {
//   //     const response = await axios.post('http://localhost:8000/shorten/', { original_url: originalUrl });
//   //     // console.log('Response data:', response.data);
//   //     setShortenedUrl(response.data.short_url);
//   //   } catch (error) {
//   //     console.error('Error:', error);
//   //   }
//   // }

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     try {
//       const response = await axios.post('http://localhost:8000/shorten/', { original_url: originalUrl });
//       setShortenedUrl(response.data.short_url);
//     } catch (error) {
//       console.error('Error:', error);
//       setShortenedUrl(''); // Reset the shortened URL in case of error
//       alert('An error occurred while shortening the URL. Please try again.');
//     }
//   }

//   return (
//     <div>
//       <h1>URL Shortener</h1>
//       <form onSubmit={handleSubmit}>
//         <label>
//           Original Url:
//           <input type="text" value={originalUrl} onChange={handleChange} />
//         </label>
//         <button type="submit">Shorten URL</button>
//         {/* <input type='button' value=' submit'/> */}
//       </form>
//       {shortenedUrl && (
//         <div>
//           <p>Shortened URL: {shortenedUrl}</p>
//           <p>Shortened URL: <a href={shortenedUrl} target='_blank' rel='noopener noreferrer '  >hello{shortenedUrl}</a></p>
//         </div>
//       )}
//     </div>
//   );
// }

// export default App;




// import React, { useState } from 'react';
// import axios from 'axios';

// function App() {
//   const [originalUrl, setOriginalUrl] = useState('');
//   const [shortenedUrl, setShortenedUrl] = useState('');

// const handleChange=async(e)=>{
//   setOriginalUrl(e.target.value);
// }

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     try {
//       const response = await axios.post('http://localhost:8000/shorten/', { original_url: originalUrl });
//       // console.log('Response data:', response.data);
//      setShortenedUrl(response.data.short_url);
//     } catch (error) {
//       console.error('Error:', error);
//     }
//   };

//   return (
//     <div>
//       <h1>URL Shortener</h1>
//       <form onSubmit={handleSubmit}>
//        <label> Original Url:
//         <input type="text" value={originalUrl} onChange={handleChange} />
//         </label>
//         <button type="submit">Shorten URL</button>
//       </form>
//       {shortenedUrl && (
//         <div>
//           {/* <p>Shortened URL: {shortenedUrl}</p>  */}
//           <p>Shortened URL: <a href={shortenedUrl} target='_blank' rel='noopener noreferrer '  >hello{shortenedUrl}</a></p>

//         </div>
//       )}
//     </div>
//   );
// }

// export default App;








