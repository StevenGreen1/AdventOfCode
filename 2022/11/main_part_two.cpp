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
    Monkey(long long int id, IntVector items, std::function<long long int(long long int)> operation, std::function<bool(long long int)> test,
            long long int testIdTrue, long long int testIdFalse) :
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
            long long int newID = m_operation(i) % 9699690;
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

    long long int                         m_count{0};
    long long int                         m_id{0};
    IntVector                   m_items;
    std::function<long long int(long long int)>     m_operation;
    std::function<bool(long long int)>    m_test;
    long long int                         m_testTrueId{-1};
    long long int                         m_testFalseId{-1};
    std::vector<Monkey*>        m_monkeys;
};


int main(int argc, char *argv[])
{
    std::vector<Monkey*> monkeys;

    Monkey *monkey0 = new Monkey(0, {77, 69, 76, 77, 50, 58}, [](long long int old){ return old * 11; }, [](long long int val){ return val % 5 == 0; }, 1, 5);
    Monkey *monkey1 = new Monkey(1, {75, 70, 82, 83, 96, 64, 62}, [](long long int old){ return old + 8; }, [](long long int val){ return val % 17 == 0; }, 5, 6);
    Monkey *monkey2 = new Monkey(2, {53}, [](long long int old){ return old * 3; }, [](long long int val){ return val % 2 == 0; }, 0, 7);
    Monkey *monkey3 = new Monkey(3, {85, 64, 93, 64, 99}, [](long long int old){ return old + 4; }, [](long long int val){ return val % 7 == 0; }, 7, 2);
    Monkey *monkey4 = new Monkey(4, {61, 92, 71}, [](long long int old){ return old * old; }, [](long long int val){ return val % 3 == 0; }, 2, 3);
    Monkey *monkey5 = new Monkey(5, {79, 73, 50, 90}, [](long long int old){ return old + 2; }, [](long long int val){ return val % 11 == 0; }, 4, 6);
    Monkey *monkey6 = new Monkey(6, {50, 89}, [](long long int old){ return old + 3; }, [](long long int val){ return val % 13 == 0; }, 4, 3);
    Monkey *monkey7 = new Monkey(7, {83, 56, 64, 58, 93, 91, 56, 65}, [](long long int old){ return old + 5; }, [](long long int val){ return val % 19 == 0; }, 1, 0);

    // 5 * 17 * 2 * 7 * 3 * 11 * 13 * 19 = 9699690

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

    for (long long int i = 0; i < 10000; i++)
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

