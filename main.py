#!/opt/anaconda3/bin/python3

import datetime
import time
import price_simulation 

def main():
    # Define parameters
    k = 100  # Number of Brownian motion paths
    steps = 5487  # Number of steps per path
    
    # Generate the Brownian motion paths and get the elapsed time
    start_time = time.time()
    paths = price_simulation.generate_brownian_motions(k, steps)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"elapsed time linear : {elapsed_time}")
    start_time = time.time()
    paths = price_simulation.generate_brownian_motions_parallel(k, steps)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"elapsed time parallel : {elapsed_time}")

    # Create an output path with the current date
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    output_path = f'output/result_{k}_{steps}_{date_str}.png'
    
    # Plot and save the result
    price_simulation.plot_combined_brownian_distribution(paths, k, steps, elapsed_time, output_path)
    print(f"Plot saved to {output_path}")

if __name__ == "__main__":
    main()