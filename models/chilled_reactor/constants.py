import numpy as np


class Constants:
    Ea = 72750      # activation energy J/gmol
    R = 8.314       # gas constant J/gmol/K
    k0 = 7.2e10     # Arrhenius rate constant 1/min
    V = 100.0       # Volume [L]
    rho = 1000.0    # Density [g/L]
    Cp = 0.239      # Heat capacity [J/g/K]
    dHr = -5.0e4    # Enthalpy of reaction [J/mol]
    UA = 5.0e4      # Heat transfer [J/min/K]
    q = 100.0       # Flowrate [L/min]
    cAi = 1.0       # Inlet feed concentration [mol/L]
    Ti = 350.0      # Inlet feed temperature [K]
    Tc = 300.0      # Coolant temperature [K]

    # Arrhenius rate expression
    @staticmethod
    def k(T):
        """

        Parameters
        ----------
        T: float
            Temperature

        Returns
        -------
        k: float
            Arrhenius rate
        """
        return Constants.k0 * np.exp(-Constants.Ea / (Constants.R * T))

