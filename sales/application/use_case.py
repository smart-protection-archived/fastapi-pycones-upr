import abc
from typing import Dict, Any, Optional

from sales.application.commands.command import Command


class UseCase(abc.ABC):

    @abc.abstractmethod
    def execute(self, command: Command) -> Optional[Dict[Any, Any]]:
        pass
