#include<stdio.h>
int main()
{
	int n,c=0,c1=0,i;
	scanf("%d",&n);
	for (i=0;i<=n;i++)
	{
		if (i%2==0)
		{
			c=c+i;
		}
		else
		{
			c1=c1+i;
		}
	}
printf("Sum of even Numbers is %d\n",c);
printf("Sum of odd Numbers is %d",c1);
}
