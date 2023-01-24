import React from 'react';
import PropTypes from 'prop-types';
import './Task.css';

const Task = (props) => {
  const updateIsComplete = props.updateIsComplete;
  const deleteTask = props.deleteTask;

  const buttonClass = props.isComplete ? 'tasks__item__toggle--completed' : '';

  return (
    <li className="tasks__item">
      <button
        className={`tasks__item__toggle ${buttonClass}`}
        onClick={() => {
          updateIsComplete(props.id, props.isComplete);
        }}
      >
        {props.title}
      </button>
      <button
        className="tasks__item__remove button"
        onClick={() => {
          deleteTask(props.id);
        }}
      >
        x
      </button>
    </li>
  );
};

Task.propTypes = {
  id: PropTypes.number.isRequired,
  title: PropTypes.string.isRequired,
  isComplete: PropTypes.bool.isRequired,
  updateIsComplete: PropTypes.func.isRequired,
  deleteTask: PropTypes.func.isRequired,
};

export default Task;
