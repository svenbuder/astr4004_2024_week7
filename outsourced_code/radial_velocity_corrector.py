def correct_radial_velocity(wavelength, velocity_kms):
    """
    Corrects the wavelength for radial velocity shift.

    Parameters:
    wavelength (numpy array): Array of wavelength values.
    velocity_kms (float): Radial velocity shift in kilometers per second (km/s).

    Returns:
    numpy array: The wavelength array corrected for the radial velocity shift.
    """
    c = 299792.458  # Speed of light in km/s
    shift_factor = 1 + velocity_kms / c
    return wavelength / shift_factor
