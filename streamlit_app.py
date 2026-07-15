import random

import streamlit as st


WORDS = [
    {"word": "friend", "meaning": "친구"},
    {"word": "beautiful", "meaning": "아름다운"},
    {"word": "library", "meaning": "도서관"},
    {"word": "travel", "meaning": "여행하다"},
    {"word": "science", "meaning": "과학"},
    {"word": "important", "meaning": "중요한"},
    {"word": "practice", "meaning": "연습"},
    {"word": "remember", "meaning": "기억하다"},
    {"word": "question", "meaning": "질문"},
    {"word": "different", "meaning": "다른"},
    {"word": "happiness", "meaning": "행복"},
    {"word": "holiday", "meaning": "휴일"},
]


def reset_game():
    st.session_state.questions = random.sample(WORDS, len(WORDS))
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.game_over = False


if "questions" not in st.session_state:
    reset_game()


st.set_page_config(page_title="영단어 & BTS 앱", page_icon="📚")
st.title("📚 영어 공부 앱")
st.write("영단어를 공부하고 BTS를 알아보세요.")

vocab_tab, bts_tab = st.tabs(["📖 영단어", "🎤 BTS 소개"])

with vocab_tab:
    st.subheader("영단어 공부")
    st.write("뜻을 보고 영어 단어를 맞혀 보세요.")

    col1, col2 = st.columns([1, 1])
    with col1:
        st.metric("점수", f"{st.session_state.score} / {len(st.session_state.questions)}")
    with col2:
        st.metric("진행도", f"{st.session_state.current_index + 1} / {len(st.session_state.questions)}")

    if st.session_state.game_over:
        st.success(f"게임이 끝났어요! {st.session_state.score}개 맞혔습니다.")
        if st.button("다시 시작", key="restart_vocab"):
            reset_game()
        st.stop()

    current_question = st.session_state.questions[st.session_state.current_index]

    st.subheader("문제")
    st.write(f"뜻: {current_question['meaning']}")

    input_key = f"answer_{st.session_state.current_index}"
    answer = st.text_input("영어 단어를 입력하세요", key=input_key)

    if st.button("정답 확인", key="check_answer"):
        if not answer.strip():
            st.warning("답을 입력해 주세요.")
        else:
            if answer.strip().lower() == current_question["word"].lower():
                st.success("정답입니다! 🎉")
                st.session_state.score += 1
            else:
                st.error(f"아쉽네요. 정답은 '{current_question['word']}'입니다.")
            st.session_state.answered = True

    if st.session_state.answered:
        if st.button("다음 문제", key="next_question"):
            if st.session_state.current_index < len(st.session_state.questions) - 1:
                st.session_state.current_index += 1
                st.session_state.answered = False
            else:
                st.session_state.game_over = True

    if st.button("처음부터", key="reset_vocab"):
        reset_game()

    st.divider()
    st.subheader("단어 목록")
    for item in WORDS:
        st.write(f"- {item['word']} : {item['meaning']}")

with bts_tab:
    st.subheader("BTS 소개")
    st.write("BTS는 방탄소년단으로, 한국의 대표적인 보이 그룹입니다.")
    st.write("멤버들은 서로 협력하며 멋진 음악과 퍼포먼스를 선보입니다.")

    st.write("- 멤버: RM, 진, 슈가, 제이홉, 지민, 뷔, 정국")
    st.write("- 대표곡: Dynamite, Butter, Spring Day")
    st.write("- 특징: 춤, 노래, 메시지, 글로벌 인기를 모두 가진 그룹")

    st.info("BTS는 '작은 것에서 시작해 큰 꿈을 이루는' 의미를 담은 그룹으로 알려져 있습니다.")
