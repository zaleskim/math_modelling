from models.chilled_reactor.chilled_reactor_model import Reactor
import numpy as np
import matplotlib.pyplot as plt

reactor = Reactor()


print(f"Initial conditions: {reactor.x0}")
minutes = 10

t_span = np.linspace(1, minutes, minutes)
u = 305
z = []

for i in range(minutes):
    sol, _ = reactor.sys_solve(u, [0, 1])
    z.append(sol)

print(z)

plt.plot(t_span, z)
plt.show()
