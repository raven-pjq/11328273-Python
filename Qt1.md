# PyQt6 Counter Application

This is a simple GUI application built using **PyQt6**. It creates a window with a counter, buttons, and interactive functionality.

---

## What the Code Can Do

### Start State
- When the program starts, the label shows **"Start!"** and the counter is set to `0`.

### Counting Clicks
- Each time the **"Click here"** button is pressed:
  - The counter increases by `1`.
  - The label updates to show the number of clicks (e.g., **"Click 3 times！"**).

### Limit Message
- If the counter reaches or exceeds `10`, the label displays **"Click over 10 times！"**, but the counter continues counting.

### Reset Functionality
- When the **"Reset"** button is pressed:
  - The counter resets to `0`.
  - The label updates to show **"Reset!"**.

---

## Code Explanation

### Imports
The code imports necessary **PyQt6** modules for:
- Creating the application window.
- Adding widgets (label and buttons).
- Managing layout.

### `MainWindow` Class

#### Initialization
- Sets up:
  - Window title: **"Click!"**.
  - Window size: **400x300 pixels**.
  - Layout for widgets.
- Initializes the counter variable.
- Connects button actions to specific methods.

#### Methods
- **`increment_counter`**:  
  Increments the counter and updates the label to reflect the new count.
- **`counter_limiter`**:  
  Displays a special message when the counter reaches or exceeds `10`.
- **`counter_reset`**:  
  Resets the counter to `0` and updates the label.

### Main Program Block
- Creates the application (`QApplication`).
- Initializes the window (`MainWindow`).
- Starts the event loop (`sys.exit(app.exec())`).

---

## How to Run the Code
1. Install **PyQt6**:
   ```bash
   pip install PyQt6
