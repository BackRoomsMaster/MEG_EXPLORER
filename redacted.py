import time
import random

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def make_choice(options):
    for i, option in enumerate(options, 1):
        slow_print(f"{i}. {option}")
    while True:
        choice = input("> ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice)
        slow_print("Scelta non valida. Riprova.")

def main():
    slow_print("Diario dell'Esploratore: La Discesa nel Livello [REDACTED]", 0.05)
    slow_print("\nAvvertenza: Le pagine seguenti contengono informazioni classificate. La lettura non autorizzata è punibile secondo il Protocollo Omega-7.", 0.05)
    
    slow_print("\nGiorno 1: Ho trovato l'accesso. Anni di ricerca, innumerevoli sacrifici, e finalmente sono qui.")
    slow_print("Il portale è... indescrivibile. Sembra un taglio nella realtà stessa, che pulsa con un'energia aliena.")
    
    choice = make_choice(["Entro immediatamente", "Eseguo i rituali di protezione"])
    if choice == 1:
        slow_print("\nL'impazienza mi tradisce. Mentre attraverso il portale, sento la mia pelle bruciare. Un errore imperdonabile.")
    else:
        slow_print("\nRecito le antiche formule di protezione. Il portale sembra reagire, pulsando più lentamente.")
    
    slow_print("\nIl passaggio è... doloroso. Sento il mio corpo distorcersi in modi impossibili.")
    slow_print("Quando riapro gli occhi, sono in un luogo che sfida ogni logica.")
    
    slow_print("\nGiorno 3: Il tempo qui scorre in modo strano. Le pareti sembrano respirare.")
    slow_print("Ho incontrato altre 'cose' qui. Non posso chiamarle persone. Si muovono in modi innaturali.")
    
    choice = make_choice(["Provo a comunicare", "Mi nascondo"])
    if choice == 1:
        slow_print("\nLe mie parole escono distorte. Le 'cose' si voltano verso di me. I loro volti... oh dio, i loro volti...")
    else:
        slow_print("\nMi rannicchio in un angolo. Sento le 'cose' passare vicino. Il loro odore è insopportabile.")
    
    slow_print("\nGiorno 7?: Ho perso il conto dei giorni. La fame mi tormenta, ma non c'è nulla di commestibile qui.")
    slow_print("Le pareti sussurrano costantemente. A volte, credo di capire cosa dicono. Vorrei non capirlo.")
    
    choice = make_choice(["Seguo i sussurri", "Cerco di ignorarli"])
    if choice == 1:
        slow_print("\nI sussurri mi guidano attraverso corridoi impossibili. Vedo cose che la mente umana non dovrebbe comprendere.")
    else:
        slow_print("\nCerco di bloccare i sussurri, ma si insinuano nella mia mente. Sento la mia sanità mentale vacillare.")
    
    slow_print("\nGiorno ??: Ho trovato una stanza. Al centro c'è un obelisco nero che emette una luce pulsante.")
    slow_print("Ci sono simboli incisi su di esso. Sembrano muoversi quando non li guardo direttamente.")
    
    choice = make_choice(["Tocco l'obelisco", "Studio i simboli", "Lascio la stanza"])
    if choice == 1:
        slow_print("\nNel momento in cui tocco l'obelisco, sento mille voci urlare nella mia mente. Vedo l'infinito.")
    elif choice == 2:
        slow_print("\nPiù studio i simboli, più sento la mia mente espandersi. Comprendo segreti cosmici. È troppo da sopportare.")
    else:
        slow_print("\nCerco di lasciare la stanza, ma le porte sono scomparse. Sono intrappolato con l'obelisco.")
    
    slow_print("\nGiorno ???: Non sono più sicuro di essere umano. Il mio corpo cambia continuamente.")
    slow_print("Ho visto gli dei antichi che governano questo luogo. La loro mera presenza è insopportabile.")
    
    slow_print("\nHo capito perché questo livello è [REDACTED]. La conoscenza che contiene non dovrebbe esistere.")
    slow_print("Posso sentire la realtà stessa piegarsi intorno a me. Non c'è via d'uscita.")
    
    slow_print("\nUltimo giorno: A chiunque trovi questo diario, vi supplico: distruggetelo.")
    slow_print("La conoscenza contenuta qui è una maledizione. Sento 'loro' avvicinarsi.")
    slow_print("Non cercate il Livello [REDACTED]. Alcune porte devono rimanere chi--")
    
    slow_print("\n--- Il diario termina bruscamente qui ---", 0.1)
    
    slow_print("\nNota dell'Archivista: Il resto del diario è macchiato di una sostanza non identificabile.")
    slow_print("L'analisi della sostanza ha portato alla pazzia tre dei nostri migliori ricercatori.")
    slow_print("Questo documento è ora classificato come Rischio Cognitivo di Classe Omega.")
    slow_print("Che Dio abbia pietà delle nostre anime.", 0.1)

if __name__ == "__main__":
    main()
