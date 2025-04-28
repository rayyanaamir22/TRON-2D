"""
Launch TRON-2D in window.
"""

# frameworks
import asyncio
import platform

# utils
from colours import *
from light_cycle import LightCycle
from light_cycle_battle import LightCycleBattle

async def main():
    # window size
    height, width = 600, 600

    # define cycles
    lc1 = LightCycle('lc1', 100, 100, 10, 0, blue)
    lc2 = LightCycle('lc2', 500, 500, -10, 0, red)
    cycles = [lc1, lc2]

    # run it
    game = LightCycleBattle(width, height, cycles)
    await game.run()

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())