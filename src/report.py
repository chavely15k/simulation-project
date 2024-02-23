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
        self.actions:list[action] = []
    def push_action(self, action:action):
        self.actions.append(action)
    def __str__(self) -> str:
        result =          "#############################################################\n"
        result = result + "################# Reporte de la simulacion: #################\n"
        result = result + "#############################################################\n"
        for i in range(len(self.actions)):
            result = result + str(i) + ". " + str(self.actions[i]) + "\n"
        return result