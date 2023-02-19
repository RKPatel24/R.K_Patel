#include<iostream>
using namespace std;

/*
	Constructor : It is a special method.
	
		Rules : 
				- Contructor name is same as the class-name,
				- No return-type in Constructor.
				- It is use to initialize the members of the class.
				
		Imp rule: -It is automatically called, when the object of 
					the class is created.
					
		There are 3 types of Contructors.
		
		1) Default Constructor/Parameterless Constructor
		
			syntax:
						class-name()
						{
							//piece of code
						}
			
		
		2) Parameterized Constructor
		
			syntax : 
			
					class-name(parameters......)
					{
						//piece of code
					}
		
		3) Copy Constructor	: Object as an Argument.
		
					class-name(const class-name &obj)
					{
						//piece of code
					}
			
		

*/

class Sample
{
	public:
		string name;
		int age;
		
		Sample()
		{
			cout<<"\nDefault Constructor Called.";
			string name = "tops";
			int age = 8;		
		}
	
		Sample(string n,int a)
		{
			cout<<"\nParameterized Constructor Called.";
			name = n;
			age = a;
		}
		
		Sample(const Sample &obj)
		{
			cout<<"\nCopy Constructor Called.";
			name = obj.name;
			age = obj.age;
		}
		
		void show()
		{
			cout<<"\nName  = "<<name;
			cout<<"\nAge  = "<<age;
		}
};


int main()
{
	Sample obj1; //Object Creation
	int age;
	string name;
	cout<<"\nEnter Name : ";
	getline(cin,name);
	cout<<"Enter Age : ";
	cin>>age;
	//Sample obj2("tops",5);
	Sample obj2(name,age);	
	obj2.show(); // Function Calling.
	Sample obj3(obj1);
	obj3.show();
	
	return 0;
}



