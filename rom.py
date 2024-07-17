from rom_data import ROM_SIZES, ROM_TYPES, LICENSE_CODE

ROM_HEADER = {
    "entry": 0,
    "logo": 0,
    "title": "",
    "new_lic_code": 0,
    "sgb_flag": 0,
    "type": 0,
    "rom_size": "",
    "ram_size": 0,
    "dest_code": 0,
    "lic_code": 0,
    "version": 0,
    "checksum": 0,
    "global_checksum": 0,
    "rom_data": []
}

class ROM:
    def __init__(self, file_path):
        self.file_path = file_path
        self.rom_data = self.load_rom()

        self.entry = 0
        self.logo = 0
        self.title = ""
        self.license_code = 0
        
        self.sgb_flag = 0
        self.rom_size = ""
        self.ram_size = 0

        self.version = 0


    def init_rom(self, rom_file):
        self.rom_data = load_rom(rom_file)
        ROM_HEADER["rom_data"] = rom_data
        print(ROM_TYPES.get(self.rom_data[0x147]))
        print(ROM_SIZES.get(self.rom_data[0x148]))
        print(LICENSE_CODE.get("%02X" % self.rom_data[0x14b]))
        title = self.rom_data[0x134 : 0x134 + 16]
        print(convert_title(title))
        print(self.rom_data[0x00])
        print("%02X" % self.rom_data[0x14c])


    def load_rom(self):
        with open(self.file_path, "rb") as file:
            rom_data = bytearray(file.read(0x150))
        return rom_data


    def convert_title(self, title):
        chars = []
        for i in title:
            if i in [ord('\t'), ord('\n'), ord('\r')] or 0x20 <= i and i <= 0x7E:
                chars.append(chr(i))
            else:
                chars.append(" ")
        return "".join(chars).strip()


    def checksum(rom_data):
        x = 0
        for i in range(0x134, 0x14D):
            x = x - rom_data[i] - 1
            x &= 0xff
        return rom_data[0x14D] == x


    def is_valid_data(data):
        nintendo_logo = [
            0xCE, 0xED, 0x66, 0x66, 0xCC, 0x0D, 0x00, 0x0B, 0x03, 0x73, 0x00, 0x83, 0x00, 0x0C, 0x00, 0x0D,
            0x00, 0x08, 0x11, 0x1F, 0x88, 0x89, 0x00, 0x0E, 0xDC, 0xCC, 0x6E, 0xE6, 0xDD, 0xDD, 0xD9, 0x99,
            0xBB, 0xBB, 0x67, 0x63, 0x6E, 0x0E, 0xEC, 0xCC, 0xDD, 0xDC, 0x99, 0x9F, 0xBB, 0xB9, 0x33, 0x3E,
        ]
        return [b for b in data[0x104 : 0x104 + len(nintendo_logo)]] == nintendo_logo


    def rom_read(self, address):
        return self.rom_data[address]


    def rom_write(address, value):
        print("Write not implemented.")

