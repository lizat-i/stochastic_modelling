# Brownian Motion and Pricing Simulations

This project provides tools for simulating various types of stochastic processes used in financial modeling, such as standard Brownian motion, geometric Brownian motion with continuous dividend yield, and mean-reverting processes often seen in energy markets. The project also includes tools for detailed statistical analysis of simulated paths.

## Features
- Simulate multiple paths of financial processes, including:
  - **Geometric Brownian Motion (GBM)**: Suitable for modeling stock prices, assuming a constant drift (expected return) and volatility.
  - **Risk-Neutral GBM with Continuous Dividend Yield**: Extends the standard GBM to account for assets that pay a continuous dividend yield, adjusting the drift by the difference between the risk-free rate and the dividend yield.
  - **Mean-Reverting Processes**: Simulates assets with a tendency to revert to a long-term mean, such as commodity prices (e.g., energy markets), using mean reversion dynamics.
- Calculate and visualize important statistical metrics like mean, variance, and standard error for the simulated paths.
- Generate detailed convergence statistics to analyze the behavior of the processes over time.
- Includes both command-line and Jupyter Notebook interfaces for ease of use.

## Project Structure
- **`main.py`**: Main script to run the simulations from the command line.
- **`main.ipynb`**: Jupyter notebook for interactive analysis.
- **`output/`**: Directory for saving simulation results (PNG images).
- **`pricing_simulation/`**: Package containing helper functions (`anciliary.py`) and models (`models.py`).

### Full Project Structure
```
brownian_simulation_project/
├── README.md                   # Project documentation
├── main.ipynb                  # Jupyter notebook for running simulations interactively
├── main.py                     # Main script to run the simulation from the command line
├── output/                     # Directory for storing simulation results
│   ├── brownian/
│   ├── geometric_brownian/
│   └── trinomial_tree/
└── pricing_simulation/         # Package for simulation functions and models
    ├── __init__.py             # Initialization of the package
    ├── anciliary.py            # Helper functions (e.g., statistical calculations)
    └── models.py               # Models for different simulation types
```

## Installation

### Option 1: Using Conda (Recommended)
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/brownian_simulation_project.git
   cd brownian_simulation_project
   ```

2. **Create a new Conda environment** and install the dependencies:
   ```bash
   conda env create -f environment.yaml
   conda activate your_env_name
   ```
   Replace `your_env_name` with the environment name specified in `environment.yaml`.

3. **Verify the installation** by running:
   ```bash
   python main.py
   ```

### Option 2: Using `requirements.txt`
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/brownian_simulation_project.git
   cd brownian_simulation_project
   ```

2. **Create a new virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify the installation** by running:
   ```bash
   python main.py
   ```

## Contributing
Feel free to open issues or submit pull requests for improvements.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
