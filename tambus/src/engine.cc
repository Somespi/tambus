#include "engine.hpp"

class TambusEngine {
public:
    void addVariable(std::string name, std::string value) {
        variables[name] = value;
    }

    std::string getVariable(std::string name) {
        return variables[name];
    }

    std::string translate( std::string code) {
        if (std::regex_search(code, std::regex("\\{\\{(.*?)\\}\\}"))) {
            code = translate_variables(code);
        }

        return code;
    }


private:
    std::map<std::string, std::string> variables;

    std::string translate_variables(std::string code) {
        
    }
};
