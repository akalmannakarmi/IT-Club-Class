#include <stdio.h>

int myfunction(){
    printf("my function");
    return 0;
}

int myfunction2(){
    myfunction();
    printf("main function");
    return 0;
}