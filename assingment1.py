import streamlit as st

st.title("BMW AUTOMIBILES")
st.header("Not just a car, it's a lifestyle")
 
# initialize session_state
if "started" not in st.session_state:
    st.session_state.started = False
if "car" not in st.session_state:
    st.session_state.car = None
    
# buy button
if st.button("Buy your BMW now! "):  # keeping your original text
    st.session_state.started = True

if st.session_state.started:
    st.header("You prove you are a REAL MAN!")
    st.write("Select your BMW")
    
    # layout grids for cars
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
         
         # real link button
         st.link_button("Tap here to visit the BMW website 🌐", "https://www.bmw.in/en/index.html")
     
else: 
    st.write("👆 Press the button above to start your BMW journey!")

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    