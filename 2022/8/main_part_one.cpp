#include <sstream>
#include <string>
#include <fstream>
#include <iostream>
#include <vector>
#include <set>

#include "../Helper.h"

// 1437 too low

bool isTreeVisible(int row, int col, IntMatrix trees, int maxRow, int maxCol)
{
    if (row == 0 ||
            col == 0 ||
            row == maxRow-1 ||
            col == maxCol-1)
        return true;

    // Look up
    bool visibleUp = true;
    for (int x = row + 1; x < maxRow; ++x)
    {
        if (trees[x][col] >= trees[row][col])
        {
            visibleUp = false;
            break;
        }
    }

    if (visibleUp)
    {
        //std::cout << trees[row][col] << " : " << row << ", " << col << " is visible down" << std::endl;
        return true;
    }

    bool visibleDown = true;
    for (int x = row - 1; x >= 0; --x)
    {
        if (trees[x][col] >= trees[row][col])
        {
            visibleDown = false;
            break;
        }
    }

    if (visibleDown)
    {
        //std::cout << trees[row][col] << " : " << row << ", " << col << " is visible up" << std::endl;
        return true;
    }

    bool visibleRight = true;
    for (int x = col + 1; x < maxCol; ++x)
    {
        if (trees[row][x] >= trees[row][col])
        {
            visibleRight = false;
            break;
        }
    }

    if (visibleRight)
    {
        //std::cout << trees[row][col] << " : " << row << ", " << col << " is visible right" << std::endl;
        return true;
    }

    bool visibleLeft = true;
    for (int x = col - 1; x >= 0; --x)
    {
        if (trees[row][x] >= trees[row][col])
        {
            visibleLeft = false;
            break;
        }
    }

    if (visibleLeft)
    {
        //std::cout << trees[row][col] << " : " << row << ", " << col << " is visible left" << std::endl;
        return true;
    }

    //std::cout << trees[row][col] << " : " << row << ", " << col << " is not visible" << std::endl;
    return false;
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
    int count = 0;

    for (int row = 0; row < maxRow; ++row)
    {
        for (int col = 0; col < maxCol; ++col)
        {
            if (isTreeVisible(row, col, trees, maxRow, maxCol))
            {
                std::cout << "\033[1;32m" << trees[row][col] << " \033[0m";
                count++;
            }
            else
            {
                std::cout << "\033[1;31m" << trees[row][col] << " \033[0m";
            }
        }
        std::cout << std::endl;
    }

    std::cout << count << std::endl;
    std::cout << maxRow << " " << maxCol << std::endl;
    return 0;
}

