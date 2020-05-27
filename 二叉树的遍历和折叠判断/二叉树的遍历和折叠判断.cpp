#include <iostream>

#include <queue>

#include <vector>

using namespace std;
typedef struct BiTNode
{
	char data;
	struct BiTNode* lchild, * rchild;
}BiTNode, * BirTree;

BirTree CreatBitTree();
void PreOrderTraverse(BirTree T);
void InOrderTraverse(BirTree T);
void PostOrderTraverse(BirTree T);
void FloorOrderTraverse(BirTree T);
bool isMirror(BirTree T1,BirTree T2);
void ZigzaglevelOrder(BirTree T);

int main()
{
	BirTree T;
	cout << "请输入二叉树数据（A、B、C...），用#代替虚节点：" << endl;
	T = CreatBitTree();
	cout << "先序遍历：" << endl;
	PreOrderTraverse(T);
	cout << endl;
	cout << "中序遍历：" << endl;
	InOrderTraverse(T);
	cout << endl;
	cout << "后序遍历：" << endl;
	PostOrderTraverse(T);
	cout << endl;
	cout << "层序遍历：" << endl;
	FloorOrderTraverse(T);
	cout << endl;
    if(isMirror(T,T))
        cout<<"该二叉树可折叠"<<endl;
    else
        cout<<"该二叉树不可折叠"<<endl;
    cout << "Zigzag遍历：" << endl;
    ZigzaglevelOrder(T);
	return 0;
}

//建立二叉树

BirTree CreatBitTree()
{
	char ch;
	cin >> ch;
	BirTree T;
	if (ch == '#')
		T = NULL;
	else
	{
		T = (BirTree)malloc(sizeof(BirTree));
		T->data = ch;
		T->lchild = CreatBitTree();
		T->rchild = CreatBitTree();
	}
	return T;
}
//前序遍历

void PreOrderTraverse(BirTree T)
{
	if (T == NULL)return;
	cout << T->data;
	PreOrderTraverse(T->lchild);
	PreOrderTraverse(T->rchild);
}
//中序遍历

void InOrderTraverse(BirTree T)
{
	if (T == NULL)return;
	InOrderTraverse(T->lchild);
	cout << T->data;
	InOrderTraverse(T->rchild);
}
//后序遍历

void PostOrderTraverse(BirTree T)
{
	if (T == NULL)return;
	PostOrderTraverse(T->lchild);
	PostOrderTraverse(T->rchild);
	cout << T->data;
}
//层序遍历

void FloorOrderTraverse(BirTree T)
{
	queue<BirTree> s;
	s.push(T);
	BirTree p;
	while (!s.empty())
	{
		p = s.front();
		cout << p->data;
		s.pop();
		if (p->lchild)
		{
			s.push(p->lchild);
		}
		if (p->rchild)
		{
			s.push(p->rchild);
		}
	}
}
void ZigzaglevelOrder(BirTree T)
{
    if (T == NULL)return;
    vector<vector<char>> result;
    queue<BirTree> que;
    bool LefttoRight=true;
    que.push(T);

    while(!que.empty())
    {
        int size=que.size();
        vector<char> low(size);
        for(int i=0;i<size;i++)
        {
            T=que.front();
            que.pop();
            int index=LefttoRight?i:size-i-1;
            low[index]=T->data;
            if(T->lchild)
                que.push(T->lchild);
            if(T->rchild)
                que.push(T->rchild);
        }
        LefttoRight=!LefttoRight;
        result.push_back(low);
    }
    for(int i=0;i<result.size();i++)
    {
        for(int j=0;j<result[i].size();j++)
            cout<<result[i][j];
    }
    cout<<endl;
}
//判断是不是可折叠(镜像

bool isMirror(BirTree T1,BirTree T2)
{
    if(T1==NULL&&T2==NULL)
        return true;
    if(T1==NULL||T2==NULL)
        return false;
    return ((T1)->data == (T2)->data) && (isMirror((T1)->rchild, (T2)->lchild)) && (isMirror((T1)->lchild, (T2)->rchild));
}

/*			a

		b		c

	#		d#		e

*/



//ab#d##c#e##
