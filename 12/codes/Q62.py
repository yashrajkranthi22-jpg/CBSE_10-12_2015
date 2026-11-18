"""Verify Question 62 using the composite trapezoidal rule."""

import math

# Define the integrand.
def g(x):
    return (math.sin(x) + math.cos(x)) / (3 + math.sin(2 * x))


# Composite trapezoidal rule.
def trapezoidal_rule(function, a, b, n):
    h = (b - a) / n

    result = 0.5 * (function(a) + function(b))

    for i in range(1, n):
        x = a + i * h
        result += function(x)

    return h * result


# Integration limits and number of subintervals.
a = 0
b = math.pi / 4
n = 4

h = (b - a) / n

# Display the function values.
print("Composite Trapezoidal Rule")
print("Question 59")
print("i\t x_i\t\t g(x_i)")

for i in range(n + 1):
    x = a + i * h
    print(f"{i}\t {x:.8f}\t {g(x):.9f}")

# Calculate the trapezoidal approximation.
approximation = trapezoidal_rule(g, a, b, n)

# Exact value of the integral.
exact_value = math.log(3) / 4

# Display the results.
print("\nTrapezoidal approximation =", approximation)
print("Exact value =", exact_value)
print("Absolute error =", abs(approximation - exact_value))
