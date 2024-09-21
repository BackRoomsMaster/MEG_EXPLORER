import random
import time

class Level6Game:
    def __init__(self):
        self.turns = 0
        self.game_over = False
        self.sanity = 100
        self.health = 100
        self.clues_found = 0
        self.inventory = []
        self.final_choice = None

    def print_slow(self, text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.03)
        print()

    def start_game(self):
        self.print_slow("\nSei un agente M.E.G. inviato nel Livello 6 per indagare sulla scomparsa di una squadra.")
        self.print_slow("Il tuo obiettivo è trovare indizi sulla loro sorte e, se possibile, uscire vivo.")
        self.print_slow("Buona fortuna. Ne avrai bisogno.")
        
        while not self.game_over:
            self.turn()

    def turn(self):
        self.turns += 1
        print(f"\nTurno {self.turns}")
        print(f"Salute: {self.health}% | Sanità mentale: {self.sanity}% | Indizi trovati: {self.clues_found}/5")
        
        action = input("Cosa fai? ").lower()

        if "muov" in action or "cammin" in action:
            self.move()
        elif "cerc" in action or "esplor" in action:
            self.search()
        elif "ascolt" in action or "sent" in action:
            self.listen()
        elif "invent" in action or "zaino" in action:
            self.check_inventory()
        elif "aiuto" in action or "help" in action:
            self.help()
        else:
            self.print_slow("Non sei sicuro di cosa stai facendo.")

        if random.random() < 0.1:
            self.encounter_entity()

        self.check_status()

    def move(self):
        movements = [
            "Ti muovi nel buio. Qualcosa sfiora il tuo viso.",
            "Avanzi lentamente. Il pavimento scricchiola sotto i tuoi piedi.",
            "Procedi a tentoni. Un suono di passi ti segue, ma non sono i tuoi.",
            "Ti sposti cautamente. L'aria diventa improvvisamente fredda."
        ]
        self.print_slow(random.choice(movements))
        if random.random() < 0.2:
            self.find_clue()

    def search(self):
        self.print_slow("Cerchi attentamente nell'area circostante.")
        if random.random() < 0.4:
            self.find_clue()
        else:
            self.print_slow("Non trovi nulla di utile.")

    def listen(self):
        sounds = [
            "Ascolti. Un respiro pesante sembra provenire da tutte le direzioni.",
            "Ti concentri sui suoni. Qualcosa si muove rapidamente intorno a te.",
            "Tendi l'orecchio. Un suono di unghie che graffiano le pareti ti circonda.",
            "Il silenzio è rotto da un suono di masticazione. È vicino. Troppo vicino."
        ]
        self.print_slow(random.choice(sounds))
        self.sanity -= random.randint(1, 3)

    def check_inventory(self):
        if not self.inventory:
            self.print_slow("Il tuo zaino è vuoto. Sei solo con il nulla.")
        else:
            self.print_slow("Nel tuo zaino trovi:")
            for item in self.inventory:
                self.print_slow(f"- {item}")
        def find_clue(self):
        clues = [
            "Un pezzo di uniforme strappato con il logo M.E.G.",
            "Un registratore audio danneggiato",
            "Una mappa parziale del livello, macchiata di sangue",
            "Un diario con le ultime annotazioni della squadra scomparsa",
            "Un dispositivo di comunicazione rotto con un messaggio criptico"
        ]
        if self.clues_found < 5:
            clue = clues[self.clues_found]
            self.print_slow(f"Hai trovato un indizio: {clue}")
            self.inventory.append(clue)
            self.clues_found += 1
            if self.clues_found == 5:
                self.final_decision()

    def encounter_entity(self):
        encounters = [
            "Qualcosa di grande si muove nell'oscurità. Ti immobilizzi.",
            "Un sibilo acuto risuona vicino al tuo orecchio. Ti volti di scatto.",
            "Senti degli artigli sfiorarti la schiena. Corri alla cieca.",
            "Un alito caldo sul collo. Ti giri. Nulla. Ma sai che c'è qualcosa."
        ]
        self.print_slow(random.choice(encounters))
        damage = random.randint(5, 20)
        self.health -= damage
        self.sanity -= random.randint(10, 20)
        self.print_slow(f"Senti dolore. Hai perso {damage}% di salute.")

    def final_decision(self):
        self.print_slow("\nI frammenti di realtà si uniscono nella tua mente offuscata.")
        self.print_slow("Due percorsi si aprono davanti a te, entrambi avvolti nell'oscurità.")
        self.print_slow("La scelta è tua, ma le conseguenze sono imperscrutabili.")
        choice = input("Scegli: (1) Seguire l'eco distante o (2) Immergersi nel silenzio profondo? ")
        if choice == "1":
            self.cryptic_escape()
        elif choice == "2":
            self.gruesome_discovery()
        else:
            self.print_slow("L'indecisione è una scelta di per sé...")
            self.void_consumption()

    def cryptic_escape(self):
        self.print_slow("\nL'eco ti guida attraverso corridoi contorti e realtà frammentate.")
        self.print_slow("Il buio pulsa, si contorce, cerca di trattenerti.")
        self.print_slow("Corri. Inciampi. Ti rialzi. Il suono cresce d'intensità.")
        self.print_slow("Un bagliore accecante. Dolore lancinante. Poi...")
        self.print_slow("Ti ritrovi altrove. O forse sei ancora lì?")
        self.print_slow("La tua mente è un groviglio di ricordi e allucinazioni.")
        self.print_slow("Sei davvero fuggito, o è solo un'altra illusione del Livello 6?")
        self.game_over = True

    def gruesome_discovery(self):
        self.print_slow("\nIl silenzio ti avvolge come un sudario mentre avanzi.")
        self.print_slow("L'aria diventa densa, metallica. Odore di sangue e putrefazione.")
        self.print_slow("Inciampi su qualcosa di morbido. Molte cose morbide.")
        self.print_slow("Le tue mani toccano carne fredda, viscida. Senti un movimento.")
        self.print_slow("Un coro di sussurri ti circonda. Riconosci le voci della squadra scomparsa.")
        self.print_slow("'Unisciti a noi', dicono all'unisono. 'Diventa uno con il buio.'")
        self.print_slow("Senti il tuo corpo cambiare. La tua mente si espande nel vuoto.")
        self.print_slow("Sei ancora tu, o sei diventato parte di qualcosa di più grande e terribile?")
        self.game_over = True

    def void_consumption(self):
        self.print_slow("\nL'oscurità si addensa intorno a te, palpabile, viva.")
        self.print_slow("Senti mille occhi invisibili che ti scrutano, ti giudicano.")
        self.print_slow("Il pavimento sotto di te scompare. Cadi nell'abisso infinito.")
        self.print_slow("La tua carne si dissolve. La tua mente si frammenta.")
        self.print_slow("Diventi uno con il vuoto. Sei ovunque e in nessun luogo.")
        self.print_slow("Il Livello 6 ti ha reclamato. Sei parte di esso ora. Per sempre.")
        self.game_over = True

    def help(self):
        self.print_slow("Comandi disponibili: muovi, cerca, ascolta, inventario, aiuto")
        self.print_slow("Il tuo obiettivo è trovare 5 indizi sulla squadra scomparsa.")

    def check_status(self):
        if self.health <= 0 or self.sanity <= 0:
            self.print_slow("Non ce la fai più. L'oscurità ti inghiotte.")
            self.game_over = True

if __name__ == "__main__":
    game = Level6Game()
    game.start_game()