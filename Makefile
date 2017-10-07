# Makefile
# 
# Josh Kaplan
# _jk@jhu.edu
# 
# Used to build the various programs

all:
	./run_tests.sh

timer:
	gcc -m32 -o timer timer.c

p1:
	nasm -f macho program1.s
	ld -o p1 program1.o 
	rm program1.o

p2:
	nasm -f macho program2.s
	ld -o p2 program2.o 
	rm program2.o

clean: 
	rm p1
	rm p2
	rm p1.dat
	rm p2.dat
	rm timer