import re

A_COMMAND = 1
C_COMMAND = 2
L_COMMAND = 3

class Parser:

	stream = None

	command_type = None

	nowline = '\n'

	a_command_rex = None

	c_command_rex = None

	l_command_rex = None

	delete_rex = None

	def __init__(self, stream):
		self.stream = stream
		self.a_command_rex = re.compile('^\\@([_.$:a-zA-Z0-9]+)')
		self.c_command_rex = re.compile(
			'^(([AMD]{1,3})=)?([-!]?[AMD01])([-+&|])?([01AMD])?(;)?(J[GELNM][TQETP])?$'
			)
		self.l_command_rex = re.compile('^\(([_.$:a-zA-Z0-9]+)\)$')
		self.delete_rex = re.compile('(?://.*| )')

	def hasMoreCommands(self):
		return self.nowline != ''

	def advance(self):
		self.nowline = self.delete_rex.sub("", self.stream.readline())
		return self.nowline

	def commandType(self):
		self.command_type = self.a_command_rex.match(self.nowline)
		if self.command_type is not None:
			return A_COMMAND

		self.command_type = self.c_command_rex.match(self.nowline)
		if self.command_type is not None:
			return C_COMMAND

		self.command_type = self.l_command_rex.match(self.nowline)
		if self.command_type is not None:
			return L_COMMAND

	def symbol(self):
		return self.command_type.group(1)

	def dest(self):
		dest = self.command_type.group(2)
		if dest is None:
			return ''

		return dest

	def comp(self):
		left_var = self.command_type.group(3)
		if left_var is None:
			left_var = ''

		ctr_var = self.command_type.group(4)
		if ctr_var is None:
			ctr_var = ''

		right_var = self.command_type.group(5)
		if right_var is None:
			right_var = ''

		return left_var + ctr_var + right_var

	def jump(self):
		jump = self.command_type.group(7)
		if jump is None:
			return ''

		return jump

class NotCommandErrorException(Exception):
	pass
