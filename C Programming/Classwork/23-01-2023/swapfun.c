#include<stdio.h>

void swap(int n1,int n2)
{
	int t;
	t = n1;
	n1 = n2;
	n2 = t;
	printf ("nIn Swap a = %d, B = %d",n1,n2);
}



void main()
{
	int a=45,b=54;
	printf("\nIn Main A = %d, B = %d",a,b);
	printf("\nStart Function");
	swap(a,b);
	printf("\nStop Function");
}