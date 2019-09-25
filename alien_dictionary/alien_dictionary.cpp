#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <iostream>

using std::vector;
using std::string;
using std::unordered_map;
using std::unordered_set;
using std::cout;
using std::endl;

using Words    = vector<string>;
using Alphabet = vector<char>;

class Ordering{
    private:
        unordered_map<char, unordered_set<char>> mapping;
    public:
        void add(char a, char b)
        {
            auto found = mapping.find(a);
            if (found == mapping.end())
            {
                mapping[a] = unordered_set<char>();
            }
            mapping[a].insert(b);
        }

        void print()
        {
            for (auto& kv : mapping)
            {
                std::cout << kv.first << " > ";
                for (auto c : kv.second)
                {
                    std::cout << c << ", ";
                }
                std::cout << std::endl;
            }
        }
};

Ordering find_ordering(Words& words, Alphabet& alphabet)
{
    // Assume all words are the same length
    // If this is not the case...?
    Ordering ordering;
    if (words.size() < 2)
    {
        return ordering;
    }
    for (int i = 1; i < words.size(); i++)
    {
        int j = 0;
        string& a = words[i - 1];
        string& b = words[i];
        while (a[j] == b[j] and j < a.size() and j < b.size()) // Should only need to check one, but maybe this will be useful later
        {
            j++;
        }
        if (a[j] == b[j])
        {
            break;
        }
        else
        {
            ordering.add(a[j], b[j]);
        }
    }
    return ordering;
}


int main()
{
    Words words       = {"ca", "dc", "db", "aa"};
    Alphabet alphabet = {'a', 'b', 'c', 'd', 'e'};

    Ordering ordering = find_ordering(words, alphabet);
    ordering.print();
}
