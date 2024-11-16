import sys

def	exit_signal(code: int, msg: str) -> None:
	"""
	This function exits the code with a message when a
	signal is received.
	:param code: the exit code
	:param msg: the message that will be printed
	:return: None
	"""
	print("\n\n\t ------------", end="")
	for _ in msg:
		print("-", end="")
	print(f"\n\t| \033[31mExited by {msg}\033[0m |")
	print("\t ------------", end="")
	for _ in msg:
		print("-", end="")
	print("\n")
	sys.exit(code)
