# libraries
import asyncio

# project deependencies
from runner.runner import RunnerInterface

class AsyncRunner(RunnerInterface):
    def __init__(self):
        pass

    def initRoutines(self, routines:list):
        async_routines = []
        for routine in routines:
            async def async_routine():
                await routine()
            async_routines.append(async_routine)
        self.routines = async_routines
        
        
    async def _run(self):
        routines = [r() for r in self.routines]
        self.g = await asyncio.gather(*routines)
        
    def start(self):
        asyncio.run(self._run())
