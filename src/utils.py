import sys

def	exit_signal(code: int, msg: str) -> None:
	print("\n\n\t ------------", end="")
	for i in msg:
		print("-", end="")
	print(f"\n\t| \033[31mExited by {msg}\033[0m |")
	print("\t ------------", end="")
	for i in msg:
		print("-", end="")
	print("\n")
	sys.exit(code)
