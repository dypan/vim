all: out
VPATH = ./util;./port
vpath %.cc ./util
vpath %.h ./util
vpath %.h ./include/leveldb
CXX=g++
CXXFLAGS=-c -g -I./include -I./ -DLEVELDB_PLATFORM_POSIX=1 -DLEVELDB_IS_BIG_ENDIAN=0
flag=-c -g -I./include -I./ -DLEVELDB_PLATFORM_POSIX=1 -DLEVELDB_IS_BIG_ENDIAN=0
obj=main.o coding.o cache.o hash.o
out: $(obj)
	$(CXX) -o out $(obj)
main.o: main.cc
coding.o: coding.cc coding.h
cache.o: cache.cc cache.h
hash.o: hash.cc hash.h
clean:
	rm out $(obj)
