# Funzione per mostrare l'introduzione con icona di caricamento a destra dei messaggi
def introduzione_gioco():
    contenitore_messaggio = st.empty()
    time.sleep(1)
    contenitore_messaggio.markdown("""
        <div style="display: flex; align-items: center; justify-content: space-between;">
            <div>🎱 Benvenuto nella Magic 8 Ball!</div>
            <div>⏳</div>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(3)
    contenitore_messaggio.markdown("""
        <div style="display: flex; align-items: center; justify-content: space-between;">
            <div>🎱 Desideri conoscere cosa il destino ha in serbo per te? Fai una domanda sul futuro!</div>
            <div>⏳</div>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(6)
    contenitore_messaggio.markdown("""
        <div style="display: flex; align-items: center; justify-content: space-between;">
            <div>🎱 Vuoi scoprire le straordinarie doti di Simone? Fai una domanda e svela i suoi talenti segreti!</div>
            <div>⏳</div>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(6)
    contenitore_messaggio.empty()

# Aggiungi il CSS per lo spinner (se necessario)
st.markdown("""
    <style>
    .loading-spinner {
        border: 4px solid rgba(0, 0, 0, 0.1);
        width: 18px;
        height: 18px;
        border-radius: 50%;
        border-left-color: #09f;
        animation: spin 1s linear infinite;
    }

    @keyframes spin {
        to { transform: rotate(360deg); }
    }
    </style>
""", unsafe_allow_html=True)
