// 6) Create a program to input any two number and an operator(+,-,*,/) 
// and perfrom the specified operation and print the result. 
# include <stdio.h>
int main(){
    int a,b;
    float result;
    char op;
    printf("Enter First Number: ");
    scanf("%d",&a);
    printf("Enter Second Number: ");
    scanf("%d",&b);
    printf("Enter Operator: ");
    scanf(" %c",&op);

    if(op=='+'){
        result = a+b;
    }else if (op=='-')
    {
        result=a-b;
    }else if (op=='*')
    {
        result=a*b;
    }else if (op=='/')
    {
        result=(float)a/(float)b;
    }
    printf("Result = %f",result);
    
    return 0;
}
