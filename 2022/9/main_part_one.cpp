//#include <sstream>
#include <string>
//#include <fstream>
#include <iostream>
#include <vector>
#include <set>

#include "../Helper.h"

class Position
{
public:
    Position(int x, int y) :
        m_x(x),
        m_y(y)
    {}

    void operator+=(const Position &to_add)
    {
        m_x += to_add.m_x;
        m_y += to_add.m_y;
    }

    bool operator< (const Position &p) const
    {
        if (m_x != p.m_x)
            return m_x < p.m_x;

        if (m_y != p.m_y)
            return m_y < p.m_y;

        return false;
    }

    int m_x = 0;
    int m_y = 0;
};

int main(int argc, char *argv[])
{
    std::string line;
    std::ifstream infile(argv[1]);

    Position head(0,0), tail(0,0);
    std::set<Position> unique;

    while (std::getline(infile, line))
    {
        std::string number;

        for (int i = 2; i < line.size(); ++i)
        {
            number += line[i];
        }

        int step_size = std::stoi(number);

        for (int y = 0; y < step_size; ++y)
        {
            Position step(0,0);
            if (line[0] == 'R')
            {
                step.m_x = 1;
            }
            else if (line[0] == 'L')
            { 
                step.m_x = -1;
            }
            else if (line[0] == 'U')
            {
                step.m_y = 1;
            }
            else if (line[0] == 'D')
            {
                step.m_y = -1;
            }

            head += step;

            if (tail.m_y - head.m_y == 2)
            {
                tail.m_y -= 1; 

                if (tail.m_x > head.m_x)
                {
                    tail.m_x -= 1;
                }
               else if (tail.m_x < head.m_x)
               {
                   tail.m_x += 1;
               }
           }
           else if (tail.m_y - head.m_y == -2)
           {
               tail.m_y += 1;

               if (tail.m_x > head.m_x)
               {
                   tail.m_x -= 1;
               }
               else if (tail.m_x < head.m_x)
               {
                   tail.m_x += 1;
               }
           }
           else if (tail.m_x - head.m_x == 2)
           {
               tail.m_x -= 1;

               if (tail.m_y > head.m_y)
               {
                   tail.m_y -= 1;
               }
               else if (tail.m_y < head.m_y)
               {
                   tail.m_y += 1;
               }
           }
           else if (tail.m_x - head.m_x == -2)
           {
               tail.m_x += 1;

               if (tail.m_y > head.m_y)
               {
                   tail.m_y -= 1;
               }
               else if (tail.m_y < head.m_y)
               {
                   tail.m_y += 1;
               }
           }
            std::cout << head.m_x << "," << head.m_y << " : " << tail.m_x << "," << tail.m_y << std::endl;
            unique.insert(tail);
        }
    }

    std::cout << "Unique points for tail " << unique.size() << std::endl;

    return 0;
}

