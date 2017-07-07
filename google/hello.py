#!/usr/bin/python3.5

import sys


#print("Before")

def Hello(name):
	name = name + '!!!!!'
	print("Hello, " + name)

def main():
#	print("Hello from main function")
#	print("argv[0..2] = " + sys.argv[0], sys.argv[1] ,sys.argv[2])
#	print("argv[0] = ", sys.argv[0])
#	print("argv[1] = ", sys.argv[1])
#	print("argv[2] = ", sys.argv[2])
#	print("argv[3] = ", sys.argv[3])
	Hello(sys.argv[1])


if __name__ == '__main__':
	main()

