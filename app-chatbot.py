import streamlit as st

#import openai
import os
import threading
import signal


st.title("TITLE NEW") # タイトル
st.header("header") # ヘッダー
st.write("write") # 表示
st.markdown("# markdown") # マークダウンで表示
st.text("text") # テキスト表示

#openai.api_key = os.getenv("OPENAI_API_KEY")
time_limit = 8  # application time limit.

# 初期のシステムメッセージ
#messages = [{"role": "system", "content": "You are a "}]

'''
def CustomChatGPT(user_input, conversation_history):
    # ユーザの入力をリストに追加
    conversation_history.append({"role": "user", "content": user_input})
    messages.append({"role": "user", "content": user_input})
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]

    # ChatGPTの返答をリストに追加
    conversation_history.append({"role": "assistant", "content": ChatGPT_reply})
    messages.append({"role": "assistant", "content": ChatGPT_reply})

    return conversation_history
'''

def close_streamlit_after_delay():
    threading.Timer(time_limit, lambda: os.kill(os.getpid(), signal.SIGINT)).start()

def main():
    st.title("ono-piano.com")

    # Streamlitのセッション状態の初期設定
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []

#    with st.form("ChatForm", clear_on_submit=True):
#        user_input = st.text_input("Please enter your message:")
#        submitted = st.form_submit_button("Submit")
#        if submitted and user_input:
#            st.session_state.conversation_history = CustomChatGPT(user_input, st.session_state.conversation_history)

    # CSSを使用して高さを制限してスクロール可能にする
#    st.markdown("""
#        <style>
#            .scrollable-container {
#                max-height: 300px;
#                overflow-y: auto;
#                padding: 10px;
#                border: 1px solid #000; /* この部分を変更 */
#                border-radius: 4px;
#                margin-top: 10px;
#            }
#            .stTextInput input {
#                border: 1px solid #000 !important;
#            }
#            }
#        </style>
#    """, unsafe_allow_html=True)

    # 会話履歴を表示
 #   chat_content = ""
 #   for message in st.session_state.conversation_history:
 #       if message["role"] == "user":
 #           chat_content += f"<p><strong>You:</strong> {message['content']}</p>"
 #       else:
 #           chat_content += f"<p><strong>Assistant:</strong> {message['content']}</p>"

#    st.markdown(f"<div class='scrollable-container' id='chatbox'>{chat_content}</div>", unsafe_allow_html=True)

    # スクロールボックスを最下部にスクロールするJavaScript
#    st.markdown("""
#        <script>
#            let chatbox = document.getElementById('chatbox');
#            chatbox.scrollTop = chatbox.scrollHeight;
#        </script>
#    """, unsafe_allow_html=True)

    close_streamlit_after_delay()

if __name__ == "__main__":
    main()
    
