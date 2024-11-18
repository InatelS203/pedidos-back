class CommandInvoker:
    def __init__(self, dependency=None):
        self.command_history = []
        self.dependency = dependency 

    def execute(self, command):
        result = command.execute()
        self.command_history.append(command)
        if self.dependency:
            self.dependency.log(f"Executed {command.__class__.__name__}")
        return result
