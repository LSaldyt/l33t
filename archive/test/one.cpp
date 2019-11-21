#include <iostream>
#include <vector>
#include <unordered_set>

std::vector<std::string> unique_names(const std::vector<std::string>& names1, const std::vector<std::string>& names2)
{
    std::unordered_set<std::string> mapping;
	std::vector<std::string> output;
	for (auto name : names1)
   	{
		mapping.insert(name);
	}
	for (auto name : names2)
   	{
		mapping.insert(name);
	}
	for (auto name : mapping)
   	{
		output.push_back(name);
	}
	return output;
}

#ifndef RunTests
int main()
{
    std::vector<std::string> names1 = {"Ava", "Emma", "Olivia"};
    std::vector<std::string> names2 = {"Olivia", "Sophia", "Emma"};
    
    std::vector<std::string> result = unique_names(names1, names2);
    for(auto element : result)
    {
        std::cout << element << ' '; // should print Ava Emma Olivia Sophia
    }
}
#endif
