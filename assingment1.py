import streamlit as st

# Load the BMW logo from the repo
st.image("bmw_logo_PNG19699.png", width=150)  # make sure the filename matches exactly

st.title("BMW AUTOMIBILES")
st.subheader("The Ultimate Driving Machine")
st.subheader("")
st.header("""Apply coupon code '[Arin6977]' 
          Get upto 2,00,000 off on your first BMW""")

# Initialize session state
if "started" not in st.session_state:
    st.session_state.started = False
if "car" not in st.session_state:
    st.session_state.car = None

# Buy button
if st.button("Buy your BMW now!"):
    st.session_state.started = True

if st.session_state.started:
    st.header("You prove you are a REAL MAN!")
    st.write("Select your BMW")
    
    # Layout grids for cars
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
    
    # Display selected car
    if st.session_state.car:
        st.success(f"🔥 You selected {st.session_state.car}!")
        st.write("✅ Thank you for your selection!")
        st.write("👉 Let's move forward...")
        st.link_button("Tap here to visit the BMW website 🌐", "https://www.bmw.in/en/index.html")
else:
    st.write("👆 Press the button above to start your BMW journey!")

# About the Creator section
st.subheader("About the Creator")
st.write("""
**Arin Saxena** – a passionate Data Science Engineer from Bhopal, skilled in building interactive apps and exploring modern technologies.  
📞 8450861638  
✉️ arinsaxena777@gmail.com  
🏫 Oriental College of Technology, Bhopal
""")
# Footer section
st.markdown("---")
st.write("© 2025 Arin Saxena. All rights reserved. Made with ❤️ in Bhopal.")