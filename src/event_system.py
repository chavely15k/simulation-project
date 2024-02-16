from client_queue import *
from server_heap import *
from distributions import *

class report:
    def __init__(self) -> None:
        self.actions = []
        self.idx = 0

    def push_action(self, start_time, end_time):
        self.idx = self.idx + 1
        self.actions.append((end_time, start_time, self.idx))

    def print(self):
        self.actions.sort()
        for action in self.actions:
            print("service index: " + (str)(action[2]) + "\nstart service time: "+ (str)(action[1]) + "\nend service time: " + (str)(action[0]))

class simulation:
    def __init__(self, n_servers, client_distribution, servers_distribution) -> None:
        self.current_time = 0
        self.report = report()
        self.busy_servers = server_heap()
        self.client_queue = client_queue()
        self.active_servers = server_heap()
        self.client_distribution = client_distribution
        for i in range(n_servers): self.active_servers.push((i, servers_distribution[i]))

    def simulate(self, n_clients):
        for i in range(n_clients): self.add_new_client()
        self.current_time = inf
        self.refresh()
        self.report.print()
        self.current_time = 0

    def add_new_client(self):
        self.current_time = self.current_time + self.client_distribution()
        self.refresh()
        self.process_new_client()

    def process_new_client(self):
        if self.active_servers.empty():
            self.client_queue.push(self.current_time)
        else:
            server = self.active_servers.pop()
            end_time = self.current_time + server[1]()
            self.report.push_action(self.current_time, end_time)
            self.busy_servers.push((end_time, server))

    def refresh(self):
        while self.active_servers.empty() and not self.client_queue.empty() and not self.busy_servers.empty() and self.busy_servers.top()[0] <= self.current_time:
            time = self.process_next_service()
            self.process_one_client_from_queue(time)
        while not self.busy_servers.empty() and self.busy_servers.top()[0] <= self.current_time:
            self.process_next_service()

    def process_next_service(self):
        time, server = self.busy_servers.pop()
        self.active_servers.push(server)
        return time

    def process_one_client_from_queue(self, time):
        end_time = time + self.active_servers.top()[1]()
        self.report.push_action(time, end_time)
        self.client_queue.pop()
        self.busy_servers.push((end_time, self.active_servers.pop()))
