// 2) Create a program to print the values of a = 10,b=25.42,c="cat",d=TRUE.

#include <stdio.h>
#include <stdbool.h>
int main(){
    int a = 10;
    float b = 25.42;
    char c[]="cat";
    bool d = true;
    printf("a is %d\n",a);
    printf("b is %f\n",b);
    printf("c is %s\n",c);
    printf("d is %d\n",d);
    return 0;
}