import PropTypes from "prop-types";
import Location from "./Location";

const LocationList = (props) => {
  const locationList = props.locationList;

  const locationListComponents = locationList.map((location, index) => {
    return (
      <Location
        key={index}
        location={location.location}
        lat={location.lat}
        lon={location.lon}
      ></Location>
    );
  });

  return <ul>{locationListComponents}</ul>;
};

LocationList.propTypes = {
  locationList: PropTypes.arrayOf(
    PropTypes.shape({
      location: PropTypes.string.isRequired,
      lat: PropTypes.string.isRequired,
      lon: PropTypes.string.isRequired,
    })
  ),
};

export default LocationList;
