#include <unordered_set>
#include <iostream>
#include <string>

class TextInput
{
	std::string inner;
public:
    virtual void add(char c) { 
        inner += c;
	}

    std::string getValue() { 
		return inner;
	}
};

class NumericInput : public TextInput 
{ 
        std::string numerics = "0123456789";
    public:

        void add(char c)
        {
            if (numerics.find(c) < numerics.size())
            {
                TextInput::add(c);
            }
        }
};

#ifndef RunTests
int main()
{
    TextInput* input = new NumericInput();
    input->add('1');
    input->add('a');
    input->add('0');
    std::cout << input->getValue();
}
#endif
