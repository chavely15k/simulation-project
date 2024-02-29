class action:
    def __init__(self, client, server, name, start_time, action_time:int = 0) -> None:
        self.name = name
        self.server = server
        self.client = client
        self.start_time = start_time
        self.action_time = action_time
    def __str__(self) -> str:
        return "El cliente " + (str)(self.client) + " realizo la sguiente operacion:\n\' " \
        + (str)(self.name) + " \' en el servidor \' " + (str)(self.server) + " \' con un tiempo de \' " \
        + (str)(self.action_time) + " \'\nal momento " + (str)(self.start_time) + " de iniciada la simulacion\n"


class simulation_report:
    def __init__(self, n_servers: int) -> None:
        self.actions:list[action] = []
        self.n_servers = n_servers
        self.total_clients_queue_time = 0
        self.total_queued_clients = 0
        self.servers_times = [0 for _ in range(n_servers)]
        self.total_servers_time = 0
        self.time = 0
    def push_action(self, action:action):
        if action.name == 'comenzar':
            self.total_servers_time = self.total_servers_time + action.action_time
            self.servers_times[action.server] = self.servers_times[action.server] + action.action_time
        if action.name == 'desencolar':
            self.total_clients_queue_time = self.total_clients_queue_time + action.action_time
            self.total_queued_clients = self.total_queued_clients + 1
        self.actions.append(action)
    def servers_occupation_percent(self):
        servers_times = []
        for i in range(len(self.servers_times)):
            servers_times.append(round((100*self.servers_times[i]/self.total_servers_time), 2))
        return servers_times
    def client_queue_media_time(self):
        if self.total_clients_queue_time == 0: return 0
        return self.total_clients_queue_time/self.total_queued_clients
    def set_time(self, time): self.time = time
    def __str__(self) -> str:
        result =          "-------------------------------------------------------------\n"
        result = result + "----------------- Reporte de la simulacion: #----------------\n"
        result = result + "-------------------------------------------------------------\n"
        for i in range(len(self.actions)):
            result = result + str(i) + ". " + str(self.actions[i]) + "\n"
        result = result + "Porcentaje de ocupacion de los servidores:\n"
        result = result + str(self.servers_occupation_percent()) + "\n\n"

        result = result + "Promedio de tiempo pasado por los clientes en cola, y cantidad de clientes ecolados:\n"
        result = result + str(self.client_queue_media_time()) + ", " + str(self.total_queued_clients) + "\n"
        return result

class report:
    def __init__(self, n_clients, n_servers: int) -> None:
        self.reports:list[simulation_report] = []
        self.n_servers = n_servers
        self.n_clients = n_clients
        self.curr = -1
    def add_new_report(self, ):
        self.reports.append(simulation_report(self.n_servers))
        self.curr += 1
    def get_current_report(self):
        return self.reports[self.curr]
    def set_time(self, time): self.reports[self.curr].set_time(time)
    def get_full_report_info(self):
        servers_use_percent_media = [0 for _ in range(self.n_servers)]
        client_queue_media_time = 0
        total_queued_clients = 0
        total_time = 0
        for report in self.reports:
            total_time += report.time
            client_queue_media_time += report.client_queue_media_time()
            servers_percent = report.servers_occupation_percent()
            total_queued_clients += report.total_queued_clients
            for server in range(self.n_servers):
                servers_use_percent_media[server] += servers_percent[server]
        for server in range(self.n_servers):
            servers_use_percent_media[server] = round(servers_use_percent_media[server] / len(self.reports), 2)
            
        return servers_use_percent_media, round(client_queue_media_time/len(self.reports), 2), total_queued_clients, round(total_time, 2)
    def __str__(self) -> str:
        result =          "----------------------------------------------------------------\n"
        result = result + "----------------- Reporte de las simulaciones: -----------------\n"
        result = result + "----------------------------------------------------------------\n\n"
        
        servers_use_percent_media, client_queue_media_time, total_queued_clients, _ = self.get_full_report_info()
        
        result = result + "Cantidad de simulaciones: " + str(len(self.reports)) + ". Cantidad de servidores: " + str(self.n_servers) + "\n\n"
        result = result + "Porcentaje de ocupacion de los servidores:\n"
        result = result + str(servers_use_percent_media) + "\n\n"

        result = result + "Promedio de tiempo pasado por los clientes en cola: " + str(client_queue_media_time) +"\n\n"
        result = result + "Promedio de clientes ecolados por simulacion: " + str(round(total_queued_clients/len(self.reports), 2)) + "\n"
        return result