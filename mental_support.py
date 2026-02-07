import streamlit as st
import ollama
import base64
import os

st.set_page_config(page_title="Mental Health Support Chatbot", page_icon="🧠")

# ======== OLLAMA MODEL NAME (SET THIS) ========
OLLAMA_MODEL = "tinyllama"
  # Edit to match your ollama list output: e.g. "phi3", "phi3-mini", or "tinyllama"

def get_base64(image_path):
    ext = os.path.splitext(image_path)[1].lower().replace(".", "")
    with open(image_path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read()).decode()
    return ext, b64_string

# Use correct mime type for background!
try:
    if os.path.exists('background.png'):
        img_ext, img_b64 = get_base64('background.png')
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/{img_ext};base64,{img_b64}");
                background-size: cover;
            }}
            /* Make chat messages visible against background */
            .stChatMessage {{
                background-color: rgba(0, 0, 0, 0.7);
                border-radius: 10px;
                padding: 10px;
                margin-bottom: 10px;
            }}
            .stChatMessage p {{
                color: #ffffff !important;
            }}
            /* Make input label white */
            .stChatInput label {{
                color: #ffffff !important;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("Background image 'background.png' not found.")
except Exception as e:
    st.error(f"Error loading background image: {e}")

st.session_state.setdefault('conversation_history', [])

def extract_content(response):
    msg = response.get('message', None)
    if msg is not None:
        try:
            content = msg.content
        except AttributeError:
            if isinstance(msg, dict) and 'content' in msg:
                content = msg['content']
            else:
                content = None
        if content:
            return content
    if 'choices' in response and response['choices']:
        return response['choices'][0]['message']['content']
    return None

def get_response(user_input):
    st.session_state['conversation_history'].append({'role': 'user', 'content': user_input})
    try:
        response = ollama.chat(model=OLLAMA_MODEL, messages=st.session_state['conversation_history'])
        ai_response = extract_content(response)
        if not ai_response:
             ai_response = "Sorry, I couldn't get a valid reply from the AI model."
    except Exception as e:
        ai_response = f"⚠️ Error: Could not connect to Ollama. Is it running? ({str(e)})"
    
    st.session_state['conversation_history'].append({'role': 'assistant', 'content': ai_response})
    return ai_response

def generate_affirmation():
    affirmation_prompt = "Provide a positive affirmation for mental health support."
    try:
        response = ollama.chat(model=OLLAMA_MODEL, messages=[{'role': 'user', 'content': affirmation_prompt}])
        content = extract_content(response)
        return content or "Sorry, the AI model could not generate an affirmation."
    except Exception as e:
         return f"⚠️ Error generating affirmation: {str(e)}"

def generate_meditation():
    meditation_prompt = "Guide me through a short mindfulness meditation."
    try:
        response = ollama.chat(model=OLLAMA_MODEL, messages=[{'role': 'user', 'content': meditation_prompt}])
        content = extract_content(response)
        return content or "Sorry, the AI model could not generate a meditation."
    except Exception as e:
        return f"⚠️ Error generating meditation: {str(e)}"

st.title("Mental Health Support Chatbot")

# Display chat history
for message in st.session_state['conversation_history']:
    role = message['role']
    content = message['content']
    with st.chat_message(role):
        st.markdown(content)

# Chat input
if prompt := st.chat_input("How can I help you today?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.spinner("Thinking..."):
        bot_response = get_response(prompt)
        with st.chat_message("assistant"):
            st.markdown(bot_response)

col1, col2 = st.columns(2)
with col1:
    if st.button("Generate Affirmation"):
        with st.spinner("Generating affirmation..."):
            affirmation = generate_affirmation()
            # Append affirmation to history as assistant message so it stays
            st.session_state['conversation_history'].append({'role': 'assistant', 'content': f"**Affirmation:** {affirmation}"})
            st.rerun()

with col2:
    if st.button("Generate Meditation"):
        with st.spinner("Generating meditation..."):
            meditation = generate_meditation()
             # Append meditation to history as assistant message so it stays
            st.session_state['conversation_history'].append({'role': 'assistant', 'content': f"**Meditation:** {meditation}"})
            st.rerun()
