import { useState } from "react";
import PropTypes from "prop-types";

const NewStudentForm = (props) => {
  const [formFields, setFormFields] = useState({
    name: "",
    email: "",
  });

  const onNameChange = (event) => {
    setFormFields({
      ...formFields,
      name: event.target.value,
    });
  };

  const onEmailChange = (event) => {
    setFormFields({
      ...formFields,
      email: event.target.value,
    });
  };

  const onFormSubmit = (event) => {
    event.preventDefault();

    props.onAddStudentData({
      nameData: formFields.name,
      emailData: formFields.email,
    });

    setFormFields({
      name: "",
      email: "",
    });
  };

  return (
    <form onSubmit={onFormSubmit}>
      <div>
        <lable htmlFor="fullName">Name:</lable>
        <input
          name="fullName"
          value={formFields.name}
          onChange={onNameChange}
        ></input>
      </div>
      <div>
        <lable htmlFor="email">Email:</lable>
        <input
          name="email"
          value={formFields.email}
          onChange={onEmailChange}
        ></input>
      </div>
      <input type="submit" value="add Student"></input>
    </form>
  );
};

NewStudentForm.propTypes = {
  onAddStudentData: PropTypes.func.isRequired,
};

export default NewStudentForm;
