import numpy as np

def normalize_spectrum(flux):
    """
    Normalizes the flux by dividing it by the continuum level.

    Parameters:
    flux (numpy array): Array of flux values to be normalized.

    Returns:
    numpy array: The normalized flux array.
    """
    continuum = np.median(flux)
    return flux / continuum
