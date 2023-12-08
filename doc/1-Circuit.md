## Class: `Circuit`

### Instance Attributes

- `title`: The title of circuit
- `nodes_dict`: Dictnary that contain all node as key and value
- `gnd`: Reference node of circuit -> $V=0$

### Methods

#### `create_node(name)`

create node with name value and make sure it's not exit before

#### `get_nodes_number()`

Get number of nodes in Curcuit

#### Parameters

- `num`: The number to be added.

# Usage

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
