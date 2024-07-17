from memory_bus import bus_read
from instructions import get_inst_by_opcode


class CPU:
    def __init__(self, rom):
        self.a = 0
        self.f = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.e = 0
        self.h = 0
        self.l = 0
        self.pc = 0x100
        self.sp = 0

        self.fetch_data = 0
        self.mem_dest = 0
        self.mem_is_dest = False
        self.cur_opcode = 0
        self.cur_inst =""
        
        self.halted = False
        self.stepping = False

        self.rom = rom


    def fetch_instruction(self):
        self.pc += 1
        self.cur_opcode = bus_read(self.rom, self.pc)
        self.cur_inst = get_inst_by_opcode(self, self.cur_opcode)


    def fetch_data(self):
        self.mem_dest = 0
        self.mem_is_dest = False


    def display_cpu_state(self):
        display_log = f"""
A: {self.a}
F: {self.f}
B: {self.b}
C: {self.c}
D: {self.d}
E: {self.e}
H: {self.h}
L: {self.l}
PC: {self.pc}
SP: {self.sp}
Fetched Data: {self.fetch_data}
Destination: {self.mem_dest}
Opcode: {self.cur_opcode}
Instruction: {self.cur_inst}
        """
        print(display_log)


    def cpu_step(self):
        if not self.halted:
            self.fetch_instruction()
            self.display_cpu_state()



