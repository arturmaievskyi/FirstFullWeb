import { useEffect, useState } from "react";


console.log("Hello world");


function App() {
    const [pageData, setPageData] = useState({});

    useEffect(() => {
        fetch('/test') // Path to your Django view
            .then(res => res.json())
            .then(data => setPageData(data));
            return data
}, []);


return (
    <div className="App">
        <h1>{pageData.message}</h1>
    </div>
);
}
console.log("Hello world");



export default App;
