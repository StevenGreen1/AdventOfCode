#include <sstream>
#include <string>
#include <fstream>
#include <iostream>
#include <vector>
#include <set>

class Node;
using Nodes = std::vector<Node*>;

class Node
{
public:
    Node(std::string name, bool isFile) :
        m_name(name),
        m_isFile(isFile)
    {};

    Node *getParent()
    {
        return m_parentNode;
    }

    void setParent(Node *parentNode)
    {
        m_parentNode = parentNode;
    }

    void addChild(Node *childNode)
    {
        m_childNodes.push_back(childNode);
    }

    std::string getName()
    {
        return m_name;
    }

    void addData(int val)
    {
        m_data += val;
    }

    int getData()
    {
        int val = 0;
        for (auto x : m_childNodes)
            val += x->getData();

        val += m_data;
        return val;
    }

    bool m_isFile{false};
    std::string m_name{""};
    Node *m_parentNode{nullptr};
    Nodes m_childNodes;
    int m_data{0};
};

int main(int argc, char *argv[])
{
    std::string line;
    std::ifstream infile(argv[1]);
    std::getline(infile, line);
    Node *current_directory_node = new Node("", false);

    Nodes activeNodes;
    activeNodes.push_back(current_directory_node);

    while (std::getline(infile, line))
    {
        if (line.find("$ cd ..") != std::string::npos)
        {
            current_directory_node = current_directory_node->getParent();
            std::cout << "cd .. ->  " << current_directory_node->getName() << std::endl;
        }
        else if (line.find("dir ") != std::string::npos)
        {
            std::string directory = current_directory_node->getName() + "/" + line.erase(0,4);

            bool set{false};
            for (auto node: activeNodes)
            {
                if (node->getName() == directory)
                {
                    set = true;
                }
            }
            if (!set)
            {
                Node *newNode = new Node(directory, false);
                current_directory_node->addChild(newNode);
                newNode->setParent(current_directory_node);
                activeNodes.push_back(newNode);
            }

            std::cout << "dir   :   " << current_directory_node->getName() << std::endl;
        }
        else if (line.find("$ cd ") != std::string::npos)
        {
            std::string directory = current_directory_node->getName() + "/" + line.erase(0,5);

            for (auto node: activeNodes)
            {
                if (node->getName() == directory)
                {
                    current_directory_node = node;
                }
            }

            std::cout << "cd :      " << current_directory_node->getName() << std::endl;
        }
        else if (line.find("$ ls") != std::string::npos)
        {
            std::cout << "ls" << std::endl;
        }
        else
        {
            std::string size;
            for (int x = 0; x < line.size(); ++x)
            {
                if (isdigit(line.at(x)))
                    size += line.at(x);
                else
                    break;
            }
            int value = std::stoi(size);
            current_directory_node->addData(value);
        }
    }

    int sum{0};

    for (auto x : activeNodes)
    {
        if (x->getData() <= 100000)
        {
            sum += x->getData();
        }
    }
    std::cout << sum << std::endl;
    // Memory will leak
    return 0;
}

