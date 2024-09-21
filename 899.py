import time
import sys

def print_loading(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def print_slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def make_choice(options):
    while True:
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        choice = input("Fai la tua scelta: ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice)
        print("Scelta non valida. Riprova.")

def simulate_loading():
    print_loading("Inizializzazione M.E.G. Memory Retrieval System v3.5...")
    time.sleep(1)
    print_loading("Caricamento dati neurali: ████████████████████ 100%")
    time.sleep(0.5)
    print_loading("Sincronizzazione memorie soggetto: Mike")
    time.sleep(0.5)
    print_loading("Obiettivo: Level 899 (Yonder's End)")
    time.sleep(0.5)
    print_loading("Calibrazione sistema di immersione neurale...")
    time.sleep(1)
    print_loading("Avvio sequenza di immersione in 3... 2... 1...")
    time.sleep(1)
    print("\n" * 3)
    print_loading("IMMERSIONE COMPLETATA")
    print("\n" * 2)

def start_game():
    simulate_loading()
    print("================================================")
    print("  M.E.G. MEMORY RETRIEVAL SYSTEM - LEVEL 899    ")
    print("================================================")
    print("\nBenvenuto, agente. Stai per rivivere i ricordi")
    print("di Mike durante l'esplorazione del Level 899.")
    print("Ricorda: le tue scelte influenzeranno l'esperienza.")
    print("\nPremi INVIO per iniziare...")
    input()
def explore_level_899():
    print_slow("\nTi ritrovi nei ricordi di Mike. Sei con Jameson, in attesa del rappresentante di Yonder's End.")
    print_slow("Una creatura simile a un gargoyle si avvicina. Si presenta come Karl.")

    choice = make_choice(["Salutare amichevolmente", "Rimanere cauto"])
    
    if choice == 1:
        print_slow("Saluti Karl calorosamente. Lei sorride, mostrando le sue zanne.")
        print_slow("'Benvenuti a Yonder's End,' dice Karl. 'Spero che troverete qui ciò che cercate.'")
    else:
        print_slow("Rimani cauto. Karl nota la tua esitazione ma rimane cordiale.")
        print_slow("'Non temete,' dice Karl. 'Qui siete al sicuro dai pericoli delle Backrooms.'")

    print_slow("\nKarl vi guida attraverso vari livelli delle Backrooms. Il viaggio dura giorni.")
    print_slow("Durante il cammino, tu e Jameson riflettete sulle vostre esperienze passate.")

    print_slow("\nJameson sospira. 'Mike, pensi mai a come sarebbe stata la nostra vita senza le Backrooms?'")
    choice = make_choice(["'A volte mi manca la normalità'", "'Le Backrooms ci hanno reso ciò che siamo'"])

    if choice == 1:
        print_slow("'Anche io,' risponde Jameson con un sorriso triste. 'Ma forse qui troveremo un po' di pace.'")
    else:
        print_slow("Jameson annuisce pensieroso. 'È vero, ma a che prezzo?'")

    print_slow("\nFinalmente arrivate a Yonder's End. Il cielo è un caleidoscopio di colori danzanti.")
    print_slow("L'isola fluttuante si estende davanti a voi, un paradiso surreale nel caos delle Backrooms.")

    print_slow("\nKarl vi offre una zuppa. 'Questa vi aiuterà ad adattarvi,' dice con un sorriso enigmatico.")
    print_slow("Dopo averla mangiata, ti senti stranamente rinvigorito, ma anche un po' disorientato.")

    print_slow("\nNei giorni seguenti, esplorate l'isola. Le coltivazioni di funghi, il lago cristallino, il cielo sempre mutevole.")
    print_slow("Osservate gli altri residenti. Sembrano felici, ma c'è qualcosa di strano nei loro occhi.")

    print_slow("\nUna sera, seduti sul bordo dell'isola, Jameson ti confida: 'Mike, sto pensando di rimanere qui.'")
    print_slow("'Sono stanco di correre, di lottare. Forse questo è il posto giusto per trovare la pace.'")

    choice = make_choice(["Incoraggiare Jameson a restare", "Cercare di dissuaderlo"])

    if choice == 1:
        print_slow("'Se pensi che sia la scelta giusta, ti appoggio,' dici, sentendo un nodo alla gola.")
    else:
        print_slow("'Sei sicuro? Non sappiamo cosa comporti veramente restare qui,' rispondi preoccupato.")

    print_slow("\nJameson sorride tristemente. 'Lo so, ma sono disposto a correre il rischio.'")

    print_slow("\nÈ arrivato il momento di decidere. Karl vi aspetta per conoscere la vostra scelta.")
    print_slow("Jameson ti guarda, i suoi occhi pieni di speranza e paura.")

    final_choice = make_choice(["Decidere di tornare al M.E.G.", "Rimanere con Jameson"])

    if final_choice == 1:
        print_slow("Con il cuore pesante, annunci la tua decisione di tornare al M.E.G.")
        print_slow("Jameson annuisce, comprensivo ma deluso. 'Ti capisco, Mike. Spero ci rivedremo un giorno.'")
        print_slow("Mentre Karl ti guida verso l'uscita, ti volti un'ultima volta.")
        print_slow("Vedi Jameson che ti saluta, una figura solitaria contro il cielo colorato di Yonder's End.")
    else:
        print_slow("Stai per dire che rimarrai, ma qualcosa ti trattiene. Un senso di dovere, forse.")
        print_slow("Realizzi che non puoi abbandonare la tua missione, il tuo ruolo nel M.E.G.")
        print_slow("Con il cuore spezzato, annunci che tornerai indietro.")
        print_slow("Jameson sembra sorpreso, ma poi sorride comprensivo. 'Capisco, Mike. Il M.E.G. ha bisogno di te.'")

    print_slow("\nMentre ti allontani, porti con te il peso di questa scelta e il ricordo di Yonder's End.")
    print_slow("Ti chiedi se un giorno rivedrai Jameson e come lo troverai cambiato.")

    print_slow("\nFINE DELLA SIMULAZIONE")
    print_slow("Connessione ai ricordi di Mike terminata.")

if __name__ == "__main__":
    start_game()
    explore_level_899()