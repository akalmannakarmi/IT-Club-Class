#include <stdio.h>

int myfunction(){
    int a = 2;
    printf("my function");
    return a;
}

int main(){
    int b = myfunction();
    printf("%d",b);
    return 0;
}