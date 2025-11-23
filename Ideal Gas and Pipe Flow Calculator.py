import math
from typing import Optional, Tuple

# --- CONSTANTS ---
R_GAS_CONSTANT = 8.314 
RE_LAMINAR_THRESHOLD = 2000
RE_TURBULENT_THRESHOLD = 4000

def get_float_input(prompt: str, min_val: float = 0.0) -> Optional[float]:
    while True:
        try:
            value = float(input(prompt))
            if value <= min_val:
                print(f"Error: Value must be greater than {min_val}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")
        except EOFError:
            return None # Allows safe exit in some environments


def ideal_gas_law_solver():
    """
    Solves for the missing variable in the Ideal Gas Law: PV = nRT.
    The user enters 'x' for the unknown variable.
    """
    print("\n--- 1. Ideal Gas Law (PV = nRT) Solver ---")
    print(f"Using Universal Gas Constant R = {R_GAS_CONSTANT} J/(mol·K)")
    print("Enter 'x' for the variable you want to solve for.")
    
    P_str = input("Pressure (P, Pa): ")
    V_str = input("Volume (V, m³): ")
    n_str = input("Moles (n, mol): ")
    T_str = input("Temperature (T, K): ")

    unknown_var = None
    known_values = {}
    
    inputs = {'P': P_str, 'V': V_str, 'n': n_str, 'T': T_str}
    
    for key, value_str in inputs.items():
        if value_str.lower() == 'x':
            if unknown_var is not None:
                print("\nError: Please enter 'x' for ONLY one unknown variable.")
                return
            unknown_var = key
        else:
            try:
                value = float(value_str)
                if key == 'T' and value <= 0:
                     print("\nError: Absolute temperature (T) must be greater than 0 K.")
                     return
                known_values[key] = value
            except ValueError:
                print(f"\nError: Invalid numerical input for {key}.")
                return

    if unknown_var is None:
        print("\nError: Please enter 'x' for one variable to solve for.")
        return
        
    P = known_values.get('P')
    V = known_values.get('V')
    n = known_values.get('n')
    T = known_values.get('T')

    try:
        if unknown_var == 'P':
            result = (n * R_GAS_CONSTANT * T) / V
            unit = "Pa"
        elif unknown_var == 'V':
            result = (n * R_GAS_CONSTANT * T) / P
            unit = "m³"
        elif unknown_var == 'n':
            result = (P * V) / (R_GAS_CONSTANT * T)
            unit = "mol"
        elif unknown_var == 'T':
            result = (P * V) / (n * R_GAS_CONSTANT)
            unit = "K"
        else:
            raise ValueError("Unknown variable identity.")

        print("-" * 35)
        print(f"Solution: {unknown_var} = {result:.4f} {unit}")
        print("-" * 35)

    except ZeroDivisionError:
        print("\nCalculation Error: Division by zero. Check that input values (especially V, n, P) are not zero.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


def reynolds_number_solver():
    """
    Calculates the Reynolds number and determines the flow regime.
    Re = (rho * v * D) / mu
    """
    print("\n--- 2. Pipe Flow Analysis (Reynolds Number) Solver ---")
    
    # Get the required physical properties from the user
    rho = get_float_input("Fluid Density (ρ, kg/m³): ")
    if rho is None: return
    
    v = get_float_input("Fluid Velocity (v, m/s): ")
    if v is None: return
    
    D = get_float_input("Pipe Diameter (D, m): ")
    if D is None: return
    
    mu = get_float_input("Dynamic Viscosity (μ, Pa·s): ")
    if mu is None: return
    
    try:
        # The Reynolds Number equation: Re = (rho * v * D) / mu
        reynolds_number = (rho * v * D) / mu
        
        # Determine flow regime based on the calculated Re
        if reynolds_number < RE_LAMINAR_THRESHOLD:
            flow_regime = "Laminar Flow (Smooth, predictable layers)"
        elif reynolds_number <= RE_TURBULENT_THRESHOLD:
            flow_regime = "Transitional Flow (Unpredictable, mix of laminar/turbulent)"
        else:
            flow_regime = "Turbulent Flow (Chaotic, high mixing)"

        print("-" * 35)
        print(f"Calculated Reynolds Number (Re): {reynolds_number:.2f}")
        print(f"Flow Regime: {flow_regime}")
        print("-" * 35)

    except ZeroDivisionError:
        print("\nCalculation Error: Dynamic Viscosity (μ) cannot be zero.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


def main():
   
    while True:
        print("\n=============================================")
        print("    Engineering Calculation Tool Menu")
        print("=============================================")
        print("1. Solve Ideal Gas Law (PV=nRT)")
        print("2. Calculate Reynolds Number (Pipe Flow)")
        print("3. Exit")
        
        choice = input("Enter your choice (1, 2, or 3): ").strip()
        
        if choice == '1':
            ideal_gas_law_solver()
        elif choice == '2':
            reynolds_number_solver()
        elif choice == '3':
            print("Exiting tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


main()