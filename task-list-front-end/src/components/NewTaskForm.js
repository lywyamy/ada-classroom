import React from 'react';
import PropTypes from 'prop-types';
import { useState } from 'react';

const NewTaskForm = (props) => {
  const [taskTitle, setTaskTitle] = useState('');

  const onTitleChange = (event) => {
    setTaskTitle(event.target.value);
  };

  const onSubmitNewTask = (event) => {
    event.preventDefault();

    props.addNewTask(taskTitle);

    setTaskTitle('');
  };

  return (
    <form onSubmit={onSubmitNewTask}>
      <div>
        <label htmlFor="taskTitle">Title:</label>
        <input name="title" value={taskTitle} onChange={onTitleChange}></input>
      </div>
      <input type="submit" value="Add New Task"></input>
    </form>
  );
};

NewTaskForm.propTypes = {
  addNewTask: PropTypes.func.isRequired,
};

export default NewTaskForm;
