#include<stdio.h>


void main()
{
	int marks[10];
	int i,j;
	
	
	for(i=0;i<5;i++)
	{
		printf ("Enter Element[%d] : ",i);
		scanf("%d",&marks[i]);
	}
	
	printf("\n\n");
	for(i=0;i<5;i++)
	{
		printf ("Element at index [%d] = %d\n",i,marks[i]);
	}
}