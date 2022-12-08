#include <fstream>
#include <iostream>
#include <vector>
#include <map>
#include <set>

#include <string>
#include <vector>
#include <sstream>

void printVector(std::vector<char> vec)
{
    for (int i = 0; i < vec.size(); i++)
        std::cout << vec[i] << " ";
    std::cout << std::endl;
}

std::vector<char> commonElements(std::vector<char> vec1, std::vector<char> vec2)
{
    std::vector<char> result;
    std::vector<char> v(vec1.size() + vec2.size());
    std::vector<char>::iterator it, st;

    sort(vec1.begin(), vec1.end());
    sort(vec2.begin(), vec2.end());

    it = set_intersection(vec1.begin(),
          vec1.end(),
          vec2.begin(),
          vec2.end(),
          v.begin());

    for (st = v.begin(); st != it; ++st)
        result.push_back(*st);

    return result;
}

int main(int argc, char **argv)
{
    std::string filename = argv[1];
    std::ifstream file(filename);
    int count = 0;

    if (file.is_open())
    {
        std::string line;
        while (std::getline(file, line))
        {
            try
            {
                //std::cout << "Line : " << line << std::endl;

                std::string one, two, three, four;
                std::string *current = &one;
                bool setTwo{true};
                bool setThree{true};
                bool setFour{true};

                for (int l = 0; l < line.size(); ++l)
                {
                    char entry = line.at(l);
                    if (isdigit(entry))
                    {
                        *current += entry;
                    }
                    else
                    {
                        if (setTwo)
                        {
                            current = &two;
                            setTwo = false;
                        }
                        else if (setThree)
                        {
                            current = &three;
                            setThree = false;
                        }
                        else if (setFour)
                        {
                            current = &four;
                            setFour = false;
                        }
                    }
                }

                //if (std::stoi(one) <= std::stoi(four) && std::stoi(two) >= std::stoi(three)) Overlap
                if (std::stoi(one) <= std::stoi(three) && std::stoi(two) >= std::stoi(four))
                {
                    count++;
                    //std::cout << "1 contains 2" << std::endl;
                }
                else if (std::stoi(three) <= std::stoi(one) && std::stoi(four) >= std::stoi(two))
                {
                    count++;
                    //std::cout << "2 contains 1" << std::endl;
                }

                //std::cout << one << ", " << two << ", " << three << ", " << four << std::endl;
            }
            catch (...)
            {
                std::cout << "Unexpected format" << std::endl;
            }
        }
        file.close();
    }

    std::cout << "Total overlap " << count << std::endl;
}
