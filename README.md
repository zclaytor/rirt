# rirt

Computes the activity index of [Lanzafame et al. (2023)](https://ui.adsabs.harvard.edu/abs/2023A%26A...674A..30L/abstract).

Eq. 7 offers a conversion between the Gaia `activityindex_espcs` index and a more temperature-insensitive index, $R'_\mathrm{IRT}$, from the Ca II infrared triplet:

$\log R'_\mathrm{IRT} = (C_0 + C_1 θ + C_2 θ^2 + C_3 θ^3) + \log α$

where $θ = \log(T_\mathrm{eff}/\mathrm{K})$, α is the Ca II IRT equivalent width in nm, and the coefficients $C_i$ depend on metallicity.

## Installation

Install using pip with git:

```bash
pip install git+https://github.com/zclaytor/rirt
```

## Usage

Compute $\log R'_\mathrm{IRT}$ for a single star:

```python
from rirt import logRirt
logRirt(0.2, -0.3, 4000)
```
> -4.4848481

Or a list of stars:

```python
logRirt([0.2, 0.11], [-0.3, 0.1], [4000, 6000])
```
> array([-4.48484841, -4.64219075])
