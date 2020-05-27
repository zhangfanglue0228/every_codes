#include <iostream>
#include <map>
#include <queue>

using namespace std;

struct node
{
    /*
	   a：到该状态的过程
	   s：该状态的矩阵形式
	   x，y：该状态0的位置
	*/
    string a;
    int s[3][3];
    int x, y;
} p, q; // p代表排好序的最终状态 q代表可能的状态

map<int, int> u; // 改状态是否出现
map<int, string> v;
string Goal;

int r[4][2] = {0, 1, 0, -1, 1, 0, -1, 0};

void bfs(int goal)
{
    int x0, y0;
    queue<node> Q;
    int i, j, k = 0;

    q.a = p.a = "";

    /* 将目标状态保存到p */
    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            p.s[i][j] = Goal[i * 3 + j] - '0';
            if (p.s[i][j] == 0)
                x0 = i, y0 = j;
        }
    }

    p.s[x0][y0] = 0, p.x = x0, p.y = y0; // 设置目标状态结构体参数，3x3矩阵中加入0，并记录0的位置
    Q.push(p);                           //将目标状态加入队列Q
    u[goal] = 1;                         // 标记目标状态已出现
    while (!Q.empty())
    {
        p = Q.front();
        Q.pop(); // p为队列Q的第一个，并将Q的第一个元素删除
        for (i = 0; i < 4; i++)
        {
            q.x = p.x + r[i][0], q.y = p.y + r[i][1];       // 通过方向属组更新上一状态移动后0的位置
            if (q.x < 0 || q.x >= 3 || q.y < 0 || q.y >= 3) // 0的位置违法，跳过此方向的检测
                continue;
            /* 复制前状态结构体的矩阵到后状态结构体的矩阵*/
            for (j = 0; j < 3; j++)
                for (k = 0; k < 3; k++)
                    q.s[j][k] = p.s[j][k];
            swap(q.s[p.x][p.y], q.s[q.x][q.y]); // 更新 后状态矩阵中0的位置
            int sum = 1;
            /* 将矩阵转化为int型，保存至sum*/
            for (j = 0; j < 3; j++)
                for (k = 0; k < 3; k++)
                    sum = sum * 10 + q.s[j][k];
            if (u[sum] == 1) // 当前状态已出现，即在map u中标记为1
                continue;
            u[sum] = 1; //当前状态未出现，则将map u中标记记为1

            /* 更新结构体中记录变化过程的字符串 */
            if (i == 0)
                q.a = p.a + 'l';
            else if (i == 1)
                q.a = p.a + 'r';
            else if (i == 2)
                q.a = p.a + 'u';
            else if (i == 3)
                q.a = p.a + 'd';
            Q.push(q);
            v[sum] = q.a;
        }
    }
}
int main()
{
    int goal; //目标状态
    string initial;
    while (1)
    {
        /* 初始化map u，v */
        u.clear();
        v.clear();
        /* 请求用户输入初始状态和目标状态 */
        cout << "Please enter goal status!" << endl;
        cin >> Goal;
        goal = atoi(Goal.c_str());
        bfs(goal);
        cout << "Please enter the initial state!" << endl;
        cin >> initial;
        if (initial == Goal)
            cout << "The two states are the same!" << endl;
        else
        {

            int l = initial.length(), i, sum = 1;
            for (i = 0; i < l; i++)
                sum = sum * 10 + initial[i] - '0';
            if (u[sum] == 0)
                printf("unsolvable\n");
            else
            {
                string st = v[sum];
                for (i = st.length() - 1; i >= 0; i--)
                    printf("%c", st[i]);
                printf("\n");
            }
        }
    }
    return 0;
}
