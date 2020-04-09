CC := gcc

# source files
SRCS := $(wildcard *.c)

# compiled files
BINS := ${SRCS:%.c=%}

all: ${BINS}

out_vars:
	@echo ${SRCS}
	@echo ${BINS}


%: %.c
	@echo "compiling " $< " ..."
	${CC} -o out/$@ $<
	
