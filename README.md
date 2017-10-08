# Pipelining

I was asked to answer the following question as a discussion prompt for my
computer architecture course:

>Do you think that you could write a program that could determine whether a
>computer is using instruction pipelining? Explain your answer.

I decided to try it out.

## How it works

The `Makefile` defines how to compile the C and assembly programs as well as
some simple cleanup behavior.

The `run_tests.sh` file is used to orchestrate the tests. It runs some cleanup,
compiles all the programs, and runs a few tests in different orders to help
reduce the impact of OS process scheduling.

The `timer.c` file is designed to time the execution of a shell command. It
is only accurate on the scale of microseconds. I couldn't find a way to do 
nanosecond timing on OS X with the amount of effort I wanted to put in to this. 
So, we  have microsecond timing. The results of the timer are dumped to .dat 
files by the *run_tests* script.

`program1.s` and `program2.s` are assembly programs with and without pipelining
hazards respectively. They execute the same exact instructions, but in a 
different order. They each loop over these instructions 25 million times. So,
they take a while to run. This is necessary.

It turns out, we need to loop many many times in the assembly code for two 
reasons: 

1. The operating system's prioritization of program execution causes a lot of
   deviation in execution time.
2. We only have microsecond timing and the difference in execution time of each
   loop iteration between program 1 and program 2 is very small. We need to run 
   many times to measure the differences on the scale of microseconds.

Finally, a Python script `results.py` reads the timing results and plots them.

Then you get a result looking something like this:

![Results](./results.png?raw=true)

## Try it yourself

First, I ran this on Mac OS X. I have not tested it on any other system. 

### Dependencies

To assemble the assembly programs, you need [nasm](http://www.nasm.us/)
installed.

To compile the C code, you need [gcc](https://gcc.gnu.org/).

The Python script depends on [matplotlib](https://matplotlib.org/) and 
[NumPy](http://www.numpy.org/). If you already have 
[pip](https://pypi.python.org/pypi/pip) and Python installed, just run
`pip install -r requirements.txt`.

### Executing Everything

Once you've gotten all the dependencies installed (and made any necessary
cross-platform changes), just run `./run_tests.sh`.

## More Results

**Loop 25,000,000 times**
![Results](./results.png?raw=true)

**Loop 1,000,000 times**
![Results](./results_less_ambiguous.png?raw=true)

**Loop 100,000 times**
![Results](./results_ambiguous.png?raw=true)


**Loop 10,000 times**
![Results](./results_more_ambiguous.png?raw=true)

