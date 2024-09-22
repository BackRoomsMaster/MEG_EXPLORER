#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <chrono>
#include <thread>
#include <iomanip>

void typeEffect(const std::string& text, int delay = 30) {
    for (char c : text) {
        std::cout << c << std::flush;
        std::this_thread::sleep_for(std::chrono::milliseconds(delay));
    }
    std::cout << std::endl;
}

void runPythonScript(const std::string& scriptName) {
    std::string command = "python " + scriptName;
    system(command.c_str());
}

int main() {
    std::vector<std::string> levels = {"256.py", "6.py", "899.py", "???.py", "redacted.py"};
    
    typeEffect("Inizializzazione sistema M.E.G. di recupero memorie...", 50);
    std::this_thread::sleep_for(std::chrono::seconds(2));
    system("clear");  // Usa "cls" su Windows

    while (true) {
        std::cout << "\033[1;32m"; // Colore verde brillante
        typeEffect("=== M.E.G. SISTEMA DI RECUPERO MEMORIE ===", 20);
        std::cout << "\033[0m"; // Resetta il colore

        typeEffect("ATTENZIONE: Accesso a memorie di classe pending. Procedere con cautela.", 30);
        std::cout << std::endl;

        for (size_t i = 0; i < levels.size(); ++i) {
            std::cout << "[" << std::setw(2) << std::setfill('0') << i + 1 << "] Memoria Livello " << levels[i].substr(0, levels[i].size() - 3) << std::endl;
        }
        std::cout << "[00] Terminare sessione" << std::endl;
        
        std::string choice;
        std::cout << "\nInserire codice memoria: ";
        std::cin >> choice;

        if (choice == "00") {
            typeEffect("Terminazione sessione di recupero memorie...", 30);
            typeEffect("Disconnessione dal sistema M.E.G. completata.", 30);
            return 0;
        }
        else {
            int choiceNum = std::stoi(choice);
            if (choiceNum > 0 && choiceNum <= static_cast<int>(levels.size())) {
                typeEffect("Inizializzazione sequenza di recupero memoria...", 30);
                std::this_thread::sleep_for(std::chrono::seconds(1));
                typeEffect("AVVISO: La seguente memoria potrebbe contenere informazioni disturbanti.", 30);
                std::this_thread::sleep_for(std::chrono::seconds(1));
                system("clear"); // Usa "cls" su Windows
                runPythonScript(levels[choiceNum - 1]);
            }
            else {
                typeEffect("Codice memoria non valido. Riprovare.", 30);
            }
        }
        
        std::cout << std::endl;
        system("clear"); // Usa "cls" su Windows
    }

    return 0;
}
