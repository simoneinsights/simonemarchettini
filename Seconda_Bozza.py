import streamlit as st
import time
import random

# Inizializza lo stato della sessione solo una volta
if 'gioco_attivo' not in st.session_state:
    st.session_state['gioco_attivo'] = True  # Inizializza il gioco come attivo
if 'introduzione' not in st.session_state:
    st.session_state['introduzione'] = False  # Verifica se l'introduzione è stata eseguita

# Funzione per mostrare l'introduzione
def introduzione_gioco():
    contenitore_messaggio = st.empty()  # Crea un contenitore vuoto
    time.sleep(1)  # Pausa di 1 secondo
    contenitore_messaggio.write("🎱 Benvenuto nella Magic 8 Ball!")  # Primo messaggio
    time.sleep(3)
    contenitore_messaggio.write("🎱 Desideri conoscere cosa il destino ha in serbo per te? Fai una domanda sul futuro!")  # Secondo messaggio
    time.sleep(5)
    contenitore_messaggio.write("🎱 Vuoi scoprire le straordinarie doti di Simone? Fai una domanda e svela i suoi talenti segreti!")  # Terzo messaggio
    time.sleep(5)
    contenitore_messaggio.empty()  # Svuota il contenitore dopo aver mostrato i messaggi

# Liste di risposte per il futuro e per Simone
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

# Funzione per suggerire domande in base al tipo scelto
def suggerisci_domande(tipo_richiesta):
    if tipo_richiesta == "futuro":
        return [
            "L'intelligenza artificiale trasformerà il mio settore?",
            "La mia azienda avrà successo l'anno prossimo?",
            "Il prossimo progetto avrà un impatto positivo sulla mia carriera?",
            "Mi licenzieranno quest'anno?",
        ]
    elif tipo_richiesta == "simone":
        return [
            "Simone è abile a tenere un discorso senza fare riferimento alla sua serie TV preferita?",
            "Simone è in grado di scrivere domande divertenti senza l'aiuto di ChatGPT?",
            "Simone riesce a non perdere le staffe quando il Wi-Fi va in panne?",
            "Simone è capace di fare brainstorming mentre balla il tango?"
        ]

# Funzione per creare suspense
def crea_suspense():
    with st.spinner("🎱 La Magic 8 Ball sta pensando..."):  # Mostra il messaggio di attesa
        barra_progresso = st.progress(0)  # Inizializza la barra di progresso
        for completamento in range(101):
            time.sleep(0.03)  # Pausa di 0.03 secondi per ogni incremento
            barra_progresso.progress(completamento)

# Funzione per chiudere il gioco
def termina_gioco():
    st.session_state['gioco_attivo'] = False  # Imposta il gioco come chiuso

# Funzione principale dell'applicazione
def avvia_gioco():
    st.markdown("<h1 style='text-align: center;'>✨ Magic 8 Ball ✨</h1>", unsafe_allow_html=True)

    st.write("\n" * 4)  # Spazio vuoto per la formattazione

    if st.session_state['gioco_attivo']:
        if not st.session_state['introduzione']:
            introduzione_gioco()
            st.session_state['introduzione'] = True

        scelta = st.radio("🛣️ Scegli la tua strada:", 
                          ("🔮 Futuro: Scopri cosa ti attende oltre l'orizzonte!", 
                           "🤹‍♂️ Simone: Esplora il mondo affascinante delle sue abilità nascoste!"))

        if st.button("Mostra suggerimenti"):
            tipo_richiesta = "futuro" if "Futuro" in scelta else "simone"
            st.write("💡 Esempi di domande:")
            for esempio_domanda in suggerisci_domande(tipo_richiesta):
                st.write(f"- {esempio_domanda}")

        if "Futuro" in scelta:
            domanda = st.text_input("Fai una domanda sul futuro:")
            if st.button("Chiedi alla Magic Ball"):
                if not domanda.strip():
                    st.warning("Per favore, inserisci una domanda!")
                else:
                    crea_suspense()
                    risposta = random.choice(risposte_futuro)
                    st.success(f"🎱 La Magic 8 Ball dice: {risposta}")
        
        elif "Simone" in scelta:
            domanda = st.text_input("Fai una domanda sulle capacità segrete di Simone:")
            if st.button("Chiedi alla Magic Ball"):
                if not domanda.strip():
                    st.warning("Per favore, inserisci una domanda!")
                else:
                    crea_suspense()
                    risposta = random.choice(risposte_simone)
                    st.success(f"🎱 La Magic 8 Ball dice: {risposta}")

        if st.button("Chiudi il gioco"):
            termina_gioco()
            st.rerun()

    else:
        st.write("Grazie per aver giocato! 🎉")
        st.write("Condividi le tue profezie... e parla di Simone ai recruiter! 🚀")
        st.write("A presto! 👋")

# Esegue la funzione principale
if __name__ == "__main__":
    avvia_gioco()
