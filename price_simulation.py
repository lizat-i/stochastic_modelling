import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import time

# Function to generate a single Brownian motion
def brownian_motion(array: np.array):
    for i in range(1, len(array)):
        array[i] = array[i - 1] + 0.002 * np.random.uniform(-1, 1)
    return array



import numpy as np
import time
import os
import matplotlib.pyplot as plt
import seaborn as sns
from concurrent.futures import ProcessPoolExecutor

# Function to generate a single Brownian motion
def brownian_motion(array: np.array):
    for i in range(1, len(array)):
        array[i] = array[i - 1] + 0.002 * np.random.uniform(-1, 1)
    return array

# Wrapper function to generate and collect k Brownian motions in parallel
def generate_brownian_motions_parallel(k: int, steps: int):
    
    # Prepare the arrays for parallel processing
    arrays = [np.zeros(steps) for _ in range(k)]

    # Use ProcessPoolExecutor for parallel execution
    with ProcessPoolExecutor() as executor:
        # Map the brownian_motion function to each array
        results = list(executor.map(brownian_motion, arrays))
    
    # Convert the list of arrays into a NumPy array
    paths = np.array(results)
    return paths


# Wrapper function to generate and collect k Brownian motions
def generate_brownian_motions(k: int, steps: int):

    paths = np.zeros((k, steps))
    for i in range(k):
        paths[i] = brownian_motion(np.zeros(steps))
        
    return paths

# Function to plot the time series and the distribution, including elapsed time
def plot_combined_brownian_distribution(paths, k, steps, elapsed_time, output_path):
    # Calculate statistics for the time series
    mean_path = np.mean(paths, axis=0)
    p5_path = np.percentile(paths, 5, axis=0)
    p95_path = np.percentile(paths, 95, axis=0)
    
    # Calculate the summed outcomes for each path
    summed_outcomes = np.sum(paths, axis=1)

    # Create the combined plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'width_ratios': [3, 1]})

    # Plot the individual Brownian motion paths as thin lines
    time_steps = np.arange(paths.shape[1])
    for path in paths:
        ax1.plot(time_steps, path, color='black', alpha=0.4, linewidth=0.1)

    # Plot the time series with mean and percentiles
    ax1.plot(time_steps, mean_path, color='green', label='Mean', linewidth=2)
    ax1.fill_between(time_steps, p5_path, p95_path, color='green', alpha=0.3, label='5% - 95%')
    ax1.set_xlabel('Tage')
    ax1.set_ylabel('Value')
    ax1.set_title(f'{k} Brownian Motion Paths')
    ax1.grid(False)
    ax1.legend(loc='upper left')

    # Add the elapsed time as a text box in the top-right corner of ax1
    ax1.text(0.95, 0.95, f'Generation Time: {elapsed_time:.2f} seconds',
             transform=ax1.transAxes, fontsize=10, verticalalignment='top', horizontalalignment='right',
             bbox=dict(facecolor='white', alpha=0.5))

    # Create the density plot of the summed outcomes on the right
    sns.kdeplot(x=summed_outcomes, ax=ax2, color='green', fill=True, alpha=0.4)
    ax2.axvline(np.mean(summed_outcomes), color='blue', linestyle='--')
    ax2.set_xlabel('Sum of Outcomes')
    ax2.set_ylabel('Density')
    ax2.set_title('Density and CDF of Summed Outcomes')
    ax2.grid(False)

    # Create a secondary x-axis for the CDF
    ax2_cdf = ax2.twinx()
    sorted_outcomes = np.sort(summed_outcomes)
    cdf = np.arange(1, len(sorted_outcomes) + 1) / len(sorted_outcomes)
    ax2_cdf.plot(sorted_outcomes, cdf, color='red', linestyle='-', linewidth=2)
    ax2_cdf.set_xlabel('Cumulative Probability')

    # Save the plot to the specified output path
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()