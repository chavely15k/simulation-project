from client_queue import *
from server_heap import *
from distributions import *

class action:
    def __init__(self, client, server, name, time) -> None:
        self.time = time
        self.name = name
        self.server = server
        self.client = client
    def __str__(self) -> str:
        # if self.name == "encolar": print("DFGWERGWTRHTR")
        return "El cliente " + (str)(self.client) + " realizo la sguiente operacion:\n\' " + (str)(self.name) + " \' en el servidor \' " + (str)(self.server) + " \'\nal momento " + (str)(self.time) + " de iniciada la simulacion\n"

class report:
    def __init__(self) -> None:
        self.actions = []
    def push_action(self, action):
        self.actions.append(action)
    def print(self):
        for action in self.actions:
            print(action)

class simulation:
    def __init__(self, client_distribution, servers_distribution) -> None:
        self.current_time = 0
        self.report = report()
        self.busy_servers = heap()
        self.client_queue = queue()
        self.active_servers = heap()
        self.client_distribution = client_distribution
        for i in range(len(servers_distribution)): self.active_servers.push((i, servers_distribution[i]))

    def simulate(self, n_clients):
        for client in range(n_clients): 
            self.current_time = self.current_time + self.client_distribution()
            self.add_new_client(client)
        self.refresh(inf) #process to the end
        self.report.print()
        self.reset_simulation()

    def add_new_client(self, client):
        self.refresh(self.current_time)
        self.process_new_client(client)

    def process_new_client(self, client):
        if self.active_servers.empty(): 
            self.push_to_queue(client)
        else: self.process(client, self.current_time)

    def refresh(self, current_time):
        while not self.busy_servers.empty() and self.busy_servers.top()[0] <= current_time:
            time = self.process_next_service()
            if not self.client_queue.empty():
                self.process_one_client_from_queue(time)

    def process_one_client_from_queue(self, time):
        client = self.client_queue.pop()
        self.process(client, time)
    
    def process_next_service(self):
        time, client, server = self.busy_servers.pop()
        self.report.push_action(action(client, server[0], "terminar", time))
        self.active_servers.push(server)
        return time
    
    def push_to_queue(self, client):
        self.report.push_action(action(client, None, "encolar", self.current_time))
        self.client_queue.push(client)
    
    def process(self, client, time):
        server = self.active_servers.pop()
        end_time = time + server[1]()
        self.report.push_action(action(client, server[0], "comenzar", time))
        self.busy_servers.push((end_time, client, server))

    def reset_simulation(self):
        self.report = report()
        self.current_time = 0

