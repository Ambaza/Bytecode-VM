class OpCode:
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4
    PUSH = 5
    POP = 6
    HALT = 7

class SimpleVM:
    def __init__(self, bytecode):
        self.bytecode = bytecode
        self.stack = []

    def run(self):
        ip = 0  # Instruction pointer
        while ip < len(self.bytecode):
            opcode = self.bytecode[ip]

            if opcode == OpCode.ADD:
                self.binary_operation(lambda x, y: x + y)
            elif opcode == OpCode.SUBTRACT:
                self.binary_operation(lambda x, y: x - y)
            elif opcode == OpCode.MULTIPLY:
                self.binary_operation(lambda x, y: x * y)
            elif opcode == OpCode.DIVIDE:
                self.binary_operation(lambda x, y: x / y)
            elif opcode == OpCode.PUSH:
                ip += 1
                value = self.bytecode[ip]
                self.stack.append(value)
            elif opcode == OpCode.POP:
                self.stack.pop()
            elif opcode == OpCode.HALT:
                break
            else:
                raise ValueError(f"Unknown opcode: {opcode}")

            ip += 1

    def binary_operation(self, operation):
        b = self.stack.pop()
        a = self.stack.pop()
        result = operation(a, b)
        self.stack.append(result)

# Example usage:
bytecode = [
    OpCode.PUSH, 3,
    OpCode.PUSH, 4,
    OpCode.ADD,
    OpCode.PUSH, 5,
    OpCode.MULTIPLY,
    OpCode.HALT
]

vm = SimpleVM(bytecode)
vm.run()
print(vm.stack[-1])
