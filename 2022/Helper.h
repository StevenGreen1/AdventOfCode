#include <fstream>
#include <iostream>
#include <vector>
#include <map>
#include <set>

using IntVector = std::vector<int>;
using IntMatrix = std::vector<IntVector>;

class Helper
{
    public:
    template <typename T>
    static void printVector(std::vector<T> vec, bool colour = false)
    {
        for (int i = 0; i < vec.size(); i++)
        {
            if (vec[i] > 0)
            {
                std::cout << "\033[1;32m" << vec[i] << " \033[0m";
            }
            else
            {
                std::cout << "\033[1;31m" << vec[i] << " \033[0m";
            }
        }
        std::cout << std::endl;
    }

    template <typename T>
    static void printMatrix(std::vector<std::vector<T>> matrix, bool colour = false)
    {
        for (int i = 0; i < matrix.size(); i++)
            printVector(matrix.at(i), colour);
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
}; 
