import streamlit as st
from groq import Groq

# =========================================================
# 1. PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Kairaé Beauty AI",
    page_icon="💗",
    layout="wide"
)

# =========================================================
# 2. CUSTOM CSS
# =========================================================

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

h1, h2, h3 {
    color: #AD1457 !important;
}

div[data-testid="stChatMessage"] {
    background-color: #FFF5F8;
    border: 1px solid #F3B6CC;
    border-radius: 15px;
}

.stButton > button {
    background-color: #C2185B;
    color: white;
    border-radius: 10px;
    border: none;
}

.stButton > button:hover {
    background-color: #880E4F;
    color: white;
}

.stChatInput {
    border-radius: 15px;
}

.product-card {
    background-color: #FFF5F8;
    padding: 15px;
    border-radius: 15px;
    border: 1px solid #F3B6CC;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# 3. HEADER
# =========================================================


  # =========================================================
# 3. HEADER
# =========================================================

st.html("""
<div style="text-align:center;">

    <h1 style="font-family:serif; font-size:50px; color:#AD1457;">
        ✨ Kairaé ✨
    </h1>

    <h3 style="letter-spacing:4px; color:#AD1457;">
        BEAUTY AI
    </h3>

    <p style="color:#AD1457; font-size:18px;">
        Your Personal Beauty & Cosmetics Assistant
    </p>

    <p style="color:#880E4F;">
        Discover your beauty. Find your glow. 💗
    </p>

</div>
""")

st.divider()


# =========================================================
# 4. PRODUCT DATABASE
# =========================================================

PRODUCTS = [

    {
        "name": "Dermive Oil-Free Moisturizer",
        "brand": "Jenpharm",
        "price": 1098,
        "category": "Moisturizer",
        "tier": "Budget-friendly",
        "skin_types": ["Oily", "Combination", "Acne-prone"],
        "concerns": ["Oiliness", "Acne", "Dehydration"],
        "description": "Lightweight moisturizer for daily hydration.",
        "quality": "Good everyday skincare option",
        "image": (
            "https://jenpharm.com/cdn/shop/files/"
            "Dermivewash_jpg.jpg?v=1778314684"
        ),
        "url": "https://jenpharm.com/products/dermive-oil-free"
    },

    {
        "name": "Acne Control Cleanser",
        "brand": "Derma London",
        "price": 1080,
        "category": "Cleanser",
        "tier": "Budget-friendly",
        "skin_types": ["Oily", "Combination", "Acne-prone"],
        "concerns": ["Acne", "Blackheads", "Oiliness"],
        "description": "Cleanser designed for acne-prone skin.",
        "quality": "Targeted skincare option",
        "image": (
            "https://dermalondon.com.pk/cdn/shop/files/"
            "1.jpg?v=1711016939"
        ),
        "url": (
            "https://dermalondon.com.pk/products/"
            "acne-control-cleanser-150ml"
        )
    },

    {
        "name": "Acne Control Serum",
        "brand": "Derma London",
        "price": 1240,
        "category": "Serum",
        "tier": "Budget-friendly",
        "skin_types": ["Oily", "Combination", "Acne-prone"],
        "concerns": ["Acne", "Blackheads", "Oiliness"],
        "description": "Serum for blemish-prone skin.",
        "quality": "Active-ingredient-focused option",
        "image": (
            "https://dermalondon.com.pk/cdn/shop/files/"
            "1_dbf13df1-bd7f-433b-aa78-f3e775b1ad60.jpg"
            "?v=1777375582"
        ),
        "url": (
            "https://dermalondon.com.pk/"
            "collections/acne-pimples"
        )
    },

    {
        "name": "Acne & Oil Control Moisturizer",
        "brand": "Derma London",
        "price": 1190,
        "category": "Moisturizer",
        "tier": "Budget-friendly",
        "skin_types": ["Oily", "Combination", "Acne-prone"],
        "concerns": ["Acne", "Oiliness"],
        "description": "Moisturizer designed for oily and acne-prone skin.",
        "quality": "Targeted skincare option",
        "image": (
            "https://dermalondon.com.pk/cdn/shop/files/"
            "1_dbf13df1-bd7f-433b-aa78-f3e775b1ad60.jpg"
            "?v=1777375582"
        ),
        "url": (
            "https://dermalondon.com.pk/"
            "collections/acne-pimples"
        )
    },

    {
        "name": "Simple Refreshing Facial Wash",
        "brand": "Simple",
        "price": 1630,
        "category": "Cleanser",
        "tier": "Mid-range",
        "skin_types": [
            "Oily", "Combination", "Sensitive",
            "Normal", "Dry"
        ],
        "concerns": ["Sensitivity", "Oiliness", "Dryness"],
        "description": "Gentle daily facial cleanser.",
        "quality": "Gentle everyday option",
        "image": (
            "https://images.unsplash.com/"
            "photo-1608248543803-ba4f8c70ae0b"
            "?auto=format&fit=crop&w=600&q=80"
        ),
        "url": (
            "https://www.cozmetics.pk/"
            "concerns/oily-acne-prone-skin"
        )
    },

    {
        "name": "Purifying Neem Face Wash",
        "brand": "Himalaya",
        "price": 680,
        "category": "Cleanser",
        "tier": "Budget-friendly",
        "skin_types": ["Oily", "Combination"],
        "concerns": ["Oiliness", "Acne"],
        "description": "Affordable neem-based facial cleanser.",
        "quality": "Basic budget cleanser",
        "image": (
            "https://himalayausa.com/cdn/shop/files/"
            "4_714ece8d-0028-483d-9a6e-e50b7f5e1656.png"
            "?v=1770222739&width=1800"
        ),
        "url": (
            "https://www.cozmetics.pk/"
            "concerns/oily-acne-prone-skin"
        )
    },

    {
        "name": "Super Light Gel Moisturizer",
        "brand": "Pond's",
        "price": 1430,
        "category": "Moisturizer",
        "tier": "Budget-friendly",
        "skin_types": ["Oily", "Combination", "Normal"],
        "concerns": ["Oiliness", "Dehydration"],
        "description": "Lightweight gel moisturizer.",
        "quality": "Lightweight daily hydration",
        "image": (
            "https://highfy.pk/cdn/shop/files/"
            "3_345886c6-d158-4bb4-bdc8-68da4a03da1f.webp"
            "?v=1784715502&width=1200"
        ),
        "url": (
            "https://www.cozmetics.pk/"
            "concerns/oily-acne-prone-skin"
        )
    },

    {
        "name": "Niacinamide 10% + Zinc 1%",
        "brand": "The Ordinary",
        "price": 2699,
        "category": "Serum",
        "tier": "Mid-range",
        "skin_types": ["Oily", "Combination"],
        "concerns": ["Oiliness", "Acne marks"],
        "description": (
            "Niacinamide serum for oiliness "
            "and the appearance of blemishes."
        ),
        "quality": "Concentrated active formula",
        "image": (
            "https://adminbeauty.hvnet.vn/Upload/Files/"
            "the-ordinary-niacinamide-10-zinc-1-30ml.jpg"
        ),
        "url": (
            "https://www.cozmetics.pk/"
            "concerns/oily-acne-prone-skin"
        )
    },

    {
        "name": "Acne Control Kit",
        "brand": "Derma London",
        "price": 3370,
        "category": "Skincare Kit",
        "tier": "Mid-range",
        "skin_types": ["Oily", "Combination", "Acne-prone"],
        "concerns": ["Acne", "Blackheads", "Oiliness"],
        "description": "A skincare kit for acne-prone skin.",
        "quality": "Multi-product skincare routine",
        "image": (
            "https://dermalondon.com.pk/cdn/shop/files/"
            "1_dbf13df1-bd7f-433b-aa78-f3e775b1ad60.jpg"
            "?v=1777375582"
        ),
        "url": (
            "https://dermalondon.com.pk/"
            "collections/acne-pimples"
        )
    }
]


# =========================================================
# 5. SIDEBAR - USER PROFILE
# =========================================================

with st.sidebar:

    st.markdown("## 🌸 Skin Profile")

    skin_type = st.selectbox(
        "Select your skin type",
        [
            "Oily",
            "Dry",
            "Combination",
            "Normal",
            "Sensitive",
            "Acne-prone"
        ]
    )

    skin_tone = st.selectbox(
        "Select your skin tone",
        [
            "Fair",
            "Light",
            "Medium",
            "Wheatish",
            "Tan",
            "Deep",
            "Dark",
            "Not sure"
        ]
    )

    concerns = st.multiselect(
        "Your skin concerns",
        [
            "Acne",
            "Blackheads",
            "Dark spots",
            "Oiliness",
            "Dryness",
            "Sensitivity",
            "Uneven skin tone",
            "Dullness",
            "Dehydration"
        ]
    )

    budget = st.selectbox(
        "Your budget",
        [
            "Budget-friendly",
            "Mid-range",
            "Premium",
            "Any budget"
        ]
    )

    st.markdown("---")

    st.markdown("## 💄 Makeup")

    makeup_interest = st.checkbox(
        "Show makeup recommendations"
    )

    st.markdown("---")

    if st.button("🗑️ Clear Conversation", use_container_width=True):

        st.session_state.messages = []
        st.rerun()

    st.markdown("""
    <div style="text-align:center;">
        <b>Kairaé Beauty AI 💗</b>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# 6. PRODUCT FILTERING
# =========================================================

def recommend_products(skin_type, concerns, budget):

    recommendations = []

    for product in PRODUCTS:

        skin_match = skin_type in product["skin_types"]

        if concerns:
            concern_match = any(
                concern in product["concerns"]
                for concern in concerns
            )
        else:
            concern_match = True

        if budget == "Budget-friendly":
            budget_match = product["price"] <= 1500

        elif budget == "Mid-range":
            budget_match = 1500 < product["price"] <= 4000

        elif budget == "Premium":
            budget_match = product["price"] > 4000

        else:
            budget_match = True

        if skin_match and concern_match and budget_match:
            recommendations.append(product)

    return recommendations


# =========================================================
# 7. PRODUCT DISPLAY
# =========================================================

def display_products(products):

    if not products:

        st.warning(
            "No products found for your selected profile. "
            "Try changing your skin concerns or budget."
        )
        return

    columns = st.columns(3)

    for index, product in enumerate(products):

        with columns[index % 3]:

            with st.container(border=True):

                st.image(
                    product["image"],
                    use_container_width=True
                )

                st.caption(product["brand"])

                st.subheader(product["name"])

                st.markdown(
                    f"### Rs. {product['price']:,}"
                )

                st.success(product["tier"])

                st.write(product["description"])

                st.write(
                    f"**Category:** {product['category']}"
                )

                st.write(
                    f"**Quality:** {product['quality']}"
                )

                st.write(
                    "**Suitable for:** "
                    + ", ".join(product["skin_types"])
                )

                st.link_button(
                    "🛍️ View Product",
                    product["url"],
                    use_container_width=True
                )


# =========================================================
# 8. PRODUCT RECOMMENDATIONS
# =========================================================

st.markdown("## 🌷 Recommended Products")

st.caption(
    "Recommendations based on your selected skin type, "
    "concerns, and budget."
)

recommended_products = recommend_products(
    skin_type,
    concerns,
    budget
)

display_products(recommended_products)

st.divider()


# =========================================================
# 9. GROQ API
# =========================================================

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


# =========================================================
# 10. SYSTEM PROMPT
# =========================================================

SYSTEM_PROMPT = f"""
You are Kairaé, an intelligent and friendly
AI beauty and cosmetics assistant.

You specialize in Pakistani skincare,
cosmetics, makeup, and beauty products.

USER PROFILE:

Skin type: {skin_type}
Skin tone: {skin_tone}
Skin concerns: {concerns}
Budget: {budget}
Interested in makeup: {makeup_interest}

PRODUCT DATABASE:

{PRODUCTS}

INSTRUCTIONS:

1. Recommend products according to the user's skin type,
   concerns, skin tone, and budget.

2. Prioritize Pakistani products and products
   available in Pakistan.

3. Explain why each recommended product is suitable.

4. For oily and acne-prone skin:
   Suggest gentle cleansers, lightweight moisturizers,
   and suitable acne-care ingredients.

5. For dry skin:
   Suggest hydrating cleansers and moisturizers.

6. For sensitive skin:
   Suggest gentle products and patch testing.

7. Skin tone is important for foundation, concealer,
   blush, and lipstick recommendations.
   Do not use skin tone to recommend skincare.

8. Suggest budget-friendly products when the user
   has selected a low budget.

9. Categorize products as budget-friendly,
   mid-range, or premium.

10. Never call a cheap product low quality
    simply because of its price.

11. Do not invent product prices or ingredients.

12. The product prices in the database are approximate.
    Explain that prices can change.

13. Recommend products from the provided database
    when possible.

14. Do not claim that products cure acne or skin diseases.

15. Do not diagnose medical conditions.

16. Recommend a dermatologist for severe,
    painful, persistent acne or skin reactions.

17. Keep answers friendly, clear, and easy to understand.

18. Reply in the language used by the user:
    English, Urdu, or Roman Urdu.

19. When creating skincare routines,
    separate morning and night routines.

20. Avoid recommending too many active ingredients
    at the same time.

21. Always encourage patch testing new products.

22. If a question is unrelated to cosmetics,
    politely redirect the user to beauty-related topics.
"""


# =========================================================
# 11. INITIALIZE CHAT HISTORY
# =========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# =========================================================
# 12. WELCOME SCREEN
# =========================================================

if len(st.session_state.messages) == 0:

    st.markdown("## 💗 Welcome to Kairaé!")

    st.write(
        "Your personal beauty assistant is here "
        "to help you discover skincare, makeup, "
        "and products suitable for your skin."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.info(
            "🌸 What products are best for oily skin?"
        )

        st.info(
            "💄 Which foundation suits wheatish skin?"
        )

    with col2:

        st.info(
            "✨ Suggest a skincare routine for acne."
        )

        st.info(
            "💗 Recommend affordable Pakistani products."
        )


# =========================================================
# 13. DISPLAY CHAT HISTORY
# =========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# =========================================================
# 14. CHAT INPUT
# =========================================================

user_input = st.chat_input(
    "Ask Kairaé about beauty, skincare, or makeup... 💗"
)


# =========================================================
# 15. AI CHAT
# =========================================================

if user_input:

    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("assistant"):

        with st.spinner("Kairaé is thinking... 🌸"):

            try:

                response = client.chat.completions.create(

                    model="openai/gpt-oss-120b",

                    messages=[
                        {
                            "role": "system",
                            "content": SYSTEM_PROMPT
                        },
                        *st.session_state.messages
                    ],

                    temperature=0.5,

                    max_tokens=1000
                )

                answer = (
                    response.choices[0]
                    .message.content
                )

                st.markdown(answer)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

            except Exception as error:

                st.error(
                    f"Something went wrong: {error}"
                )


# =========================================================
# 16. FOOTER
# =========================================================

# =========================================================
# 16. FOOTER
# =========================================================

st.markdown("---")

st.html("""
<div style="text-align:center; padding:15px;">

    <h3 style="color:#AD1457;">
        ✨ Kairaé Beauty AI ✨
    </h3>

    <p style="color:#AD1457;">
        Your beauty. Your confidence. Your glow. 💗
    </p>

    <p style="font-size:13px; color:#880E4F;">
        AI-powered cosmetics and skincare assistant
    </p>

</div>
""")
