from cpu import CPU
from rom import ROM

emu_context = {
    "running": True,
    "paused": False,
    "ticks": 0
}


def main():
    import time

    rom = ROM("roms/cpu_instrs.gb")
    # rom = ROM("roms/Tetris.gb")
    cpu = CPU(rom)

    while emu_context["running"]:
        cpu.cpu_step()
        time.sleep(1)


if __name__=="__main__":
    main()