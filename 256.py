import random
import time

def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()

def make_choice(options):
    while True:
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        choice = input("Scegli un'opzione: ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice)
        print("Scelta non valida. Riprova.")

def investigate_terminal():
    displays = [
        "Lo schermo mostra il tuo riflesso, ma i tuoi occhi sono completamente neri.",
        "Appare un video di te che dormi. La data è di domani.",
        "Un labirinto infinito si dispiega sullo schermo. Riconosci corridoi del Level 256.",
        "Il terminale mostra una sequenza di numeri. Realizzi che è un conto alla rovescia della tua vita.",
        "Vedi l'agente scomparso che urla silenziosamente, chiedendo aiuto.",
        "Lo schermo si riempie di occhi che ti fissano. Sbattono le palpebre all'unisono.",
        "Appare un messaggio: 'NON SEI MAI ENTRATO. NON PUOI USCIRE.'",
        "Il terminale mostra una mappa del Level 256. Noti che si sta espandendo in tempo reale.",
        "Vedi te stesso entrare nel Level 256. La figura sullo schermo si volta e ti sorride.",
        "Il terminale si spegne. Nel riflesso nero, vedi una figura in piedi dietro di te."
    ]
    slow_print(random.choice(displays))

def cryptic_event():
    events = [
        "Le pareti sembrano respirare lentamente. Senti di essere all'interno di qualcosa di vivo.",
        "Senti un sussurro nel tuo orecchio: 'Benvenuto a casa'. La voce è la tua.",
        "Il pavimento sotto di te diventa liquido per un istante. Affondi fino alle caviglie prima che si solidifichi.",
        "Vedi l'ombra dell'agente scomparso. Quando la raggiungi, realizzi che è la tua.",
        "Le luci si spengono. Quando si riaccendono, tutti i corridoi sono cambiati.",
        "Senti il suono di unghie che graffiano metallo. Proviene da dentro le pareti.",
        "Un'ondata di vertigini ti colpisce. Per un momento, vedi il Level 256 dall'esterno, fluttuante nel vuoto.",
        "Trovi una porta che non c'era prima. Quando la apri, vedi te stesso dall'altra parte che la apre.",
        "Il tuo riflesso in una superficie lucida non imita i tuoi movimenti. Ti fissa e sorride.",
        "Senti un grido distante. Riconosci la tua voce, ma non stai urlando.",
        "Le pareti iniziano a sanguinare un liquido nero e viscoso.",
        "Vedi una figura in lontananza. Più ti avvicini, più si allontana, sempre alla stessa distanza.",
        "Il tuo corpo diventa trasparente per alcuni secondi. Vedi i tuoi organi pulsare innaturalmente.",
        "Un corridoio si estende all'infinito davanti a te. Quando ti giri, vedi la stessa cosa dietro.",
        "Senti il peso di mille occhi invisibili che ti osservano. La pressione è quasi fisica."
    ]
    slow_print(random.choice(events))

def briefing():
    slow_print("Sei l'ultimo agente rimasto del M.E.G. (Major Explorers' Group) assegnato al Level 256.")
    slow_print("Negli ultimi mesi, squadre intere sono scomparse in questo livello.")
    slow_print("L'ultima trasmissione ricevuta parlava di 'realtà che si scioglie' e 'l'edificio è cosciente'.")
    slow_print("Sei l'ultima speranza di scoprire cosa sta succedendo. Non c'è possibilità di estrazione.")
    slow_print("Ti prepari per entrare, sapendo che potresti non tornare mai più.")

def arrival():
    slow_print("Ti risvegli nel Level 256. Non ricordi come sei entrato.")
    slow_print("Sei in un corridoio infinito, illuminato da una luce bluastra che sembra provenire da nessuna parte.")
    slow_print("L'aria è densa, quasi liquida. Respirare richiede uno sforzo cosciente.")
    slow_print("Un silenzio opprimente ti circonda, interrotto solo dal battito del tuo cuore.")

def main():
    sanity = 100
    turns = 0
    revelations = 0

    briefing()
    arrival()

    slow_print("Inizi la tua esplorazione del Level 256. Ogni passo potrebbe essere l'ultimo nella realtà che conosci.")

    while sanity > 0 and turns < 30 and revelations < 10:
        turns += 1
        choice = make_choice(["Avanza nel corridoio", "Interagisci con un terminale", "Investiga un'anomalia", "Riposati (se puoi)"])

        if choice == 1:
            slow_print("Avanzi nel corridoio apparentemente infinito.")
            if random.random() < 0.6:
                cryptic_event()
            sanity -= 3
        elif choice == 2:
            investigate_terminal()
            if random.random() < 0.4:
                slow_print("Hai scoperto qualcosa di inquietante sulla natura del Level 256.")
                revelations += 1
            sanity -= 5
        elif choice == 3:
            slow_print("Ti avvicini a qualcosa di strano e innaturale.")
            cryptic_event()
            if random.random() < 0.5:
                slow_print("Questa esperienza ti ha rivelato una terribile verità.")
                revelations += 1
            sanity -= 7
        elif choice == 4:
            slow_print("Chiudi gli occhi, cercando un momento di riposo.")
            if random.random() < 0.7:
                slow_print("I tuoi sogni sono invasi da visioni del Level 256. Non c'è riposo qui.")
                sanity -= 10
            else:
                slow_print("Riesci a riposare un po', ma ti senti come se avessi dormito per secoli.")
                sanity += 5

        sanity = max(0, min(100, sanity))
        slow_print(f"Sanità mentale: {sanity}% | Rivelazioni: {revelations}/10")
        
        if sanity <= 50 and random.random() < 0.4:
            slow_print("Cominci a dubitare della tua stessa esistenza. Sei davvero qui o sei sempre stato parte del Level 256?")

    if sanity <= 0:
        slow_print("La tua mente si frammenta. Diventi un tutt'uno con il Level 256, un'altra anima intrappolata nella sua coscienza collettiva.")
    elif revelations >= 10:
        slow_print("Comprendi la vera natura del Level 256. La rivelazione è così orribile che il tuo senso di realtà collassa.")
        slow_print("Sei diventato parte del livello, condannato a osservare altri esploratori cadere nella stessa trappola.")
    else:
        slow_print("Riesci in qualche modo a fuggire, ma le tue esperienze ti hanno cambiato per sempre.")
        slow_print("Sai che una parte di te rimarrà sempre nel Level 256, in attesa del tuo ritorno.")

    slow_print("FINE DELLA MISSIONE - LA VERITÀ RIMANE NASCOSTA NELLE PROFONDITÀ DEL LEVEL 256")

if __name__ == "__main__":
    main()