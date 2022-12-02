// Prims

#include <iostream>
#define INFINITY 9999
using namespace std;


int main() {
	int n;

	cout << "\nEnter the number of offices: ";
	cin >> n;

	char *vertices = new char[n];
	int graph[n][n];

	for (int i = 0; i < n; i++) 
	{
		for (int j = 0; j < n; j++) 
		{
			graph[i][j] = INFINITY;
		}
	}

	for (int i = 0; i < n; i++)
	{
		vertices[i] = 65 + i;
	}

	for (int i = 0; i < n; i++) {
		for (int j = i+1; j < n; j++) 
		{
			cout << "\nCost of line between office " << vertices[i] << " and office " << vertices[j] << ": ";

			int cost;
			cin >> cost;

			if(i==j)
			{
			cost=0;
			graph[i][j]=0;
			graph[j][i]=0;
			continue;
			}

			if (cost > 0)
			{
				graph[i][j] = cost;
				graph[j][i] = cost;
			}
		}
	}
	cout << endl;


	for (int i = 0; i < n; i++) 
	{
		for (int j = i+1; j < n; j++)
		{
			cout << graph[i][j] << "	";
		}
		cout << "\n";
	}

	int selected[n];
	int min, a, b;
	int current = 0, total = 0;
	for (int i = 0; i < n; i++)
		selected[i] = 0;

	cout << "\nEnter starting office ";
	for (int i = 0; i < n; i++) 
	{
		cout << vertices[i] << " ";
	}
	cout << ": ";
	char c;
	cin >> c;
	for (int i = 0; i < n; i++)
		if(vertices[i] == c)
			selected[i] = 1;

	while (current < n - 1) {
		min = INFINITY;
		for (int i = 0; i < n; i++) 
		{
			if (selected[i] == 1)
			{
				for (int j = 0; j < n; j++)
				{
					if (selected[j] == 0) 
					{
						if (min > graph[i][j])
						{
							min = graph[i][j];
							a = i;
							b = j;
						}
					}
				}
			}
		}
		selected[b] = 1;
		cout << "\n" << vertices[a] << " -> " << vertices[b];
		total += min;
		current++;
	}
	cout << "\nTotal Cost: " << total << endl;
	return 0;
}