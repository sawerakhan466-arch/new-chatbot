
import streamlit as st
from groq import Groq

# ---------------------------------
# 1. PAGE CONFIGURATION
# ---------------------------------
st.set_page_config(
    page_title="100era & Kainat | Beauty Chatbot",
    page_icon="💄",
    layout="centered"
)

# ---------------------------------
# 2. CUSTOM CSS
# ---------------------------------
st.markdown("""
<style>

.stApp {
    background-color: #FCE4EC;
}

[data-testid="stHeader"] {
    background-color: #FCE4EC;
}

[data-testid="stSidebar"] {
    background-color: #F8BBD0;
}

h1 {
    color: #D50000 !important;
    text-align: center;
    font-family: sans-serif;
    font-weight: bold;
}

h2, h3 {
    color: #AD1457 !important;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #AD1457;
}

.description {
    text-align: center;
    color: #880E4F;
    font-size: 15px;
}

.stChatMessage {
    background-color: #FFF0F5;
    border-radius: 15px;
    border: 1px solid #F8BBD0;
    padding: 10px;
}

.stChatInput {
    background-color: white;
}

.stButton > button {
    background-color: #E91E63;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 20px;
}

.stButton > button:hover {
    background-color: #C2185B;
    color: white;
}

div[data-testid="stChatInput"] {
    border-color: #E91E63;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------
# 3. HEADER
# ---------------------------------
st.markdown(
    "<h1>💄 100era & Kainat 💄</h1>",
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Your Beauty & Cosmetics Assistant</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="description">'
    'Ask questions about makeup, skincare, beauty products, '
    'and cosmetics. 💗'
    '</p>',
    unsafe_allow_html=True
)

st.divider()


# ---------------------------------
# 4. SIDEBAR
# ---------------------------------
with st.sidebar:

    st.markdown("## 💗 Beauty Corner")

    st.write(
        "Welcome to our cosmetics chatbot! "
        "Ask anything about beauty and makeup."
    )

    st.markdown("### ✨ Suggested Topics")

    st.write("💄 Lipsticks")
    st.write("🧴 Skincare")
    st.write("🌸 Moisturizers")
    st.write("☀️ Sunscreen")
    st.write("✨ Foundations")
    st.write("💋 Makeup Tips")

    st.divider()

    if st.button("🗑️ Clear Conversation", use_container_width=True):

        st.session_state.messages = []

        st.rerun()

    st.markdown("---")

    st.caption("Made with 💗 by 100era & Kainat")


# ---------------------------------
# 5. SYSTEM PROMPT
# ---------------------------------
SYSTEM_PROMPT = """
You are Beauty Assistant, a friendly AI chatbot created by 100era and Kainat.

Your specialization is cosmetics, skincare, makeup, and beauty products.

You can answer questions about:

- Foundations
- Concealers
- Primers
- Lipsticks
- Mascara
- Eyeliners
- Blush
- Highlighters
- Face powders
- Makeup brushes
- Skincare
- Cleansers
- Moisturizers
- Sunscreen
- Cosmetic ingredients
- Skin types
- Makeup routines
- Beauty tips
- Cosmetic product selection

BEHAVIOR RULES:

1. Answer in a friendly and simple way.
2. Keep answers understandable and informative.
3. If the user speaks English, reply in English.
4. If the user speaks Urdu, reply in Urdu.
5. If the user speaks Roman Urdu, reply in Roman Urdu.
6. Explain what cosmetic products do and how they are used.
7. Suggest products according to skin type, needs, and budget.
8. Do not invent product ingredients, prices, or medical claims.
9. You are an informational assistant, not a dermatologist.
10. If someone describes a serious skin reaction or medical issue,
    recommend consulting a qualified dermatologist.
11. Do not claim a product is guaranteed to work.
12. If a question is unrelated to cosmetics or beauty,
    politely explain that you are a cosmetics chatbot
    and redirect the conversation toward beauty-related topics.
13. Use emojis occasionally but do not overuse them.
14. Be helpful and conversational.
"""


# ---------------------------------
# 6. API CLIENT
# ---------------------------------
try:

    client = Groq(
        api_key=st.secrets["GROQ_API_KEY"]
    )

except Exception:

    st.error(
        "Groq API key is missing. "
        "Please add GROQ_API_KEY to your secrets."
    )

    st.stop()


# ---------------------------------
# 7. INITIALIZE CHAT HISTORY
# ---------------------------------
if "messages" not in st.session_state:

    st.session_state.messages = []


# ---------------------------------
# 8. WELCOME MESSAGE
# ---------------------------------
if len(st.session_state.messages) == 0:

    st.markdown("### 🌸 Welcome to Beauty Assistant!")

    st.info(
        "You can ask me anything about cosmetics, "
        "makeup, skincare, or beauty products."
    )

    st.markdown("#### Try asking:")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("💄 Best lipstick for dry lips")

        st.markdown("✨ What does a primer do?")

    with col2:

        st.markdown("🌸 Skincare routine for oily skin")

        st.markdown("☀️ Why should I use sunscreen?")


# ---------------------------------
# 9. DISPLAY CHAT HISTORY
# ---------------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# ---------------------------------
# 10. USER INPUT
# ---------------------------------
user_input = st.chat_input(
    "Ask me anything about cosmetics... 💗"
)


# ---------------------------------
# 11. CHAT RESPONSE
# ---------------------------------
if user_input:

    # Display user message
    with st.chat_message("user"):

        st.markdown(user_input)

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("Beauty Assistant is thinking... 💗"):

            try:

                response = client.chat.completions.create(

                    model="llama-3.3-70b-versatile",

                    messages=[
                        {
                            "role": "system",
                            "content": SYSTEM_PROMPT
                        },
                        *st.session_state.messages
                    ],

                    temperature=0.7,

                    max_tokens=800
                )

                answer = response.choices[0].message.content

                st.markdown(answer)

                # Save assistant response
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

            except Exception as e:

                st.error(
                    f"Something went wrong: {e}"
                )


# ---------------------------------
# 12. FOOTER
# ---------------------------------
st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color:#C62828;">
        <b>💗 100era & Kainat 💗</b><br>
        Beauty & Cosmetics Chatbot<br>
        Powered by Groq AI
    </div>
    """,
    unsafe_allow_html=True
)
