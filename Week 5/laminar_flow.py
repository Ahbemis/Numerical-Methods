import numpy as np
import matplotlib.pyplot as plt
import math

# Define constants for the problem
delta_p = 100  # pressure drop in Pa
mu = 0.001  # dynamic viscosity in Pa.s
L = 10  # length of the pipe in m
R = 0.1  # radius of the pipe in m

def laminar_flow():
    # Create an array of radial positions from 0 to R
    r = np.linspace(0, R, 500)
    
    # Calculate the velocity profile using the Hagen-Poiseuille equation
    u = (delta_p / (4 * mu * L)) * (R**2 - r**2)
    dudr = np.gradient(u, r)
    
    # Plot the velocity profile
    plt.figure(figsize=(8, 5))
    plt.plot(r, u, color='#000000', lw=2, label='Velocity Profile')
    
    # Plot the kinetic energy profile
    plt.plot(r, dudr, 'r', lw=2, label='kinetic energy')
    
    # Label the axes
    plt.xlabel('r (m)')
    plt.ylabel('v (m/s)')
    
    # Add a title to the plot
    plt.title('Velocity Profile of Laminar Flow in a Pipe')
    
    # Add a grid to the plot
    plt.grid()
    
    # Add a legend to the plot
    plt.legend(['Velocity Profile', 'kinetic energy'])
    
    # Display the plot
    plt.show()

# Call the function to execute the plotting
laminar_flow()