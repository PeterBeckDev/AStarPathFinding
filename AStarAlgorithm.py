from tkinter import *
import time
import random

def createMaze(width, height):
    start = [0,0]
    mazeArr = []
    for i in range(height):
        tempArr = []
        for j in range(width):
            tempArr.append(['1111',0])
        mazeArr.append(tempArr)
    genPattern(start,mazeArr)
    return mazeArr

def randSqr(coord,maze):
    choiceList=[[0,1],[0,-1],[1,0],[-1,0]]
    newVert = [0,0]
    while True:
        ranDir = random.choice(choiceList)
        newVert[0],newVert[1] = coord[0] + ranDir[0], coord[1] + ranDir[1]
        if newVert[0] < 0 or newVert[0] >= len(maze[0]) or newVert[1] < 0 or newVert[1] > len(maze)-1:
            choiceList.remove(ranDir)
        elif maze[newVert[1]][newVert[0]][1] == 1:
            choiceList.remove(ranDir)
        elif maze[newVert[1]][newVert[0]][1] == 0:
            return newVert
        if len(choiceList) == 0:
            return None
        
    return newVert
def connectVert(vert1,vert2,maze):
    temp1 = list(maze[vert1[1]][vert1[0]][0])
    temp2 = list(maze[vert2[1]][vert2[0]][0])    
    if vert1[0]-vert2[0] == 1 :#up
        temp1[0] = '0'
        temp2[2] = '0'
    if vert1[0]-vert2[0] == -1 :#down
        temp1[2] = '0'
        temp2[0] = '0'
    if vert1[1]-vert2[1] == 1 :#left
        temp1[3] = '0'
        temp2[1] = '0'
    if vert1[1]-vert2[1] == -1 :#right
        temp1[1] = '0'
        temp2[3] = '0'
    maze[vert1[1]][vert1[0]][0] = "".join(temp1)
    maze[vert2[1]][vert2[0]][0] = "".join(temp2)
    
def genPattern(coord,maze):
    maze[coord[1]][coord[0]][1] = 1
    newVert = randSqr(coord,maze)
    while newVert != None:
        connectVert(coord,newVert,maze)
        genPattern(newVert,maze)
        newVert = randSqr(coord,maze)
        
    
    
def AstarList(maze):
    starList = []
    for i in range(0,len(maze)):
        tempList = []
        for j in range(0,len(maze[i])):
            tempList.append([-1,i+j])
        starList.append(tempList)
    return starList

def ColourMaze(maze):
    cList = []
    for i in range(0,len(maze)):
        tempList = []
        for j in range(0,len(maze[i])):
            tempList.append(0)
        cList.append(tempList)
    return cList

def TileMaze(dr):
    iw,ih,ix,iy = 0,0,0,0
    if int(dr[0]) == 0 :
        ih += 1
        iy -= 1
    if int(dr[2]) == 0 :
        ih += 1
    if int(dr[1]) == 0 :
        iw += 1
    if int(dr[3]) == 0 :
        iw += 1
        ix -= 1
    return ix,iy,iw,ih

def RenderMaze(mazeMatrix,cMaze):
    for i in range(0,len(mazeMatrix)):
        for j in range(0,len(mazeMatrix[i])):
            if cMaze[j][i] == 1:
                col = "green"
            elif cMaze[j][i] == 2:
                col = "yellow"
            else:
                col = "white"
            ix,iy,iw,ih = TileMaze(mazeMatrix[j][i][0])
            box = Frame(frame, width = boxW - gridWid + iw*gridWid, height=boxH - gridWid + ih*gridWid,bg =col, bd=0)
            box.pack()
            box.place(x = gridWid + boxW * j + ix * gridWid, y = gridWid + boxH * i + iy * gridWid)

def h(coord,ASmaze):
    return ASmaze[coord[1]][coord[0]][1]
def g(coord,ASmaze):
    return ASmaze[coord[1]][coord[0]][0]

def walkable(vert1,vert2,maze):
    if vert1[0]-vert2[0] == 1:#check north
        if maze[vert1[1]][vert1[0]][0][0] == '0':
            return True
    if vert1[0]-vert2[0] == -1:#check south
        if maze[vert1[1]][vert1[0]][0][2] == '0':
            return True
    if vert1[1]-vert2[1] == 1:#check west
        if maze[vert1[1]][vert1[0]][0][3] == '0':
            return True
    if vert1[1]-vert2[1] == -1:#check east
        if maze[vert1[1]][vert1[0]][0][1] == '0':
            return True
    return False


def starStep(maze,ASmaze,cMaze):
    start = [len(maze[0])-1,len(maze)-1]
    if ASmaze[start[1]][start[0]][0] == -1:
        ASmaze[start[1]][start[0]][0] = 0
    openNodes = []
    closedNodes = []
    parents = []

    openNodes.append(start)

    while len(openNodes) != 0:
        curr = openNodes[0]
        curIndex = 0
        

        for i in openNodes:
            if (g(i,ASmaze)+1+h(i,ASmaze)) < (g(curr,ASmaze)+1+h(curr,ASmaze)):
                curr = i
                curIndex = openNodes.index(i)
        cMaze[curr[1]][curr[0]] = 2
        print("current = " + str(curr))
        openNodes.pop(curIndex)
        closedNodes.append(curr)
        
        if curr == [0,0]:
            while (curr != start):
                cMaze[curr[1]][curr[0]] = 1
                for i in parents:
                    if i[0] == curr:
                        curr = i[1]
            cMaze[curr[1]][curr[0]] = 1
            RenderMaze(maze,cMaze)
            return None

        children = []

        for i in [[1,0],[-1,0],[0,1],[0,-1]]:
            if not (curr[0]+i[0] < 0 or curr[0]+i[0] > len(maze)-1 or curr[1]+i[1] < 0 or curr[1]+i[1] > len(maze)-1):
                newPos=[curr[0]+i[0],curr[1]+i[1]]
                if walkable(curr,newPos,maze):
                    children.append(newPos)

        print("childs: " + str(children))
        for i in children:
            if (i in closedNodes):
                continue
                
                

            for j in openNodes:
                if (i == j):
                    if g(i,ASmaze) > g(j,ASmaze):
                        ASmaze[j[1]][j[0]][0] = g(curr,ASmaze) + 1
                        continue
            openNodes.append(i)
            parents.append([i,curr])            
                
            
                
        
####################################
    
root = Tk()
frame = Frame(root, width = 1920, height = 1080)
frame.pack()

labels = []


boxW = 40
boxH = 40
gridWid = 7

boxFrame = Frame(frame, width = 1600 + gridWid, height= 1600 + gridWid ,bg ="black", bd=0)
boxFrame.pack()

newMaze = createMaze(25,25)
starStep(newMaze,AstarList(newMaze),ColourMaze(newMaze))
        
        
