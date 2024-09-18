import numpy as np

def read_spectrum(filename):
    """
    Reads a spectrum from a text file.

    Parameters:
    filename (str): The path to the spectrum file. The file is expected to have two columns: 
                    the first for wavelength and the second for flux.

    Returns:
    tuple: A tuple containing two numpy arrays:
        - wavelength (numpy array): Array of wavelength values.
        - flux (numpy array): Array of corresponding flux values.
    """
    data = np.loadtxt(filename)
    wavelength, flux = data[:, 0], data[:, 1]
    return wavelength, flux

