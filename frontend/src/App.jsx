import { useEffect, useState } from "react";

function App() {
  const [MyTitle, Content, About] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000")
      .then(res => res.json())
      .then(data => setPosts(data))
      .catch(err => console.error(err));
  }, []);

  return (
    
    <div className="App">
      <h1>{MyTitle}</h1>
      <p>{Content}</p>
      <p>{About}</p>
    </div>
  );
}

export default App;
