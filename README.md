# Ideal-Gas-and-Pipe-Flow-Calculator
Engineers often need quick calculations for state properties (like pressure and temperature changes in a closed system) or flow characteristics (like Reynolds number to determine if flow is laminar or turbulent). Manually solving these repetitive equations is time-consuming and error-prone. A specialized calculator speeds up this process.

Manual calculation of engineering formulas is prone to simple arithmetic errors, especially when rearranging equations to solve for different variables (e.g., isolating T in PV=nRT). Furthermore, students often forget specific constants (like the Universal Gas Constant R) or the thresholds for flow regimes. There is a need for a lightweight, digital tool that:

---Handles equation rearrangement automatically.

---Validates user input (e.g., preventing negative absolute temperature).

---Provides immediate, clear results with units.



The tool offers two main modes:

Mode 1: Ideal Gas Law PV=nRT Calculation
The user provides three of the four main variables (Pressure , Volume , Moles , Temperature), and the program calculates the missing one.Constants: You'll need to define the universal gas constant .Logic: Use conditional statements to determine which variable the user omitted and solve for it.

Mode 2: Pipe Flow Analysis (Laminar vs. Turbulent)
Calculate the Reynolds Number  to determine the flow regime in a pipe. .Logic:Get the four necessary inputs from the user.Calculate Re. Report the result and classify the flow: Re < 2000 : Laminar flow
