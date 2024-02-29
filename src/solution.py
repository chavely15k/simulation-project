from event_system import *
from distributions import *
import time
import matplotlib.pyplot as plt

start = time.time()
# for i in range(pow(10, 8)): pass
# t1 = time.time()
# print(t1 - start)
for i in range(3, 5):
    n_clients = pow(10, i)
    client_distribution = generate_exponential
    servers_distributions = []; x = []; y = []
    for j in range (1, 9):
        servers_distributions.append(generate_exponential); x.append(j)
        sim = simulation(n_clients, client_distribution, servers_distributions)
        for i in range(100):
            sim.simulate()
        y.append(sim.report.get_full_report_info()[1])
        print(sim.report)
    plt.figure()
    plt.xlabel('Cantidad de servidores'); plt.ylabel('Tiempo de espera promedio')
    plt.title(f"Tiempo de espera promedio por cantidad de servidores con {n_clients} clientes")
    plt.plot(x, y); plt.savefig(f'assets/Tiempo de espera promedio por cantidad de servidores con {n_clients} clientes.png')
    plt.clf()

end = time.time()

print(str(end-start))
