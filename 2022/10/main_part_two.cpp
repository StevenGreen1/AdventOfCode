//#include <sstream>
#include <string>
//#include <fstream>
#include <iostream>
#include <vector>
#include <set>
#include <math.h>

#include "../Helper.h"
//14720 too high
int main(int argc, char *argv[])
{
    std::string line;
    std::ifstream infile(argv[1]);

    IntVector xs;
    int x = 1;

    while (std::getline(infile, line))
    {
        std::string instruction = line.substr(0, 4);

        if (instruction == "noop")
        {
            xs.push_back(x);
        }
        else if (instruction == "addx")
        {
            xs.push_back(x);
            std::string number;
            for (int x = 5; x < line.size(); ++x)
            {
                if (isdigit(line.at(x)))
                    number += line.at(x);
            }
            int value = std::stoi(number);

            if (line.at(5) == '-')
                value *= -1;

            xs.push_back(x);
            x += value;
        }
    }

    IntMatrix data(6, IntVector(40, 0));

    for (int count = 0; count < xs.size(); ++count)
    {
        int spritePosition = xs.at(count);
        bool shouldDraw(std::abs(spritePosition-count%40) < 2);
        int row = floor(count/40);
        int col = count % 40;
        std::cout << row << " " << col << std::endl;
        data.at(row).at(col) = shouldDraw ? 1 : 0;
    }

    Helper::printMatrix(data, true);

    return 0;
}

