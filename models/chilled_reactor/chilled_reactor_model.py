"""
Mathematical model of chilled stirred reactor.
Source: https://jckantor.github.io/CBE30338/02.06-Exothermic-CSTR.html
"""

from scipy.integrate import solve_ivp
import numpy as np
from models.abstract_model.model_interface import ModelInterface
from .constants import Constants as const


class Reactor(ModelInterface):
    def __init__(self, C0=0.5, T0=350.0, Tcf=300.0):
        self.x0 = [C0, T0, Tcf]  # Initial concentration [mol/L] and tank and coolant temperatures [K]

    @staticmethod
    def sys_deriv(t, x0: [], u: []):
        qc = u
        C, T, Tc = x0
        dC = (const.q / const.V) * (const.Cf - C) - const.k(T) * C
        dT = (const.q / const.V) * (const.Tf - T) + (-const.dHr / const.rho / const.Cp) * const.k(T) *\
             C + (const.UA / const.V / const.rho / const.Cp) * (Tc - T)
        dTc = (qc / const.Vc) * (const.Tcf - Tc) + (const.UA / const.Vc / const.rho / const.Cp) * (T - Tc)
        return [dC, dT, dTc]

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
