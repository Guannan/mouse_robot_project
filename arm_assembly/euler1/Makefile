
# Makefile
all: euler1

euler1: euler1.o
	gcc -o $@ $+

euler1.o : euler1.s
	as -o $@ $<

clean:
	rm -vf euler1 *.o

