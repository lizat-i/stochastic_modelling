import numpy as np
    

def brownian_motion_with_mean_reversion(array: np.array):
    """
    Extension of the simple geometric brownian motion, to include the mean reversion property observed in energy markets.
    Schwartz97.

    Equuation dS = alpha(mu - In S)Sdt +sigma Sdz

    int this model spot prices mean reverts to the long term level S_hat = exp(mu) with a speed given by the mean reversion rate alphs
    the mean reversion rate can and is being derived by historical data.
    
    Parameters:
    - mu: Drift coefficient, representing the average expected return of the asset.
    - sigma: Volatility of the asset, representing the randomness in price changes.
    - dS incremental change in asset price
    - S_hat  long term mean Spot price level 
    - alpha is the mean reversion rate, which describes the speed at which the spot price reverts to its long term average level
    - T: Total time duration (e.g., in years).
    


    Returns:
    - np.array: The input array filled with simulated asset prices over time.
    """
    mu      = 0.01 
    sigma   = 0.3
    T       = 5.0
    # Number of steps derived from the length of the array
    steps = len(array)
    
    # Calculate the time increment for each step
    dt = T / steps
    
    # Set the initial value of the asset price
    array[0] = 100  # You can change this to your desired starting price (e.g., S0)

    # Generate the random shocks (Wiener process increments)
    random_shocks = np.random.normal(0, 1, steps - 1)
    
    # Iterate through each time step to calculate the price using the GBM formula
    for i in range(1, steps):
        # Calculate the change in the price
        dS = (mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * random_shocks[i - 1]
        
        # Update the price based on the previous price and the calculated change
        array[i] = array[i - 1] * np.exp(dS)
    
    return array

def trinomial_tree(array: np.array):
    """
    Simulates a Geometric Brownian Motion (GBM) path using an input array.
    
    Parameters:
    - array: An array of zeros with length equal to the number of steps.
    - mu: Drift coefficient, representing the average expected return of the asset.
    - sigma: Volatility of the asset, representing the randomness in price changes.
    - T: Total time duration (e.g., in years).
    
    Returns:
    - np.array: The input array filled with simulated asset prices over time.
    """
    mu      = 0.01 
    sigma   = 0.3
    T       = 5.0
    # Number of steps derived from the length of the array
    steps = len(array)
    
    # Calculate the time increment for each step
    dt = T / steps
    
    # Set the initial value of the asset price
    array[0] = 100  # You can change this to your desired starting price (e.g., S0)

    # Generate the random shocks (Wiener process increments)
    random_shocks = np.random.normal(0, 1, steps - 1)
    
    # Iterate through each time step to calculate the price using the GBM formula
    for i in range(1, steps):
        # Calculate the change in the price
        dS = (mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * random_shocks[i - 1]
        
        # Update the price based on the previous price and the calculated change
        array[i] = array[i - 1] * np.exp(dS)
    
    return array

def geometric_brownian_motion(array: np.array):
    """
    Simulates a Geometric Brownian Motion (GBM) path using an input array.
    
    Parameters:
    - array: An array of zeros with length equal to the number of steps.
    - mu: Drift coefficient, representing the average expected return of the asset.
    - sigma: Volatility of the asset, representing the randomness in price changes.
    - T: Total time duration (e.g., in years).
    
    Returns:
    - np.array: The input array filled with simulated asset prices over time.
    """
    mu      = 0.01 
    sigma   = 0.3
    T       = 5.0
    # Number of steps derived from the length of the array
    steps = len(array)
    
    # Calculate the time increment for each step
    dt = T / steps
    
    # Set the initial value of the asset price
    array[0] = 100  # You can change this to your desired starting price (e.g., S0)

    # Generate the random shocks (Wiener process increments)
    random_shocks = np.random.normal(0, 1, steps - 1)
    
    # Iterate through each time step to calculate the price using the GBM formula
    for i in range(1, steps):
        # Calculate the change in the price
        dS = (mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * random_shocks[i - 1]
        
        # Update the price based on the previous price and the calculated change
        array[i] = array[i - 1] * np.exp(dS)
    
    return array

# Function to generate a single Brownian motion
def brownian_motion(array: np.array):
    array[0] = 100 
    for i in range(1, len(array)):
        array[i] = array[i - 1] + 0.002 * np.random.uniform(-1, 1)
    return array
