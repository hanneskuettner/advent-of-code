class Frame:
	def __init__(self):
		self.instr_p = 0
		self.sounds = []
		self.send_count = 0
		self.waiting = False

def instr_snd(instr, registers, frame, other_frame):
	frame.sounds.append(instr.get_x_val(registers))
	frame.send_count += 1
	frame.instr_p += 1

def instr_set(instr, registers, frame, other_frame):
	registers[instr.x] = instr.get_y_val(registers)
	frame.instr_p += 1

def instr_add(instr, registers, frame, other_frame):
	registers[instr.x] += instr.get_y_val(registers)
	frame.instr_p += 1

def instr_mul(instr, registers, frame, other_frame):
	registers[instr.x] *= instr.get_y_val(registers)
	frame.instr_p += 1

def instr_mod(instr, registers, frame, other_frame):
	registers[instr.x] %= instr.get_y_val(registers)
	frame.instr_p += 1

def instr_jgz(instr, registers, frame, other_frame):
	if instr.get_x_val(registers) > 0:
		frame.instr_p += instr.get_y_val(registers)
	else:
		frame.instr_p += 1

def instr_rcv1(instr, registers, frame, _):
	if instr.get_x_val(registers) != 0:
		print(frame.sounds.pop())
		return True
	frame.instr_p += 1

def instr_rcv2(instr, registers, frame, other_frame):
	if other_frame.sounds:
		frame.waiting = False
		registers[instr.x] = other_frame.sounds.pop(0)
		frame.instr_p += 1
	else:
		frame.waiting = True


class Instruction:
	SND = 'snd'
	SET  = 'set'
	ADD = 'add'
	MUL = 'mul'
	MOD = 'mod'
	RCV = 'rcv'
	JGZ ='jgz'


	def __init__(self, s):
		parts = s.split()
		self.instruction = parts[0]
		self.x = parts[1]
		try:
			self.x = int(self.x)
			self.x_is_num = True
		except Exception as e:
			self.x_is_num = False
		if len(parts) == 3:
			try:
				self.y = int(parts[2])
				self.y_is_num = True
			except:
				self.y = parts[2]
				self.y_is_num = False

	def get_x_val(self, registers):
		if self.x_is_num:
			return self.x
		else:
			return registers[self.x]

	def get_y_val(self, registers):
		if self.y_is_num:
			return self.y
		else:
			return registers[self.y]


INSTRUCTIONS = {
	Instruction.SND: instr_snd,
	Instruction.SET: instr_set,
	Instruction.ADD: instr_add,
	Instruction.MUL: instr_mul,
	Instruction.MOD: instr_mod,
	Instruction.RCV: instr_rcv1,
	Instruction.JGZ: instr_jgz
}

def eval_instr(instr, registers, frame, other_frame):
	return INSTRUCTIONS[instr.instruction](instr, registers, frame, other_frame)

# part 1
instr = [Instruction(l) for l in open('input.txt').readlines()]
registers = dict([i.x, 0] for i in instr if not i.x_is_num)
frame = Frame()

while not eval_instr(instr[frame.instr_p], registers, frame, None):
	pass


# part 2
registers = [dict([i.x, 0] for i in instr if not i.x_is_num), 
			 dict([i.x, 0] for i in instr if not i.x_is_num)]
registers[1]['p'] = 1
frames = [Frame(), Frame()]
INSTRUCTIONS[Instruction.RCV] = instr_rcv2

while True:
	eval_instr(instr[frames[0].instr_p], registers[0], frames[0], frames[1])
	eval_instr(instr[frames[1].instr_p], registers[1], frames[1], frames[0])
	if frames[0].waiting and frames[1].waiting:
		print(frames[1].send_count)
		break
