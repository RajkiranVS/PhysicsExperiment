# importing the required libraries

from tkinter import *
import numpy as np
from scipy.spatial.distance import euclidean

# Creating an empty Tkinter window
root = Tk()

# Setting the Tkinter window properties
root.wm_title('My Universe')
canvas = Canvas(root, width=700, height=700, bg='black')
canvas.grid(row=0, column=0)

G = 0.01  # Gravitational constant
Bodies = []  # List of Bodies in n-bodies


class Body:
    """
    The class to create n-bodies with following properties
    :param
     mass: List of Mass of N-Bodies
     px: List of positions of the body with respect to X-axis
     py: List of position of the body with respect to Y-axis
     v: List of the velocities of the N-Bodies
    :return
    The basic properties of the N-Bodies
    """
    def __init__(self, mass, px, py, v):
        self.Mass = mass
        self.Px = px
        self.Py = py
        self.P = np.array([self.Px, self.Py], dtype=float)
        self.V = v
        self.logX = []
        self.logY = []
        self.R = np.cbrt((self.Mass/3.14))

    def fg(self, other):
        """
        :param other: Other bodies with respect to self
        :return: None
        """
        if self == other:
            self.dv = np.array([0, 0], dtype=float)
        else:
            self.dist = euclidean([self.P[0], self.P[1]],
                                  [other.P[0], other.P[1]])
            self.dv = np.array([0, 0], dtype=float)
            if self.dist == 0:
                self.dv = 0
            else:
                self.F = (-1 * G * self.Mass * other.Mass / self.dist**2) * (self.P - other.P) / self.dist
                self.dv = self.F/self.Mass
                if self.dist < self.R + other.R + 5:
                    self.dv *= -0.5
            self.V = self.dv

            if self.P[0] < 10+self.R:
                self.V[0] *= -0.9
                self.P[0] += 1
            if self.P[0] > 690 - self.R:
                self.V[0] *= -0.9
                self.P[0] -= 1
            if self.P[1] < 10+self.R:
                self.V[1] *= -0.9
                self.P[1] += 1
            if self.P[1] > 690 - self.R:
                self.V[1] *= -0.9
                self.P[1] -= 1

BODIES = 25

for i in range(0, BODIES):
    Bodies.append(Body(np.random.randint(1, 500), np.random.randint(6, 650), np.random.randint(5, 650),
                       [np.random.randint(100, 10000), np.random.randint(100, 10000)]))
    T = 0
    Tx = True
    while Tx:
        T += 1

        canvas.delete("all")

        for Body1 in Bodies:
            for Body2 in Bodies:
                Body1.fg(Body2)
            Body1.P += Body1.V

            if Body1.P[1] < 5:
                Body1.V[1] *= -0.005

            if Body1.P[1] > 695:
                Body1.V[1] *= -0.005

            if Body1.P[0] < 5:
                Body1.V[0] *= -0.009

            if Body1.P[0] > 695:
                Body1.V[0] *= -0.009

            canvas.create_oval(Body1.P[0] - Body1.R, Body1.P[1] - Body1.R, Body1.P[0] + Body1.R,
                               Body1.P[1] + Body1.R, fill='red')
        canvas.update()

        if 10000 == T:
            Tx = False
mainloop()

