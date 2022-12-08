#include <fstream>
#include <iostream>

int main()
{
    std::string filename = "Input.txt";
    std::ifstream file(filename);

    int max_cal = 0;
    int local_max = 0;

    if (file.is_open())
    {
        std::string line;
        while (std::getline(file, line))
        {
            if (line == "")
            {
                max_cal = std::max(max_cal, local_max);
                local_max = 0;
            }
            else
            {
                int current_cal = std::stoi(line);
                local_max += current_cal;
            }
        }
        file.close();
    }
    std::cout << "Max elf calories is " << max_cal;
}
