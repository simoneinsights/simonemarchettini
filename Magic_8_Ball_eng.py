import streamlit as st
import time
import random

# Initialize session state only once
if 'game_active' not in st.session_state:
    st.session_state['game_active'] = True
if 'introduction' not in st.session_state:
    st.session_state['introduction'] = False
if 'question' not in st.session_state:
    st.session_state['question'] = ''
if 'reset_key' not in st.session_state:
    st.session_state['reset_key'] = 0  # Key to force resetting the input field

# Function to display the introduction with a loading spinner on the left of the messages
def game_introduction():
    message_container = st.empty()  # Container for the messages
    time.sleep(2)
    message_container.markdown("""
        <div style="display: flex; align-items: center;">
            <div style="flex-shrink: 0; margin-right: 10px;">
                <div class="loading-spinner"></div>
            </div>
            <div>🎱 The <b>magic</b> is about to begin!</div>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(3)
    message_container.markdown("""
        <div style="display: flex; align-items: center;">
            <div style="flex-shrink: 0; margin-right: 10px;">
                <div class="loading-spinner"></div>
            </div>
            <div>🎱 Do you want to know what <b>fate</b> has in store for you? Ask a <b>question</b> about the future!</div>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(6)
    message_container.markdown("""
        <div style="display: flex; align-items: center;">
            <div style="flex-shrink: 0; margin-right: 10px;">
                <div class="loading-spinner"></div>
            </div>
            <div>🎱 Want to discover the extraordinary talents of <b>Simone</b>? Ask a question and reveal his <b>hidden talents</b>!</div>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(6)
    message_container.empty()  # Clear the container

# Add CSS for the spinner
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

# Lists of responses for the future and for Simone
future_responses = [
    "Yes, definitely.",
    "I don't know, try asking again.",
    "Seems unlikely.",
    "Maybe.",
    "Probably not.",
    "It's certain.",
    "It's impossible.",
]

simone_responses = [
    "Mmm... ask again!",
    "Not much!",
    "Quite a bit!",
    "Yes, definitely!",
    "A lot!",
    "Absolutely not!"
]

# Function to suggest questions based on the chosen type
def suggest_questions(request_type):
    if request_type == "future":
        return [
            "Will AI transform my industry?",
            "Will my company succeed next year?",
            "Will my next project positively impact my career?",
            "Will I be fired this year?",
        ]
    elif request_type == "simone":
        return [
            "Can Simone meet a deadline without setting reminders even on the microwave?",
            "Is Simone capable of staying calm when the Wi-Fi goes down?",
            "Is Simone good at writing funny questions without the help of ChatGPT?",
            "Can Simone send an email without forgetting the attachment?"
        ]

# Function to create suspense
def create_suspense():
    st.write("🎱 The Magic 8 Ball is thinking...")
    progress_bar = st.progress(0)
    for completion in range(101):
        time.sleep(0.03)
        progress_bar.progress(completion)

# Function to end the game
def end_game():
    st.session_state['game_active'] = False
    st.rerun()

# Callback function to handle inserting suggested questions
def insert_question(example_question):
    st.session_state['question'] = example_question  # Inserts the question into the input field
    st.session_state['reset_key'] += 1  # Forces a reset of the input field

# Main function of the app
def start_game():
    st.markdown("<div style='text-align: center; font-size: 40px; font-weight: bold;'>✨ Magic 8 Ball ✨</div>", unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.write("")
    st.write("")

    if st.session_state['game_active']:
        if not st.session_state['introduction']:
            game_introduction()
            st.session_state['introduction'] = True

        choice = st.radio("🛣️ **Choose** your path:",
                          ("🔮 **Future**: Discover what's beyond the **horizon**!",
                           "🤹‍♂️ **Simone**: Explore the fascinating world of his **hidden skills**!"))

        # Create a list of suggested questions
        if st.button("Show suggestions"):
            request_type = "future" if "Future" in choice else "simone"
            st.write("❓ **Example questions:**")
            suggestions = suggest_questions(request_type)
            for i, example_question in enumerate(suggestions):
                st.button(example_question, key=f"suggestion_{i}", on_click=insert_question, args=(example_question,))
            if request_type == "simone":
                st.write("**💡 Tip:** for better accuracy, ask about specific situations that highlight **Simone's skills**. 🤔")
            else:
                st.write("**💡 Tip:** for better accuracy, think of a question that can be answered simply with **'Yes' or 'No'**. 🤔")

        # Show input field for the question, with a dynamic key based on reset_key
        st.write("<div style='display: flex; align-items: center;'>", unsafe_allow_html=True)
        question = st.text_input("Ask a question:", key=f"question_input_{st.session_state['reset_key']}", value=st.session_state['question'])
        if st.button("Clear"):
            st.session_state['question'] = ''  # Resets the question
            st.session_state['reset_key'] += 1  # Forces a reset of the input field
            st.rerun()
        st.write("</div>", unsafe_allow_html=True)

        if "Future" in choice:
            if st.button("Ask the Magic 8 Ball"):
                if not question.strip():
                    st.warning("Please enter a **question**!")
                else:
                    create_suspense()
                    st.markdown(f"🎱 The Magic 8 Ball says: **{random.choice(future_responses)}**")

        elif "Simone" in choice:
            if st.button("Ask the Magic 8 Ball"):
                if not question.strip():
                    st.warning("Please enter a **question**!")
                else:
                    create_suspense()
                    st.markdown(f"🎱 The Magic 8 Ball says: **{random.choice(simone_responses)}**")

        if st.button("End the game"):
            end_game()

    else:
        st.write("**Thank you** for playing! 🎉")
        st.write("Want to discover how the wonderful **Magic 8 Ball** works? 🎱 Here's how:")
        st.write("1. Click on the **GitHub Logo** 🐱 (the stylized cat) at the top right, next to the '**Fork**' button.")
        st.write("2. Once clicked, the **project** page will open, where you can explore the **source code** written in **Python** for the app's logic, **HTML** for creating custom visual elements, and **Streamlit** for making the interface interactive. Happy exploring! 🔍")
        st.write("Don't forget to **share** your **prophecies** in the meeting... and mention the talented **Simone** to the **recruiters**! 🚀")
        st.write("See you soon! 👋")

# Run the main function
if __name__ == "__main__":
    start_game()
