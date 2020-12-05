class IntcodeComputer():
    def __init__(self, input, prog, child=None, relative_base=0, name='A'):
        self.input = input
        self.ip = 0
        self.input_pointer   = 0
        self.diagnostic_code = 0
        self.relative_base = relative_base
        self.name = name
        self.prog = prog + ([0] * 10000) # is there a way to do this lazily?
        self.run = True

        # input/break/output values
        self.completed = False
        self.waiting   = False
        self.outputs = []

        self.child = child
        self.opcodes = {
         '01' : self.add,
         '02' : self.mul,
         '03' : self.save,
         '04' : self.out,
         '05' : self.jmpt,
         '06' : self.jmpf,
         '07' : self.lt,
         '08' : self.eq,
         '09' : self.base,
        }

    def access(self, mode, index):
        opr = 0
        if mode == '0':
            opr = self.prog[self.prog[index]]
        elif mode == '1':
            opr = self.prog[index]
        elif mode == '2':
            opr = self.prog[self.prog[index] + self.relative_base]
        else:
            print('INVALID MODE')
        return opr

    def add(self, modes=[]):
        result_loc         = self.prog[self.ip+3]
        opr0, opr1 = self.access(modes[-1], self.ip+1), self.access(modes[-2], self.ip+2)

        if modes[-3] == '2':
            self.prog[result_loc + self.relative_base] = opr0 + opr1
        else:
            self.prog[result_loc] = opr0 + opr1

        self.ip += 4

    def mul(self, modes=[]):
        result_loc         = self.prog[self.ip+3]
        opr0, opr1 = self.access(modes[-1], self.ip+1), self.access(modes[-2], self.ip+2)

        if modes[-3] == '2':
            self.prog[result_loc + self.relative_base] = opr0 * opr1
        else:
            self.prog[result_loc] = opr0 * opr1
        self.ip += 4

    def save(self, modes=[]):
        if self.input_pointer >= len(self.input):
            self.run = False
            self.waiting = True
        else:
            self.waiting = False
            if modes[-1] == '0':
                self.prog[self.prog[self.ip+1]] = self.input[self.input_pointer]
            elif modes[-1] == '1':
                self.prog[self.ip+1] = self.input[self.input_pointer]
            elif modes[-1] == '2':
                self.prog[self.prog[self.ip+1] + self.relative_base] = self.input[self.input_pointer]
            else:
                print('INVALID MODE')

            self.input_pointer += 1
            self.ip += 2

    def out(self, modes=[]):
        self.diagnostic_code = self.access(modes[-1], self.ip+1)
        self.outputs.append(self.diagnostic_code)
        self.ip += 2

    def jmpt(self,  modes=[]):
        opr0, opr1 = self.access(modes[-1], self.ip+1), self.access(modes[-2], self.ip+2)
        if opr0 != 0:
            self.ip = opr1
        else:
            self.ip += 3

    def jmpf(self, modes=[]):
        opr0, opr1 = self.access(modes[-1], self.ip+1), self.access(modes[-2], self.ip+2)
        if opr0 == 0:
            self.ip = opr1
        else:
            self.ip += 3

    def lt(self, modes=[]):
        opr0, opr1 = self.access(modes[-1], self.ip+1), self.access(modes[-2], self.ip+2)

        if modes[-3] == '2':
            self.prog[self.prog[self.ip+3] + self.relative_base] = 1 if opr0 < opr1 else 0
        else:
            self.prog[self.prog[self.ip+3]] = 1 if opr0 < opr1 else 0
        self.ip += 4

    def eq(self, modes=[]):
        opr0, opr1 = self.access(modes[-1], self.ip+1), self.access(modes[-2], self.ip+2)

        if modes[-3] == '2':
            self.prog[self.prog[self.ip+3] + self.relative_base] = 1 if opr0 == opr1 else 0
        else:
            self.prog[self.prog[self.ip+3]] = 1 if opr0 == opr1 else 0
        self.ip += 4

    def base(self, modes=[]):
        opr0 = self.access(modes[-1], self.ip+1)
        self.relative_base += opr0
        self.ip += 2

    def execute(self):
        self.run = True
        while(self.run):
            opcode = str(self.prog[self.ip])[-2:]
            if (opcode == '99'):
                self.run = False
                self.completed = True
            else:
                opcode = '0'+opcode if (len(opcode) == 1) else opcode
                modes = (['0','0','0'] + [i for i in str(self.prog[self.ip])[:-2]])[-3:]

                self.opcodes[opcode](modes)
