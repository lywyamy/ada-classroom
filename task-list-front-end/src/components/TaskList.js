import React from 'react';
import PropTypes from 'prop-types';
import Task from './Task';
import './TaskList.css';

const TaskList = (props) => {
  const taskListComponents = [];
  const taskList = props.tasks;
  const updateIsComplete = props.updateIsComplete;
  const deleteTask = props.deleteTask;

  for (const task of taskList) {
    taskListComponents.push(
      <Task
        key={task.id}
        id={task.id}
        title={task.title}
        isComplete={task.isComplete}
        updateIsComplete={updateIsComplete}
        deleteTask={deleteTask}
      ></Task>
    );
  }

  return <ul className="tasks__list no-bullet">{taskListComponents}</ul>;
};

TaskList.propTypes = {
  tasks: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.number.isRequired,
      title: PropTypes.string.isRequired,
      isComplete: PropTypes.bool.isRequired,
    })
  ).isRequired,
  updateIsComplete: PropTypes.func.isRequired,
  deleteTask: PropTypes.func.isRequired
};

export default TaskList;
