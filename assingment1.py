import streamlit as st

# ✅ Page title (no icon)
st.set_page_config(
    page_title="BMW AUTOMOBILES",
    layout="centered"
)

st.title("BMW AUTOMIBILES")

# 👇 Show BMW logo under the title
st.image("bmw_logo_PNG19699.png", width=200)   # use your real filename here

st.subheader("The Ultimate Driving Machine")
st.header("""Apply coupon code "ArinSaxena6977"
          Get up to 2,00,000 off on your first BMW""")

# initialize session_state
if "started" not in st.session_state:
    st.session_state.started = False
if "car" not in st.session_state:
    st.session_state.car = None

# buy button
if st.button("Buy your BMW now! "):
    st.session_state.started = True

if st.session_state.started:
    st.header("You prove you are a REAL MAN!")
    st.write("Select your BMW")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("BMW 1 series"):
            st.session_state.car = "BMW 1 series"
        if st.button("BMW 2 series"):
            st.session_state.car = "BMW 2 series"
        if st.button("BMW 3 series"):
            st.session_state.car = "BMW 3 series"
        if st.button("BMW 4 series"):
            st.session_state.car = "BMW 4 series"

    with col2:
        if st.button("BMW 5 Series"):
            st.session_state.car = "BMW 5 Series"
        if st.button("BMW 6 Series"):
            st.session_state.car = "BMW 6 Series"
        if st.button("BMW 7 Series"):
            st.session_state.car = "BMW 7 Series"
        if st.button("BMW 8 Series"):
            st.session_state.car = "BMW 8 Series"

    with col3:
        if st.button("BMW X1"):
            st.session_state.car = "BMW X1"
        if st.button("BMW X3"):
            st.session_state.car = "BMW X3"
        if st.button("BMW X5"):
            st.session_state.car = "BMW X5"
        if st.button("BMW X7"):
            st.session_state.car = "BMW X7"

    # display chosen car
    if st.session_state.car:
        st.success(f"🔥 You selected {st.session_state.car}!")
        st.write("✅ Thank you for your selection!")
        st.write("👉 Let's move forward...")

        st.link_button("Tap here to visit the BMW website 🌐", "https://www.bmw.in/en/index.html")

else:
    st.subheader("👨‍💻 Know more about the creator")
    if st.button("About Arin Saxena"):
        st.write("""
        **Arin Saxena**  
        *(Aspiring Data Science Engineer | Python Enthusiast)*  

        Driven by curiosity and a passion for turning data into action, I thrive at the crossroads of analysis, automation, and problem-solving. With a strong foundation in Python, I’ve architected data pipelines, streamlined workflows, and built interactive dashboards that delight users—and delight the business too.  

        **Quick snapshot of my superpowers**:  
        🐍 Python wizardry — turning your data chaos into clean, reusable code.  
        📈 Dashboarding & UIs — because numbers deserve a stylish interface.  
        ⏱ Automation addict — life’s too short to do repetitive data tasks by hand.  

        ---
        📞 **Contact:** 8450861638  
        📧 **Email:** arinsaxena777@gmail.com  
        🎓 **College:** Oriental College of Technology  
        """)
