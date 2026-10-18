import pandas as pd
import streamlit as st
import os

# --------------------------------------------------
# BEYOND BESTSELLERS
# Transparent, rule-based fashion recommendations
# --------------------------------------------------

st.set_page_config(
    page_title="Beyond Bestsellers",
    layout="wide"
)

# --------------------------------------------------
# EDITORIAL DESIGN SYSTEM
# --------------------------------------------------

st.markdown("""
<style>

/* Streamlit top toolbar */
header[data-testid="stHeader"] {
    background-color: #282522 !important;
    height: 3.5rem !important;
}

/* Make toolbar controls readable */
header[data-testid="stHeader"] button,
header[data-testid="stHeader"] button *,
header[data-testid="stHeader"] a,
header[data-testid="stHeader"] span {
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
}

/* Overall page */
.stApp {
    background-color: #F7F3EC;
    color: #282522;
}

.block-container {
    max-width: 1440px;
    padding-top: 2.4rem;
    padding-bottom: 4rem;
}

/* Typography */
html, body {
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}

h1, h2, h3 {
    color: #282522;
    letter-spacing: -0.035em;
}

h1 {
    font-family: Georgia, "Times New Roman", serif !important;
    font-weight: 400 !important;
}

h2 {
    font-family: Georgia, "Times New Roman", serif !important;
    font-weight: 400 !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #EEE7DC;
    border-right: 1px solid #D9CFC1;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    font-family: Georgia, "Times New Roman", serif !important;
}

/* Subtle dividers */
hr {
    border-color: #D9CFC1 !important;
}

/* Buttons */
.stButton > button {
    background-color: #743D49;
    color: #FFFFFF;
    border: 1px solid #743D49;
    border-radius: 2px;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    background-color: #5D303A;
    color: #FFFFFF;
    border-color: #5D303A;
}

/* Inputs */
div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div {
    background-color: #FFFCF7;
    border-color: #D9CFC1;
    border-radius: 3px;
}

/* Metrics */
[data-testid="stMetric"] {
    background-color: #FFFCF7;
    border: 1px solid #E3DACE;
    padding: 1rem 1.1rem;
    border-radius: 3px;
}

[data-testid="stMetricLabel"] {
    color: #71685F;
    font-size: 0.82rem;
}

[data-testid="stMetricValue"] {
    color: #743D49;
    font-family: Georgia, "Times New Roman", serif;
}


}

/* Product photos */
[data-testid="stImage"] img {
    border-radius: 2px;
}

/* Expanders */
[data-testid="stExpander"] {
    border-color: #D9CFC1;
    border-radius: 3px;
}

/* Captions */
.stCaption, [data-testid="stCaptionContainer"] {
    color: #766D64;
}

/* Links */
a {
    color: #743D49 !important;
}

/* Keep layout comfortable on smaller screens */
@media (max-width: 768px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
        padding-top: 1.2rem;
    }
}

/* Make sidebar text easy to read */
[data-testid="stSidebar"] {
    background-color: #F1EAE2;
}

[data-testid="stSidebar"] label,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #282522 !important;
}

[data-testid="stSidebar"] input,
[data-testid="stSidebar"] [data-baseweb="select"] {
    color: #282522 !important;
}


/* Improve sidebar control contrast */
[data-testid="stSidebar"] [data-baseweb="select"] *,
[data-testid="stSidebar"] [data-baseweb="slider"] *,
[data-testid="stSidebar"] [data-testid="stWidgetLabel"] * {
    color: #282522 !important;
}

[data-testid="stSidebar"] [data-baseweb="select"] > div {
    background-color: #FFFCF7 !important;
}



/* Fix the two sidebar dropdowns */
[data-testid="stSidebar"] [data-testid="stSelectbox"] div[data-baseweb="select"] > div {
    background-color: #FFFCF7 !important;
    border-color: #D9CFC1 !important;
}

[data-testid="stSidebar"] [data-testid="stSelectbox"] div[data-baseweb="select"] * {
    color: #282522 !important;
    -webkit-text-fill-color: #282522 !important;
}

/* Keep dropdown option menus readable */
[data-baseweb="popover"] [role="option"] {
    color: #282522 !important;
    background-color: #FFFCF7 !important;
}


</style>
""", unsafe_allow_html=True)




# --------------------------------------------------
# EDITORIAL HERO
# --------------------------------------------------

st.markdown("""
<div style="padding: 24px 0; border-top: 1px solid #BFB1A1; border-bottom: 1px solid #BFB1A1;">
    <p style="color: #743D49; font-size: 12px; letter-spacing: 3px;">
        INDEPENDENT FASHION DISCOVERY · STUDENT RESEARCH 2026
    </p>
    <h1 style="font-family: Georgia, serif; font-size: 56px; font-weight: normal; color: #282522; line-height: 1.15;">
        Beyond <span style="color: #743D49;">Bestsellers.</span>
    </h1>
    <p style="font-family: Georgia, serif; font-size: 22px; color: #514941;">
        Less scrolling. More personal style.
    </p>
    <p style="font-size: 15px; color: #514941; line-height: 1.8;">
        Discover fashion around your style, your plans, and your budget.
        Explore transparent recommendations built with Python, pandas,
        Streamlit, and explainable rules — not a trained AI model.
    </p>
</div>
""", unsafe_allow_html=True)



# --------------------------------------------------
# 1. SAMPLE PRODUCT CATALOG
# --------------------------------------------------

products = pd.DataFrame([
    {
        "product": "Pookiie Solid Wrap Top",
        "image": "images/pookiiw.png",
        "platform": "Myntra",
        "price": 551,
        "category": "Western",
        "tags": ["solid", "wrap"],
        "occasions": ["Everyday university wear", "Casual everyday"],
        "versatile": True,
        "rating": "4.0 (about 1.6K reviews)",
        "evidence_note": "Rating and review count recorded during research"
    },
    {
        "product": "Aaghnya Ethnic Motifs Printed Kurti",
        "image": "images/aaghnya.png",
        "platform": "Myntra",
        "price": 564,
        "category": "Indian",
        "tags": ["printed", "motif_pattern"],
        "occasions": ["Everyday university wear", "Casual everyday"],
        "versatile": True,
        "rating": "4.1 (475 reviews)",
        "evidence_note": "Rating and review count recorded during research"
    },
    {
        "product": "Wardrobe by Westside Black Solid Mock-Neck Top",
        "image": "images/Wardrobe.png",
        "platform": "Tata CLiQ",
        "price": 799,
        "category": "Western",
        "tags": ["solid", "mock_neck"],
        "occasions": ["Everyday university wear", "Casual everyday"],
        "versatile": True,
        "rating": "5.0 (1 review)",
        "evidence_note": "Only one review was recorded"
    },
    {
        "product": "Soch Pink Rayon Tunic",
        "image": "images/Soch_Pink.png",
        "platform": "Tata CLiQ",
        "price": 719,
        "category": "Indian",
        "tags": ["tunic", "solid"],
        "occasions": ["Everyday university wear", "Casual everyday"],
        "versatile": True,
        "rating": "No rating recorded",
        "evidence_note": "No rating was visible on the captured product card"
    },
    {
        "product": "Outzidr Cape-Style Draped Top",
        "image": "images/Outzidr.png",
        "platform": "Tata CLiQ",
        "price": 999,
        "category": "Western",
        "tags": ["solid", "cape_style", "draped"],
        "occasions": ["Casual everyday"],
        "versatile": False,
        "rating": "Not verified",
        "evidence_note": "Rating information requires verification"
    },
    {
        "product": "Biba Embroidered A-Line Kurta",
        "image": "images/Biba.png",
        "platform": "Tata CLiQ",
        "price": 899,
        "category": "Indian",
        "tags": ["embroidered", "a_line"],
        "occasions": ["Festive/traditional"],
        "versatile": False,
        "rating": "Not verified",
        "evidence_note": "Rating information requires verification"
    },
    {
        "product": "Arbiter Collection Solid Top",
        "image": "images/Arbiter.png",
        "platform": "Myntra",
        "price": 790,
        "category": "Western",
        "tags": ["solid", "jacket_like", "statement_buttons"],
        "occasions": ["Casual everyday"],
        "versatile": False,
        "rating": "Not verified",
        "evidence_note": "Rating information requires verification"
    },
    {
        "product": "rarethread Mustard Kurta",
        "image": "images/rarethread.png",
        "platform": "Myntra",
        "price": 560,
        "category": "Indian",
        "tags": ["decorative_neckline", "decorative_border"],
        "occasions": ["Festive/traditional"],
        "versatile": False,
        "rating": "Not verified",
        "evidence_note": "Rating information requires verification"
    }
])

# These are illustrative, manually assigned labels.
# They are not verified claims about comfort or quality.

# --------------------------------------------------
# 2. SHOPPER PREFERENCES
# --------------------------------------------------

st.sidebar.header("Your shopping preferences")

budget = st.sidebar.slider(
    "Maximum budget (₹)",
    min_value=300,
    max_value=3000,
    value=1500,
    step=50
)
min_col, max_col = st.sidebar.columns(2)

with min_col:
    st.markdown("300")

with max_col:
    st.markdown(
        "<div style='text-align: right;'>3000</div>",
        unsafe_allow_html=True
    )

category = st.sidebar.selectbox(
    "What are you shopping for?",
    ["Everything", "Western", "Indian"]
)

occasion = st.sidebar.selectbox(
    "Where would you wear it?",
    [
        "Everyday university wear",
        "Casual everyday",
        "Festive/traditional"
    ]
)

st.sidebar.caption(
    "Occasion labels are manually assigned examples, "
    "not independently verified product claims."
)

preferred_tags = st.sidebar.multiselect(
    "Styles you prefer",
    options=[
        "solid",
        "wrap",
        "printed",
        "motif_pattern",
        "mock_neck",
        "tunic",
        "draped",
        "a_line"
    ],
    default=["solid"],
    format_func=lambda tag: tag.replace("_", " ").title()
)

avoided_tags = st.sidebar.multiselect(
    "Styles you want to avoid",
    options=[
        "cape_style",
        "jacket_like",
        "embroidered",
        "decorative_neckline",
        "decorative_border",
        "statement_buttons"
    ],
    format_func=lambda tag: tag.replace("_", " ").title()
)

prioritize_versatility = st.sidebar.checkbox(
    "Prioritize versatile pieces",
    value=True,
    help="Give one extra point to products manually labelled versatile."
)

# --------------------------------------------------
# 3. EXPLAINABLE SCORING FUNCTION
# --------------------------------------------------

def score_product(
        product,
        preferred,
        avoided,
        selected_occasion,
        prioritize_versatile
):
    """Score a product using explicit, explainable rules."""

    score = 0
    matched = []
    conflicts = []
    reasons = []

    # Rule 1: Preferred styles earn two points each.
    for tag in preferred:
        if tag in product["tags"]:
            score += 2
            matched.append(tag)
            reasons.append(
                f"+2: Matches preferred style '{tag.replace('_', ' ')}'"
            )

    # Rule 2: Avoided styles lose two points each.
    for tag in avoided:
        if tag in product["tags"]:
            score -= 2
            conflicts.append(tag)
            reasons.append(
                f"-2: Contains avoided style '{tag.replace('_', ' ')}'"
            )

    # Rule 3: Matching the selected occasion earns two points.
    if selected_occasion in product["occasions"]:
        score += 2
        reasons.append("+2: Matches the selected occasion")
    else:
        reasons.append(
            "0: No match for the selected occasion in the sample labels"
        )

    # Rule 4: Versatility earns one optional point.
    if prioritize_versatile and product["versatile"]:
        score += 1
        reasons.append("+1: Labelled versatile in the sample dataset")

    if not matched:
        reasons.append("No preferred style tags matched")

    if not conflicts:
        reasons.append("No avoided style tags matched")

    return {
        "score": score,
        "matched": matched,
        "conflicts": conflicts,
        "reasons": reasons
    }


# --------------------------------------------------
# 4. FILTER PRODUCTS AND RANK RESULTS
# --------------------------------------------------

results = products.copy()

# Budget is a strict filter.
results = results[results["price"] <= budget].copy()

# Apply the selected category.
if category != "Everything":
    results = results[results["category"] == category].copy()


# Exclude products matching any avoided style.
if avoided_tags:
    results = results[
        ~results["tags"].apply(
            lambda tags: any(tag in tags for tag in avoided_tags)
        )
    ].copy()


# Calculate how much of the budget remains.
results["budget_remaining"] = budget - results["price"]

# Calculate scores and explanations for every remaining product.
details = [
    score_product(
        product,
        preferred_tags,
        avoided_tags,
        occasion,
        prioritize_versatility
    )
    for _, product in results.iterrows()
]

results["preference_score"] = [
    item["score"] for item in details
]

results["matched_preferences"] = [
    item["matched"] for item in details
]

results["conflicting_preferences"] = [
    item["conflicts"] for item in details
]

results["scoring_reasons"] = [
    item["reasons"] for item in details
]

# --------------------------------------------------
# 5. DISPLAY RECOMMENDATIONS
# --------------------------------------------------

st.markdown("""
<div style="margin: 2.5rem 0 1rem 0;">
    <div style="
        color: #743D49;
        font-size: 0.72rem;
        letter-spacing: 0.17em;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
    ">
        Curated for your preferences
    </div>
    <h2 style="
        font-family: Georgia, 'Times New Roman', serif;
        font-size: 2.4rem;
        font-weight: 400;
        margin: 0;
        letter-spacing: -0.04em;
    ">
        Your edit
    </h2>
    <p style="color: #766D64; margin-top: 0.5rem;">
        Every match is ranked by your selected preferences,
        with the reasoning visible to you.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Products within your filters", len(results))

with col2:
    st.metric("Your budget", f"₹{budget:,}")

with col3:
    if not results.empty:
        st.metric(
            "Lowest matching price",
            f"₹{results['price'].min():,}"
        )
    else:
        st.metric("Lowest matching price", "—")

st.caption(
    "Ranking reflects the selected rules and manually assigned labels. "
    "It is not a ranking of product quality or popularity."
)

if results.empty:
    st.warning(
        "No products match your budget and category. "
        "Try increasing your budget or changing your category."
    )

else:
    # Show the highest-scoring matches first.
    results = results.sort_values(
        by="preference_score",
        ascending=False,
        kind="stable"
    )

    for _, product in results.iterrows():
        with st.container(border=True):
            image_col, left, right = st.columns(
                [1.4, 3, 1.2],
                gap="large"
            )

            with image_col:
                image_path = product.get("image", "")

                # Some products do not have image paths yet.
                if (
                        isinstance(image_path, str)
                        and image_path
                        and os.path.isfile(image_path)
                ):
                    st.image(
                        image_path,
                        use_container_width=True
                    )
                else:
                    st.caption("Product image unavailable")

            with left:
                st.subheader(product["product"])

                st.write(f"**Platform:** {product['platform']}")
                st.write(f"**Category:** {product['category']}")
                st.write(f"**Recorded rating:** {product['rating']}")
                st.write(f"**Selected occasion:** {occasion}")

                if product["matched_preferences"]:
                    readable_matches = [
                        tag.replace("_", " ").title()
                        for tag in product["matched_preferences"]
                    ]
                    st.write(
                        "**Matched styles:** "
                        + ", ".join(readable_matches)
                    )

                if product["conflicting_preferences"]:
                    readable_conflicts = [
                        tag.replace("_", " ").title()
                        for tag in product["conflicting_preferences"]
                    ]
                    st.write(
                        "**Styles to reconsider:** "
                        + ", ".join(readable_conflicts)
                    )

                with st.expander(
                        "Why did this product receive this score?"
                ):
                    for reason in product["scoring_reasons"]:
                        st.markdown(f"- {reason}")

                    st.caption(product["evidence_note"])

                    st.caption(
                        "Comfort, fabric quality, fit and current "
                        "availability have not been independently verified."
                    )

            with right:
                st.metric("Price", f"₹{product['price']:,}")

                st.write(
                    f"Budget remaining: ₹"
                    f"{product['budget_remaining']:,}"
                )

                st.metric(
                    "Preference score",
                    product["preference_score"]
                )


# --------------------------------------------------
# 6. VIEW PRODUCT DATA
# --------------------------------------------------

with st.expander("View product data and scoring details"):
    st.write(
        "This small catalog uses manually entered product records. "
        "Scores are generated using the explicit rules described above."
    )

    display_data = results[
        [
            "product",
            "platform",
            "price",
            "category",
            "tags",
            "occasions",
            "versatile",
            "budget_remaining",
            "preference_score"
        ]
    ].copy()

    for column in ["tags", "occasions"]:
        display_data[column] = display_data[column].apply(
            lambda values: ", ".join(values)
        )

    st.dataframe(
        display_data,
        use_container_width=True,
        hide_index=True
    )

# --------------------------------------------------
# 7. PROJECT LIMITATIONS AND FUTURE WORK
# --------------------------------------------------

st.divider()
st.header("About this prototype")

st.subheader("Current capabilities")

st.markdown(
    """
    - Filters products by a strict budget and clothing category.
    - Uses manually assigned occasion labels.
    - Ranks products using explicit style-matching rules.
    - Explains positive and negative scoring contributions.
    - Shows the recorded rating information and missing evidence.
    """
)

st.subheader("Current limitations")

st.markdown(
    """
    - The product catalog is small and manually entered.
    - Occasion and versatility labels require human review.
    - The prototype does not access live retailer inventories.
    - Comfort, fit and fabric quality are not inferred.
    - The score measures rule-based preference matching, not quality.
    - No trained machine-learning model or generative AI is used.
    """
)

st.subheader("Future direction")

st.write(
    "A future version could explore AI-assisted matching between "
    "natural-language shopping requests and product descriptions. "
    "That feature has not been implemented and would require a larger "
    "dataset and evaluation against this rule-based baseline."
)

st.caption(
    "Beyond Bestsellers | Student project | Python, pandas and Streamlit"
)
