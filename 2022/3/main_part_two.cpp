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
        std::string line1, line2, line3;
        while (std::getline(file, line1))
        {
            try
            {
                std::getline(file, line2);
                std::getline(file, line3);

                std::vector<char> bag1(line1.begin(), line1.end());
                std::vector<char> bag2(line2.begin(), line2.end());
                std::vector<char> bag3(line3.begin(), line3.end());

                std::vector<char> common12 = commonElements(bag1, bag2);
                std::vector<char> common23 = commonElements(bag2, bag3);
                std::vector<char> common_all = commonElements(common12, common23);

                if (common_all.size() != 1)
                {
                    std::cout << "Problem" << std::endl;
                    printVector(common_all);
                }

                score += mapper[common_all[0]];
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
