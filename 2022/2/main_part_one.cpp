#include <fstream>
#include <iostream>

int main(int argc, char **argv)
{
    std::string filename = argv[1];
    std::ifstream file(filename);

    char me = 0;
    char oppo = 0;
    int score = 0;

    if (file.is_open())
    {
        std::string line;
        while (std::getline(file, line))
        {
            try
            {
                oppo = line[0];
                me = line[2];

                int round = 0;
                // X = A = Rock, Y = B = Paper, Z = C = Scissors
                if (oppo == 'A' && me == 'Z' ||
                        oppo == 'B' && me == 'X' ||
                        oppo == 'C' && me == 'Y')
                {
                    // Lose
                    std::cout << "Lose" << std::endl;
                    round += 0;
                }
                else if (oppo == 'A' && me == 'X' ||
                        oppo == 'B' && me == 'Y' ||
                        oppo == 'C' && me == 'Z')
                {
                    // Draw
                    std::cout << "Draw" << std::endl;
                    round += 3;
                }
                else
                {
                    // Win
                    std::cout << "Win" << std::endl;
                    round += 6;
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
