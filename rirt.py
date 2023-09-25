"""
rirt.py

Computes the activity index of Lanzafame et al. (2023)
(https://ui.adsabs.harvard.edu/abs/2023A%26A...674A..30L/abstract)

Eq. 7 offers a conversion between the Gaia `activityindex_espcs` index and a
more temperature-insensitive index, R'_IRT, from the Ca II infrared triplet:

log(R'_IRT) = (C0 + C1 θ + C2 θ2 + C3 θ3) + log(α),

where θ = log(Teff), α is the Ca II IRT equivalent width in nm,
and the coefficients themselves depend on metallicity.
"""

import numpy as np
from scipy.interpolate import interp1d


m_h = [-0.5, 0.0, 0.25, 0.5]
coeff_table = np.transpose([
    [-3.3391, -0.1564, -0.1046, 0.0311],
    [-3.3467, -0.1989, -0.1020, 0.0349],
    [-3.3501, -0.2137, -0.1029, 0.0357],
    [-3.3527, -0.2219, -0.1056, 0.0353]])


coeffs = interp1d(m_h, coeff_table)


@np.vectorize
def logRirt(alpha, m_h, teff):
    """
    Compute the log of the R'_IRT index.

    Arguments:
        alpha (float): the Ca II IRT equivalent width in nm, recorded in the
            Gaia archive as `activityindex_espcs`.
        m_h (float): the solar-scaled stellar metallicity [M/H].
        teff (float): the effective temperature in kelvins.

    Returns:
        logR (float): the log10 of the R'_IRT index.

    Note:
        This function requires that `alpha` be positive since it is a width
        measurement and the equation computes its logarithm. However,
        some values of `activityindex_espcs` in Gaia are negative or zero,
        and I haven't done the reading to see how to interpret those.
        Probably just low or immeasurable activity?

        R'IRT is defined for metallicities between [M/H] of -0.5 and 0.5.
        There is no formal restriction on Teff, but Lanzafame et al. show
        stars from 3000 to 7000 K. Take caution for stars with Teff outside
        this range.
    """
    if (m_h <= -0.5) or (m_h >= 0.5) or (alpha <= 0):
        return np.nan
    
    c = coeffs(m_h)
    logR = np.polynomial.Polynomial(c)(np.log10(teff)) + np.log10(alpha)
    if logR.size == 1:
        return logR.item()
    else:
        return logR