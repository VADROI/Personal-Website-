import streamlit as st
st.set_page_config(
    page_title="Arya Roi",
    page_icon="🚇",
    layout="wide"
)
left_logo, spacer1, center_logo, spacer2, right_space = st.columns([1, 1, 1, 1, 1])

with left_logo:
    st.image(r"siemens-seeklogo.png", use_container_width=True)
    st.markdown(
        "<p style='text-align:left; font-size:20px;'>Ex Data Scientist - 3 Years</p>",
        unsafe_allow_html=True
    )

with center_logo:
    st.image(
        r"NYU_Long_RGB_Black.png",
        use_container_width=True
    )
    st.markdown(
        "<p style='text-align:left; font-size:20px; font-color: #898989;'>Master's Student - May 27'</p>",
        unsafe_allow_html=True
    )

with right_space:
    st.image(
        r"Untitled - June 04, 2026 at 16.53.59.png",
        use_container_width=True
    )
    st.markdown(
        "<p style='text-align:left; font-size:20px; font-color: #898989;'>Summer Intern - 26'</p>",
        unsafe_allow_html=True
    )

# --------------------------------------------------
# STYLING
# --------------------------------------------------
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">

<style>

div[data-testid="stImage"] {
    margin-bottom: -10px;
    margin-top: 10px;
}

p {
    margin-top: 0.1px;
    margin-bottom: 0px;
}

/* Remove Streamlit padding */
.block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
}
header[data-testid="stHeader"] {
    display: none;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* Background */
.stApp {
    background-color: #f7f7f7;
}

/* Fonts */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Name */
.name {
    font-family: 'Cormorant Garamond', serif;
    font-size: 5rem;
    font-weight: 700;
    text-align: center;
    letter-spacing: 2px;
    color: #1a1a1a;
    margin: 0;
}

/* Purple line */

.name-line {
    width: 120px;
    height: 4px;
    background: #57068c;
    margin: 0px auto 5px auto;
    border-radius: 10px;
}

.subtitle {
    text-align: center;
    font-size: 1.25rem;
    color: #666666;
    margin-top: 0px;
    margin-bottom: 0px;
}

/* Cards */
.card {
    background: white;
    border-radius: 20px;
    padding: 30px;
    text-align: center;
    min-height: 230px;
    box-shadow: 0px 4px 18px rgba(0,0,0,0.08);
}

.card-title {
    font-size: 1.4rem;
    font-weight: 600;
    margin-top: 15px;
}

.card-desc {
    color: #666;
    margin-top: 10px;
}

/* Subway circles */
.circle {
    width: 70px;
    height: 70px;
    border-radius: 50%;
    margin: auto;
    font-size: 34px;
    font-weight: bold;
    line-height: 70px;
    color: white;
}

.yellow {
    background: #FCCC0A;
    color: black;
}

.red {
    background: #EE352E;
}

.green {
    background: #00933C;
}

.grey {
    background: #898989;
}

/* Footer */
.footer {
    text-align:center;
    color:#888;
    margin-top:0px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

left_img, title_col, right_img = st.columns([1, 4, 1])

with left_img:
    st.image(
        r"IMG_2877.jpg",   # your new left image
        use_container_width=True
    )

with title_col:
    st.markdown("""
    <div class="name">
        ARYA ROI
    </div>
    """, unsafe_allow_html=True)

with right_img:
    st.image(r"NYC.png",
        use_container_width=True
    )

st.markdown("""
<div class="name-line"></div>
<div class="subtitle">
    Everything's • Stronger • With Data
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# ABOUT
# --------------------------------------------------

st.markdown("""
<div style='text-align:center;
            max-width:850px;
            margin:auto;
            color:#444;
            font-size:1.1rem;
            padding-bottom:0px;'>

Expert - AI | Data Visualization
</div>
""", unsafe_allow_html=True)
# --------------------------------------------------
# RESUME FILE
# --------------------------------------------------

with open(
    r"Arya_Roi_Resume1.pdf",
    "rb"
) as file:
    resume = file.read()

# --------------------------------------------------
# FIRST ROW
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="card">
        <div class="circle yellow">R</div>
        <div class="card-title">Resume</div>
        <div class="card-desc">
            Download my latest resume.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.download_button(
        "Download Resume",
        data=resume,
        file_name="Arya_Roi_Resume1.pdf",
        mime="application/pdf",
        use_container_width=True
    )

with col2:

        st.markdown("""
    <div class="card">
        <div class="circle grey">L</div> 
        <div class="card-title">LinkedIn</div>
        <div class="card-desc">
            Professional experience and networking.
        </div>
    </div>
    """, unsafe_allow_html=True)

        st.link_button(
        "Visit LinkedIn",
        "https://linkedin.com/in/arya-roi",
        use_container_width=True
    )
# --------------------------------------------------
# SECOND ROW
# --------------------------------------------------

col3, col4 = st.columns(2)

with col3:

    st.markdown("""
    <div class="card">
        <div class="circle green">G</div>
        <div class="card-title">GitHub</div>
        <div class="card-desc">
            Machine Learning and Data Science projects.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "Visit GitHub",
        "https://github.com/VADROI",
        use_container_width=True
    )

with col4:
    st.markdown("""
    <div class="card">
        <div class="circle red">T</div>
        <div class="card-title">Tableau Public</div>
        <div class="card-desc">
            Interactive dashboards and analytics projects.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "View Tableau Portfolio",
        "https://public.tableau.com/app/profile/arya.roi/vizzes",
        use_container_width=True
    )

   

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("""
<div class="footer">
© 2026 Arya Roi • New York University
</div>
""", unsafe_allow_html=True)