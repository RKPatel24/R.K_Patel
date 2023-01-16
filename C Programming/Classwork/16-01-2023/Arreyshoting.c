#include<stdio.h>

void main()

{
	int roll[5];
	int i,j,t;
	
	printf("\n\n\t\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2  Enter Array Elements  \xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	for (i=0;i<5;i++)
	{
		printf ("\t\tEnter Element [%d] : ",i);
		scanf ("%d",&roll[i]);
	}
	
	printf("\n\n\t\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2  Array Elements are :   \xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	for(i=0;i<5;i++)
	{
		printf ("\t\tElement at index [%d] = %d\n",i,roll[i]);
	}
	
	printf("\n\n\t\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2  Array Element in Ascending order : \xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	
	for (i=0;i<5;i++)
	{
		for(j=i;j<5;j++)
		{
			if(roll[i]>roll[j])
			{
				t=roll[i];
				roll[i]=roll[j];
				roll[j]=t;
			}
		}
	}
	
	for(i=0;i<5;i++)
	{
		printf("\n\t\tElement at Index[%d] : %d",i,roll[i]);
	}
	
	printf("\n\n\t\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2  Array Element in Decending order : \xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	
	for (i=0;i<5;i++)
	{
		for(j=i;j<5;j++)
			{
			if(roll[i]<roll[j])
			{
				t=roll[i];
				roll[i]=roll[j];
				roll[j]=t;
			}
		}
	}
	
	for(i=0;i<5;i++)
	{
		printf("\n\t\tElement at Index[%d] : %d",i,roll[i]);
	}

}