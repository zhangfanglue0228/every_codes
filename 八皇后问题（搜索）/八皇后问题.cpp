//八皇后问题 问题描述：在8×8格的国际象棋上摆放八个皇后，使其不能互相攻击，即任意两个皇后都不能处于同一行、同一列或同一斜线上，请列出所有摆法。要求使用栈实现。
#include <iostream>

using namespace std;
#define StackSize 8 //最多放8个皇后

int queen[StackSize][StackSize] = { 0 }; /*棋盘*/
int ans = 0, top = -1, datas[8];//date存储皇后位置

void Push(int x)//入栈

{
	top++;
	datas[top] = x;
}
void Pop() { top--; }//出栈

//判断合法性

bool Judgement()
{
	for (int i = 0; i < top; i++)//依次检查前面各行的皇后位置

		if (datas[top] == datas[i] || (abs(datas[top] - datas[i])) == (top - i))    //判断是否在同一列同一斜线

			return 0;                                            
	return 1;                                                    
}
void Output()
{
	cout << "第" << ans << "情况:" << endl;
	for (int i = 0; i < StackSize; i++)
	{
		for (int j = 0; j < datas[i]; j++)
			cout << "█";
		cout << "QQ";
		for (int j = StackSize - 1; j > datas[i]; j--)
			cout << "█";
		cout << endl;
	}
	cout << endl;
}
void solve(int row) //在栈顶放置符合条件的值的操作,即摆放皇后

{
	for (int i = 0; i < StackSize; i++)
	{
		Push(i);
		if (Judgement())//判断是否符号条件

		{
			if (row < StackSize - 1)//若还没有第八个皇后，则下一个

				solve(row + 1);
			else
			{
				ans++;//解数加1

				Output();//打印成功的棋盘

			}
		}
		Pop();//若不符合条件则出栈

	}
}


int main()
{
	solve(0);                                        //从栈底开始赋值

	cout << "总共有" << ans << "情况" << endl;
	return 0;
}
