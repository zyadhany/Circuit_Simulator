# Circuit Simulator

This is the Simulation project that provides a GUI interface for circuit analysis.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

Steps to install the project:

```bash
pip install numpy
pip install scipy
pip install sympy
pip install tabulate
pip install matplotlib
pip install nose
```

## Usage

### Running the Application

To run the GUI interface, execute the following command:

```bash
python3 main.py
```

### Implementation Notes

#### Define Circuit


- **importing**:
    ```python
    from ahkab.circuit import Circuit
    ```
- **main functions**: 
    ```python
    Circuit.add_resistor()
    Circuit.add_capacitor()
    Circuit.add_inductor()
    Circuit.add_vsource()
    Circuit.add_isource()
    Circuit.add_diode()
    Circuit.add_mos()
    Circuit.add_cccs()
    Circuit.add_vcvs()
    Circuit.add_vccs()
    Circuit.add_user_defined()
    Circuit.remove_elem()
    ```
- **Testing**: Test your changes thoroughly to ensure they work as expected.
- **Submit a Pull Request**: Once tested, submit a pull request to the repository's `develop` branch, detailing the changes made and the rationale behind them.

### Code Structure


### Notes

Include any additional notes, tips, or caveats here.

## Features

List of features provided by the project:

- GUI interface for circuit analysis
- Feature 2
- ...

## Contributing


## License

Specify the project's license.

---
