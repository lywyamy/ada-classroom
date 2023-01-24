import PropTypes from "prop-types";
import "./Student.css";

const Student = (props) => {
  // const [isPresent, setIsPresent] = useState(false);

  // const togglePresence = () => {
  //   setIsPresent(!isPresent);
  // };

  const onAttendanceButtonClick = () => {
    const updatedStudent = {
      id: props.id,
      nameData: props.name,
      emailData: props.email,
      isPresentData: !props.isPresent,
    };

    props.onUpdate(updatedStudent);
  };

  const nameColor = props.isPresent ? "green" : "red";

  return (
    <div>
      <ul>
        <li className={nameColor}>Nickname: {props.name}</li>
        <li>Email: {props.email}</li>
      </ul>
      <button onClick={onAttendanceButtonClick}>
        Toggle if {props.name} is present
      </button>
    </div>
  );
};

Student.propTypes = {
  id: PropTypes.number.isRequired,
  name: PropTypes.string.isRequired,
  email: PropTypes.string.isRequired,
  isPresent: PropTypes.bool,
  onUpdate: PropTypes.func.isRequired,
};

export default Student;
