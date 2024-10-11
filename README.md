# Brownian Motion and Pricing Simulations

This project contains tools for simulating various types of stochastic processes like Brownian motion, geometric Brownian motion, and trinomial tree models, along with detailed statistical analysis.

## Features
- Simulate multiple paths of Brownian motion, geometric Brownian motion, and trinomial trees.
- Calculate and visualize statistical metrics like mean, variance, and standard error.
- Generate detailed convergence statistics for analysis.

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
