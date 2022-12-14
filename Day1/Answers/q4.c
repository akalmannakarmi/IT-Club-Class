// 4) Create a program to print first 10 terms 2,4,8,....

#include <stdio.h>

int main(){
    int i = 2;
    while (i<22){
        printf("%d\n",i);
        i++;i++;
    }

    return 0;
}