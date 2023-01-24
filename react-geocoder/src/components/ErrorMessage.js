import PropTypes from "prop-types";
import "./ErrorMessage.css";

const ErrorMessage = (props) => {
  return props.successfulSearch ? (
    ""
  ) : (
    <div id="error-message-box">
      <h3 id="error-message-header">Uh, oh! Error!</h3>
      <p id="error-message-body">
        Sorry, we're unable to geocode this location.
      </p>
    </div>
  );
};

ErrorMessage.propTypes = {
  successfulSearch: PropTypes.bool.isRequired,
};

export default ErrorMessage;
