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

pip install opencv-python
pip install pyautogui
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
- **example**:
    ```python
    mycircuit = circuit.Circuit(title="Example circuit", filename=None)
    # no filename since there will be no deck associated with this circuit.
    # get the ref node (gnd)
    gnd = mycircuit.get_ground_node()
    # add a node named n1 and a 600 ohm resistor connected between n1 and gnd
    mycircuit.add_resistor(part_id="R1", n1="n1", n2=gnd, R=600)
    ```
- **useful functions**:
    ```python
    #get node id
    my_circuit.nodes_dict[int_node]
    ```
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

