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
            long long int newID = m_operation(i) % 96577;
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

    Monkey *monkey0 = new Monkey(0, {79, 98}, [](long long int old){ return old * 19; }, [](long long int val){ return val % 23 == 0; }, 2, 3);
    Monkey *monkey1 = new Monkey(1, {54, 65, 75, 74}, [](long long int old){ return old + 6; }, [](long long int val){ return val % 19 == 0; }, 2, 0);
    Monkey *monkey2 = new Monkey(2, {79, 60, 97}, [](long long int old){ return old * old; }, [](long long int val){ return val % 13 == 0; }, 1, 3);
    Monkey *monkey3 = new Monkey(3, {74}, [](long long int old){ return old + 3; }, [](long long int val){ return val % 17 == 0; }, 0, 1);

    monkeys.push_back(monkey0);
    monkeys.push_back(monkey1);
    monkeys.push_back(monkey2);
    monkeys.push_back(monkey3);

    monkey0->setMonkeys(monkeys);
    monkey1->setMonkeys(monkeys);
    monkey2->setMonkeys(monkeys);
    monkey3->setMonkeys(monkeys);

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

