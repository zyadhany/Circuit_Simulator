### Simulating Circuits

#### Main Functions

- [`new_ac`](#new_ac): Set up AC analysis.
- [`new_dc`](#new_dc): Configure DC analysis.
- [`new_op`](#new_op): Initialize an Operating Point (OP) analysis for simple DC circuits.
- [`new_pss`](#new_pss): Create a Periodic Steady State analysis.
- [`new_pz`](#new_pz): Set up Pole-Zero analysis.
- [`new_symbolic`](#new_symbolic): Configure Symbolic analysis.
- [`new_tran`](#new_tran): Initialize Transient analysis.

#### Parameters

- `guess`: Set to `True` for starting the analysis from an initial guess.
- `x0`: Matrix of starting points (leave as `None` in most cases).
- `outfile`: File to store the analysis results.
- `verbose`: Debugging level (0 to 6).

#### `new_op()` Function

Assembles an Operating Point (OP) analysis object, suitable for simple DC circuits.

#### Running a Simulation

```python
# Create your circuit (replace 'mycir' with your circuit instance)
mycir = create_your_circuit()

# Set up the simulation object based on your requirements
opa = ahkab.new_op()

# Run the simulation
res = ahkab.run(mycir, opa)
```

#### Usage

1. **Create Your Circuit**: Define your circuit using the appropriate methods or components.
2. **Select Simulation Object**: Choose the simulation object based on the analysis you need (e.g., `new_op()` for simple DC analysis).
3. **Run the Simulation**: Execute the simulation by passing your circuit instance and simulation object to `ahkab.run()`.

This setup allows you to perform various analyses on your circuits, such as DC analysis for basic circuit behavior or other analyses for more specific insights.

