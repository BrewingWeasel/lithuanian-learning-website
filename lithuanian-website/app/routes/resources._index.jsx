export const meta = () => {
  return [
    { title: "Lithuanian resources" },
    { name: "description", content: "Resources for learning Lithuanian" },
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

function Resources() {

  return (
    <div className="App">
      <NavBar />
      <p>WIP</p>
    </div>
  );
}

export default Resources;
