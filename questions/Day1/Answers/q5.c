// 5) Create a program to print the smallest and the largest number in the array/list [2,7,8,23,75,23,64].

# include <stdio.h>
int main(){
    int myArray[] = {2,7,8,23,75,23,64};
    int myArraylength = sizeof(myArray)/sizeof(int);
    int largest = myArray[0];
    int smallest = myArray[0];
    for (int i = 0; i < myArraylength; i++)
    {
        if(myArray[i]>largest){
            largest = myArray[i];
        }
        if(myArray[i]<smallest){
            smallest = myArray[i];
        }
    }
    printf("largest is %d\n",largest);
    printf("smallest is %d\n",smallest);
    return 0;
}