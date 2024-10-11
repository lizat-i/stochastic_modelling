import numpy as np
    
def brownian_motion_with_mean_reversion(array: np.array,params):
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
    drift = params["drift"]
    volatility = params["volatility"]
    time_horizon = params["time_horizon"]
    initial_value = params["initial_value"]
    
    dt = time_horizon / len(array)
    drift      = 0.01 
    volatility   = 0.3
    T       = 5.0
    # Number of steps derived from the length of the array
    steps = len(array)
    
    # Calculate the time increment for each step
    dt = T / steps
    
    # Set the initial value of the asset price
    array[0] = initial_value  # You can change this to your desired starting price (e.g., S0)

    # Generate the random shocks (Wiener process increments)
    random_shocks = np.random.normal(0, 1, steps - 1)
    
    # Iterate through each time step to calculate the price using the GBM formula
    for i in range(1, steps):
        # Calculate the change in the price
        dS = (drift - 0.5 * volatility**2) * dt + volatility * np.sqrt(dt) * random_shocks[i - 1]
        
        # Update the price based on the previous price and the calculated change
        array[i] = array[i - 1] * np.exp(dS)
    
    return array

def brownian_motion(array, params):
    """
    Simulates a path of a standard Brownian motion.
    
    Parameters:
        array (np.ndarray): Array initialized with zeros, to be filled with the simulated path.
        params (dict): Dictionary containing model parameters such as:
            - "drift" (float): The drift coefficient, representing the mean trend of the process.
            - "volatility" (float): The volatility coefficient, determining the process's variability.
            - "time_horizon" (float): Total time span for the simulation.
            - "initial_value" (float): The starting value of the process.
    
    Returns:
        np.ndarray: A simulated path of the Brownian motion.
    
    Explanation:
    - Uses the drift and volatility terms to generate changes in the value over time.
    - The time horizon is divided into equal time steps, and each step contributes to the process's evolution.
    """
    drift = params["drift"]
    volatility = params["volatility"]
    time_horizon = params["time_horizon"]
    initial_value = params["initial_value"]
    
    dt = time_horizon / len(array)
    for t in range(1, len(array)):
        array[t] = array[t-1] + drift * dt + volatility * np.sqrt(dt) * np.random.normal()
    
    return array

def geometric_brownian_motion(array, params):
    """
    Simulates a path of a geometric Brownian motion.
    
    Parameters:
        array (np.ndarray): Array initialized with zeros, to be filled with the simulated path.
        params (dict): Dictionary containing model parameters such as:
            - "drift" (float): The drift coefficient.
            - "volatility" (float): Volatility affecting the magnitude of fluctuations.
            - "time_horizon" (float): Time span of the simulation.
            - "initial_value" (float): Starting point for the simulation.
    
    Returns:
        np.ndarray: A simulated path of the geometric Brownian motion.
    
    Explanation:
    - Models stock prices or other financial instruments where changes are proportional to the current value.
    - Evolves according to the stochastic differential equation: dS = μS dt + σS dW.
    """
    drift = params["drift"]
    volatility = params["volatility"]
    time_horizon = params["time_horizon"]
    initial_value = params["initial_value"]
    
    dt = time_horizon / len(array)
    array[0] = initial_value
    for t in range(1, len(array)):
        array[t] = array[t-1] * np.exp((drift - 0.5 * volatility**2) * dt + volatility * np.sqrt(dt) * np.random.normal())
    
    return array
