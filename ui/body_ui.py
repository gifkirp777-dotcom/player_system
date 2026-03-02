import streamlit as st

def render_body_ui():
    inputs = {}

    st.markdown("### BODY INPUT")

    inputs["time"] = st.number_input(
        "TIME (мин)",
        min_value=0,
        max_value=300,
        value=20,
        step=1
    )

    st.markdown("INTENSITY")

    if "body_intensity" not in st.session_state:
        st.session_state["body_intensity"] = 1

    col1, col2 = st.columns(2)
    intensity_values = [0.5, 1, 1.5, 2]

    for i, value in enumerate(intensity_values):

        active = st.session_state["body_intensity"] == value
        label = f"▶ {value}" if active else str(value)

        with (col1 if i % 2 == 0 else col2):
            if st.button(label, use_container_width=True, key=f"int_{value}"):
                st.session_state["body_intensity"] = value
                st.rerun()

    inputs["intensity"] = st.session_state["body_intensity"]

    inputs["result"] = st.slider(
        "RESULT",
        min_value=0.0,
        max_value=1.5,
        value=1.0,
        step=0.1,
        key="body_time"
    )

    return inputs