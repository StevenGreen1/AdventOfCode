#include <fstream>
#include <iostream>
#include <vector>
#include <map>
#include <set>

#include <string>
#include <vector>
#include <sstream>

#include "../Helper.h"

int main(int argc, char **argv)
{
    std::string filename = argv[1];
    std::ifstream file(filename);
    int count = 0;

    std::vector<std::vector<char>> data;

    for (int x = 0; x < 9; ++x)
    {
        std::vector<char> add;
        data.push_back(add);
    }

    if (file.is_open())
    {
        std::string line;
        for (int i = 0; i < 8; ++i)
        {
            std::getline(file, line);

            for (int j = 0; j < 9; ++j)
            {
//                std::cout << "Char " << line.at(4*j+1) << std::endl;
                if (isalpha(line.at(4*j+1)))
                {
//                    std::cout << "Adding" << std::endl;
                    data.at(j).push_back(line.at(4*j+1));
                }
            }
        }

        for (int i = 0; i < 9; ++i)
        {
            std::cout << "Start Vector " << i << std::endl;
            std::reverse(data.at(i).begin(), data.at(i).end());
            Helper::printVector(data.at(i));
        }

        // Junk lines
        std::getline(file, line);
        std::getline(file, line);

        while (std::getline(file, line))
        {
            try
            {
                //std::cout << "Line : " << line << std::endl;
                //move 1 from 4 to 8

                bool moveSet{false};
                bool fromSet{false};
                bool toSet{false};

                std::string moveStr;
                std::string fromStr;
                std::string toStr;

                for (int i = 5; i < line.size(); ++i)
                {
                    char entry = line.at(i);

                    if (isdigit(entry))
                    {
                        if (!moveSet)
                        {
                            moveStr += entry;
                        }
                        else if (!fromSet)
                        {
                            fromStr += entry;
                        }
                        else
                        {
                            toStr += entry;
                        }
                    }
                    else
                    {
                        if (!moveSet)
                        {
                            moveSet = true;
                            i += 5;
                        }
                        else if (!fromSet)
                        {
                            fromSet = true;
                            i += 3;
                        }
                    }
                }
                int move = std::stoi(moveStr);
                int from = std::stoi(fromStr) - 1;
                int to = std::stoi(toStr) - 1;
                //std::cout << "Move " << move << " from " << from << " to " << to << std::endl;
                std::vector<char> *fromVec = &data.at(from);
                std::vector<char> *toVec = &data.at(to);

                for (int x = 0; x < move; x++)
                {
                    char to_move = fromVec->back();
                    fromVec->pop_back();
                    toVec->push_back(to_move);
                }
            }
            catch (...)
            {
                std::cout << "Unexpected format" << std::endl;
            }
        }
        file.close();
    }

    for (int i = 0; i < 9; ++i)
    {
        std::cout << "End Vector " << i << std::endl;
        Helper::printVector(data.at(i));
    }

//    std::cout << "Total overlap " << count << std::endl;
}
