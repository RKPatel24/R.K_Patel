#include<stdio.h>

void main()

{
	int num1 = 43;
	int num2 = 57;
	printf("Number1 = %d \nNumber2 = %d",num1,num2);
	//printf("\nnumber2 = %d",num2);
	printf("\nAddition : %d",(num1+num2));
	printf("\nSubtraction : %d",(num1-num2));
	printf("\nMultiplication : %d",(num1*num2));
	printf("\nDivision : %.2f",((float)num1/num2));
}