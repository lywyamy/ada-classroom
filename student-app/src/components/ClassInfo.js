import PropTypes from "prop-types";

const ClassInfo = (props) => {
  const onClearButtonClick = () => {
    props.onClearStudentData();
  };

  return (
    <section>
      <h2>Class Information</h2>
      <ul>
        <li>Name: Team Semicolons</li>
        <li>Number of members: {props.studentCount}</li>
      </ul>
      <button onClick={onClearButtonClick}>Delete All Students!</button>
    </section>
  );
};

ClassInfo.propTypes = {
  studentCount: PropTypes.number.isRequired,
  onClearStudentData: PropTypes.func.isRequired,
};

export default ClassInfo;
