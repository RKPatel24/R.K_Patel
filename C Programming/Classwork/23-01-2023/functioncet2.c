#include<stdio.h>




void add(int x,int y)
{
	printf("\nInside UDF X = %d, Y = %d",x,y);
	printf("\nAddition : %d",(x+y));
}






void main()

{
	int a,b;
	
	printf("\n\t Enter value for a : ");
	scanf("%d",&a);
	printf("\n\t Enter value for b : ");
	scanf("%d",&b);
	printf("\nInside Main A = %d, B = %d",a,b);
	printf("\nStart Function");
	add(a,b);
	printf("\nStop Function");
}