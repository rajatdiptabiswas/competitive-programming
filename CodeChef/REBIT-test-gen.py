from random import randint

ops = ['0', '^', '|', '&']
n = 6

for i in range(n-len(ops)+1):
	ops.append('x')

def gen_exp(op):
	if op == '0':
		return '#'
	elif op == '^' or op == '|' or op == '&':
		return '(#'+op+'#)'
	else:
		return '('+gen_exp(ops[randint(0,n)])+ops[randint(1,3)]+gen_exp(ops[randint(0,n)])+')'

def main():
	print(1)
	print(gen_exp(ops[randint(0,n)]))

if __name__ == '__main__':
	main()