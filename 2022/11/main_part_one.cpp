//#include <sstream>
#include <string>
//#include <fstream>
#include <iostream>
#include <vector>
#include <set>

#include "../Helper.h"

// 57120 too low
//
class Monkey
{
    public:
    Monkey(int id, IntVector items, std::function<int(int)> operation, std::function<bool(int)> test,
            int testIdTrue, int testIdFalse) :
        m_id(id),
        m_items(items),
        m_operation(operation),
        m_test(test),
        m_testTrueId(testIdTrue),
        m_testFalseId(testIdFalse)
    {
    } 

    void step()
    {
        for (auto i : m_items)
        {
            m_count++;
            int newID = m_operation(i);
            newID /= 3;
            bool testOutcome = m_test(newID);
            if (testOutcome)
            {
                m_monkeys.at(m_testTrueId)->m_items.push_back(newID);
            }
            else
            {
                m_monkeys.at(m_testFalseId)->m_items.push_back(newID);
            }
        }
        m_items.clear();
    }

    void setMonkeys(std::vector<Monkey*> monkeys)
    {
        m_monkeys = monkeys;
    }

    int                         m_count{0};
    int                         m_id{0};
    IntVector                   m_items;
    std::function<int(int)>     m_operation;
    std::function<bool(int)>    m_test;
    int                         m_testTrueId{-1};
    int                         m_testFalseId{-1};
    std::vector<Monkey*>        m_monkeys;
};


int main(int argc, char *argv[])
{
    std::vector<Monkey*> monkeys;

    Monkey *monkey0 = new Monkey(0, {77, 69, 76, 77, 50, 58}, [](int old){ return old * 11; }, [](int val){ return val % 5 == 0; }, 1, 5);
    Monkey *monkey1 = new Monkey(1, {75, 70, 82, 83, 96, 64, 62}, [](int old){ return old + 8; }, [](int val){ return val % 17 == 0; }, 5, 6);
    Monkey *monkey2 = new Monkey(2, {53}, [](int old){ return old * 3; }, [](int val){ return val % 2 == 0; }, 0, 7);
    Monkey *monkey3 = new Monkey(3, {85, 64, 93, 64, 99}, [](int old){ return old + 4; }, [](int val){ return val % 7 == 0; }, 7, 2);
    Monkey *monkey4 = new Monkey(4, {61, 92, 71}, [](int old){ return old * old; }, [](int val){ return val % 3 == 0; }, 2, 3);
    Monkey *monkey5 = new Monkey(5, {79, 73, 50, 90}, [](int old){ return old + 2; }, [](int val){ return val % 11 == 0; }, 4, 6);
    Monkey *monkey6 = new Monkey(6, {50, 89}, [](int old){ return old + 3; }, [](int val){ return val % 13 == 0; }, 4, 3);
    Monkey *monkey7 = new Monkey(7, {83, 56, 64, 58, 93, 91, 56, 65}, [](int old){ return old + 5; }, [](int val){ return val % 19 == 0; }, 1, 0);

    monkeys.push_back(monkey0);
    monkeys.push_back(monkey1);
    monkeys.push_back(monkey2);
    monkeys.push_back(monkey3);
    monkeys.push_back(monkey4);
    monkeys.push_back(monkey5);
    monkeys.push_back(monkey6);
    monkeys.push_back(monkey7);

    monkey0->setMonkeys(monkeys);
    monkey1->setMonkeys(monkeys);
    monkey2->setMonkeys(monkeys);
    monkey3->setMonkeys(monkeys);
    monkey4->setMonkeys(monkeys);
    monkey5->setMonkeys(monkeys);
    monkey6->setMonkeys(monkeys);
    monkey7->setMonkeys(monkeys);

    for (int i = 0; i < 20; i++)
    {
        for (auto monkey: monkeys)
        {
            monkey->step();
        }
    }

    for (auto monkey: monkeys)
        std::cout << "Monkey " << monkey->m_id << " inspected " <<  monkey->m_count << " items." << std::endl;

    return 0;
}

