#include <fstream>
#include <iostream>
#include <vector>
#include <map>
#include <set>

void printVector(std::vector<char> vec)
{
    for (int i = 0; i < vec.size(); i++)
        std::cout << vec[i] << " ";
    std::cout << std::endl;
}

int main(int argc, char **argv)
{
    std::string filename = argv[1];
    std::ifstream file(filename);

    std::map<char, int> mapper;
    mapper['a'] = 1;
    mapper['b'] = 2;
    mapper['c'] = 3;
    mapper['d'] = 4;
    mapper['e'] = 5;
    mapper['f'] = 6;
    mapper['g'] = 7;
    mapper['h'] = 8;
    mapper['i'] = 9;
    mapper['j'] = 10;
    mapper['k'] = 11;
    mapper['l'] = 12;
    mapper['m'] = 13;
    mapper['n'] = 14;
    mapper['o'] = 15;
    mapper['p'] = 16;
    mapper['q'] = 17;
    mapper['r'] = 18;
    mapper['s'] = 19;
    mapper['t'] = 20;
    mapper['u'] = 21;
    mapper['v'] = 22;
    mapper['w'] = 23;
    mapper['x'] = 24;
    mapper['y'] = 25;
    mapper['z'] = 26;
    mapper['A'] = 27;
    mapper['B'] = 28;
    mapper['C'] = 29;
    mapper['D'] = 30;
    mapper['E'] = 31;
    mapper['F'] = 32;
    mapper['G'] = 33;
    mapper['H'] = 34;
    mapper['I'] = 35;
    mapper['J'] = 36;
    mapper['K'] = 37;
    mapper['L'] = 38;
    mapper['M'] = 39;
    mapper['N'] = 40;
    mapper['O'] = 41;
    mapper['P'] = 42;
    mapper['Q'] = 43;
    mapper['R'] = 44;
    mapper['S'] = 45;
    mapper['T'] = 46;
    mapper['U'] = 47;
    mapper['V'] = 48;
    mapper['W'] = 49;
    mapper['X'] = 50;
    mapper['Y'] = 51;
    mapper['Z'] = 52;

    int score = 0;

    if (file.is_open())
    {
        std::string line;
        while (std::getline(file, line))
        {
            try
            {
                std::vector<char> comp1;
                std::vector<char> comp2;
                std::set<char> to_add;

                int length = line.length();
                for (int i = 0; i < length; ++i)
                {
                    if (i < length/2)
                        comp1.push_back(line[i]);
                    else
                        comp2.push_back(line[i]);
                }

                std::vector<char> v(comp1.size() + comp2.size());
                std::vector<char>::iterator it, st;

                sort(comp1.begin(), comp1.end());
                sort(comp2.begin(), comp2.end());

                it = set_intersection(comp1.begin(),
                      comp1.end(),
                      comp2.begin(),
                      comp2.end(),
                      v.begin());

                std::cout << line << std::endl;
                printVector(comp1);
                printVector(comp2);
                std::cout << "\nCommon elements:\n";
                for (st = v.begin(); st != it; ++st)
                {
                    to_add.insert(*st);
                    std::cout << *st << ", " << std::endl;;
                }

                for (auto i : to_add)
                {
                    std::cout << "Adding " << i << ", val " << mapper[i] << std::endl;
                    score += mapper[i];
                }
            }
            catch (...)
            {
                std::cout << "Unexpected format" << std::endl;
            }
        }
        file.close();
    }
    std::cout << "Total score is " << score << std::endl;
}
