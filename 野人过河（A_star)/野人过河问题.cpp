#include <stdio.h>
#include <stdlib.h>
int M ,C, K;
struct NODE
{
    int m;                      //在左岸的传教士人数
    int c;                      //在左岸的野人人数
    int b;                      //b=1表示船在左岸,b=0表示船在右岸
    double g;                   //该节点的g值
    double f;                   //该节点的f值
    struct NODE *pFather;       //指向该节点的父节点
    struct NODE *pNext;         //在OPEN表或者CLOSED表中，指向下一个元素
};

struct NODE *Open = NULL;    //OPEN表
struct NODE *Closed = NULL;      //CLOSED表

int Equal(struct NODE *pNode1, struct NODE *pNode2)//判断两个节点所表示的状态是否相等
{
    if(pNode1->m == pNode2->m && pNode1->c == pNode2->c &&pNode1->b == pNode2->b)
        return 1;
    else
        return 0;
}

struct NODE *NewNode(int m, int c, int b)//动态产生一个节点，其状态值由参数m，c，b给定。
/**
m：河左岸的传教士人数
c：河左岸的野人人数
b：船是否在左岸，1：表示在左岸，0：表示不在左岸**/
{
    struct NODE *pNode = NULL;
    pNode =(struct NODE *) malloc(sizeof(struct NODE));
    if (pNode == NULL)
        return NULL;
    pNode->m = m;
    pNode->c = c;
    pNode->b = b;
    pNode->g = 0;
    pNode->f = 0;
    pNode->pFather = NULL;
    pNode->pNext = NULL;
    return pNode;
}

void FreeList(struct NODE *pList)//释放动态产生的链表
{
    struct NODE *pNode = NULL;
    while (pList)
    {
        pNode = pList;
        pList = pList->pNext;
        free(pNode);
    }
}

struct NODE *In(struct NODE *pNode, struct NODE *pList)//判断一个节点是否在一个链表
//当pNode在pList中时，返回以pNode为首的链表的后一部分，否则返回NULL
{
    if (pList == NULL)
        return NULL;
    if (Equal(pNode, pList))
        return pList;
    return
        In(pNode, pList->pNext);
}

struct NODE *Del(struct NODE *pNode, struct NODE *pList)
//从链表pList中删除节点pNode，返回值：删除给定节点后的链表
{
    if (pList == NULL)
        return NULL;
    if (Equal(pNode, pList))
        return pList->pNext;//相当于删除该节点
    pList->pNext = Del(pNode, pList->pNext);
    return pList;
}

struct NODE *AddToOpen(struct NODE *pNode, struct NODE *pOpen)
//将一个节点按照f值（从小到大）插入到OPEN表中，指向插入给定节点后OPEN表的指针
{
    if (pOpen == NULL)  //OPEN表为空
    {
        pNode -> pNext = NULL;
        return pNode;
    }
    if (pNode->f<pOpen->f)   //给定节点的f值小于OPEN表第一个节点的f值
    {
        pNode->pNext = pOpen;    //插入到OPEN的最前面
        return pNode;
    }
    pOpen->pNext = AddToOpen(pNode, pOpen->pNext);    //递归
    return pOpen;
}

struct NODE *AddToClosed(struct NODE *pNode, struct NODE *pClosed)
//将一个节点插入到CLOSED表中，返回值：指向插入给定节点后CLOSED表的指针
{
    pNode->pNext = pClosed;
    return pNode;
}

void PrintPath(struct NODE *pGoal)
//在屏幕上打印解路径。在搜索过程中，每个节点指向其父节点，从目标节点开始，逆向打印各节点既得到解路径
{
    if (pGoal == NULL)
        return;
    PrintPath(pGoal->pFather);   //递归
    printf("(%d %d %d)\n", pGoal->m, pGoal->c, pGoal->b);
}

int IsGrandFather(struct NODE *pNode, struct NODE *pFather)//判断一个节点是否与自己的祖父节点所表示的状态一样
{
    if (pFather == NULL)
        return 0;
    if (pFather->pFather == NULL)
        return 0;
    return
        Equal(pNode, pFather->pFather);
}

int IsGoal(struct NODE *pNode)//判断是否到达终点
{
    if (pNode->m == 0 && pNode->c == 0 && pNode->b == 0)
        return 1;
    else
        return 0;
}

int Safe(struct NODE *pNode)//判断一个状态是否为安全的
{
    if (pNode->m<0 || pNode->c<0 || pNode->m > M || pNode->c > C)
        return 0;
    if (pNode->m == M || pNode->m == 0)
        return 1;
    return !(pNode->m < pNode->c);
}

int H(struct NODE *pNode)//计算给定节点的h值，h = m + c - K*b
{
    return pNode->m + pNode->c - K*pNode->b;
}

struct NODE *A_Star(struct NODE *s)
//返回值：指向求解得到的目标节点的指针，或者返回NULL表示空间不够用或者找不到问题的解           *
{
    struct NODE *n = NULL, *m = NULL, *pNode = NULL;
    int i, j;
    Open = s;    //初始化OPEN表和CLOSED表
    Closed = NULL;
    while (Open)     //OPEN表不空
    {
        n = Open;    //取出OPEN表的第一个元素n
        if (IsGoal(n))
            return n; //如果n为目标节点，则成功结束
        Open = Open->pNext; //否则，从OPEN表中删除n
        Closed = AddToClosed(n, Closed);  //将n加入到CLOSED中
        // 以下两重循环，i表示上船的传教士人数，j表示上船的野人人数
        for (i = 0; i <= K; i++)
        {
            for (j = 0; j <= K; j++)
            {
                if (i + j == 0 ||  i + j > K || (i != 0 && i<j))//非法的上船组合  船不能为空 也不能超出容量 野人数量不能超过传教士
                    continue;
                if (n->b == 1)//当船在左岸时
                {
                    m = NewNode(n->m-i, n->c-j, 0);//产生下一个状态m
                    if(M-n->m+i<C-n->c+j&&(M-n->m+i))
                        continue;
                }
                else//当船在右岸时
                {
                    m = NewNode(n->m+i, n->c+j, 1);//产生下一个状态m
                    if(M-n->m-i<C-n->c-j&&(M-n->m-i))
                        continue;
                }
                if (IsGrandFather(m, n) || !Safe(m))
                    //如果m与他的祖父状态相同，或者是一个非法状态，则舍弃m
                {
                    free(m);
                    continue;
                }
                //当m是合法状态时
                m->pFather = n;  //标记其父节点为n
                m->g = n->g + 1;  //其g值为其父节点的g值加1
                m->f = m->g + H(m);  //计算其f值，f = g+h
                if (pNode = In(m, Open)) //如果m已经出现在OPEN表中
                {
                    if (m->f<pNode->f)   //如果m的f值小于OPEN表中相同状态的f值
                    {
                        //则将该f值大的节点从OPEN表中删除，并将m加入到OPEN表中。
                        Open = AddToOpen(m, Del(pNode, Open));
                        free(pNode);
                    }
                    else    //否则舍弃m
                    {
                        free(m);
                    }
                }
                else if (pNode = In(m, Closed))  //如果m已经出现在CLOSED中
                {
                    if (m->f<pNode->f)   //如果m的f值小于CLOSED表中相同状态的f值
                    {
                        //则将该节点从CLOSED表中删除，并重新添加到OPEN表中
                        Closed = Del(pNode, Closed);
                        Open = AddToOpen(m, Open);
                        free(pNode);
                    }
                    else    //否则舍弃m节点
                    {
                        free(m);
                    }
                }
                else    //其他情况，将m加入到OPEN表中
                {
                    Open = AddToOpen(m, Open);
                }
            }
        }
    }
    //如果OPEN表空了，还没有找到目标节点，则搜索以失败结束，
    //返回NULL
    return NULL;
}

int main()
{
    printf("输入传教士、野人、船的容量:");
    scanf("%d%d%d",&M,&C,&K);
    struct NODE *s;
    s = NewNode(M, C, 1);   //设置初始节点
    s = A_Star(s);  //A*搜索
    if (s)
        PrintPath(s);    //如果找到问题的解，则输出解路径
    else
        printf("找不到问题的解!\n");
    FreeList(Open);  //释放动态节点
    FreeList(Closed);
}
