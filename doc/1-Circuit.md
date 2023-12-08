## Class: `Circuit`

### Instance Attributes

- `title`: The title of the circuit.
- `nodes_dict`: A dictionary containing all nodes as keys and values.
- `gnd`: Reference node of the circuit -> $V=0$.

### Methods

#### `create_node(name)`

- Creates a node with a given name and ensures it doesn't exist before.

#### `add_node(name)`

- Adds a node with a given name value, replacing it if it already exists.

#### `get_nodes_number()`

- Gets the number of nodes in the circuit.

#### `is_nonlinear()`

- Checks if the circuit is linear or not.

#### `get_elem_by_name(part_id)`

- Gets the object by its name or ID.

#### `add_resistor(part_id, n1, n2, value):`

- Adds a resistor object by its name or ID.

#### Parameters

-   `part_id` : string
        The resistor part_id (e.g., "R1"). The first letter is replaced by an R.

-    `n1, n2` : string
        The nodes to which the resistor is connected.

-    `value` : float,

    The resistance between ``n1`` and ``n2`` in Ohm.

    .. seealso::
    :func:`add_resistor`, :func:`add_inductor` :func:`add_vsource`, :func:`add_isource`, :func:`add_diode`, :func:`add_mos`, :func:`add_vcvs`, :func:`add_vccs`, :func:`add_cccs`, :func:`add_user_defined`, :func:`remove_elem`


#### `remove_elem(elem_or_id)`

- Removes an object from the circuit by its object or ID.

## Usage

- **Importing**:
    ```python
    from ahkab.circuit import Circuit
    ```
- **Main Functions**: 
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
- **Example**:
    ```python
    mycircuit = circuit.Circuit(title="Example circuit", filename=None)
    # no filename since there will be no deck associated with this circuit.
    # get the reference node (gnd)
    gnd = mycircuit.get_ground_node()
    # add a node named n1 and a 600 ohm resistor connected between n1 and gnd
    mycircuit.add_resistor(part_id="R1", n1="n1", n2=gnd, R=600)
    ```