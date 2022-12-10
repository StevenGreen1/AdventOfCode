#include <sstream>
#include <string>
#include <fstream>
#include <iostream>
#include <vector>
#include <set>

#include "../Helper.h"

// 1437 too low

int treeScore(int row, int col, IntMatrix trees, int maxRow, int maxCol)
{
    // Look up
    int visibleUp = 0;
    for (int x = row + 1; x < maxRow; ++x)
    {
        ++visibleUp;
        if (trees[x][col] >= trees[row][col])
        {
            break;
        }
    }

    int visibleDown = 0;
    for (int x = row - 1; x >= 0; --x)
    {
        ++visibleDown;
        if (trees[x][col] >= trees[row][col])
        {
            break;
        }
    }

    int visibleRight = 0;
    for (int x = col + 1; x < maxCol; ++x)
    {
        ++visibleRight;
        if (trees[row][x] >= trees[row][col])
        {
            break;
        }
    }

    int visibleLeft = 0;
    for (int x = col - 1; x >= 0; --x)
    {
        ++visibleLeft;
        if (trees[row][x] >= trees[row][col])
        {
            break;
        }
    }

    return visibleUp * visibleDown * visibleRight * visibleLeft;
}

int main(int argc, char *argv[])
{
    std::string line;
    std::ifstream infile(argv[1]);

    IntMatrix trees;

    while (std::getline(infile, line))
    {
        IntVector row;
        for (char height : line)
        {
//            std::cout << height << std::endl;
            row.push_back(height-48);
        }
        trees.push_back(row);
    }

//    for (auto x : trees)
//        Helper::printVector(x);

    int maxRow = trees.size();
    int maxCol = trees.at(0).size();
    int max_score = 0;

    for (int row = 0; row < maxRow; ++row)
    {
        for (int col = 0; col < maxCol; ++col)
        {
            int score = treeScore(row, col, trees, maxRow, maxCol);
            max_score = std::max(max_score, score);
        }
    }

    std::cout << max_score << std::endl;
    return 0;
}

