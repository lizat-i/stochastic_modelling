
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
        "drift": 0.05,                # Drift coefficient for Brownian motion models
        "volatility": 0.2,            # Volatility for the geometric Brownian motion
        "time_horizon": 5.0,          # Time horizon (in years)
        "initial_value": 100,         # Starting value of the process
        # Add other parameters as necessary
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