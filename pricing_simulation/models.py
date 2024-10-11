import numpy as np
    
def gbm_mean_reversion(array, params):
    """
    Simulates a path of a mean-reverting process, commonly used for modeling energy prices.
    
    This model assumes that the asset price tends to revert to a long-term level (Ŝ = exp(mu)) at a rate defined by alpha, the mean reversion speed. The mean reversion property is suitable for modeling commodities like energy where prices exhibit long-term stability.

    Stochastic Differential Equation (SDE):

        dS = alpha(ln(S_hat) - ln(S))S dt + sigma S dz
    
    Parameters:
        - "mean_reversion_rate" (float): The rate (alpha) at which prices revert to the long-term mean.
        - "S_hat" (float): long term average (mu).
        - "volatility" (float): Volatility (sigma) of the asset.
        - "time_horizon" (float): Total time span for the simulation.
        - "initial_value" (float): The starting value (S0) of the process.
        - dz is the underlying uncertainty driving the model and represents an increment in a Weiner process during dt.
    
    Returns:
        np.ndarray: A simulated path of the mean-reverting process.
    
    Explanation:
    - If the spot price is above the long-term mean, the drift becomes negative, causing the price to decrease.
    - If the spot price is below the long-term mean, the drift becomes positive, causing the price to increase.
    - The rate of reversion is controlled by the parameter alpha.
    """
    mean_reversion_rate = params["mean_reversion_rate"]
    S_hat = params["long_term_average"]
    volatility = params["volatility"]
    time_horizon = params["time_horizon"]
    initial_value = params["initial_value"]
    
    print("")
    dt = time_horizon / len(array)

    array[0] = initial_value

    for t in range(1, len(array)):
        array[t] = array[t - 1] * np.exp((mean_reversion_rate*(np.log(S_hat)-np.log(array[t - 1])) - 0.5 * volatility**2) * dt + volatility * np.sqrt(dt) * np.random.normal())
    
    return array

def risk_neutral_gbm_with_dividends(array, params):
    """
    Simulates a path of a geometric Brownian motion under a risk-neutral measure with continuous dividend yield.
    
    This model is commonly used in the pricing of derivatives on assets that pay dividends. It adjusts the drift to account for the difference between the risk-free rate (r) and the continuous dividend yield (δ).

    Stochastic Differential Equation (SDE):
        dS = (r - δ)S dt + sigmaS dW

    Parameters:
        array (np.ndarray): Array initialized with zeros, to be filled with the simulated path.
        params (dict): Dictionary containing model parameters such as:
            - "risk_free_rate" (float): The risk-free interest rate (r), representing the return on a riskless investment.
            - "dividend_yield" (float): Continuous dividend yield (δ), representing the yield paid out by the asset.
            - "volatility" (float): Volatility (sigma) of the asset.
            - "time_horizon" (float): Total time span for the simulation.
            - "initial_value" (float): The starting value (S0) of the process.
    
    Returns:
        np.ndarray: A simulated path of the risk-neutral geometric Brownian motion.
    
    Explanation:
    - Adjusts the drift to reflect the difference between the risk-free rate and dividend yield.
    - Useful for modeling assets like stocks that pay continuous dividends.
    """
    risk_free_rate = params["risk_free_rate"]
    dividend_yield = params["dividend_yield"]
    volatility = params["volatility"]
    time_horizon = params["time_horizon"]
    initial_value = params["initial_value"]
    
    dt = time_horizon / len(array)
    array[0] = initial_value
    for t in range(1, len(array)):
        array[t] = array[t - 1] * np.exp((risk_free_rate - dividend_yield - 0.5 * volatility**2) * dt + volatility * np.sqrt(dt) * np.random.normal())
    
    return array

def gbm(array, params):
    """
    Simulates a path of a geometric Brownian motion (GBM).
    
    This model assumes that the proportional changes in the asset price follow a stochastic 
    process characterized by a constant drift (mu) and volatility (sigma). It is commonly used 
    for modeling stock prices under the Black-Scholes-Merton framework.

    Stochastic Differential Equation (SDE):
        dS = muS dt + sigmaS dW
    
    Parameters:
        array (np.ndarray): Array initialized with zeros, to be filled with the simulated path.
        params (dict): Dictionary containing model parameters such as:
            - "drift" (float): The risk-neutral drift term, representing the expected return of the asset.
            - "volatility" (float): Volatility (sigma) of the asset, representing the randomness in price changes.
            - "time_horizon" (float): Total time span for the simulation.
            - "initial_value" (float): The starting value (S0) of the process.
    
    Returns:
        np.ndarray: A simulated path of the geometric Brownian motion.
    
    Explanation:
    - This model assumes that asset prices have constant drift and volatility.
    - The drift term represents the expected growth rate, while volatility represents 
      the randomness in asset prices.
    """
    drift = params["drift"]
    volatility = params["volatility"]
    time_horizon = params["time_horizon"]
    initial_value = params["initial_value"]
    
    dt = time_horizon / len(array)
    array[0] = initial_value
    for t in range(1, len(array)):
        array[t] = array[t - 1] * np.exp((drift - 0.5 * volatility**2) * dt + volatility * np.sqrt(dt) * np.random.normal())
    
    return array