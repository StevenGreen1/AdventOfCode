#include <string>
#include <iostream>
#include <vector>
#include <set>
#include <limits>

#include "../Helper.h"

// 381 too high

class Node
{
    public:
    Node(int x, int y, int height) :
        m_x(x),
        m_y(y),
        m_height(height)
    {
    }

    int m_x{0};
    int m_y{0};
    int m_height{0};
    int m_start_distance{1000000}; //std::numeric_limits<int>::max()};
    Node *m_previous_node{nullptr}; 
};

using NodeVector = std::vector<Node *>;
using NodeMatrix = std::vector<NodeVector>;

std::ostream &operator<<(std::ostream &os, Node const* node)
{
    std::string has_prev_node = node->m_previous_node != nullptr ? "True" : "False";
    int prev_node_id_x = node->m_previous_node != nullptr ? node->m_previous_node->m_x : -1;
    int prev_node_id_y = node->m_previous_node != nullptr ? node->m_previous_node->m_y : -1;
    return os << "x " << node->m_x << ", y " << node->m_y << ", height " << node->m_height
        << ", start distance " << node->m_start_distance << ", previous node set " << has_prev_node << ", prev node " << prev_node_id_x << "," << prev_node_id_y;
}

Node *getNode(int x, int y, NodeVector nodes)
{
    for (auto node : nodes)
    {
        if (node->m_x == x && node->m_y == y)
            return node;
    }
    return nullptr;
}

int find_steps(NodeVector nodes, Node *start);

void dijkstra(IntMatrix &grid)
{
    NodeVector nodes;
    NodeVector starts;

    for (int row = 0; row < grid.size(); ++row)
    {
        for (int col = 0; col < grid.at(0).size(); ++col)
        {
            int height = grid.at(row).at(col);
            Node *node = new Node(row, col, height);
            if (height == -14)
            {
                // Start
//                node->m_start_distance = 0;
                node->m_height = 0;
                starts.push_back(node); 
            }           
            else if (height == -28)
            {
                // End
                node->m_height = 26;
            } 
            else if (height == 0)
            {
                starts.push_back(node); 
            }
            //else
            //{
            //    // Normal point
            //}
            nodes.push_back(node);
        }
    }

    int min_steps = 1000000;
    for (auto start : starts)
    {
        NodeVector copy_nodes;
        for (auto node : nodes)
            copy_nodes.push_back(new Node(*node));

        Node *copy_start_node = getNode(start->m_x, start->m_y, copy_nodes);
        copy_start_node->m_start_distance = 0;
        int steps = find_steps(copy_nodes, copy_start_node);
        min_steps = std::min(min_steps, steps);
    }
    std::cout << min_steps << std::endl;
    return;
}

int find_steps(NodeVector nodes, Node *start)
{
    IntVector nei_x = {1, -1, 0, 0 };
    IntVector nei_y = {0, 0,  1, -1};

    while (nodes.size() > 0)
    {
        std::sort(nodes.begin(), nodes.end(), []( const Node* lhs, const Node* rhs ) { return lhs->m_start_distance > rhs->m_start_distance; });
        Node *current_node = nodes.back();
        //std::cout << "Current : " << current_node << std::endl;

        for (int i = 0; i < 4; ++i)
        {
            int next_row = current_node->m_x + nei_x.at(i);
            int next_col = current_node->m_y + nei_y.at(i);

            Node *next = getNode(next_row, next_col, nodes);
            if (!next)
                continue;

            if (next->m_height > current_node->m_height + 1)
                continue;

            int this_distance = current_node->m_start_distance + 1;

            if (this_distance < next->m_start_distance)
            {
                next->m_start_distance = this_distance;
                next->m_previous_node = current_node;
            }
            if (next->m_height == 26) //-28)
            {
                std::cout << next << std::endl;
                return next->m_start_distance;
            }
        }
        nodes.pop_back();
    }
    return 0;
}

int returnVal(char x)
{
    return (int)x - 97;
}

int main(int argc, char *argv[])
{
    std::string line;
    std::ifstream infile(argv[1]);

    IntMatrix grid;

    while (std::getline(infile, line))
    {
        grid.push_back(IntVector());
        for (auto element : line)
        {
            grid.back().push_back(returnVal(element));
        }
    }

    dijkstra(grid);

    Helper::printMatrix(grid, true);

    return 0;
}

