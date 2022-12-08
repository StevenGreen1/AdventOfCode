#include <fstream>
#include <iostream>
#include <map>

int main(int argc, char **argv)
{
    std::string filenaresult = argv[1];
    std::ifstream file(filenaresult);

    char result = 0;
    char oppo = 0;
    int score = 0;

    std::map<char, char> win, draw, lose;
    win['A'] = 'Y';
    win['B'] = 'Z';
    win['C'] = 'X';

    lose['A'] = 'Z';
    lose['B'] = 'X';
    lose['C'] = 'Y';

    draw['A'] = 'X';
    draw['B'] = 'Y';
    draw['C'] = 'Z';

    if (file.is_open())
    {
        std::string line;
        while (std::getline(file, line))
        {
            try
            {
                oppo = line[0];
                result = line[2];

                int round = 0;
                char me;
                // X = A = Rock, Y = B = Paper, Z = C = Scissors
                if (result == 'Z')
                {
                    // Win
                    round += 6;
                    me = win[oppo];
                }
                else if (result == 'Y')
                {
                    // Draw
                    round += 3;
                    me = draw[oppo];
                }
                else
                {
                    // Lose
                    me = lose[oppo];
                }

                round += (me == 'X' ? 1 : me == 'Y' ? 2 : 3);
                score += round;
                std::cout << line << ", score " << round << ", total " << score << std::endl;
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
