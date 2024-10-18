import streamlit as st
import time
import random

# Inizializza lo stato della sessione solo una volta
if 'gioco_attivo' not in st.session_state:
    st.session_state['gioco_attivo'] = True
if 'introduzione' not in st.session_state:
    st.session_state['introduzione'] = False
if 'domanda' not in st.session_state:
    st.session_state['domanda'] = ''
if 'reset_key' not in st.session_state:
    st.session_state['reset_key'] = 0  # Chiave per forzare il reset del campo input

# Funzione per mostrare l'introduzione con uno spinner di caricamento a sinistra dei messaggi
def introduzione_gioco():
    contenitore_messaggio = st.empty()  # Contenitore per i messaggi
    time.sleep(2)
    contenitore_messaggio.markdown("""
        <div style="display: flex; align-items: center;">
            <div style="flex-shrink: 0; margin-right: 10px;">
                <div class="loading-spinner"></div>
            </div>
            <div>🎱 La <b>magia</b> sta per cominciare!</div>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(3)
    contenitore_messaggio.markdown("""
        <div style="display: flex; align-items: center;">
            <div style="flex-shrink: 0; margin-right: 10px;">
                <div class="loading-spinner"></div>
            </div>
            <div>🎱 Desideri conoscere cosa il <b>destino</b> ha in serbo per te? Fai una <b>domanda</b> sul futuro!</div>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(6)
    contenitore_messaggio.markdown("""
        <div style="display: flex; align-items: center;">
            <div style="flex-shrink: 0; margin-right: 10px;">
                <div class="loading-spinner"></div>
            </div>
            <div>🎱 Vuoi scoprire le straordinarie doti di <b>Simone</b>? Fai una domanda e svela i suoi <b>talenti segreti</b>!</div>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(6)
    contenitore_messaggio.empty()  # Pulisce il contenitore

# Aggiungi il CSS per lo spinner
st.markdown("""
<style>
.loading-spinner {
    border: 4px solid rgba(0, 0, 0, 0.1);
    width: 16px;
    height: 16px;
    border-radius: 50%;
    border-left-color: #09f;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    to { transform: rotate(360deg); }
}
</style>
""", unsafe_allow_html=True)

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
            "Simone riesce a rispettare una scadenza senza impostare promemoria anche sul microonde?",
            "Simone è in grado di non perdere le staffe quando il Wi-Fi va in panne?",
            "Simone è abile a scrivere domande divertenti senza l'aiuto di ChatGPT?",
            "Simone è capace di inviare un'email senza dimenticarsi l'allegato?"
        ]

# Funzione per creare suspense
def crea_suspense():
    st.write("🎱 La Magic 8 Ball sta pensando...")
    barra_progresso = st.progress(0)
    for completamento in range(101):
        time.sleep(0.03)
        barra_progresso.progress(completamento)

# Funzione per chiudere il gioco
def termina_gioco():
    st.session_state['gioco_attivo'] = False
    st.rerun()

# Funzione callback per gestire l'inserimento delle domande suggerite
def inserisci_domanda(esempio_domanda):
    st.session_state['domanda'] = esempio_domanda  # Inserisce la domanda nel campo di input
    st.session_state['reset_key'] += 1  # Forza il reset del campo di input

# Funzione principale dell'applicazione
def avvia_gioco():
    st.markdown("<div style='text-align: center; font-size: 40px; font-weight: bold;'>✨ Magic 8 Ball ✨</div>", unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.write("")
    st.write("")

    if st.session_state['gioco_attivo']:
        if not st.session_state['introduzione']:
            introduzione_gioco()
            st.session_state['introduzione'] = True

        scelta = st.radio("🛣️ **Scegli** la tua strada:",
                          ("🔮 **Futuro**: Scopri cosa ti attende oltre l'**orizzonte**!",
                           "🤹‍♂️ **Simone**: Esplora il mondo affascinante delle sue **abilità nascoste**!"))

        # Crea una lista per le domande suggerite
        if st.button("Mostra suggerimenti"):
            tipo_richiesta = "futuro" if "Futuro" in scelta else "simone"
            st.write("❓ **Esempi di domande:**")
            suggerimenti = suggerisci_domande(tipo_richiesta)
            for i, esempio_domanda in enumerate(suggerimenti):
                st.button(esempio_domanda, key=f"suggerimento_{i}", on_click=inserisci_domanda, args=(esempio_domanda,))
            if tipo_richiesta == "simone":
                st.write("**💡 Consiglio:** per una migliore accuratezza, chiedi di situazioni specifiche che evidenziano le **abilità di Simone**. 🤔")
            else:
                st.write("**💡 Consiglio:** per una migliore accuratezza, rifletti su una domanda a cui si possa rispondere semplicemente con **'Sì' o 'No'**. 🤔")

        # Mostra il campo di input per la domanda, con chiave dinamica basata su reset_key
        st.write("<div style='display: flex; align-items: center;'>", unsafe_allow_html=True)
        domanda = st.text_input("Fai una domanda:", key=f"domanda_input_{st.session_state['reset_key']}", value=st.session_state['domanda'])
        if st.button("Cancella"):
            st.session_state['domanda'] = ''  # Resetta la domanda
            st.session_state['reset_key'] += 1  # Forza il reset del campo di input
            st.rerun()
        st.write("</div>", unsafe_allow_html=True)

        if "Futuro" in scelta:
            if st.button("Chiedi alla Magic 8 Ball"):
                if not domanda.strip():
                    st.warning("Per favore, inserisci una **domanda**!")
                else:
                    crea_suspense()
                    st.markdown(f"🎱 La Magic 8 Ball dice: **{random.choice(risposte_futuro)}**")

        elif "Simone" in scelta:
            if st.button("Chiedi alla Magic 8 Ball"):
                if not domanda.strip():
                    st.warning("Per favore, inserisci una **domanda**!")
                else:
                    crea_suspense()
                    st.markdown(f"🎱 La Magic 8 Ball dice: **{random.choice(risposte_simone)}**")

        if st.button("Chiudi il gioco"):
            termina_gioco()

    else:
        st.write("**Grazie** per aver giocato! 🎉")
        st.write("Vuoi scoprire come funziona la meravigliosa **Magic 8 Ball**? 🎱 Ecco come fare:")
        st.write("1. Clicca sul **Logo di GitHub** 🐱 (il gatto stilizzato) che si trova in alto a destra, accanto al pulsante '**Fork**'.")
        st.write("2. Una volta cliccato, si aprirà la pagina del **progetto**, dove potrai esplorare il **codice sorgente** scritto in **Python** per la logica dell'applicazione, **HTML** per la creazione di elementi visivi personalizzati e **Streamlit** per rendere l'interfaccia interattiva. Buona esplorazione! 🔍")
        st.write("Non dimenticare di **condividere** le tue **profezie** in riunione... e di menzionare il talentuoso **Simone** ai **recruiter**! 🚀")
        st.write("A presto! 👋")

# Esegue la funzione principale
if __name__ == "__main__":
    avvia_gioco()