# C++ Bellman Ford算法求最短路
#### 测试数据：
	1. 存在负环的数据
		4 6 1
		1 2 20
		1 3 5
		4 1 -200
		2 4 4
		4 2 4
		3 4 2
	2. 正确数据
		4 6 1
		1 2 2
		1 3 5
		4 1 10
		2 4 4
		4 2 4
		3 4 2
## 算法描述
[参考文档](blog.csdn.net/niushuai666/article/details/6791765)
1. 给定图G(V, E)（其中V、E分别为图G的顶点集与边集），源点s，数组Distant[i]记录从源点s到顶点i的路径长度，初始化数组Distant[n]为, Distant[s]为0；

2. 以下操作循环执行至多n-1次，n为顶点数：
    + 对于每一条边e(u, v)，如果Distant[u] + w(u, v) < Distant[v]，则另Distant[v] = Distant[u]+w(u, v)。w(u, v)为边e(u,v)的权值；
    + 若上述操作没有对Distant进行更新，说明最短路径已经查找完毕，或者部分点不可达，跳出循环。否则执行下次循环；

3. <font color=red>为了检测图中是否存在负环路，即权值之和小于0的环路。对于每一条边e(u, v)，如果存在Distant[u] + w(u, v) < Distant[v]的边，则图中存在负环路，即是说改图无法求出单源最短路径。否则数组Distant[n]中记录的就是源点s到各顶点的最短路径长度。</font>

4. Bellman-Ford算法寻找单源最短路径的时间复杂度为O(V*E).
