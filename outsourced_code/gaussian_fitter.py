import numpy as np
from scipy.optimize import curve_fit

def gaussian(x, amp, center, width, offset):
    """
    Defines a Gaussian function to fit the absorption line.

    Parameters:
    x (numpy array): Array of x-values (wavelengths).
    amp (float): Amplitude of the Gaussian.
    center (float): Center of the Gaussian (mean).
    width (float): Width of the Gaussian (standard deviation).
    offset (float): Offset from zero (baseline flux).

    Returns:
    numpy array: The computed Gaussian values for the input x-values.
    """
    return amp * np.exp(-(x - center) ** 2 / (2 * width ** 2)) + offset

def fit_gaussian(wavelength, flux, initial_guess):
    """
    Fits a Gaussian function to the absorption line in the spectrum.

    Parameters:
    wavelength (numpy array): Array of wavelength values.
    flux (numpy array): Array of corresponding flux values.
    initial_guess (list): List of initial guesses for the Gaussian parameters:
                          [amplitude, center, width, offset].

    Returns:
    tuple: A tuple containing:
        - popt (array): Optimal values for the Gaussian parameters (amplitude, center, width, offset).
        - gaussian (function): The Gaussian function used for the fit.
    """
    popt, _ = curve_fit(gaussian, wavelength, flux, p0=initial_guess)
    return popt, gaussian
