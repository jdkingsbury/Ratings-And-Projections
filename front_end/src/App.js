import React, { useEffect, useState } from 'react';
import Header from './components/Header';
import { fetchNBAData } from './api';

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    const getData = async () => {
      try {
        const nbaData = await fetchNBAData("functionName", {
          params: "params",
        });
        setData(nbaData);
      } catch (error) {
        console.error(error);
      }
    };
    getData();
  }, []);

  return (
    <div className="App">
      <Header />
      <div>
        {data ? <pre>{JSON.stringify(data, null, 2)}</pre> : <p>Loading...</p>}
      </div>
    </div>
  );
}

export default App;
