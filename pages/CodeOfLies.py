import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from gspread_dataframe import set_with_dataframe

# Function to write data to Google Sheet
if 'submit_clicked' not in st.session_state:
    st.session_state.submit_clicked = False

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("litforms.json", scope)
client = gspread.authorize(creds)

# Replace 'Sheet Name' with your actual sheet name
sheet_er = client.open_by_key("1OmpeCBR4L5Z0f4MBEYJcklIevM9NPsE0VTXcGhYxsJw").worksheet("Event Reg")
sheet_tr = client.open_by_key("1EnkWPqyIqCawvYHn35BrvlhLxekr9pGOM-GyFCGg0Ew").worksheet("Code of Lies")

# Specify the column to search for IDs
id_column = "J"

st.title("Team Registration for Code of Lies")
search_id = st.text_input("Enter your ID:")

if search_id:

    # Fetch entire row corresponding to the ID
    # Check in sheet_tr
    cell_tr = sheet_tr.find(search_id)

    if cell_tr:
        st.warning("Team already registered")
    else:
        # Check in sheet_er
        cell_er = sheet_er.find(search_id, in_column=id_column)

        if cell_er:
            row_values = sheet_er.row_values(cell_er.row)
            name_str = row_values[cell_er.col]
            st.write(f"Hello, {name_str} 👋!")

            game_str = row_values[cell_er.col + 7]
            game_list = game_str.split(",") if game_str else []

            st.write(f"Event for ID {search_id}:")
            st.write(game_list)

            with st.form("Team_Reg"):
                st.info("Team: Min 1, Max 2 members, with one as the leader.")
                teammate_info_list = []

                for game in game_list:
                    st.title(f"Teammates for: {game}")

                    num = 1  # Assuming num is always 1 for now

                    teammate_names = []
                    teammate_numbers = []
                    teammate_emails = []

                    for i in range(num):
                        teammate_name = st.text_input(f"Name of Teammate {i + 1}:", key=f"{game}_name_{i}")
                        teammate_number = st.text_input(f"Contact no. of Teammate {i + 1}:", max_chars=10,
                                                        key=f"{game}_num_{i}")
                        teammate_email = st.text_input(f"Email of Teammate {i + 1}:", key=f"{game}_em_{i}")

                        teammate_names.append(teammate_name)
                        teammate_numbers.append(teammate_number)
                        teammate_emails.append(teammate_email)

                    # Concatenate teammate info with commas
                    teammate_info = {
                        'ID': search_id,
                        'For Event': game,
                        'Names': ', '.join(teammate_names),
                        'Numbers': ', '.join(teammate_numbers),
                        'Emails': ', '.join(teammate_emails)
                    }

                    teammate_info_list.append(teammate_info)

                submit_button = st.form_submit_button("Submit")
                if submit_button:
                    df = pd.DataFrame(teammate_info_list)
                    print(teammate_info_list)
                    w = client.open_by_key("1EnkWPqyIqCawvYHn35BrvlhLxekr9pGOM-GyFCGg0Ew").worksheet("Code of Lies")
                    last = len(w.col_values(1)) + 1
                    set_with_dataframe(w, df, row=last, include_index=False, include_column_header=False)
                    st.success("Team Registered! ✨")
                    st.dataframe(df)
                    st.info("Thank You")

        else:
            st.warning("ID not found")

elif not search_id:
    st.warning("Enter a valid ID")
