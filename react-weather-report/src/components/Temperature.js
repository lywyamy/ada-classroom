import { useState } from "react";
import "./Temperature.css";

const Temperature = () => {
  const [currentTemp, updateTemp] = useState(18);

  const increaseTemp = () => {
    updateTemp(currentTemp + 1);
  };

  const decreaseTemp = () => {
    updateTemp(currentTemp - 1);
  };

  let colorRange;
  if (currentTemp >= 26) {
    colorRange = "red";
  } else if (currentTemp >= 20) {
    colorRange = "orange";
  } else if (currentTemp >= 15) {
    colorRange = "yellow";
  } else if (currentTemp >= 10) {
    colorRange = "green";
  } else {
    colorRange = "blue";
  }

  return (
    <div>
      <button onClick={increaseTemp}>&#8593;</button>
      <p className={colorRange}>The temperature is {currentTemp}</p>
      <button onClick={decreaseTemp}>&#8595;</button>
    </div>
  );
};

export default Temperature;
