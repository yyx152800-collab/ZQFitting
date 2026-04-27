#Z-Q Relation Exponential Fitting

Hydrological rating curve analysis using exponential equation.

#Principle

Exponential equation for stable stage-discharge relation:

Q = C × (Z - Z0)^n

Where:
- Z0 = constant water level (m)
- Ze = Z - Z0 = difference between water level and constant (m)
- C, n = fitting parameters

#Files

| File | Description |
| Z Q_fit.py | Main program: data loading, parameter fitting, curve plotting |
| Q.xlsx | Data file with Z(m) and Q(m³/s) columns |
| requirements.txt | Python dependency list |

#Usage

1. Install dependencies:
   pip install -r requirements.txt

2. Run program:
   python ZQ_fit.py

3. Check output: fitted parameters Z0, C, n, R², and Z-Q relation curve

## Method

Nonlinear least squares fitting via scipy.optimize.curve_fit.
Initial guess: p0 = [Zmin - 0.1, 10.0, 2.0]

## Sample Output

Formula: Q = 5.000 × (Z - 10.000)^2.500
R² = 0.999