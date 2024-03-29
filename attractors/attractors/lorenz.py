#!/usr/bin/env python3
# -*- coding UFT-8 -*-
"""Lorenz attractor objects definition.
"""
import numpy as np

from attractor import ChaosAttractor


class Lorenz(ChaosAttractor):
    """Lorenz attractors specific attributes and methods.

    Attributes
    ----------
    name: str, default='lorenz'
        Name of the attractor given by user.

    init_state: np.ndarray, shape=(3, ), default=np.array([1, 0, -1])
        Initial position of the particle.

    time_domain: np.ndarray, shape=(n, ), default=np.linspace(0, 100, 10000)
        Time domain of the simulation.
    """

    def __init__(self, name: str = 'lorenz',
                 init_state: np.ndarray = np.array([1, 0, -1]),
                 time_domain: np.ndarray = np.linspace(0, 100, 10000)) -> None:
        """Associating class attributes and setup inheritance with
        'ChaosAttractor' objects.
        """
        self.sigma, self.rho, self.beta = 10, 28, 8/3
        super().__init__(name, init_state, time_domain)

    def __len__(self) -> int:
        return self.ts.shape[0]

    def get_jacobian_matrix(self, position: np.ndarray) -> np.ndarray:
        """Compute jacobian matrix of the system at a specific position of the
        trajectory.

        Parameters
        ----------
        position: np.ndarray, shape=(3, ), default=None
            Position at which compute the jacobian.

        Returns
        -------
        jacobian: np.ndarray, shape=(3, 3)
            Jacobian matrix evaluated at specific position.
        """
        x, y, z = position
        jacobian = np.array([
            [-self.sigma, self.sigma, 0],
            [self.rho - z, -1, -x],
            [y, x, -self.beta]
        ])
        return jacobian

    def differential_system(self, r: np.ndarray, ts: np.ndarray) -> np.ndarray:
        """Defines the differential equations system of Lorenz attractor.
        """
        # Initial position
        x, y, z = r

        # Update coordinates
        x_dot = self.sigma * (y - x)
        y_dot = self.rho * x - y - x * z
        z_dot = -self.beta * z + x * y

        return np.array([x_dot, y_dot, z_dot])


if __name__ == '__main__':
    ex = Lorenz()
