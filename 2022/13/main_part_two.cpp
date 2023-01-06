#include <string>
#include <iostream>
#include <vector>
#include <set>
#include <limits>
#include <optional>

#include "../Helper.h"

// 6454 too high
// 5306 too low
// 5659 too low
// 5884 wrong
class Node
{
    public:
    // Any vectors the list contains
    std::vector<Node*> m_contents;

    // Parent node
    Node* m_parent{nullptr};

    // If a value
    std::optional<int> m_value;

    // Node with value
    Node(int value) :
        m_value{value}
    {}

    Node(){}

    int lessThan(Node *rhs)
    {
        //std::cout << "(1)" << std::endl;

        if (m_value.has_value() && rhs->m_value.has_value())
        {
            if (m_value.value() == rhs->m_value.value())
            {
                //std::cout << "LHS : " << m_value.value() << " < " << rhs->m_value.value() << " RHS : 2" << std::endl;
                return 2;
            }
            //std::cout << "LHS : " << m_value.value() << " < " << rhs->m_value.value() << " RHS : " << (m_value.value() < rhs->m_value.value() ? 1 : 0) << std::endl;
            return m_value.value() < rhs->m_value.value() ? 1 : 0;
        }
        //std::cout << "(2)" << std::endl;

        if (m_contents.empty() && !m_value.has_value() && !rhs->m_contents.empty())
            return 1;
        //std::cout << "(3)" << std::endl;

        if (!m_contents.empty() && rhs->m_contents.empty() && !rhs->m_value.has_value())
            return 0;

        if (m_contents.empty() && !m_value.has_value() && rhs->m_contents.empty() && !rhs->m_value.has_value())
            return 2;

        //std::cout << "(4)" << std::endl;

        if (m_value.has_value() && !rhs->m_value.has_value())
        {
            for (auto i : rhs->m_contents)
            {
                int ans = lessThan(i);
                if (ans != 2)
                    return ans;
            }
            return 2;
        }

        //std::cout << "(5)" << std::endl;
        if (!m_value.has_value() && rhs->m_value.has_value())
        {
            for (auto i : m_contents)
            {
                int ans = i->lessThan(rhs);
                if (ans != 2)
                    return ans;
            }
            return 2;
        }

        //std::cout << "(6)" << std::endl;
        if (!m_contents.empty() && !rhs->m_contents.empty())
        {
            for (int i = 0; i < std::min(m_contents.size(), rhs->m_contents.size()); ++i)
            {
                Node *left = m_contents.at(i);
                Node *right = rhs->m_contents.at(i);
                ////std::cout << left << " vs " << right << std::endl;
                //std::cout << "Element : " << i << std::endl;
                int ans = left->lessThan(right);
                //std::cout << "Element : " << i << ", Cmp " << ans << std::endl;
                if (ans == 2)
                    continue;
                return ans;
            }
            if (m_contents.size() == rhs->m_contents.size())
                return 2;
            return m_contents.size() < rhs->m_contents.size() ? 1 : 0;
        }

        //std::cout << "Should not get here" << std::endl;
        return -1;
    }
};

std::ostream &operator<<(std::ostream &os, Node const* node)
{
    if (!node)
        return os << "null node";
    if (node->m_value.has_value())
    {
        return os << node->m_value.value() << ",";
    }
    else if (node->m_contents.empty())
    {
        return os << "[]";
    }
    else
    {
        os << "[";
        for (auto n : node->m_contents)
        {
            os << n;
        }
        os << "]";
    }
    return os;
}

Node *process_input(std::string &line)
{
    Node *current = nullptr;

    for (char element : line)
    {
        if (element == '[')
        {
            Node *child = new Node();
            child->m_parent = current;
            if (current)
            {
                current->m_contents.push_back(child);
            }
            current = child;
        }
        else if (element == ']')
        {
            if (current->m_parent)
                current = current->m_parent;
        }
        else if (std::isdigit(element))
        {
            std::string str_el;
            str_el.push_back(element);
            Node *value_node = new Node(std::stoi(str_el));
            value_node->m_parent = current;
            current->m_contents.push_back(value_node);
        }
        else if (element == ',')
        {
            continue;
        }
    }

    return current;
}

int main(int argc, char *argv[])
{
    std::string line;
    std::ifstream infile(argv[1]);
    int idx = 0;
    int count = 0;

    while (std::getline(infile, line))
    {
        std::string left = line;
        std::getline(infile, line);
        std::string right = line;
        idx++;

        // Empty line
        std::getline(infile, line);

        Node *parentLeft = process_input(left);
        std::cout << left << " = " << parentLeft << std::endl;

        Node *parentRight = process_input(right);
        std::cout << right << " = " << parentRight << std::endl;

        int leftLTright = parentLeft->lessThan(parentRight);

        if (leftLTright > 0)
            count += idx;
        std::cout << "Comparison : " << (leftLTright ? "Correct Order" : "Not Correct Order") << std::endl;
    }
    std::cout << count << std::endl;
    return 0;
}

