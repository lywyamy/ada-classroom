import PropTypes from "prop-types";

const Location = (props) => {
  return (
    <div>
      <h3>{props.location}</h3>
      <p>
        Latitude: {props.lat} Longitude: {props.lon}
      </p>
    </div>
  );
};

Location.propTypes = {
  location: PropTypes.string.isRequired,
  lat: PropTypes.string.isRequired,
  lon: PropTypes.string.isRequired,
};

export default Location;
