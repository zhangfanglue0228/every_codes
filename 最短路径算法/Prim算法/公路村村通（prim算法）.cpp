/*

公路村村通
现有村落间道路的统计数据表中，列出了有可能建设成标准公路的若干条道路的成本，
求使每个村落都有公路连通所需要的最低成本。
输入格式:
        输入数据包括城镇数目正整数N（≤1000）和候选道路数目M（≤3N）；随后的M行对应M
        条道路，每行给出3个正整数，分别是该条道路直接连通的两个城镇的编号以及该道路
        改建的预算成本。为简单起见，城镇从1到N编号。
输出格式:
        输出村村通需要的最低成本。如果输入数据不足以保证畅通，则输出−1，表示需要建设
        更多公路。
输入样例:
        6 1 5
        1 2 5
        1 3 3
        1 4 7
        1 5 4
        1 6 2
        2 3 4
        2 4 6
        2 5 2
        2 6 6
        3 4 6
        3 5 1
        3 6 1
        4 5 10
        4 6 8
        5 6 3
输出样例：
        12

*/


#include <cstdio>
#include <iostream>
using namespace std;
#define inf 0x3f3f3f
#define N 1000
int Graph[N][N];
int n,m,lowcost[N];
int prim()
{
    int k,cnt=1,sum=0,minn;
    for(int i=1;i<=n;i++)
        lowcost[i]=Graph[1][i];
    lowcost[1]=0;
    for(int i=1;i<=n;i++)
    {
        k=0,minn=inf;
        for(int j=1;j<=n;j++)
        {
            if(lowcost[j]!=0&&lowcost[j]<minn)
            {
                minn=lowcost[j];
                k=j;
            }
        }
        if(k==0)
            break;
        sum+=lowcost[k];
        lowcost[k]=0;
        for(int j=1;j<=n;j++)
            if(lowcost[j]>Graph[k][j])
                lowcost[j]=Graph[k][j];
        cnt++;
    }
    if(cnt!=n)
        return -1;
    else
        return sum;
}
int main()
{
    int x,y,w;
    cin>>n>>m;
    for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)
            Graph[i][j]=inf;
    while(m--)
    {
        cin>>x>>y>>w;
        Graph[x][y]=Graph[y][x]=w;
    }
    printf("%d\n",prim());
    return 0;
}
