import React, {useEffect, useState} from "react";

export default function App(){
  const [items, setItems] = useState([]);
  useEffect(()=>{
    fetch("/api/items")
      .then(res=>res.json())
      .then(setItems)
      .catch(console.error);
  }, []);
  return (
    <div style={{padding:20}}>
      <h1>Sample App</h1>
      <ul>
        {items.map((it, idx)=> <li key={idx}>{it.name} - {it.value}</li>)}
      </ul>
    </div>
  )
}

