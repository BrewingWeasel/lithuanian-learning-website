// import './App.css';
// import axios from "axios";
import { useState } from 'react'

export const meta = () => {
  return [
    { title: "New Remix App" },
    { name: "description", content: "Welcome to Remix!" },
  ];
};


function NavBar() {
  return (
    <div id="header">
      <ul>
        <li><a href="">Home</a></li>
        <li><a href="resources">Resources</a></li>
        <li><a href="wip">Decliner</a></li>
        <li><a href="wip">Conjugator</a></li>
        <li><a href="about">About</a></li>
      </ul>
    </div>
  );
}

function Index() {


  const [info, setInfo] = useState(null);

  function getData() {
    // axios({
    //   method: "GET",
    //   url: "/info"
    // }).then((response) => {
    //     const res = response.data
    //     setInfo(({
    //       translation: res.word
    //     }))
    //   }).catch((error) => {
    //   if (error.response) {
    //     console.log(error.response)
    //     console.log(error.response.status)
    //     console.log(error.response.headers)
    //     }
    // })
    setInfo(({
      translation: "labas"
    }))
  }

  return (
    <div className="App">
      <NavBar />
      <p>To get your profile details: </p><button onClick={getData}>Click me</button>
      {info && <div>
        <p>Translation: {info.translation}</p>
      </div>
      }
    </div>
  );
}

export default Index;
