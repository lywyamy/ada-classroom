import LocationSearchForm from "./components/LocationSearchForm";
import LocationList from "./components/LocationList";
import ErrorMessage from "./components/ErrorMessage";
import axios from "axios";
import { useState } from "react";

function App() {
  const [latestSearch, setLatestSearch] = useState({});
  const [searchHistory, setSearchHistory] = useState([]);
  const [successfulSearch, setSuccefulSearch] = useState(true);

  const getLocationInfo = (location) => {
    axios
      .get("http://127.0.0.1:5000/location", { params: { q: location } })
      .then((response) => {
        const lat = response.data[0].lat;
        const lon = response.data[0].lon;

        const successfulLocation = {
          location: location,
          lat: lat,
          lon: lon,
        };

        setLatestSearch(successfulLocation);

        const updatedSearchHistory = [...searchHistory];
        updatedSearchHistory.push(successfulLocation);
        setSearchHistory(updatedSearchHistory);

        setSuccefulSearch(true);
      })
      .catch((error) => {
        const unsuccessfulLocation = {
          location: location,
          lat: "N/A",
          lon: "N/A",
        };

        setLatestSearch(unsuccessfulLocation);

        setSuccefulSearch(false);
        console.log(error);
      });
  };
  return (
    <main>
      <div>
        <h1>Get Latitude and Longitude</h1>
        <LocationSearchForm
          locationInfo={latestSearch}
          getLocationInfo={getLocationInfo}
        ></LocationSearchForm>
      </div>
      <div>
        <ErrorMessage successfulSearch={successfulSearch}></ErrorMessage>
      </div>
      <div>
        <h2>Search History</h2>
        <LocationList locationList={searchHistory}></LocationList>
      </div>
    </main>
  );
}

export default App;
