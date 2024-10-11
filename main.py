
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

        "volatility": 0.2,          # Volatility (σ) for GBM and mean-reverting models, representing the 
                                    # standard deviation of the asset's returns, which measures the degree 
                                    # of random fluctuations around the drift.

        "time_horizon": 1.0,        # Total time span (T) for the simulation in years. Determines the period 
                                    # over which the simulation is performed. For example, T = 5.0 represents 
                                    # a simulation over 5 years.

        "initial_value": 100,       # Starting value (S0) of the process. This is the initial price or value 
                                    # from which the simulated paths will evolve.

        "risk_free_rate": 0.07,     # Risk-free rate (r) used in the risk-neutral GBM models, representing the 
                                    # theoretical return of an investment with zero risk, typically derived 
                                    # from government bonds.

        "dividend_yield": 0.02,     # Continuous dividend yield (δ) for assets that pay a continuous yield. 
                                    # Represents the proportion of the asset price paid out as dividends.     

        "mean_reversion_rate": 100, # Mean reversion speed (α) for mean-reverting models, representing how 
                                    # quickly the price reverts to its long-term mean. A higher value means 
                                    # faster reversion.
        "long_term_average":     100, # long-term average level (Ŝ = exp(mu)) energy asset prices
                                     #  tend to revert to   
    }

    steps = 8760
    k_values = [10,100, 500]

    output_dir_gbm= 'output/gbm'
    output_dir_risk_neutral_gbm_with_dividends = 'output/risk_neutral_gbm_with_dividends'
    output_dir_gbm_mean_reversion = 'output/risk_neutral_gbm_mean_reversion'

    #ps.anciliary.run_simulation_for_ks(ps.models.gbm, steps, k_values, output_dir_gbm,model_params)
    #ps.anciliary.run_simulation_for_ks(ps.models.risk_neutral_gbm_with_dividends,steps, k_values, output_dir_risk_neutral_gbm_with_dividends,model_params)
    ps.anciliary.run_simulation_for_ks(ps.models.gbm_mean_reversion, steps, k_values, output_dir_gbm_mean_reversion,model_params)

if __name__ == "__main__":
    main()