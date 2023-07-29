#ifndef ENGINE_H
#define ENGINE_H

#include <string>
#include <vector>
#include <map>
#include <regex>
#include <iostream>

#include "engine.hpp"

class TambusEngine {
public:
    void addVariable(std::string name, std::string value);

    std::string getVariable(std::string name);

    std::string translate( std::string code);


private:
    std::map<std::string, std::string> variables;

    std::string translate_variables(std::string code);
};



#endif