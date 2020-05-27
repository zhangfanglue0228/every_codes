/*

求最大岛屿的面积
假设矩阵由0，1组成，0代表海洋，1代表陆地。如果矩阵中的一个点与它周围（上下左右）点的值相同，
认为这两个点是连通的，值为1的点的连通区域形成岛屿，求一共有多少个岛屿，最大岛屿的面积是多少。
注：矩阵不一定是方阵

*/


#include <iostream>
#include <cstdio>
#include <queue>
using namespace std;
#define N 100
struct node
{
    int x,y;
}Node;
int n,m,a[N][N],result;
bool vis[N][N];
int dx[4]={0,0,1,-1};
int dy[4]={1,-1,0,0};
int judge(int x,int y)
{
    if(x>=n||x<0||y>=m||y<0)
        return 0;
    if(a[x][y]==0||vis[x][y])
        return 0;
    return 1;
}
void BFS(int x,int y)
{
    int num=1;
    queue<node> q;
    Node.x=x;
    Node.y=y;
    q.push(Node);
    vis[x][y]=1;
    while(!q.empty())
    {
        node top=q.front();     //取出队首元素
        q.pop();
        for(int i=0;i<4;i++)
        {
            int newX=top.x+dx[i];
            int newY=top.y+dy[i];
            if(judge(newX,newY))
            {
                num++;
                Node.x=newX;
                Node.y=newY;
                q.push(Node);
                vis[newX][newY]=1;
            }
        }
    }
    //cout<<num<<endl;
    result=max(result,num);
}
int main()
{
    cout<<"请输入矩阵的长和宽："<<endl;
    scanf("%d%d",&n,&m);
    cout<<"请输入矩阵信息："<<endl;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            scanf("%d",&a[i][j]);
        }
    }
    int ans=0;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            if(a[i][j]==1&&!vis[i][j])
            {
                ans++;
                BFS(i,j);
            }
        }
    }
    cout<<"总共有个"<<ans<<"岛屿"<<endl;
    cout<<"最大的岛屿的面积为"<<result<<endl;
    return 0;
}
