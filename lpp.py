from scipy.optimize import linprog

# Objective function coefficients (negative for maximization problem)
c = [-640, -440, -200, -480, -330, -150, -480, -330, -150, 0, 0, 0]

# Constraint matrix
A = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],        # x1 ≤ 25
    [1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0],       # x1 - x10 ≤ 0
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],        # x2 ≤ 60
    [0, 1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0],       # x2 - x10 ≤ 0
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],        # x3 ≤ 210
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, -1],       # x3 - x12 ≤ 0
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],        # x4 ≤ 12
    [0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0],       # x4 - x10 ≤ 0
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],        # x5 ≤ 30
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0],       # x5 - x11 ≤ 0
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],        # x6 ≤ 130
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1],       # x6 - x12 ≤ 0
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],        # x7 ≤ 5
    [0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0],       # x7 - x10 ≤ 0
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],        # x8 ≤ 9
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0],       # x8 - x11 ≤ 0
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],        # x9 ≤ 150
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1],       # x9 - x12 ≤ 0
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1.5, 1],      # 2x10 + 1.5x11 + x12 ≤ 190
]

b = [25, 0, 60, 0, 210, 0, 12, 0, 30, 0, 130, 0, 5, 0, 9, 0, 150, 0, 190]

# All variables must be non-negative
bounds = [(0, None)] * 12

# Solve the problem
result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='revised simplex')

# Display results
print("Optimal solution:")
for i, val in enumerate(result.x):
    print(f"x{i+1} = {val:.2f}")
print(f"Maximum value of Z = {-result.fun:.2f}")