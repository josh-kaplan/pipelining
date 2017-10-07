/**
 * timer.c
 *
 * Josh Kaplan
 * _jk@jhu.edu
 *
 * This program times the execution of a command in microseconds.
 */
    
#include <stdio.h>          // for printf
#include <stdlib.h>         // for malloc
#include <string.h>         // for strcat, strlen
#include <sys/time.h>       // gettimeofday()


int main(int argc, char* argv[])
{
    int cmd_size = 0;
    char* cmd;
    struct timeval t1, t2;
    
    // determine the size of the command string
    for (int i = 1; i < argc; i++)
    {
        cmd_size += strlen(argv[i]);
        if (i != argc - 1)
            cmd_size += 1;
    }

    // allocate memory for command size
    cmd = malloc(sizeof(char) * cmd_size);

    // concatenate strings to form command
    for (int i = 1; i < argc; i++)
    {
        strcat(cmd, argv[i]);
        if (i != argc - 1)
            strcat(cmd, " ");
    }

    // run command 1000 times
    // this will help reduce errors at the OS layer
    for (int i = 0; i < 1000; i++)
    {
        gettimeofday(&t1, NULL); // start timer
        system(cmd);             // run command
        gettimeofday(&t2, NULL); // stop timer

        // print execution time in microseconds   
        printf("%d\n", (t2.tv_usec - t1.tv_usec)); 
    }
    return 0;
}



