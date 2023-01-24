# Exceptions Activity

## Wave 0: Setup

1. Have one team member fork AND clone this repository. They will be the driver. All commands and code will be run on their computer.

2. Make sure you do not have a virtual environment from another project active. We will create a new virtual environment for this activity.

3. Navigate to the activity directory and create a virtual environment inside it.
```
python3 -m venv venv
```

4. Activate the virtual environment.
```
source venv/bin/activate
```

5. Install requirements.
```
pip install -r requirements.txt
```

## Wave 1: Understanding the code.

1. Run the code, entering a few numbers and computing an average.
```
python3 main.py
```

2. Read the code in `average_calculator/calc.py`, discussing with your group how it works.
In particular, what is the try/except doing?

3. Predict what will happen if you run the code and try to compute an average before entering any numbers. Then, try actually running it. What happens? Does it match what you expected? 

## Wave 2: Raising a better exception.

1. Modify the average function. Make it so that it does NOT raise a `ZeroDivisionError`. Instead, have it raise a `ValueError` when an empty list is passed in. The description of the new error you create should be `cannot compute average of an empty collection`.

2. Run the code again, attempting to compute an average before entering any numbers. Verify that your new exception shows up.

3. Create a new commit with your changes added, and push it to GitHub.

## Wave 3: Catching an exception.

1. Modify the `calculator` function, adding a new try/catch to catch your new exception. Make it so that the code does not crash if the user attempts to calculate an average before entering numbers. Instead, it should show the message `You must enter at least one number before calculating an average`. It should then continue to prompt the user for more input.

2. Create a new commit with your changes added, and push it to GitHub.

## Wave 4: Tests

1. Verify that pytest is set up correctly by running `pytest` on the terminal (make sure you have your virtual environment activated!). You should see two tests skipped.

2. Open `tests/test_calc.py` and complete `test_average_of_two_numbers_is_properly_computed`. This does not require any exception handling. Unskip the test and verify that it works.

3. Complete `test_average_of_empty_list_raises_ValueError`. This does require testing for an exception. Unskip the test and verify that it works.

4. Create a new commit with your changes added, and push it to GitHub.

## OPTIONAL Wave 5:

1. Add additional tests to more thoroughly test the code.

2. Try modifying the `calculator` function to instead use the "Look Before You Leap" strategy, so that you do not need to use a try/except for the average. Which style do you prefer? What are the tradeoffs between the two, especially when we imagine adding more and more code that uses these functions?