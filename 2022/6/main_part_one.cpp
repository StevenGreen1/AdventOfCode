#include <sstream>
#include <string>
#include <fstream>
#include <iostream>
#include <vector>
#include <set>

bool duplicates(std::vector<char> vec);

int main(int argc, char *argv[])
{
    std::string line;
    std::ifstream infile(argv[1]);
    int i = 4;

    while (std::getline(infile, line))
    {
        std::vector<char> values;
        values.push_back(line.at(0));
        values.push_back(line.at(1));
        values.push_back(line.at(2));
        values.push_back(line.at(3));

        bool check = duplicates(values);

        if (!duplicates(values))
            break;

        for (; i < line.size(); ++i)
        {
            values.push_back(line.at(i));
            values.erase(values.begin());

            for (auto j:values)
                std::cout << j << ", ";
            std::cout << std::endl;


            if (!duplicates(values))
                break;
        }
    }
    std::cout << "Number of chars " << i+1 << std::endl;
    return 0;
}

bool duplicates(std::vector<char> vec)
{
    std::set<char> s;
    for (int x: vec)
        s.insert(x);
    if (s.size() == vec.size())
        return false;

    return true;
}

