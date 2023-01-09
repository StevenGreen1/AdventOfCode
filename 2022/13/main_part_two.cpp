#include <string>
#include <iostream>
#include <vector>
#include <set>
#include <limits>
#include <optional>
#include <algorithm>

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

    Node(const Node& source) :
        m_parent{source.m_parent},
        m_value{source.m_value}
    {
        for (auto node : source.m_contents)
        {
            m_contents.push_back(new Node(*node));
        }
    }

    Node(Node&& source) :
        m_parent{source.m_parent},
        m_value{source.m_value}
    {
        for (auto node : source.m_contents)
        {
            m_contents.push_back(node);
        }
    }

    Node(){}
};

int lessThan(Node *lhs, Node *rhs)
{
    bool is_rhs_empty = !rhs->m_value.has_value() && rhs->m_contents.empty();
    bool is_lhs_empty = !lhs->m_value.has_value() && lhs->m_contents.empty();
    bool is_rhs_number = rhs->m_value.has_value();
    bool is_lhs_number = lhs->m_value.has_value();
    bool is_rhs_array = !rhs->m_contents.empty();
    bool is_lhs_array = !lhs->m_contents.empty();

    // (1) Number vs Number
    //std::cout << "(1)" << std::endl;
    if (is_rhs_number & is_lhs_number)
    {
        if (lhs->m_value.value() == rhs->m_value.value())
        {
//            std::cout << "LHS : " << lhs->m_value.value() << " < " << rhs->m_value.value() << " RHS : 2" << std::endl;
            return 2;
        }
//        std::cout << "LHS : " << lhs->m_value.value() << " < " << rhs->m_value.value() << " RHS : " << (lhs->m_value.value() < rhs->m_value.value() ? 1 : 0) << std::endl;
        return lhs->m_value.value() < rhs->m_value.value() ? 1 : 0;
    }

    // (2) Number vs Empty
    if (is_lhs_number && is_rhs_empty)
        return 0;

    // (3) Empty vs Number
    if (is_rhs_number && is_lhs_empty)
        return 1;

    // (4) Empty vs Empty
    if (is_rhs_empty && is_lhs_empty)
        return 2;

    // (5) Number vs Array
    if (is_lhs_number && is_rhs_array)
    {
        int ans = lessThan(lhs, rhs->m_contents.at(0));
        if (ans != 2)
            return ans;

        if (rhs->m_contents.size() == 1)
            return 2;
        return 1;
    }

    // (6) Array vs Number
    if (is_rhs_number && is_lhs_array)
    {
        int ans = lessThan(lhs->m_contents.at(0), rhs);
        if (ans != 2)
            return ans;

        if (lhs->m_contents.size() == 1)
            return 2;
        return 0;
    }

    // (7) Empty vs Array
    if (is_lhs_empty && is_rhs_array)
    {
        return 1;
    }

    // (8) Array vs Empty
    if (is_rhs_empty && is_lhs_array)
    {
        return 0;
    }

    // (9) Array vs Array
    if (is_rhs_array && is_lhs_array)
    {
        for (int i = 0; i < std::min(lhs->m_contents.size(), rhs->m_contents.size()); ++i)
        {
            Node *left = lhs->m_contents.at(i);
            Node *right = rhs->m_contents.at(i);
            int ans = lessThan(left, right);
            if (ans == 2)
                continue;
            return ans;
        }
        if (lhs->m_contents.size() == rhs->m_contents.size())
            return 2;
        return lhs->m_contents.size() < rhs->m_contents.size() ? 1 : 0;
    }

    std::cout << "Should not get here" << std::endl;
    return -1;
}

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
    std::string str_el;
    bool reading = false;

    for (char element : line)
    {
        if (std::isdigit(element))
        {
            str_el.push_back(element);
            reading = true;
        }
        else if (reading)
        {
            Node *value_node = new Node(std::stoi(str_el));
            value_node->m_parent = current;
            current->m_contents.push_back(value_node);
            reading = false;
            str_el = "";
        }

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
    }

    return current;
}



int main(int argc, char *argv[])
{
    std::string line;
    std::ifstream infile(argv[1]);
    int idx = 0;
    int count = 0;

    IntVector vals;
    std::vector<Node*> nodes; 

    while (std::getline(infile, line))
    {
        std::string left = line;
        std::getline(infile, line);
        std::string right = line;
        idx++;
        //std::cout << "Index : " << idx << std::endl;

        // Empty line
        std::getline(infile, line);

        Node *parentLeft = process_input(left);
        nodes.push_back(parentLeft);
        Node *parentRight = process_input(right);
        nodes.push_back(parentRight);
    }

    std::sort(nodes.begin(), nodes.end(), [](Node* lhs, Node* rhs){
        int ans = lessThan(lhs, rhs);
        if (ans == 2)
        {
            std::cout << "Bug : " << lhs << " " << rhs << std::endl;
            return 0;
        }
        return ans; });

    for (int i = 0; i < nodes.size(); ++i)
    {
        std::cout << i+1 << " " << nodes.at(i) << std::endl;
    }
    return 0;
}

// 109, 184 are the packets in order, giving = 20,056 
