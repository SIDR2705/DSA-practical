#include <bits/stdc++.h>
using namespace std;

int sum(int frequency[], int i, int j)
{
	int sum=0;
	for(int x = i ;x <= j;x++)
		sum += frequency[x];
	return sum;

}

int optimalcost(int frequency[], int i, int j)
{
	if(j<i)
		return 0;
	if(j==i)
		return frequency[i];

	int frequencySum=sum(frequency,i,j);

	int min= INT_MAX;

	for (int r=i;r<=j;++r)
	{
	int cost= optimalcost(frequency,i,r-1)+optimalcost(frequency,r+1,j);

	if(cost<min)
		cost=min;
	}

	return min+frequencySum;
}

int optimalsearchtree(int keys[], int frequency[], int n)
{
	return optimalcost(frequency, 0, n-1);
}

int main()
{
	int keys[]={44, 66, 34};
	int frequency[]={64 , 58, 66};
	int n= sizeof(keys)/sizeof(keys[0]);

	cout<<"The optimal cost of tree is : "<<optimalsearchtree(keys, frequency, n);
	return 0;
}
