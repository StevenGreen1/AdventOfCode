#include <fstream>
#include <iostream>
#include <vector>

int main()
{
    std::string filename = "Input.txt";
    std::ifstream file(filename);

    std::vector<int> calories;
    int local_max = 0;

    if (file.is_open())
    {
        std::string line;
        while (std::getline(file, line))
        {
            if (line == "")
            {
                calories.push_back(local_max);
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

    std::nth_element(calories.begin(), calories.begin()+3, calories.end(), std::greater{});
    std::cout << "The largest element is " << calories[0] << std::endl;
    std::cout << "The second largest element is " << calories[1] << std::endl;
    std::cout << "The third largest element is " << calories[2] << std::endl;

    std::cout << "Sum " << calories[0] + calories[1] + calories[2] << std::endl;
}
