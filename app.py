import streamlit as st
import pandas as pd
import time

def main():
    st.set_page_config(
        page_title="Denizen Cloud",
        page_icon="Utilities/logo.ico",
        layout="wide",
    )

    page_options = ["Home", "Connected Home Appliances", "Recent Orders"]
    selected_page = st.sidebar.selectbox("Go To", page_options)

    if selected_page == "Home":
        display_home_page()
    elif selected_page == "Recent Orders":
        display_recent_orders_page()
    elif selected_page == "Connected Home Appliances":
        display_connected_appliances_page()

def display_home_page():
    st.image("Utilities/welcome-page logo.png", width = 200);
    st.write()
    st.title("Welcome to Denizen Cloud")
    # Add more content specific to the Home page if needed

def display_recent_orders_page():
    st.title("Recent Orders")
    st.write()
    table = pd.read_csv("Utilities/Recent Orders.csv")
    st.table(data = table)
    # Add more content specific to the Recent Orders page if needed

def display_connected_appliances_page():
    st.title("Connected Home Appliances")
    appliances = ["", "HP Smart Tank 510", "LG GL-B211HSCD"]
    selected_appliance = st.selectbox("Select Appliance", appliances)

    if selected_appliance == "HP Smart Tank 510":
        display_hp_page()
    elif selected_appliance == "LG GL-B211HSCD":
        display_lg_page()
    else:
        st.write("")

def display_hp_page():
    st.write()
    st.title("Printer Statistics")
    st.write()
    st.image("Utilities/ink-levels.png")
    st.warning('Black Ink depleting fast!!!',icon="⚠️")

    time.sleep(1)
    st.toast("Order for Black Ink placed on Amazon!")
    
    st.subheader("Complete Your Order now")
    st.write("[Your Cart]()");

    # Add more content specific to HP Smart Tank 510 if needed

def display_lg_page():
    st.write()
    st.title("Refrigerator Statistics")
    st.write()
    st.image("Utilities/temp-gauge.png")
    st.write()
    st.error("Temperature Value too high!!!", icon="⚠️")

    time.sleep(2)
    st.toast("Service Request placed on LG's Customer Care!")
    
    st.header("Booked Service Details")
    st.write()
    st.write("Booking ID: **LG23478A4**");
    st.write("Technician Contact Details: **+91-9347691208**");
    st.write("Visiting Address: **15, Nehru Place, New Delhi 110019**");
    st.write("Visiting Date: **15 April, 2024**");

if __name__ == "__main__":
    main()
