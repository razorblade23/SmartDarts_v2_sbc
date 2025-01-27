[![build](https://github.com/razorblade23/SmartDarts_v2_sbc/actions/workflows/python-app.yml/badge.svg?branch=master&event=push)](https://github.com/razorblade23/SmartDarts_v2_sbc/actions/workflows/python-app.yml)


# SmartDarts 🎯

SmartDarts is a web-based application designed to bring smart functionality to electronic dartboards. It is built to run on single-board computers (SBCs) like Raspberry Pi and interfaces with the physical dartboard via GPIO pins to accurately register hits. The project aims to make local dart games more engaging and interactive.

---

# WARNING ⚠️
THIS IS A WORK IN PROGRESS AND IS NOT RUNNABLE YET.

---

## Features ✨

### Current Capabilities: 🚀
- **Dartboard Integration**:
  - Uses GPIO pins to connect and interact with physical electronic dartboards.
  - Configurable for various dartboard models via a guided initialization process. This allows you to map specific pins to numbers on the dartboard. (WORK IN PROGRESS)

- **Player Support**:
  - Supports up to 8 players in a single game session. (WORK IN PROGRESS)

- **Game Modes**:
  1. **X01**: 
     - Popular game modes such as 301, 501, 701, and more. (WORK IN PROGRESS
  2. **Cricket**:
     - Full support for this strategic dart game. (WORK IN PROGRESS)

- **Simulation Mode**:
  - Its possible to run the application in simulation mode. This DOES NOT require hardware components, wiring and physical dartboard, and is used for testing the application logic.

### Work in Progress: 🛠️
- Enhanced user interface.
- Additional game modes and options.
- Advanced analytics and scoring breakdowns.
- Remote game hosting and multiplayer support.

---

## Dartboard GPIO Connections 🔌

### Overview
The dartboard connects to the GPIO pins of the SBC in a matrix configuration. Each dartboard segment (e.g., specific numbers, doubles, and triples) corresponds to a row and column connection. 

### Wiring Explanation
1. **Matrix Layout**:
   - The dartboard uses a matrix system where rows and columns correspond to specific GPIO pins.
   - When a dart hits a segment, it closes the circuit at the intersection of the respective row and column.

2. **Resistors**:
   - Each column is connected via pull-down resistors to prevent floating signals and ensure stable readings.

3. **Pin Mapping**:
   Below is a mapping of the dartboard's segments to the GPIO pins:

   | Dartboard Column | GPIO Pin |
   |-------------------|----------|
   | Column 1          | GPIO 6   |
   | Column 2          | GPIO 27  |
   | Column 3          | GPIO 5   |
   | Column 4          | GPIO 17  |
   | Column 5          | GPIO 10  |
   | Column 6          | GPIO 22  |
   | Column 7          | GPIO 26  |

   The rows are connected similarly, with each dartboard number linked to specific pins for segment detection.

4. **Status LED**:
   - An optional status LED can be connected to GPIO pins to show system activity.

---

## Getting Started 🏁

### Prerequisites
To use SmartDarts (as intended), you will need:
- A single-board computer (e.g., Raspberry Pi) with GPIO support.
- A compatible electronic dartboard.
- Basic wiring to connect the dartboard's output pins to the SBC's GPIO pins.




### Installation (Method: 1) 💻
1. Clone this repository to your SBC:
   ```bash
   git clone https://github.com/razorblade23/SmartDarts_v2_sbc
   
   cd SmartDarts_v2_sbc

   ```
2. Install the necessary dependencies:
   ```bash
   sudo apt-get update
   sudo apt-get install -y python3 python3-pip
   python3 -m venv .venv
   source .venv/bin/activate
   pip install pip-tools
   pip-compile pyproject.toml
   pip install -r requirements.txt

   ```
3. Run the application:
   ```bash
   python3 app.py
   ```
4. Access the SmartDarts interface by navigating to `http://<your-sbc-ip>:5000` in your browser.





### Installation (Method: 2) 🖥️
1. Clone this repository to your SBC:
   ```bash
   git clone https://github.com/razorblade23/SmartDarts_v2_sbc
   cd SmartDarts_v2_sbc
   ```
2. Install the necessary dependencies:

   Check This [UV Official Docs](https://docs.astral.sh/uv/) For More Information on how to use UV
   #### requires uv dependancy
   ```bash
   uv sync
   ```
3. Run the application:
   ```bash
   uv run python run.py
   ```
4. Access the SmartDarts interface by navigating to `http://<your-sbc-ip>:5000` in your browser.

---





## Usage 🕹️

### Initial Setup 🔧
1. Power up your SBC and connect it to the local network.
2. Launch the application and configure your dartboard thrue guided proccess.
3. Once configured, you can select a game mode and add players to begin playing.

### Initial setup without SBC
1. A script in root dir called `sim_cli.py` can be used to simulate throwing darts in specified game. Game must be initialized, players added and game started.

---

## Contributing 🤝
Contributions are welcome! To contribute:
1. Fork this repository.
2. Create a branch for your feature or bug fix:
   ```bash
   git checkout -b feature/my-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add my feature"
   ```
4. Push to your branch and submit a pull request.

---

## License 📜
This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgements 🙏
- The Raspberry Pi community for GPIO libraries and support.
- Dart enthusiasts worldwide for game inspiration.

---

Enjoy playing darts with SmartDarts!
