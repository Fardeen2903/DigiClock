# DigiClock
Simple python code for a digital clock

Here's a sample README file for your digital clock code:

---

# Digital Clock with Turtle Graphics

This Python program uses the `turtle` graphics library to display a digital clock with a glossy crimson red background and black lettering for the time. The time updates every second and is shown inside a rectangular box.

## Features
- **Digital Clock**: Displays the current time in `hh:mm:ss` format.
- **Glossy Background**: The background is a glossy crimson red color.
- **Centered Time**: The time is displayed inside a rectangular box, centered within the screen.

## Requirements
- Python 3.x
- `turtle` graphics library (comes pre-installed with Python)

## Installation
1. Install Python 3.x from the official website: [Python Downloads](https://www.python.org/downloads/).
2. The `turtle` module is included with Python, so no additional installation is required for the graphics library.

## Usage
1. Save the code in a `.py` file (e.g., `digiclock.py`).
2. Run the file using Python.

```bash
python digiclock.py
```

Once the program starts, a window will pop up showing the digital clock with a crimson red background and black time display.

## How It Works
1. **Turtle Setup**:
   - Two turtles are used: One for drawing the rectangular box and another for displaying the time.
   - The screen background is set to crimson red using `s.bgcolor("crimson")`.
   
2. **Time Display**:
   - The current hour, minute, and second are obtained from the system using Python’s `datetime` module.
   - The time is written in the format `hh:mm:ss`, with leading zeros for single-digit numbers.
   - The time is updated every second with the `time.sleep(1)` function.
   
3. **Box for Time**:
   - A rectangular box is drawn around the time using the first turtle.
   - The time is centered inside the box.

4. **Loop**:
   - The time updates continuously within the loop, adjusting the second, minute, and hour accordingly.

## License
This project is open-source and free to use.

---

Feel free to customize or add more details based on your specific needs!
