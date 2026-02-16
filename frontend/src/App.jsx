import { useEffect, useState } from "react";


console.log("Hello world");


function App() {
    const [pageData, setPageData] = useState({});

    useEffect(() => {
        fetch('http://127.0.0.1:8000/') // Path to your Django view
            // .then(res => res.json())
            .then(data => setPageData(data));
}, []);


return (
    <div className="App">
        <h1>{data.message}</h1>
    </div>
);
}
console.log("Hello world");



export default App;
