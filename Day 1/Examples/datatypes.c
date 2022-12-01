#include <stdio.h>
#include <stdbool.h>

int main(){
    int a = 1;
    printf("a is %d \n",a);
    float b = 1.2;
    printf("b is %f \n",b);

    bool work = true;
    printf("work is %i \n",work);

    char character = 'a';
    printf("character is %c \n",character);

    char str[] = "hello me";
    printf("str[] is %s \n",str);
    char * address = "Earth";
    printf("address is %s \n",address);
    
    char name[10] = "name";
    printf("name is %s \n",name);
    int grades[5] = {1,2,3,4,5};
    printf("grades is %d \n",grades);

    int i =0;
    while(i<5) {
        printf("%d ", grades[i]);
        i++;
    }

    return 0;
}