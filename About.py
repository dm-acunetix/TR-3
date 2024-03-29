import streamlit as st

#from oauth2client.service_account import ServiceAccountCredentials
FOLDER_ID="1T3RiNpcYS-vbtSa_AN7z_ZlQbiZtLJfj"


st.set_page_config(
    page_title="Team Registration for Acunetix 11.0",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)
page_by_img = '''
<style>
[data-testid="stApp"]::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: url("https://i.ibb.co/Sd250Cf/c770813e40f8416abbe0175a171c13de.png") center center / cover;
    opacity: 0.5; /* Adjust the overlay opacity value as needed (0.0 to 1.0) */
}
[data-testid="stHeader"] {
background: rgba(0,0,0,0);
}


</style>
'''
st.markdown(page_by_img, unsafe_allow_html=True)


image_url = "https://i.ibb.co/1dCdYrG/Acunetix-gform-header.png"
st.image(image_url, use_column_width=True) 

# Function to write data to Google Sheet
# if 'submit_clicked' not in st.session_state:
#     st.session_state.submit_clicked = False

# scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
# creds = ServiceAccountCredentials.from_json_keyfile_name("litforms.json", scope)
# client = gspread.authorize(creds)

# # Replace 'Sheet Name' with your actual+ sheet name
# sheet = client.open_by_key("1VeWt6NBUGqc_4TldxqFfrw9qWhd_4n_FKM0H0XEvoLw").worksheet("Sheet1")

#Font
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Exo+2:wght@300;500&display=swap');

        h1, h2, h3, h4, h5, h6 {
            font-family: 'Orbitron', sans-serif;
            color: #00FEFC; /* Set your desired color */
        }
        p{
            font-family: 'Atomic Age', sans-serif;

        }
    </style>
    """,
    unsafe_allow_html=True
)

# Adding a title with style
st.title("Team Registration for Acunetix 11.0 🛑🚀")

st.markdown("---")

# Adding the general guidelines with style
st.subheader("General Guidelines for Acunetix 11.0 Participants:")
st.write("🛑 Fill details of every team member.")
st.write("🔮 All participants are advised to report at the event venue 15 minutes before the event start time.")
st.write("📡If any candidate(s) fail to comply with the event rules, the team will be disqualified immediately.")
st.write("🌐Misbehavior or any acts that may lead to disruption of any event won't be tolerated. "
         "Any participant(s) found guilty will be disqualified immediately.")
st.write("🌌Team Acunetix will only engage in communication with the Team leads. "
         "Team leads are responsible for any further communication between Team members. "
         "Hence, we advise the team leads to check on updates.")
st.write("🕰️ Team Acunetix reserves the right to modify decisions in case of any fouls and won't be accountable.")
st.markdown("---")

st.subheader("Ready to Register?")
st.write("🚀 Secure your team's spot in the chronicles of Acunetix 11.0! Time waits for no one.")
st.info('To register for team event access the sidebar using the button in the top left corner') 
st.error("Team leader i.e. YOU need not register, only register your fellow teammates")


# Function to display event buttons with links
def display_event_buttons():
    st.subheader("Select an Event:")
    
    # Define event pairs for mobile display
    event_pairs = [
        {"name": "Brainiac", "link": "https://teamreg-beta-acunetix11.streamlit.app/Brainiac"},
        {"name": "CinemeyesLens", "link": "https://teamreg-beta-acunetix11.streamlit.app/CinemeyesLens"},
        {"name": "Code of Lies", "link": "https://teamreg-beta-acunetix11.streamlit.app/CodeOfLies"},
        {"name": "Ctrl Alt Elite", "link": "https://teamreg-beta-acunetix11.streamlit.app/CtrlAltElite"},
        {"name": "InsightOPS", "link": "https://teamreg-beta-acunetix11.streamlit.app/InsightOPS"},
        {"name": "PromptSaga", "link": "https://teamreg-beta-acunetix11.streamlit.app/PromptSaga"},
        {"name": "GameStorm", "link": "https://teamreg-beta-acunetix11.streamlit.app/Gamestorm"},  # Existing GameStorm button
        {"name": "DPL", "link": "https://teamreg-beta-acunetix11.streamlit.app/DPL"},
        {"name": "Timescape", "link": "https://teamreg-beta-acunetix11.streamlit.app/Timescapes"},
        {"name": "TreasureTrove", "link": "https://teamreg-beta-acunetix11.streamlit.app/TresureTrove"},
        {"name": "UXHunt", "link": "https://teamreg-beta-acunetix11.streamlit.app/UXHunt"}
    ]

    # Display event buttons with links in pairs
    for i in range(0, len(event_pairs), 2):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(
                f'<a href="{event_pairs[i]["link"]}" style="display: inline-block; background-color: rgba(51, 153, 255, 0.2); color: rgba(204, 229, 225, 1.0); padding: 15px 32px; text-align: center; text-decoration: none; font-size: 16px; border-radius: 9px; cursor: pointer;">{event_pairs[i]["name"]}</a>',
                unsafe_allow_html=True
            )
        
        with col2:
            if i + 1 < len(event_pairs):
                st.markdown(
                    f'<a href="{event_pairs[i + 1]["link"]}" style="display: inline-block; background-color: rgba(51, 153, 255, 0.2); color: rgba(204, 229, 225, 1.0); padding: 15px 32px; text-align: center; text-decoration: none; font-size: 16px; border-radius: 9px; cursor: pointer;">{event_pairs[i + 1]["name"]}</a>',
                    unsafe_allow_html=True
                )

# Display additional event buttons with links, including GameStorm
display_event_buttons()
