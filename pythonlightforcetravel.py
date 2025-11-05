import math

class LightForceSimulator:
    """
    A speculative physics simulation demonstrating the exponential build-up of 
    "Light Force Thrust" based on density and reflection in a contained volume.

    NOTE: This model uses non-standard, speculative physics concepts to
    simulate the user's request regarding light's momentum, density, and 
    repelling force. It should not be taken as an established scientific model.
    """

    # --- STANDARD PHYSICS CONSTANTS ---
    C = 2.99792458e8    # Speed of Light (m/s)
    RHO_ATM = 1.225     # Standard Atmospheric Density at sea level (kg/m^3)
    
    # --- HYPOTHETICAL/EMPIRICAL FACTORS ---
    K_ENV = 1.0         # Environmental Constant (K) - Fixed for simplicity
    BETA = 2.0          # Pressure Build-up Exponent (beta) - Creates the exponential effect
    A_EFF = 1.0         # Effective Area for Force calculation (m^2)

    def __init__(self):
        """Initializes default simulation parameters."""
        self.total_intensity_w = 50000.0  # Total Power of all light sources (Watts)
        self.container_volume_m3 = 10.0  # Volume of the enclosed environment (m^3)
        self.reflectivity_alpha = 0.95   # Reflectivity (alpha) of the walls (0 to 1)

    def set_parameters(self, intensity, volume, alpha):
        """Sets the simulation parameters based on user input."""
        self.total_intensity_w = max(0.0, intensity)
        self.container_volume_m3 = max(0.1, volume)
        self.reflectivity_alpha = min(1.0, max(0.0, alpha))
    
    def calculate_relativistic_mass_density(self):
        """
        Calculates the Relativistic Mass Density (rho_rel) of the light energy
        contained within the volume, based on E=mc^2 and Energy Density U=E/V.

        The total energy (E) is derived from Power (I_w * Time). Since we are 
        interested in instantaneous density, we use the energy equivalence of power 
        flux: E/V = U = I/c. Then rho = U/c^2 = I / c^3. 
        We use the total power/energy rate from the sources for this concentration.
        """
        # Calculate Energy Density (U) based on total power over volume 
        # (A simplified approach for a contained system over time)
        # Total Power (W) / Volume (m^3) * C-factor
        
        # We model the build-up proportional to Power / (Volume * c^2)
        # The result is in kg/m^3 (Mass Density)
        rho_rel = self.total_intensity_w / (self.container_volume_m3 * (self.C ** 2))
        
        return rho_rel

    def calculate_light_force_thrust(self):
        """
        Calculates the non-standard Light Force Thrust (F_thrust) in Newtons 
        using the speculative compounded formula.
        
        F_thrust = (K * F_rad) * (rho_rel / rho_atm) ^ beta
        """
        
        # 1. Calculate Standard Radiation Force (F_rad)
        # F_rad = P_rad * A_eff = ( (1 + alpha) * I ) / c * A_eff
        # I (Irradiance) = Power (W) / Area (A_eff). Here, Power is I_w.
        
        # The term (I_w / A_eff) * A_eff simplifies to I_w (Total Power)
        force_rad_base = (1.0 + self.reflectivity_alpha) * self.total_intensity_w / self.C

        # 2. Calculate the Relativistic Density Ratio
        rho_rel = self.calculate_relativistic_mass_density()
        
        # Ensure we don't divide by zero for atmospheric density, though RHO_ATM is > 0
        if self.RHO_ATM == 0:
            density_ratio = 1.0
        else:
            density_ratio = rho_rel / self.RHO_ATM

        # 3. Apply Exponential Density Amplification
        # This term creates the non-linear "pressurized weight" build-up of momentum.
        density_amplification = self.K_ENV * (density_ratio ** self.BETA)

        # 4. Calculate Final Hypothetical Thrust Force
        # The base radiation force is amplified by the density build-up.
        f_thrust = force_rad_base * density_amplification
        
        return f_thrust, force_rad_base, rho_rel

def run_simulation():
    """Runs the interactive simulation loop."""
    simulator = LightForceSimulator()

    print("--- Light Force Momentum and Pressure Simulator ---")
    print("A speculative model to demonstrate the exponential 'thrust' of contained light.")
    print(f"Constants Used: Speed of Light (c) = {simulator.C:.2e} m/s, Density Exponent (beta) = {simulator.BETA}")
    print("--------------------------------------------------")

    while True:
        try:
            print("\nCurrent Parameters:")
            print(f"  [1] Total Light Power (Watts): {simulator.total_intensity_w:.2f} W")
            print(f"  [2] Container Volume (m³): {simulator.container_volume_m3:.2f} m³")
            print(f"  [3] Wall Reflectivity (0-1): {simulator.reflectivity_alpha:.2f}")
            print("-" * 34)

            choice = input("Enter a number to change a parameter (1, 2, 3), or 'R' to Run, or 'Q' to Quit: ").lower()

            if choice == 'q':
                break
            
            elif choice == 'r':
                f_thrust, f_rad_base, rho_rel = simulator.calculate_light_force_thrust()

                # --- Display Results ---
                print("\n\n=============== SIMULATION RESULTS ===============")
                
                # Relativistic Mass Density is the key factor
                print(f"A. Relativistic Light Density (ρ_rel): {rho_rel:.3e} kg/m³")
                print(f"   (This is the 'Weight Density' build-up of energy)")
                
                # Standard Physics Base Force
                print(f"B. Standard Radiation Force (F_rad): {f_rad_base:.3e} Newtons")
                
                # The Amplified, Hypothetical Force
                print(f"C. HYPOTHETICAL LIGHT FORCE THRUST (F_LF): {f_thrust:.3e} Newtons")
                
                print("==================================================")
                print(f"\nResult C shows the force exponentially amplified by the light's effective density build-up (Factor of (ρ_rel / ρ_atm)^{simulator.BETA}).")

            elif choice in ('1', '2', '3'):
                try:
                    if choice == '1':
                        new_val = float(input("Enter new Total Light Power (Watts, e.g., 50000): "))
                        simulator.set_parameters(new_val, simulator.container_volume_m3, simulator.reflectivity_alpha)
                    elif choice == '2':
                        new_val = float(input("Enter new Container Volume (m³, min 0.1): "))
                        simulator.set_parameters(simulator.total_intensity_w, new_val, simulator.reflectivity_alpha)
                    elif choice == '3':
                        new_val = float(input("Enter new Wall Reflectivity (0.0 to 1.0, e.g., 0.99 for high reflection): "))
                        simulator.set_parameters(simulator.total_intensity_w, simulator.container_volume_m3, new_val)
                except ValueError:
                    print("Invalid input. Please enter a numerical value.")
            
            else:
                print("Invalid choice. Please enter 1, 2, 3, R, or Q.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break

if __name__ == "__main__":
    run_simulation()