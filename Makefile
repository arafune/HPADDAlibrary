CC=gcc
CFLAGS = -Wall `pkg-config --cflags python-3.5`
CFLAGS += -fPIC
LDFLAGS = `pkg-config --libs python-3.5`

%o.: %.c
	$(CC) $(CFLAGS) -c $< -o $@

all: ADtest libhpadda.so

ADtest: HPADDAlibrary.c main.c HPADDAlibrary.h
	gcc -o $@ HPADDAlibrary.c HPADDAlibrary.h main.c -lbcm2835 -lm

libhpadda.so:  HPADDAlibrary.o 
	$(CC) $(CFLAGS) -shared -o $@ $< -lbcm2835

clean:
	-rm *.o Test
	-rm *.so

.PHONY: all clean
