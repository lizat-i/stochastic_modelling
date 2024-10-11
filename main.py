
import time
import pricing_simulation as ps
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns

# Define and run the simulation
def main():
    S0 = 100
    steps = 5487
    k_values = [10,100, 500]

    output_dir_brownian= 'output/brownian'
    output_dir_geometrical_brownian = 'output/geometric_brownian'
    output_dir_trinomial_tree_brownian = 'output/trinonmial_tree'

    ps.anciliary.run_simulation_for_ks(ps.models.brownian_motion, S0, steps, k_values, output_dir_brownian)
    ps.anciliary.run_simulation_for_ks(ps.models.geometric_brownian_motion, S0, steps, k_values, output_dir_geometrical_brownian)
    ps.anciliary.run_simulation_for_ks(ps.models.brownian_motion_with_mean_reversion, S0, steps, k_values, output_dir_trinomial_tree_brownian)

if __name__ == "__main__":
    main()