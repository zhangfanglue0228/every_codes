/*

Bellman_Ford算法求最短路

测试数据：
	（1）(存在负环的数据)
		4 6 1
		1 2 20
		1 3 5
		4 1 -200
		2 4 4
		4 2 4
		3 4 2
	（2）(正确数据)
		4 6 1
		1 2 2
		1 3 5
		4 1 10
		2 4 4
		4 2 4
		3 4 2

*/

#include <iostream>
#include <cstdio>
using namespace std;

#define MAX 0x3f3f3f3f
#define N 1010
int nodenum, edgenum, original; //点数，边数，起点

typedef struct Edge //边
{
	int u, v;
	int cost;
} Edge;

bool Bellman_Ford();

Edge edge[N];
int dis[N], pre[N];

int main()
{
	cout << "输入图的点数、边数和起点："<< endl;
	while (scanf_s("%d%d%d", &nodenum, &edgenum, &original) != EOF)
	{
		pre[original] = original;
		cout << "按顺序输入边的起点、边的终点和边的权值（共" << edgenum << "组）" << endl;
		for (int i = 1; i <= edgenum; ++i)
		{
			scanf_s("%d%d%d", &edge[i].u, &edge[i].v, &edge[i].cost);
		}
		cout << endl;
		if (Bellman_Ford())
			for (int i = 1; i <= nodenum; ++i) //每个点最短路
				cout << "起点到" << i << "号点的最短路径长为" << dis[i] << endl << endl;
		else
			cout << "该图存在负环，请重新输入数据" << endl << endl;
		cout << endl << endl << "输入图的点数、边数和起点：" << endl;
	}
	return 0;
}

bool Bellman_Ford()
{
	for (int i = 1; i <= nodenum; ++i) //初始化
		dis[i] = (i == original ? 0 : MAX);
	for (int i = 1; i <= nodenum - 1; ++i)
		for (int j = 1; j <= edgenum; ++j)
			if (dis[edge[j].v] > dis[edge[j].u] + edge[j].cost) //松弛：如果起点到u点的距离+u点到v点的距离<起点到v点的距离，则dis[v]更新
			{
				dis[edge[j].v] = dis[edge[j].u] + edge[j].cost;
				pre[edge[j].v] = edge[j].u;
			}
	//判断是否含有负权回路
	for (int i = 1; i <= edgenum; ++i)
		if (dis[edge[i].v] > dis[edge[i].u] + edge[i].cost) //存在路比最小路径更短则为存在负环
			return 0;
	return 1;
}