from enum import Enum

class InterpolatorType(Enum):
    """
    Enum for the different interpolator types

    Each value is a unique identifier.
    """

    BASE = "BASE"
    BASE_DISCRETE = "BASE_DISCRETE"
    FINITE_DIFFERENCE = "FINITE_DIFFERENCE"
    DISCRETE_FOLD = "DISCRETE_FOLD"
    PIECEWISE_LINEAR = "PIECEWISE_LINEAR"
    PIECEWISE_QUADRATIC = "PIECEWISE_QUADRATIC"
    BASE_DATA_SUPPORTED = "BASE_DATA_SUPPORTED"
    SURFE = "SURFE"
    PIECEWISE_LINEAR_CONSTANT_NORM = "PIECEWISE_LINEAR_CONSTANT_NORM"
    FINITE_DIFFERENCE_CONSTANT_NORM = "FINITE_DIFFERENCE_CONSTANT_NORM"



