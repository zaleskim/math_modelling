from abc import ABC, abstractmethod


class ModelInterface(ABC):

    @abstractmethod
    def sys_solve(self, u: [], t_span):
        """
        Computes systems dynamics

        Parameters
        ----------
        u : array_like, float or None
            Control vector
        t_span : 2-tuple of floats
            Interval of integration

        Returns
        -------
        dXdt : array_like or float
            Calculated system state
        """
        pass
