

def DEC_05(cpu): # 05 DEC B
    t = cpu.B - 1
    flag = 0b01000000
    flag += ((t & 0xFF) == 0) << FLAGZ
    flag += (((cpu.B & 0xF) - (1 & 0xF)) < 0) << FLAGH
    cpu.F &= 0b00010000
    cpu.F |= flag
    t &= 0xFF
    cpu.B = t
    cpu.PC += 1
    cpu.PC &= 0xFFFF
    return 4


def LD_0E(cpu, v): # 0E LD C,d8
    cpu.c = v
    cpu.pc += 2
    cpu.pc &= 0xFFFF
    return 8


def get_inst_by_opcode(cpu, opcode):
    if opcode == 0x00:
        return "NOP_00"
    elif opcode == 0x05:
        return "IN_DEC"
    elif opcode == 0x0E:
        return LD_0E(cpu, 0)
    elif opcode == 0xAF:
        return "IN_XOR"
    elif opcode == "0xC3":
        return "IN_JP"
    elif opcode == 0xF3:
        return "IN_DI"
    else:
        return "No instructions found..."

