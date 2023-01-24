import PropTypes from "prop-types";
import { useState } from "react";

const Location = (props) => {
  const [location, setLocation] = useState("Chengdu");

  const onSubmitSearchRequest = (event) => {
    event.preventDefault();

    props.getLocationInfo(location);

    setLocation("");
  };

  return (
    <div>
      <form onSubmit={onSubmitSearchRequest}>
        <input
          onChange={(event) => setLocation(event.target.value)}
          placeholder="Chengdu"
        ></input>
        <input type="submit"></input>

        <div>
          <h2>Results for {props.locationInfo.location}</h2>
          <ul>
            <li>Latitude: {props.locationInfo.lat}</li>
            <li>Longitude: {props.locationInfo.lon}</li>
          </ul>
        </div>
      </form>
    </div>
  );
};

Location.propTypes = {
  locationInfo: PropTypes.shape({
    location: PropTypes.string,
    lat: PropTypes.string,
    lon: PropTypes.string,
  }),
  getLocationInfo: PropTypes.func.isRequired,
};

export default Location;
