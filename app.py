import streamlit as st
import pandas as pd
import joblib


# এখানে আপনার Facebook প্রোফাইলের লিংক বসান।
FACEBOOK_URL = "https://www.facebook.com/takdir2006"


st.set_page_config(
    page_title="Heart Check • AZ TAKDIR",
    page_icon="♡",
    layout="centered",
)


st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@400;500;600;700;800&family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&display=swap');

    /* ---------- APP ---------- */

    .stApp {
        color: #30283d;
        color-scheme: light;
        font-family: "Bricolage Grotesque", sans-serif;
        background:
            radial-gradient(
                ellipse at 8% 8%,
                rgba(255, 203, 174, 0.43),
                transparent 43%
            ),
            radial-gradient(
                ellipse at 92% 38%,
                rgba(209, 190, 247, 0.39),
                transparent 45%
            ),
            radial-gradient(
                ellipse at 35% 95%,
                rgba(196, 225, 211, 0.30),
                transparent 42%
            ),
            #fbf9f6;
        background-size: 145% 145%;
        animation: background-drift 20s ease-in-out infinite alternate;
    }

    .stApp p,
    .stApp label,
    .stApp input,
    .stApp textarea,
    .stApp select,
    .stApp button,
    .stApp [data-baseweb="select"] {
        font-family:
            "Bricolage Grotesque",
            "Trebuchet MS",
            sans-serif !important;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    .block-container {
        max-width: 1000px;
        padding-top: 1rem !important;
        padding-bottom: 1.8rem;
    }

    /* ---------- BRAND ---------- */

    .brand-bar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 12px;
        padding: 8px 0 18px;
        border-bottom: 1px solid #e9e2da;
        margin-bottom: 23px;
        animation: enter-up 650ms ease-out both;
    }

    .brand-name {
        display: flex;
        align-items: center;
        gap: 10px;
        color: #303148;
        font-family: "Fraunces", Georgia, serif;
        font-size: 1.3rem;
        font-weight: 600;
        letter-spacing: -0.04em;
    }

    .brand-icon {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 36px;
        height: 36px;
        border-radius: 12px;
        background: #fbe1d8;
        color: #bd563e;
        font-family: Georgia, serif;
        font-size: 1.6rem;
        animation: heartbeat 3.2s ease-in-out infinite;
    }

    .brand-credit {
        color: #777184;
        font-family: "Bricolage Grotesque", sans-serif;
        font-size: 0.8rem;
    }

    /* ---------- HERO ---------- */

    .hero {
        padding: 3px 0 19px;
        animation: enter-up 800ms ease-out both;
    }

    .hero-tag {
        display: inline-block;
        padding: 7px 12px;
        margin-bottom: 16px;
        border: 1px solid rgba(128, 97, 178, 0.12);
        border-radius: 999px;
        background: #eee8fc;
        color: #7452aa;
        font-family: "Bricolage Grotesque", sans-serif;
        font-size: 0.76rem;
        font-weight: 600;
        letter-spacing: 0.025em;
        animation: tag-glow 4s ease-in-out infinite;
    }

    .hero h1 {
        margin: 0 !important;
        padding: 0 0 17px !important;
        color: #2d2d43 !important;
        font-family: "Fraunces", Georgia, serif !important;
        font-optical-sizing: auto;
        font-size: clamp(2.8rem, 6.8vw, 4.7rem) !important;
        font-weight: 600 !important;
        line-height: 1.08 !important;
        letter-spacing: -0.055em !important;
        animation: heading-reveal 950ms ease-out both;
    }

    .hero h1 .coral,
    .hero h1 .purple {
        display: inline-block;
        transition:
            transform 350ms ease,
            text-shadow 350ms ease;
    }

    .hero h1 .coral {
        color: #c85f49;
    }

    .hero h1 .purple {
        color: #8061b2;
    }

    .hero h1 .coral:hover {
        transform: translateY(-4px) rotate(-2deg);
        text-shadow: 0 8px 23px rgba(200, 95, 73, 0.20);
    }

    .hero h1 .purple:hover {
        transform: translateY(-4px) rotate(2deg);
        text-shadow: 0 8px 23px rgba(128, 97, 178, 0.20);
    }

    .hero-description {
        max-width: 570px;
        margin: 0;
        color: #797384;
        font-size: 1.04rem;
        line-height: 1.75;
    }

    /* ---------- SECTION CARDS ---------- */

    [data-testid="stVerticalBlockBorderWrapper"]:has(
        .section-heading
    ),
    [data-testid="stVerticalBlock"]:has(
        > [data-testid="stElementContainer"] .section-heading
    ) {
        border-radius: 20px !important;
        background: rgba(255, 255, 255, 0.62);
        box-shadow: 0 7px 25px rgba(62, 42, 80, 0.035);
        animation: enter-up 800ms ease-out both;
        transition:
            box-shadow 300ms ease,
            border-color 300ms ease;
    }

    [data-testid="stVerticalBlockBorderWrapper"]:has(
        .section-heading
    ):hover,
    [data-testid="stVerticalBlock"]:has(
        > [data-testid="stElementContainer"] .section-heading
    ):hover {
        border-color: rgba(151, 113, 182, 0.40) !important;
        box-shadow: 0 15px 35px rgba(62, 42, 80, 0.08);
    }

    .section-heading {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 6px;
        font-family: "Fraunces", Georgia, serif;
        font-size: 1.45rem;
        font-weight: 600;
        letter-spacing: -0.035em;
    }

    .section-number {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        width: 30px;
        height: 30px;
        border-radius: 10px;
        font-family: "Bricolage Grotesque", sans-serif;
        font-size: 0.77rem;
        font-weight: 700;
        transition:
            transform 300ms ease,
            box-shadow 300ms ease;
    }

    .section-heading:hover .section-number {
        transform: rotate(-9deg) scale(1.1);
        box-shadow: 0 5px 13px rgba(106, 73, 137, 0.12);
    }

    .personal-heading {
        color: #ad513f;
    }

    .personal-heading .section-number {
        background: #fbe4dc;
        color: #ad513f;
    }

    .clinical-heading {
        color: #7655a7;
    }

    .clinical-heading .section-number {
        background: #eee6fb;
        color: #7655a7;
    }

    .section-description {
        margin: 0 0 16px;
        color: #847e8b;
        font-family: "Bricolage Grotesque", sans-serif;
        font-size: 0.86rem;
        line-height: 1.6;
    }

    /* ---------- INPUT LABELS ---------- */

    [data-testid="stWidgetLabel"] p {
        color: #51475e !important;
        font-size: 0.94rem !important;
        font-weight: 600 !important;
    }

    /* ---------- NUMBER INPUT CONTRAST ---------- */

    .stApp [data-testid="stNumberInput"] {
        color-scheme: light;
    }

    .stApp [data-testid="stNumberInput"] > div,
    .stApp [data-testid="stNumberInput"] [data-baseweb="input"],
    .stApp [data-testid="stNumberInput"] [data-baseweb="base-input"] {
        background: #ffffff !important;
        background-color: #ffffff !important;
        color: #30283d !important;
        border-radius: 12px !important;
    }

    .stApp [data-testid="stNumberInput"] > div {
        border: 1px solid #d9cde5 !important;
        overflow: hidden;
        box-shadow: 0 3px 9px rgba(71, 45, 97, 0.035);
        transition:
            border-color 220ms ease,
            box-shadow 220ms ease;
    }

    .stApp [data-testid="stNumberInput"] input {
        background: #ffffff !important;
        background-color: #ffffff !important;
        color: #30283d !important;
        -webkit-text-fill-color: #30283d !important;
        caret-color: #72509b !important;
        font-size: 1.08rem !important;
        font-weight: 600 !important;
        opacity: 1 !important;
    }

    .stApp [data-testid="stNumberInput"] button {
        background: #f1eaf8 !important;
        background-color: #f1eaf8 !important;
        color: #65438e !important;
        border: none !important;
        transition:
            background 180ms ease,
            color 180ms ease;
    }

    .stApp [data-testid="stNumberInput"] button svg {
        color: #65438e !important;
        fill: currentColor !important;
    }

    .stApp [data-testid="stNumberInput"] button:hover {
        background: #e3d4f1 !important;
        color: #40245f !important;
    }

    .stApp [data-testid="stNumberInput"] > div:focus-within {
        border-color: #9872bd !important;
        box-shadow: 0 0 0 4px rgba(144, 103, 183, 0.14);
    }

    /* ---------- DROPDOWNS ---------- */

    .stApp [data-baseweb="select"] > div {
        background: #ffffff !important;
        color: #30283d !important;
        border: 1px solid #ded3e8 !important;
        border-radius: 12px !important;
        transition:
            border-color 220ms ease,
            box-shadow 220ms ease;
    }

    .stApp [data-baseweb="select"] span,
    .stApp [data-baseweb="select"] input,
    .stApp [data-baseweb="select"] [role="combobox"] {
        color: #30283d !important;
        -webkit-text-fill-color: #30283d !important;
    }

    .stApp [data-baseweb="select"] svg {
        color: #76549a !important;
    }

    .stApp [data-baseweb="select"] > div:focus-within {
        border-color: #9872bd !important;
        box-shadow: 0 0 0 4px rgba(144, 103, 183, 0.12);
    }

    [data-baseweb="popover"] [role="listbox"] {
        background: #ffffff !important;
        color: #30283d !important;
        font-family: "Bricolage Grotesque", sans-serif !important;
    }

    [data-baseweb="popover"] [role="option"] {
        background: #ffffff !important;
        color: #30283d !important;
    }

    [data-baseweb="popover"] [role="option"]:hover,
    [data-baseweb="popover"] [role="option"][aria-selected="true"] {
        background: #eee6f8 !important;
    }

    /* ---------- SLIDERS ---------- */

    [data-testid="stSlider"] {
        padding-bottom: 8px;
    }

    [data-testid="stSlider"] [role="slider"] {
        background-color: #9471b9 !important;
        box-shadow: 0 0 0 4px rgba(148, 113, 185, 0.12);
        transition: box-shadow 180ms ease;
    }

    [data-testid="stSlider"] [role="slider"]:hover,
    [data-testid="stSlider"] [role="slider"]:focus-visible {
        box-shadow: 0 0 0 8px rgba(148, 113, 185, 0.20);
    }

    /* ---------- PREDICTION BUTTON ---------- */

    .stButton > button {
        position: relative;
        isolation: isolate;
        overflow: hidden;
        min-height: 56px;
        margin-top: 10px;
        border: none !important;
        border-radius: 14px;
        color: #ffffff !important;
        background: linear-gradient(
            115deg,
            #72509b,
            #946bb2,
            #72509b
        ) !important;
        background-size: 200% 100% !important;
        box-shadow: 0 6px 16px rgba(114, 80, 155, 0.18);
        animation: button-gradient 6s ease-in-out infinite;
        transition:
            transform 220ms ease,
            box-shadow 220ms ease;
    }

    .stButton > button::before {
        content: "";
        position: absolute;
        top: 0;
        left: -65%;
        width: 42%;
        height: 100%;
        background: linear-gradient(
            90deg,
            transparent,
            rgba(255, 255, 255, 0.25),
            transparent
        );
        transform: skewX(-20deg);
        pointer-events: none;
        animation: button-shine 5.5s ease-in-out infinite;
    }

    .stButton > button p {
        position: relative;
        z-index: 1;
        color: #ffffff !important;
        font-size: 1.12rem !important;
        font-weight: 700 !important;
    }

    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 27px rgba(114, 80, 155, 0.27);
    }

    .stButton > button:active {
        transform: translateY(0) scale(0.99);
    }

    /* ---------- RESULT ---------- */

    .result-card {
        position: relative;
        overflow: hidden;
        margin: 18px 0 8px;
        padding: 25px;
        border: 1px solid;
        border-radius: 19px;
        animation: result-reveal 750ms cubic-bezier(.2,.8,.2,1) both;
    }

    .result-card.high {
        background: #fff0e9;
        border-color: #f0cbb9;
        color: #914e36;
    }

    .result-card.low {
        background: #eaf4ef;
        border-color: #c9dfd1;
        color: #33664e;
    }

    .result-eyebrow {
        margin-bottom: 9px;
        font-family: "Bricolage Grotesque", sans-serif;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.12em;
    }

    .result-title {
        margin-bottom: 11px;
        font-family: "Fraunces", Georgia, serif;
        font-size: 1.95rem;
        font-weight: 600;
        line-height: 1.2;
        letter-spacing: -0.04em;
    }

    .result-description {
        font-family: "Bricolage Grotesque", sans-serif;
        font-size: 0.92rem;
        line-height: 1.75;
    }

    /* ---------- FOOTER ---------- */

    .footer {
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 12px;
        margin-top: 30px;
        padding-top: 18px;
        border-top: 1px solid #e9e2da;
        color: #827988;
        font-family: "Bricolage Grotesque", sans-serif;
        font-size: 0.79rem;
    }

    .footer a {
        display: inline-block;
        color: #76529d !important;
        text-decoration: none !important;
        transition:
            color 220ms ease,
            transform 220ms ease;
    }

    .footer a:hover {
        color: #ba5c47 !important;
        transform: translateY(-2px);
        text-decoration: underline !important;
        text-underline-offset: 5px;
    }

    /* ---------- ANIMATION KEYFRAMES ---------- */

    @keyframes enter-up {
        from {
            opacity: 0;
            transform: translateY(18px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes heading-reveal {
        from {
            opacity: 0;
            transform: translateY(22px);
            filter: blur(5px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
            filter: blur(0);
        }
    }

    @keyframes background-drift {
        from {
            background-position: 0% 0%;
        }
        to {
            background-position: 100% 75%;
        }
    }

    @keyframes heartbeat {
        0%, 38%, 64%, 100% {
            transform: scale(1);
        }
        45%, 56% {
            transform: scale(1.12);
        }
        50% {
            transform: scale(1.025);
        }
    }

    @keyframes tag-glow {
        0%, 100% {
            box-shadow: 0 0 0 0 rgba(128, 97, 178, 0);
        }
        50% {
            box-shadow: 0 0 0 7px rgba(128, 97, 178, 0.065);
        }
    }

    @keyframes button-gradient {
        0%, 100% {
            background-position: 0% 50%;
        }
        50% {
            background-position: 100% 50%;
        }
    }

    @keyframes button-shine {
        0%, 60% {
            left: -65%;
        }
        90%, 100% {
            left: 140%;
        }
    }

    @keyframes result-reveal {
        from {
            opacity: 0;
            transform: translateY(18px) scale(0.97);
        }
        to {
            opacity: 1;
            transform: translateY(0) scale(1);
        }
    }

    /* ---------- MOBILE ---------- */

    @media (max-width: 640px) {
        .block-container {
            padding-top: 0.7rem !important;
        }

        .brand-bar {
            margin-bottom: 19px;
        }

        .brand-name {
            font-size: 1.15rem;
        }

        .brand-credit {
            font-size: 0.71rem;
        }

        .hero h1 {
            font-size: 3rem !important;
        }

        .section-heading {
            font-size: 1.3rem;
        }

        .footer {
            align-items: flex-start;
            flex-direction: column;
        }
    }

    /* Respect the device's reduced-motion preference. */

    @media (prefers-reduced-motion: reduce) {
        .stApp,
        .stApp *,
        .stApp *::before,
        .stApp *::after {
            animation: none !important;
            transition: none !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


model = joblib.load("KNN_heart.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")


st.markdown(
    """
    <div class="brand-bar">
        <div class="brand-name">
            <span class="brand-icon">♡</span>
            Heart Check
        </div>
        <div class="brand-credit">A project by TAKDIR</div>
    </div>

    <div class="hero">
        <div class="hero-tag">A little insight into your heart</div>
        <h1>
            Your heart.<br>
            A <span class="coral">closer</span>
            <span class="purple">look.</span>
        </h1>
        <p class="hero-description">
            A few details, one model prediction.
            Start with your information below.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


with st.container(border=True):
    st.markdown(
        """
        <div class="section-heading personal-heading">
            <span class="section-number">01</span>
            Let's start with you
        </div>
        <div class="section-description">
            Your basic details and recorded maximum heart rate.
        </div>
        """,
        unsafe_allow_html=True,
    )

    left, right = st.columns(2, gap="large")

    with left:
        age = st.slider("Age", 18, 100, 40)
        sex = st.selectbox("Sex", ["M", "F"])

    with right:
        max_hr = st.slider("Max Heart Rate", 60, 220, 150)
        chest_pain = st.selectbox(
            "Chest Pain Type",
            ["ATA", "NAP", "TA", "ASY"],
        )


with st.container(border=True):
    st.markdown(
        """
        <div class="section-heading clinical-heading">
            <span class="section-number">02</span>
            A few more details
        </div>
        <div class="section-description">
            Enter the values from your available test records.
        </div>
        """,
        unsafe_allow_html=True,
    )

    left, right = st.columns(2, gap="large")

    with left:
        resting_bp = st.number_input(
            "Resting Blood Pressure (mm Hg)",
            80,
            200,
            120,
        )
        fasting_bs = st.selectbox(
            "Fasting Blood Sugar > 120 mg/dL",
            [0, 1],
        )
        exercise_angina = st.selectbox(
            "Exercise-Induced Angina",
            ["Y", "N"],
        )

    with right:
        cholesterol = st.number_input(
            "Cholesterol (mg/dL)",
            100,
            600,
            200,
        )
        resting_ecg = st.selectbox(
            "Resting ECG",
            ["Normal", "ST", "LVH"],
        )
        st_slope = st.selectbox(
            "ST Slope",
            ["Up", "Flat", "Down"],
        )

    oldpeak = st.slider(
        "Oldpeak (ST Depression)",
        0.0,
        6.0,
        1.0,
    )


if st.button("See my prediction →", use_container_width=True):
    raw_input = {
        "Age": age,
        "RestingBP": resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS": fasting_bs,
        "MaxHR": max_hr,
        "Oldpeak": oldpeak,
        "Sex_" + sex: 1,
        "ChestPainType_" + chest_pain: 1,
        "RestingECG_" + resting_ecg: 1,
        "ExerciseAngina_" + exercise_angina: 1,
        "ST_Slope_" + st_slope: 1,
    }

    input_df = pd.DataFrame([raw_input])
    input_df = input_df.reindex(columns=columns, fill_value=0)

    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]

    if prediction == 1:
        result_class = "high"
        result_title = "Heart disease predicted"
    else:
        result_class = "low"
        result_title = "No heart disease predicted"

    st.markdown(
        f"""
        <div class="result-card {result_class}" role="status">
            <div class="result-eyebrow">RESULT</div>
            <div class="result-title">{result_title}</div>
            <div class="result-description">
                This is a machine learning prediction, not a medical
                diagnosis or a guarantee of your heart health.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.markdown(
    f"""
    <div class="footer">
        <span>Educational project · Not for clinical use</span>
        <a href="{FACEBOOK_URL}"
           target="_blank"
           rel="noopener noreferrer">
            Design &amp; development by TAKDIR ↗
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)