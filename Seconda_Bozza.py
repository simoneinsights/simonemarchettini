import streamlit as st
import time
import random

# Inizializza lo stato della sessione solo una volta
if 'gioco_attivo' not in st.session_state:
    st.session_state['gioco_attivo'] = True  # Inizializza il gioco come attivo
if 'introduzione' not in st.session_state:
    st.session_state['introduzione'] = False  # Verifica se l'introduzione è stata eseguita
if 'domanda' not in st.session_state:
    st.session_state['domanda'] = ''  # Inizializza il campo della domanda

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
    st.markdown("<div style='text-align: center; font-size: 40px; font-weight: bold;'>✨ Magic 8 Ball ✨</div>", unsafe_allow_html=True)

    st.write("")  # Quattro righe vuote
    st.write("") 
    st.write("")  
    st.write("")  

    if st.session_state['gioco_attivo']:
        if not st.session_state['introduzione']:
            introduzione_gioco()
            st.session_state['introduzione'] = True

        scelta = st.radio("🛣️ Scegli la tua strada:", 
                          ("🔮 Futuro: Scopri cosa ti attende oltre l'orizzonte!", 
                           "🤹‍♂️ Simone: Esplora il mondo affascinante delle sue abilità nascoste!"))

        # Crea una lista per le domande suggerite
        tipo_richiesta = "futuro" if "Futuro" in scelta else "simone"
        domande_suggerite = suggerisci_domande(tipo_richiesta)
        
        # Crea un menu a tendina per scegliere il suggerimento
        domanda_scelta = st.selectbox("💡 Scegli una domanda suggerita:", domande_suggerite)

        # Se una domanda suggerita è stata selezionata, aggiorna il campo di input
        if domanda_scelta:
            st.session_state['domanda'] = domanda_scelta

        # Mostra il campo di input per la domanda, precompilato se una domanda è stata scelta
        domanda = st.text_input("Fai una domanda:", value=st.session_state['domanda'])  # Precompila il campo se c'è una domanda nel session state

        if "Futuro" in scelta:
            if st.button("Chiedi alla Magic Ball"):
                if not domanda.strip():
                    st.warning("Per favore, inserisci una domanda!")
                else:
                    crea_suspense()
                    risposta = random.choice(risposte_futuro)
                    st.success(f"🎱 La Magic 8 Ball dice: {risposta}")
        
        elif "Simone" in scelta:
            if st.button("Chiedi alla Magic Ball"):
                if not domanda.strip():
                    st.warning("Per favore, inserisci una domanda!")
                else:
                    crea_suspense()
                    risposta = random.choice(risposte_simone)
                    st.success(f"🎱 La Magic 8 Ball dice: {risposta}")

        if st.button("Chiudi il gioco"):
            termina_gioco()

    else:
        # Messaggio di ringraziamento e istruzioni per visualizzare il codice su GitHub
        st.write("Grazie per aver giocato! 🎉")
        st.write("Vuoi scoprire come funziona la meravigliosa Magic 8 Ball? 🎱 Ecco come fare:")
        st.write("1. **Clicca sul Logo di GitHub** 🐱 (il gatto stilizzato) che si trova in alto a destra, accanto al pulsante 'Fork'")
        st.write("2. Una volta cliccato, si aprirà la pagina del progetto, dove potrai esplorare il codice sorgente scritto in Python e Streamlit. Buona esplorazione! 🔍")
        st.write("Non dimenticare di condividere le tue profezie in riunione... e di menzionare il talentuoso Simone ai recruiter! 🚀")
        st.write("A presto! 👋")

# Esegue la funzione principale
if __name__ == "__main__":
    avvia_gioco()
