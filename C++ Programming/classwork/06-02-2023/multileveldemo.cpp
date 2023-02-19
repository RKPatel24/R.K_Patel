#include<iostream>
using namespace std;

class A
{
	public:
		int a;
		
		void getA(int x)
		{
			a = x;
		}
		
		void showA()
		{
			cout<<"\nA = "<<a;
		}
};

class B : public A
{
	public:
		int b;
		
		void getB(int y)
		{
			b = y;
		}
		
		void showB()
		{
			cout<<"\nB = "<<b;
		}
};

class C: public B{
	public:
		int c;
		void getC(int z)
		{
			c= z;
		}
		
		void showC()
		{
			cout<<"\n C = "<<c;
		}
};

int main()
{
/*	A obj1;
	obj1.getA(45);
	obj1.showA();
	
	B obj2;
	obj2.getB(14);
	obj2.showB();	
*/	

	C b;
	int a,b1,c;
	cout<<"\nEnter A : ";
	cin>>a;
	cout<<"\nEnter B : ";
	cin>>b1;
	cout<<"\nEnter C : ";
	cin>>c;
	b.getA(a);
	b.getB(b1);
	b.getC(c);
	b.showA();
	b.showB();
	b.showC();

}