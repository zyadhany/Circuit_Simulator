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
    from ahkab.circuit import Circuit

    mycir.add_resistor('R1', 'n1', mycir.gnd, value=5)
    mycir.add_vsource('V1', 'n2', 'n1', dc_value=8)
    mycir.add_resistor('R2', 'n2', mycir.gnd, value=2)
    mycir.add_vsource('V2', 'n3', 'n2', dc_value=4)
    mycir.add_resistor('R3', 'n3', mycir.gnd, value=4)
    mycir.add_resistor('R4', 'n3', 'n4', value=1)
    mycir.add_vsource('V3', 'n4', mycir.gnd, dc_value=10)
    mycir.add_resistor('R5', 'n2', 'n4', value=4)
    ```