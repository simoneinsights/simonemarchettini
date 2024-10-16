import streamlit as st
import time
import random

# Inizializza lo stato della sessione solo una volta
if 'gioco_attivo' not in st.session_state:
    st.session_state['gioco_attivo'] = True  # Inizializza il gioco come attivo
if 'mostra_messaggi' not in st.session_state:
    st.session_state['mostra_messaggi'] = False  # Verifica se i messaggi iniziali sono stati mostrati

# Funzione per mostrare messaggi con ritardo
def mostra_messaggi_con_ritardo():
    messaggio = st.empty()  # Crea un contenitore vuoto
    time.sleep(1)  # Pausa di 1 secondo
    messaggio.write("🎱 Benvenuto nella Magic 8 Ball!")  # Primo messaggio
    time.sleep(3)
    messaggio.write("🎱 Vuoi scoprire cosa il destino ha in serbo per te? Fai una domanda sul futuro!")  # Secondo messaggio
    time.sleep(5)
    messaggio.write("🎱 Desideri conoscere le straordinarie doti di Simone? Fai una domanda e svela i suoi talenti segreti!")  # Terzo messaggio
    time.sleep(5)
    messaggio.empty()  # Svuota il contenitore dopo aver mostrato i messaggi

# Liste di risposte
risposte_futuro = [
    "Sì, sicuramente.",
    "Non saprei, prova a rifare la domanda.",
    "Sembra improbabile.",
    "Forse.",
    "Probabilmente no.",
    "È certo.",
    "È impossibile.",
]

risposte_simone = [

    "Mmm... chiedi di nuovo!",
    "Non molto!",
    "Abbastanza!",
    "Sì, decisamente!",
    "Molto!",
    "Assolutamente no!"
]

# Funzione per suggerire domande a seconda del tipo
def suggerisci_domanda(tipo):
    if tipo == "futuro":
        return [
            "L'intelligenza artificiale trasformerà il mio settore?",
            "La mia azienda avrà successo l'anno prossimo?",
            "Il prossimo progetto avrà un impatto positivo sulla mia carriera?",
            "Mi licenzieranno quest'anno?",
        ]
    elif tipo == "simone":
        return [
            "Simone è abile a tenere un discorso senza fare riferimento alla sua serie TV preferita?",
            "Simone è in grado di scrivere domande divertenti senza l'aiuto di ChatGPT?",
            "Simone riesce a non perdere le staffe quando il Wi-Fi va in panne?",
            "Simone è capace di fare brainstorming mentre balla il tango?"
        ]

# Funzione per creare suspense
def crea_suspense():
    with st.spinner("🎱 La Magic 8 Ball sta pensando..."):  # Mostra il messaggio di attesa
        progress_bar = st.progress(0)  # Inizializza la barra di progresso
        for percent_complete in range(101):
            time.sleep(0.03)  # Pausa di 0.03 secondi per ogni incremento (circa 3 secondi totali)
            progress_bar.progress(percent_complete)  # Aggiorna la barra

# Funzione per chiudere il gioco
def chiudi_gioco():
    st.session_state['gioco_attivo'] = False  # Imposta il gioco come chiuso

# Funzione principale dell'applicazione
def main():
    # Titolo dell'app con HTML per la formattazione
    st.markdown("<h1 style='text-align: center;'>✨ Magic 8 Ball ✨</h1>", unsafe_allow_html=True)

    # Spazio vuoto per la formattazione
    st.write("\n" * 4)

    # Controlla se il gioco è attivo
    if st.session_state['gioco_attivo']:
        # Mostra i messaggi iniziali solo una volta
        if not st.session_state['mostra_messaggi']:
            mostra_messaggi_con_ritardo()
            st.session_state['mostra_messaggi'] = True  # Impedisce che i messaggi siano mostrati di nuovo

        # Opzioni di scelta per l'utente
        scelta = st.radio("🛣️ Scegli la tua strada:", 
                          ("🔮 Futuro: Scopri cosa ti attende oltre l'orizzonte!", 
                           "🤹‍♂️ Simone: Esplora il mondo affascinante delle sue abilità nascoste!"))

        # Mostra suggerimenti di domande se l'utente lo desidera
        if st.button("Mostra i suggerimenti"):
            tipo_domanda = "futuro" if "Futuro" in scelta else "simone"  # Determina il tipo di domanda basato sulla scelta
            st.write("💡 Esempi di domande:")
            for esempio in suggerisci_domanda(tipo_domanda):
                st.write(f"- {esempio}")

        # Sezione per gestire le domande
        if "Futuro" in scelta:
            domanda = st.text_input("Fai una domanda sul futuro:")
            if st.button("Chiedi alla Magic Ball"):
                if not domanda.strip():
                    st.warning("Per favore, inserisci una domanda!")
                else:
                    crea_suspense()
                    risposta = random.choice(risposte_futuro)  # Sceglie una risposta casuale per il futuro
                    st.success(f"🎱 La Magic 8 Ball dice: {risposta}")
        
        elif "Simone" in scelta:
            domanda = st.text_input("Fai una domanda sulle capacità segrete di Simone:")
            if st.button("Chiedi alla Magic Ball"):
                if not domanda.strip():
                    st.warning("Per favore, inserisci una domanda!")
                else:
                    crea_suspense()
                    risposta = random.choice(risposte_simone)  # Sceglie una risposta casuale per Simone
                    st.success(f"🎱 La Magic 8 Ball dice: {risposta}")

        # Bottone per chiudere il gioco
        if st.button("Chiudi il gioco"):
            chiudi_gioco()  # Chiude il gioco
            st.rerun()  # Ricarica l'app per riflettere il nuovo stato

    else:
        # Se il gioco è chiuso, mostra i messaggi di ringraziamento
        st.write(" Grazie per aver giocato! 🎉 ")
        st.write(" Non dimenticare di condividere le tue profezie in riunione... e di menzionare Simone ai recruiter: il talento che cercano! 🚀")
        st.write(" A presto! 👋")

# Esegue la funzione principale
if __name__ == "__main__":
    main()
