import os
import time
import datetime
from concurrent.futures import ProcessPoolExecutor, as_completed
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm

# Statistical KPI functions
def calculate_mean_terminal_value(paths):
    """
    Calculates the mean of the terminal values from a set of simulation paths.
    """
    return np.mean(paths[:, -1])

def calculate_variance_terminal_value(paths):
    """
    Calculates the variance of the terminal values from a set of simulation paths.
    """
    return np.var(paths[:, -1])

def calculate_sem_terminal_value(paths, k):
    """
    Calculates the Standard Error of the Mean (SEM) for the terminal values.
    """
    return np.std(paths[:, -1]) / np.sqrt(k)

def calculate_cumulative_means(paths, k):
    """
    Calculates the cumulative means of the terminal values over time.
    """
    return [np.mean(paths[:i, -1]) for i in range(1, k)]

def calculate_cumulative_variances(paths, k):
    """
    Calculates the cumulative variances of the terminal values over time.
    """
    return [np.var(paths[:i, -1]) for i in range(1, k)]

def calculate_sem_values(paths, k):
    """
    Calculates the cumulative standard error of the mean (SEM) over time.
    """
    return [np.std(paths[:i, -1]) / np.sqrt(i) for i in range(1, k)]

# Wrapper function to generate and collect k Brownian motions in parallel
def generate_brownian_motions(func, k: int, steps: int, desc: str = "Generating motions"):
    arrays = [np.zeros(steps) for _ in range(k)]
    results = []

    with tqdm(total=k, desc=desc) as pbar, ProcessPoolExecutor() as executor:
        futures = [executor.submit(func, array) for array in arrays]
        for future in as_completed(futures):
            results.append(future.result())
            pbar.update(1)

    return np.array(results)

# Function to plot the time series and the distribution, including convergence metrics
def plot_combined_brownian_distribution_statistics(paths, k, steps, S0, elapsed_time, output_path):
    mean_path = np.mean(paths, axis=0)
    p5_path = np.percentile(paths, 5, axis=0)
    p95_path = np.percentile(paths, 95, axis=0)
    summed_outcomes = np.sum(paths, axis=1) / steps / S0

    std_dev = np.std(paths, axis=0)
    std_error = std_dev / np.sqrt(paths.shape[0])

    mean_terminal_value = calculate_mean_terminal_value(paths)
    variance_terminal_value = calculate_variance_terminal_value(paths)
    sem_terminal_value = calculate_sem_terminal_value(paths, k)
    cumulative_means = calculate_cumulative_means(paths, k)
    cumulative_variances = calculate_cumulative_variances(paths, k)
    sem_values = calculate_sem_values(paths, k)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 10), gridspec_kw={'width_ratios': [3, 1]})
    time_steps = np.arange(paths.shape[1])
    for path in paths:
        ax1.plot(time_steps, path, color='black', alpha=0.4, linewidth=0.1)
    
    ax1.plot(time_steps, mean_path, color='green', label='Mean', linewidth=2)
    ax1.fill_between(time_steps, p5_path, p95_path, color='green', alpha=0.3, label='5% - 95%')
    ax1.set_xlabel('Days')
    ax1.set_ylabel('Value')
    ax1.set_title(f'{k} Brownian Motion Paths')
    ax1.grid(False)
    ax1.legend(loc='upper left')

    ax1.text(0.05, 0.75, f'Generation Time: {elapsed_time:.2f} s\n'
                         f'Mean Terminal Value: {mean_terminal_value:.4f}\n'
                         f'Standard Deviation: {np.mean(std_dev):.4f}\n'
                         f'Standard Error: {np.mean(std_error):.4f}\n'
                         f'Variance of Terminal Value: {variance_terminal_value:.4f}\n'
                         f'SEM of Terminal Value: {sem_terminal_value:.4f}',
             transform=ax1.transAxes, fontsize=9, verticalalignment='top', horizontalalignment='left',
             bbox=dict(facecolor='white', alpha=0.7))
    
    sns.kdeplot(x=summed_outcomes, ax=ax2, color='green', fill=True, alpha=0.4)
    ax2.axvline(np.mean(summed_outcomes), color='blue', linestyle='--')
    ax2.set_xlabel('Sum of Outcomes')
    ax2.set_ylabel('Density')
    ax2.set_title('Density and CDF of Summed Outcomes')
    ax2.grid(False)

    ax2_cdf = ax2.twinx()
    sorted_outcomes = np.sort(summed_outcomes)
    cdf = np.arange(1, len(sorted_outcomes) + 1) / len(sorted_outcomes)
    ax2_cdf.plot(sorted_outcomes, cdf, color='red', linestyle='-', linewidth=2)
    ax2_cdf.set_ylabel('Cumulative Probability', color='red')
    ax2_cdf.tick_params(axis='y', labelcolor='red')

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)
    
    return cumulative_means, cumulative_variances, sem_values

# Function to plot convergence statistics
def plot_convergence_statistics(convergence_stats, cumulative_means_list, cumulative_variances_list, sem_values_list, output_dir):
    k_values = convergence_stats['k_values']
    means = convergence_stats['mean_terminal_values']
    variances = convergence_stats['variance_terminal_values']
    sems = convergence_stats['sem_terminal_values']

    fig = plt.figure(figsize=(18, 24))
    gs = fig.add_gridspec(4, 3, height_ratios=[1, 1, 1, 2])

    ax1 = fig.add_subplot(gs[0, 0])
    ax1.plot(k_values, means, marker='o', label='Mean Terminal Value', color='blue')
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    ax1.set_xlabel('Number of Simulations (k)')
    ax1.set_ylabel('Mean')
    ax1.set_title('Convergence of Mean Terminal Values')
    ax1.grid(True)
    ax1.legend()

    ax2 = fig.add_subplot(gs[0, 1])
    ax2.plot(k_values, variances, marker='o', label='Variance of Terminal Value', color='purple')
    ax2.set_xscale('log')
    ax2.set_yscale('log')
    ax2.set_xlabel('Number of Simulations (k)')
    ax2.set_ylabel('Variance')
    ax2.set_title('Convergence of Variance')
    ax2.grid(True)
    ax2.legend()

    ax3 = fig.add_subplot(gs[0, 2])
    ax3.plot(k_values, sems, marker='o', label='Standard Error of Mean', color='orange')
    ax3.set_xscale('log')
    ax3.set_yscale('log')
    ax3.set_xlabel('Number of Simulations (k)')
    ax3.set_ylabel('Standard Error')
    ax3.set_title('Convergence of Standard Error')
    ax3.grid(True)
    ax3.legend()

    ax4 = fig.add_subplot(gs[1, :])
    ax4.set_title('Convergence of Cumulative Mean Over Time')
    for i, k in enumerate(k_values):
        ax4.plot(cumulative_means_list[i], label=f'Cumulative Mean (k={k})')
    ax4.set_xlabel('Number of Simulations')
    ax4.set_ylabel('Cumulative Mean')
    ax4.set_yscale('log')
    ax4.set_xscale('log')
    ax4.grid(True)
    ax4.legend()

    ax5 = fig.add_subplot(gs[2, :])
    ax5.set_title('Convergence of Cumulative Variance Over Time')
    for i, k in enumerate(k_values):
        ax5.plot(cumulative_variances_list[i], label=f'Cumulative Variance (k={k})')
    ax5.set_xlabel('Number of Simulations')
    ax5.set_ylabel('Cumulative Variance')
    ax5.set_yscale('log')
    ax5.set_xscale('log')
    ax5.grid(True)
    ax5.legend()

    ax6 = fig.add_subplot(gs[3, :])
    ax6.set_title('Convergence of Standard Error Over Time')
    for i, k in enumerate(k_values):
        ax6.plot(sem_values_list[i], label=f'SEM (k={k})')
    ax6.set_xlabel('Number of Simulations')
    ax6.set_ylabel('Standard Error')
    ax6.set_yscale('log')
    ax6.set_xscale('log')
    ax6.grid(True)
    ax6.legend()

    plt.tight_layout()
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    output_path = os.path.join(output_dir, f'convergence_statistics_{date_str}.png')
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(output_path, dpi=300)
    plt.close(fig)

    print(f"Convergence statistics plot saved to {output_path}")

# Main function to run the simulations
def run_simulation_for_ks(solver: int, S0, steps, k_values, output_dir):
    convergence_stats = {
        'k_values': [],
        'mean_terminal_values': [],
        'variance_terminal_values': [],
        'sem_terminal_values': [],
        'elapsed_times': []
    }
    cumulative_means_list = []
    cumulative_variances_list = []
    sem_values_list = []

    for k in k_values:
        start_time = time.time()
        paths = generate_brownian_motions(solver, k, steps)
        elapsed_time = time.time() - start_time

        mean_terminal_value = calculate_mean_terminal_value(paths)
        variance_terminal_value = calculate_variance_terminal_value(paths)
        sem_terminal_value = calculate_sem_terminal_value(paths, k)

        convergence_stats['k_values'].append(k)
        convergence_stats['mean_terminal_values'].append(mean_terminal_value)
        convergence_stats['variance_terminal_values'].append(variance_terminal_value)
        convergence_stats['sem_terminal_values'].append(sem_terminal_value)
        convergence_stats['elapsed_times'].append(elapsed_time)

        date_str = datetime.datetime.now().strftime("%Y-%m-%d")
        output_path = os.path.join(output_dir, f'result_brownian_{k}_{steps}_{date_str}.png')
        cumulative_means, cumulative_variances, sem_values = plot_combined_brownian_distribution_statistics(
            paths, k, steps, S0, elapsed_time, output_path)
        
        cumulative_means_list.append(cumulative_means)
        cumulative_variances_list.append(cumulative_variances)
        sem_values_list.append(sem_values)

        print(f"Plot saved to {output_path}")

    plot_convergence_statistics(convergence_stats, cumulative_means_list, cumulative_variances_list, sem_values_list, output_dir)