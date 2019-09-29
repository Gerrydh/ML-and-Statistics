# Adapted from: https://tour.golang.org/flowcontrol/8

def sqrt(x):
    # Initial guess
    z = 1.0
    # keep getting a better estimate for the square root of 
    # x, until you are within 2 decimal places.

    while abs(z*z - x) >= 0.01:
    # Get a better approximation for teh square root.
     z -= (z*z - x) / (2*z)
    # Return z.
    return z
# Calculate the square root of 8    
z = sqrt(8.0)
# Print z.
print(z)
# Print the square root of the square root of z.
print(z*z)
