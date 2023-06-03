# Time Tracker Pro

![Time Tracker Pro Logo](icon.png)

Time Tracker Pro is a robust application designed to help you keep track of the time you spend on your various projects. It's implemented using Python and TKinter and stores all time records in a csv file. It's simple, efficient, and easy to use!

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

* User-friendly Interface: Built with Python's Tkinter toolkit, Time Tracker Pro boasts a clean and straightforward GUI that is easy to navigate.
* Time Tracking: Tracks time spent on different projects accurately.
* Data Storage: All time data is stored in a neat CSV file that can be easily exported or imported.
* Data Visualisation: Provides a summary of the tracked time in a clear and comprehensive format.

## Installation

1. Clone this repository:
```sh
git clone https://github.com/PenguinPoweredApps/TimeTrackerPro.git
```

2. Change to the repository's directory:
```sh
cd TimeTrackerPro
```

3. Install necessary Python dependencies:
```sh
pip install -r requirements.txt
```

4. Run the app:
```sh
python time_tracker_pro
```

## Usage

1. **Add Project**: Click on the Project text box and enter the name of the project you want to track.

2. **Add Task Description**: Click on the Task Description text box and enter the name of the Task Description you want to track.

3. **Start Tracking**: To start tracking time, hit the 'Start' button.

4. **Stop Tracking**: To stop tracking time, hit the 'Stop' button.

5. **Save Tracking**: To save tracking time, hit the 'Save' button.

6. **View Tracked Time**: All your time data is stored in a CSV file named `<Project>-<StartTime>.csv` in the same directory.

7. **Build native app for Linux, Windows or Mac**: pyinstaller time_tracker_pro.spec

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please make sure to update tests as appropriate.

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

For any questions, feel free to open an issue or reach out to me directly.
