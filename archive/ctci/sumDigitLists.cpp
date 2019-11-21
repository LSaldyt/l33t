#include <iostream>
#include <cmath>

struct Node
{
    int value;
    Node* next;
};

int toInt(Node * x)
{
    int i = 0;
    int total = 0;
    while (x != nullptr)
    {
        total += x->value * int(pow(10, i));
        i++;
        x = x->next;
    }
    return total;
}

Node* toList(int x)
{
    Node* result = new Node();
    Node* end = result;
    int i = 1;
    do {
        int power = int(pow(10, i));
        end->value = x % power;
        x = x / power;
        end->next = new Node();
        end = end->next;
        i++;
    } while (x > 0);
    return result;
}

Node* sumDigitLists(Node* a, Node* b)
{
    return toList(toInt(a) + toInt(b));
}

int main()
{
    std::cout << toInt(toList(2)) << std::endl;
    std::cout << toInt(sumDigitLists(toList(767), toList(23))) << std::endl;
    return 0;
}
