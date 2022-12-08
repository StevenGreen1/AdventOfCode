#include <fstream>
#include <iostream>
#include <vector>
#include <map>
#include <set>

class Helper
{
    public:
    static void printVector(std::vector<char> vec)
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
}; 
