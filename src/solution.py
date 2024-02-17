from event_system import *
from distributions import distributions

def ask_how_many_clients():
    print("Escriba la cantidad de clientes para la simulacion.")
    return (int)(input())
def ask_how_many_servers():
    print("Escriba la cantidad de servidores para la simulacion.")
    return (int)(input())
def ask_for_client_distribution():
    print("Ecoja la distribucion que desea utilizar para el intervalo entre los clientes(escribiendo el numero correspondiente):")
    for i in range(len(distributions)):
        print((str)(i) + " " + distributions[i].__name__)
    return (int)(input())
def ask_for_servers_distributions(idx):
    print("Ecoja las distribuciones que desea utilizar para el timepo de servicio en cada servidor(escribiendo el numero correspondiente):")
    for i in range(len(distributions)):
        print((str)(i) + " " + distributions[i].__name__)
    distribution = distributions[(int)(input())]
    print("escriba la cantidad de servidores a partir del " + (str)(idx) + "-esimo a aplicarsela")
    return distribution, (int)(input())
    
    

m_clients = ask_how_many_clients()
n_servers = ask_how_many_servers()
client_distribution = distributions[ask_for_client_distribution()]
servers_distributions = []
i = 0
while i < n_servers:
    d, k = ask_for_servers_distributions(i)
    for j in range(min(k, n_servers - i)):
        servers_distributions.append(d)
    i = i + k

sim = simulation(client_distribution, servers_distributions)
sim.simulate(m_clients)
