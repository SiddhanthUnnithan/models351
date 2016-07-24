# CONSTANTS
wheel_radius = # m 
cart_mass = # kg
mag1_mass = # kg - mass of the magnet in sys 1
mag2_mass = # kg - mass of the magnet in sys 2
spring_const = # N/m => kg/s^2
inertial_mass = # (is this moment of inertia)
pin_dist = # m - distance from center of wheel to rigid arm pin
ra_length = # m - length of the rigid arm
rail_height = # m - vertical distance from the rail to the center of the wheel

# INPUT FUNCTIONS
def input_torque(t):
    """
        input torque as a function of time.
    
        Parameters
        ----------
        t : {numpy array}
            timeseries with appropriate range
    """
    # TODO : define an equation for the input torque
    
    return 1.0

def mag_force(theta):
    """
        repelling force as a function of distance between the two magnets.
        distance between magnets is function of theta.
        
        Parameters
        ----------
        theta : {numpy.array}
    """
    # compute L - distance from the center of the wheel to the magnet
    center_dist = pin_dist * np.cos(theta) + \
        np.sqrt(ra_length**2 - (rail_height + pin_dist * np.sin(theta)))
    
    # TODO: compute magnetomotive force
    
    return 1.0

# SIMULATION
def model_1(y, t):
    """
        generate series of RHS equations from system 1 to be passed
        into solver.
        
        Parameters
        ----------
        y : {numpy.array}
            initial conditions for system
        
        t : {numpy.array}
            timeseries with appropriate range
    """
    p2 = y[0]
    
    dp2 = input_torque(t) / (1 + (R**2)*mag1_mass/intertial_mass)
    dtheta = p2/inertial_mass
    
    return [dp2, dtheta]
    
def model_2(y, t):
    """
        generate series of RHS equations from system 2 to be passed
        into solver.

        Parameters
        ----------
        y : {numpy.array}
            initial conditions for system

        t : {numpy.array}
            timeseries with appropriate range
    """
    q8 = y[0]
    p7 = y[1]
    theta = y[2]
    
    dp7 = (mag_force(theta) * q8/spring_const)/(1 + mag2_mass/cart_mass)
    dq8 = p7/cart_mass

    return [dp7, dq8]

# initial conditions
p2_0 = # angular momentum (2)
q8_0 = # spring displacement (8)
p7_0 = # momentum (7)

time = np.linspace(0.0, 30, 100) # 100 points between 0 and 30 seconds

"""
    We compute angular momentum and theta first as we've split the two
    systems and because the magnetomotive repelling force is a function
    of theta.
"""
y_init_1 = np.array([p2_0])

# angular momentum and theta
y1 = odeint(model_1, y_init_1, time)

p2 = y1[:,0]

theta = y1[:, 1]

y_init_2 = np.array([q8_0, p7_0, theta])

# spring displacement and cart momentum
y2 = odeint(model_2, y_init_2, time)

# TODO: PLOT