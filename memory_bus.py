

def bus_read(rom, address):
    if address < 0x8000:
        return rom.rom_read(address)

    print("NO IMPL")


def bus_write(rom, address, value):
    if address < 0x8000:
        rom.rom_write(address, value)
        return

    print("NO IMPL")

