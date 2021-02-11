import abc

from sales.application.commands.command import Command


class UseCase(abc.ABC):

    @abc.abstractmethod
    def execute(self, command: Command):
        pass
