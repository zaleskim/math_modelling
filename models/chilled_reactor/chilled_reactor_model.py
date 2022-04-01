"""
Mathematical model of chilled stirred reactor.
Source: https://jckantor.github.io/CBE30338/02.06-Exothermic-CSTR.html
"""

from scipy.integrate import solve_ivp
import numpy as np
from models.abstract_model.model_interface import ModelInterface
from .constants import Constants as const


class Reactor(ModelInterface):
    def __init__(self, cA0=0.5, T0=350.0):
        self.x0 = [cA0, T0]  # Initial concentration [mol/L] and temperature [K]

    @staticmethod
    def sys_deriv(t, x0: [], u: []):
        cA, T = x0
        Tc = u
        dcAdt = (const.q / const.V) * (const.cAi - cA) - const.k(T) * cA
        dTdt = (const.q / const.V) * (const.Ti - T) + (-const.dHr / const.rho / const.Cp) \
               * const.k(T) * cA + (const.UA / const.V / const.rho / const.Cp) * (Tc - T)
        return [dcAdt, dTdt]

    def sys_solve(self, u: [], t_span):
        solution = solve_ivp(self.sys_deriv, t_span, self.x0, args=(u,))
        solver_sts = solution.status
        self.x0 = np.squeeze(solution.y[:, -1:]).tolist()

        return self.x0, solver_sts

    # def plot(self):
    #     fig, ax = plt.subplots(1, 2, figsize=(12, 4))
    #     def plot_reactor(ax, t, y):
    #         ax[0].plot(t, y[0], label=str(Tc))
    #         ax[0].set_xlabel('Time [min]')
    #         ax[0].set_ylabel('Concentration [gmol/liter]')
    #         ax[0].set_title('Concentration')
    #         ax[0].set_ylim(0, 1)
    #         ax[0].legend()
    #
    #         ax[1].plot(t, y[1], label=str(Tc))
    #         ax[1].set_xlabel('Time [min]')
    #         ax[1].set_ylabel('Temperature [K]')
    #         ax[1].set_title('Temperature')
    #         ax[1].set_ylim(300, 450)
    #         ax[1].legend()
    #
    #     plot_reactor(ax, soln.t, soln.y)
