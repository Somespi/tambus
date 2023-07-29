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
        std::string result = code;
        std::smatch match;
        while (std::regex_search(result, match, std::regex("\\{\\{(.*?)\\}\\}"))) {
            std::string placeholder = match[0].str();
            std::string variable = match[1].str();
            if (variables.find(variable) != variables.end()) {
                result = std::regex_replace(result, std::regex(placeholder), variables[variable]);
            } else {
                result = std::regex_replace(result, std::regex(placeholder), "UNKNOWN");
            }
        }
        return result;
    }
};
