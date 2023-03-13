#include<stdio.h>

int food()
{
	char ch;   
	int choice,quantity,amount,total_amount;
	
	//Display Menu
	printf("\n\t\e[1m \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2 ");
	printf("\n\t \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\e[1m  Menu \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2");
	printf("\n\t\e[1m \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2 \v");
	printf("\t--------------------------------");
	printf("\n\t   1.PIZZA\t\t 180rs/pcs");
	printf("\n\t   2.BURGER\t\t 100rs/pcs");
	printf("\n\t   3.DOSA\t\t 120rs/pcs");
	printf("\n\t   4.IDLI\t\t 50rs/pcs");
	printf("\n\t--------------------------------");
	printf("\n\t Enter your choice : ");
	scanf("%d",&choice);
		if(choice==1)
		{
			printf("\t You have selected PIZZA.");
			printf("\n\t Enter the quantity : ");
			scanf("%d",&quantity);
			amount = 180*quantity;
			printf("\t Amount = %dRs/-",amount);
			total_amount = amount;
			printf("\n\t Total Amount = %dRs/-",total_amount);
			printf("\n\t --------------------------------");
		}
		else if(choice==2)
		{
			printf("\t You have selected BURGER.");
			printf("\n\t Enter the quantity : ");
			scanf("%d",&quantity);
			amount = 100*quantity;
			printf("\t Amount = %dRs/-",amount);
			total_amount = amount;
			printf("\n\t Total Amount = %dRs/-",total_amount);
			printf("\n\t --------------------------------");
		}
		else if(choice==3)
		{
			printf("\t You have selected DOSA.");
			printf("\n\t Enter the quantity : ");
			scanf("%d",&quantity);
			amount = 120*quantity;
			printf("\t Amount = %dRs/-",amount);
			total_amount = amount;
			printf("\n\t Total Amount = %dRs/-",total_amount);
			printf("\n\t --------------------------------");
		}
		else if(choice==4)
		{
			printf("\t You have selected IDLI.");
			printf("\n\t Enter the quantity : ");
			scanf("%d",&quantity);
			amount = 50*quantity;
			printf("\t Amount = %dRs/-",amount);
			total_amount = amount;
			printf("\n\t Total Amount = %dRs/-",total_amount);
			printf("\n\t --------------------------------");
		}
		else
		{
			printf("\n\t Please select ITEM from 1-4.");
			printf("\n\t --------------------------------");
		}
		fflush(stdin);
//		total_amount = amount+amount+amount+amount;
//		printf("\n Total amount to pay = %d", total_amount);
}


	
int main()
	{
		char ch;
		int total_amount;
		food();
	do
	{
	
		printf("\n\t Do you want place more orders? Y/N = ");
		scanf("%c",&ch);
		if(ch == 'Y')
		{
			food();
		}
		else
		{
			
		}
	}
	while(ch == 'Y');
	
		printf("\n\t Thank You for Dining With Us.");
	
}




