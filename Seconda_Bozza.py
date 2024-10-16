import streamlit as st
import time
import random

# Inizializza lo stato della sessione solo una volta
if 'gioco_attivo' not in st.session_state:
    st.session_state['gioco_attivo'] = True
if 'introduzione' not in st.session_state:
    st.session_state['introduzione'] = False
if 'domanda' not in st.session_state:
    st.session_state['domanda'] = ''  # Inizializza il campo della domanda

# Funzione per mostrare l'introduzione
def introduzione_gioco():
    contenitore_messaggio = st.empty()
    time.sleep(1)
    contenitore_messaggio.write("🎱 Benvenuto nella Magic 8 Ball!")
    time.sleep(3)
    contenitore_messaggio.write("🎱 Desideri conoscere cosa il destino ha in serbo per te? Fai una domanda sul futuro!")
    time.sleep(5)
    contenitore_messaggio.write("🎱 Vuoi scoprire le straordinarie doti di Simone? Fai una domanda e svela i suoi talenti segreti!")
    time.sleep(5)
    contenitore_messaggio.empty()

# Liste di risposte per il futuro e per Simone
risposte_futuro = [
    "Sì, sicuramente.", "Non saprei, prova a rifare la domanda.", "Sembra improbabile.",
    "Forse.", "Probabilmente no.", "È certo.", "È impossibile.",
]

risposte_simone = [
    "Mmm... chiedi di nuovo!", "Non molto!", "Abbastanza!", "Sì, decisamente!", "Molto!", "Assolutamente no!"
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
    with st.spinner("🎱 La Magic 8 Ball sta pensando..."):
        barra_progresso = st.progress(0)
        for completamento in range(101):
            time.sleep(0.03)
            barra_progresso.progress(completamento)

# Funzione per chiudere il gioco
def termina_gioco():
    st.session_state['gioco_attivo'] = False
    st.rerun()

# Funzione principale dell'applicazione
def avvia_gioco():
    st.markdown("<div style='text-align: center; font-size: 40px; font-weight: bold;'>✨ Magic 8 Ball ✨</div>", unsafe_allow_html=True)
    
    if st.session_state['gioco_attivo']:
        if not st.session_state['introduzione']:
            introduzione_gioco()
            st.session_state['introduzione'] = True

        # Selezione del tipo di domanda
        scelta = st.radio("🛣️ Scegli la tua strada:", 
                          ("🔮 Futuro: Scopri cosa ti attende oltre l'orizzonte!", 
                           "🤹‍♂️ Simone: Esplora il mondo affascinante delle sue abilità nascoste!"))

        tipo_richiesta = "futuro" if "Futuro" in scelta else "simone"
        domande_suggerite = ["Seleziona un suggerimento"] + suggerisci_domande(tipo_richiesta)

        # Dropdown per domande suggerite
        domanda_scelta = st.selectbox("💡 Scegli una domanda suggerita:", domande_suggerite)

        # Non modifica il testo in input a meno che non sia selezionata una domanda diversa da "Seleziona un suggerimento"
        if domanda_scelta != "Seleziona un suggerimento":
            st.session_state['domanda'] = domanda_scelta

        # Campo input per la domanda
        domanda = st.text_input("Fai una domanda:", value=st.session_state['domanda'])

        # Colonne per pulsanti
        col1, col2 = st.columns([2, 1])

        with col1:
            if st.button("Chiedi alla Magic Ball"):
                if not domanda.strip():
                    st.warning("Per favore, inserisci una domanda!")
                else:
                    crea_suspense()
                    risposta = random.choice(risposte_futuro if "Futuro" in scelta else risposte_simone)
                    st.success(f"🎱 La Magic 8 Ball dice: {risposta}")

        with col2:
            # Cancella il campo input senza considerare la selezione nel dropdown
            if st.button("Cancella"):
                st.session_state['domanda'] = ''  # Resetta sempre la domanda
                st.rerun()

        if st.button("Chiudi il gioco"):
            termina_gioco()

    else:
        st.write("Grazie per aver giocato! 🎉")
        st.write("A presto! 👋")

# Esegue la funzione principale
if __name__ == "__main__":
    avvia_gioco()
