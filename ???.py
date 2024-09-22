import random

class NightmareInTheUnknown:
    def __init__(self):
        self.team = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
        self.team_status = {member: "OK" for member in self.team}
        self.turn = 0
        self.game_over = False
        self.sanity = 100
        self.disturbing_events = [
            "Un membro della squadra inizia a ridere incontrollabilmente.",
            "Qualcuno riferisce di vedere il proprio riflesso invecchiare rapidamente.",
            "Un operativo afferma di sentire voci provenienti dalle pareti.",
            "La squadra trova una stanza piena di manichini che sembrano muoversi.",
            "Un membro della squadra giura di aver visto se stesso in lontananza.",
            "La gravità sembra invertirsi per un momento.",
            "Gli orologi della squadra iniziano a girare al contrario.",
            "Un operativo trova una foto di se stesso bambino... scattata ieri.",
            "La squadra sente il suono di una ninna nanna distorta.",
            "Le ombre sembrano muoversi indipendentemente dalla luce.",
            "Un membro della squadra inizia a parlare in una lingua sconosciuta.",
            "Il pavimento sotto i piedi della squadra diventa liquido per un istante.",
            "Tutti i membri della squadra vedono contemporaneamente un'ombra umanoide correre via.",
            "Le pareti iniziano a 'respirare' lentamente.",
            "Un operativo trova un diario con la sua calligrafia, ma non ricorda di averlo mai scritto.",
            "La squadra sente l'eco di una conversazione che avranno in futuro.",
            "Un membro della squadra vede il proprio corpo da una prospettiva in terza persona.",
            "Tutti i dispositivi elettronici della squadra mostrano lo stesso messaggio criptico.",
            "La squadra trova una porta che si apre su un abisso infinito.",
            "Un operativo sente il proprio battito cardiaco provenire da fuori il suo corpo.",
            "La squadra trova una stanza identica a quella in cui si trovavano da bambini.",
            "Un membro della squadra inizia a invecchiare rapidamente, poi torna normale.",
            "La squadra sente il suono di passi che li seguono, ma non c'è nessuno dietro di loro.",
            "Un operativo trova un biglietto nel suo zaino che dice 'Svegliati' con la sua calligrafia.",
            "La squadra vede una versione distorta di se stessa riflessa in ogni superficie.",
            "Un membro della squadra scompare per alcuni secondi, poi riappare senza ricordare nulla.",
            "La squadra trova una stanza piena di schermi che mostrano i loro ricordi d'infanzia.",
            "Un operativo sente la propria voce provenire da un altro membro della squadra.",
            "La squadra trova una scala che sale e scende all'infinito.",
            "Un membro della squadra vede i propri genitori in lontananza, ma quando si avvicina scompaiono."
        ]
        self.final_messages = [
            "Non c'è via d'uscita. Non c'è mai stata. Siamo sempre stati qui.",
            "Posso vederli tutti ora. Sono ovunque. Sono... noi.",
            "Ho capito tutto. Questo posto... siamo noi. È sempre stato così.",
            "Non tornate a cercarci. Per il vostro bene, dimenticate che siamo mai esistiti.",
            "Le pareti... stanno sussurrando la verità. È bellissima e terrificante.",
            "Vedo infinite versioni di me stesso. Quale sono io? Sono... tutti loro.",
            "Il tempo non esiste qui. Siamo sempre stati qui e sempre lo saremo.",
            "Questo è il nostro vero volto. La realtà era solo un'illusione.",
            "Sento le voci di tutti coloro che sono venuti prima. Presto mi unirò a loro.",
            "Non siamo mai stati reali. Siamo solo echi di qualcosa di più grande.",
            "La verità è qui. È sempre stata qui. Ed è meravigliosa.",
            "Vedo l'inizio e la fine. Sono la stessa cosa.",
            "Non c'è più differenza tra noi e questo posto. Siamo diventati una cosa sola.",
            "Le nostre vite precedenti erano solo un sogno. Questa è la realtà.",
            "Posso sentire i pensieri di tutti. Sono... pacifici.",
        ]

    def start(self):
        print("Benvenuto, agente di supporto del M.E.G.")
        print("Sei in contatto con una squadra di 5 esploratori nel Livello ??? (The Unknown).")
        print("Il tuo compito è guidarli, ma ricorda: in questo livello, la realtà è un concetto fluido.")
        
        while not self.game_over:
            self.turn += 1
            print(f"\n--- Turno {self.turn} ---")
            self.status_report()
            self.player_action()
            self.environment_event()
            self.sanity_check()
            
            if all(status == "Perso" for status in self.team_status.values()) or self.sanity <= 0:
                self.game_over = True
                self.end_game()

    def status_report(self):
        print("\nStato della squadra:")
        for member, status in self.team_status.items():
            print(f"{member}: {status}")
        print(f"Sanità mentale della squadra: {self.sanity}%")

    def player_action(self):
        print("\nCosa vuoi dire alla squadra?")
        print("1. Continuate ad esplorare")
        print("2. Fermatevi e riposate")
        print("3. Tornate indietro")
        print("4. Separatevi per coprire più terreno")
        print("5. Meditate per centrare la mente")
        choice = input("Inserisci il numero della tua scelta: ")
        
        if choice == "1":
            print("'Dobbiamo andare avanti. Non importa cosa succederà.'")
            self.sanity -= 5
        elif choice == "2":
            print("'Fermatevi un attimo. Abbiamo bisogno di riprendere fiato.'")
            self.sanity += 5
        elif choice == "3":
            print("'Torniamo indietro! Questo posto è maledetto!'")
            self.sanity -= 10
        elif choice == "4":
            print("'Separatevi. Dobbiamo coprire più terreno possibile.'")
            self.sanity -= 15
        elif choice == "5":
            print("'Fermatevi e meditate. Dobbiamo centrare le nostre menti.'")
            self.sanity += 10 if random.random() < 0.5 else -10
        else:
            print("Il silenzio della radio aumenta il panico della squadra.")
            self.sanity -= 15

    def environment_event(self):
        event = random.choice(self.disturbing_events)
        print(f"\nRapporto dalla squadra: {event}")
        self.sanity -= random.randint(5, 15)
        
        if random.random() < 0.15:  # 15% di possibilità di perdere un membro
            victims = [m for m in self.team_status.keys() if self.team_status[m] == "OK"]
            if victims:
                victim = random.choice(victims)
                self.team_status[victim] = "Perso"
                print(f"\nALLARME! {victim} è scomparso! L'ultimo messaggio: 'Vedo... me stesso?'")
                self.sanity -= 20

    def sanity_check(self):
        if self.sanity <= 30:
            print("\nLa squadra sta perdendo il controllo. I loro messaggi diventano incoerenti.")
        if self.sanity <= 10:
            print("\nLa follia sta prendendo il sopravvento. La squadra non distingue più la realtà.")

    def end_game(self):
        print("\nGAME OVER")
        if all(status == "Perso" for status in self.team_status.values()):
            last_survivor = random.choice(self.team)
            final_message = random.choice(self.final_messages)
            print(f"Hai perso il contatto con tutta la squadra. L'ultimo messaggio di {last_survivor}: '{final_message}'")
        elif self.sanity <= 0:
            print("La squadra è impazzita completamente. L'ultimo messaggio: 'Finalmente capiamo. Siamo sempre stati qui.'")
        print("\nIl Livello ??? (The Unknown) reclama altre vittime. La missione è un fallimento totale.")
        print(f"La squadra è sopravvissuta per {self.turn} turni prima di soccombere all'ignoto.")

if __name__ == "__main__":
    game = NightmareInTheUnknown()
    game.start()
