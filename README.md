# AStarPathFinding
Project about generating mazes and finding the quickest path using the a* algorithm. Coded in A levels to improve my understanding of algorithms for my Computer Science exams.

For the maze generation I used a randomized Depth First Search. In the code this is the recursive function genPattern(coord,maze).

![alt text](https://github.com/PeterBeckDev/AStarPathFinding/blob/2af8f493d411792808ecb60f1a13f2b52dd8375a/MazeGeneration.png)


This image shows the A* algorithm pathfinding, they yellow squares are all the squares that were checked and the green squares are the shortest solution.

![alt text](https://github.com/PeterBeckDev/AStarPathFinding/blob/bad96ed303ceb93ce01e0a1ce78e2b07c999e114/SmallMazePath.png)

This bigger maze shows not all of the tiles need to be checked in order to find the shortest path as the white boxes are unvisited nodes.


![alt text](https://github.com/PeterBeckDev/AStarPathFinding/blob/2af8f493d411792808ecb60f1a13f2b52dd8375a/BigMazePath.png)
