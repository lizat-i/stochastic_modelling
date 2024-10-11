
import time
import pricing_simulation as ps
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns

# Define and run the simulation
def main():

# Define model parameters in a dictionary
    model_params = {
        "drift": 0.05,              # Drift coefficient (μ) for GBM and mean-reverting models, representing 
                                    # the expected rate of return or growth of the asset over time.

        "volatility": 0.2,            # Volatility (σ) for GBM and mean-reverting models, representing the 
                                    # standard deviation of the asset's returns, which measures the degree 
                                    # of random fluctuations around the drift.

        "time_horizon": 5.0,          # Total time span (T) for the simulation in years. Determines the period 
                                    # over which the simulation is performed. For example, T = 5.0 represents 
                                    # a simulation over 5 years.

        "initial_value": 100,         # Starting value (S0) of the process. This is the initial price or value 
                                    # from which the simulated paths will evolve.

        "risk_free_rate": 0.03,       # Risk-free rate (r) used in the risk-neutral GBM models, representing the 
                                    # theoretical return of an investment with zero risk, typically derived 
                                    # from government bonds.

        "dividend_yield": 0.02,       # Continuous dividend yield (δ) for assets that pay a continuous yield. 
                                    # Represents the proportion of the asset price paid out as dividends.

        "mean_reversion_speed": 0.1,  # Mean reversion speed (α) for mean-reverting models, representing how 
                                    # quickly the price reverts to its long-term mean. A higher value means 
                                    # faster reversion.

        "long_term_mean": 4.6,        # Long-term average level (Ŝ) for mean-reverting models. This is the 
                                    # level to which prices tend to revert over time. It is typically derived 
                                    # from historical data.

        # Add other parameters as necessary for more advanced models or specific use cases.
    }
    S0 = 100
    steps = 5487
    k_values = [10,100, 500]

    output_dir_brownian= 'output/gbm'
    output_dir_geometrical_brownian = 'output/risk_neutral_gbm_with_dividends'
    output_dir_trinomial_tree_brownian = 'output/risk_neutral_gbm_with_dividends'

    ps.anciliary.run_simulation_for_ks(ps.models.gbm, S0, steps, k_values, output_dir_brownian,model_params)
    ps.anciliary.run_simulation_for_ks(ps.models.risk_neutral_gbm_with_dividends, S0, steps, k_values, output_dir_geometrical_brownian,model_params)
    ps.anciliary.run_simulation_for_ks(ps.models.gbm_mean_reversion, S0, steps, k_values, output_dir_trinomial_tree_brownian,model_params)

if __name__ == "__main__":
    main()