#include<stdio.h>

void main()

{
	int i,j;
	printf("\nEnter value to start : ");
	scanf("%d",&i);
	printf("\nEnter value to end : ");
	scanf("%d",&j);
	
	for(i= 0;i<=10;i++)
	{
		for(j=0;j<=10;j++)
		{
			printf("%d X %d = %d\n",i,j,(i*j));
		}
	}
}