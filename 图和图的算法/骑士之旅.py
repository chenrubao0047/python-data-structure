# -*- coding:utf-8 -*- 
__author__ = 'John 2017/11/21 12:07'

from pythonds.graphs import Graph


def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            newPositions = genLegalMoves(row, col, bdSize)
            for e in newPositions:
                nid = posToNodeId(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeId, nid)
    return ktGraph


def posToNodeId(row, column, board_siza):
    return (row * board_siza) + column


def genLegalMoves(x, y, bdSize):
    newMoves = []
    moveOffsets = [
        (-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, -1), (2, 1)
    ]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, bdSize) and legalCoord(newY, bdSize):
            newMoves.append((newY, newY))
    return newMoves


def legalCoord(x, bdSize):
    # if 0 <= x < bdSize:
    #     return True
    # else:
    #     return False
    return 0 <= x < bdSize


print(legalCoord(100, 20))