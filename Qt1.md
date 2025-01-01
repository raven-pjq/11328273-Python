What the Code Can Do
Start State:
When the program starts, the label shows "Start!" and the counter is set to 0.

Counting Clicks:
Each time the "Click here" button is pressed:

The counter increases by 1.
The label updates to show the number of clicks (e.g., "Click 3 times！").
Limit Message:
If the counter reaches or exceeds 10, the label displays "Click over 10 times！" but the counter continues counting.

Reset Functionality:
When the "Reset" button is pressed:

The counter resets to 0.
The label updates to show "Reset!".

Code Explanation
Imports:
The code imports necessary PyQt6 modules for creating the application window, widgets (label and buttons), and layout.

MainWindow Class:

Initialization:
Sets up the window title, size, and layout. Initializes the counter variable and connects button actions to specific methods.
Methods:
increment_counter: Increments the counter and updates the label.
counter_limiter: Displays a special message when the counter is 10 or more.
counter_reset: Resets the counter and updates the label.
Main Program Block:

Creates the application (QApplication), initializes the window (MainWindow), and runs the event loop (sys.exit(app.exec())).
