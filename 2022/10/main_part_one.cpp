//#include <sstream>
#include <string>
//#include <fstream>
#include <iostream>
#include <vector>
#include <set>

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

        if (xs.size() > 200)
        {
            std::cout << line << std::endl;
            std::cout << "xs.size() " << xs.size() << ", x " << x << std::endl;
        }

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

    IntVector vals = {20, 60, 100, 140, 180, 220}; 

    int answer = 0;

    for (auto val : vals)
    {
        std::cout << val << " * " << xs.at(val - 1) << " = " << val * xs.at(val - 1)<< std::endl;
        answer += val * xs.at(val - 1);
    }

    std::cout << "Answer : " << answer << std::endl;

    return 0;
}

