import logo from './logo.svg';
import './App.css';
import axios from "axios";
import { useState } from 'react'

function App() {


  const [info, setInfo] = useState(null);

  function getData() {
    axios({
      method: "GET",
      url: "/info"
    }).then((response) => {
        const res = response.data
        setInfo(({
          translation: res.word
        }))
      }).catch((error) => {
      if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
        }
    })
  }

  return (
    <div className="App">
       <p>To get your profile details: </p><button onClick={getData}>Click me</button>
        {info && <div>
              <p>Translation: {info.translation}</p>
            </div>
          }
    </div>
  );
}

export default App;
