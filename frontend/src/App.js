import './App.css';
import{useEffect, useState} from 'react';
import './output.css';

function App() {
  const [data,setData]=useState({})
  useEffect(()=>{
    fetchData();
  },[]);

  const fetchData=async ()=>{
    const response=await fetch("http://127.0.0.1:5000/api/data")
    const jsondata=await response.json()
    setData(jsondata)
  }
  return (
    <div className="App">
      <h1 class="text-white bg-black p-5">Front End with React and Tailwind</h1>
      <h1 class="bg-orange-500 p-5 mt-5 font-bold ">
        {data.message} <br />
        {data.name} <br />
        {data.email} <br />
        </h1>
    </div>
  );
}

export default App;
