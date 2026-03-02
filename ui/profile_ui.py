import streamlit as st



def render_profile(data):

   
    def rank_color(rank):
        colors = {
            "E": "#9CA3AF",
            "D": "#60A5FA",
            "C": "#34D399",
            "B": "#A78BFA",
            "A": "#F59E0B",
            "S": "#D4AF37",
            "SS": "#FFFFFF"
        }

        if not rank:
            return "#9CA3AF"

        rank = str(rank).strip().upper()

        return colors.get(rank, "#9CA3AF")

    # ===== ЗАГОЛОВОК =====
    st.markdown(
        """
        <div style="
            text-align:center;
            font-size:44px;
            font-weight:800;
            color:#D4AF37;
            letter-spacing:4px;
            margin-bottom:25px;
        ">
            ⚔ СИСТЕМА ИГРОКА
        </div>
        """,
        unsafe_allow_html=True
    )
   

    # ===== УРОВЕНЬ / РАНГ =====
    
    # ===== УРОВЕНЬ / РАНГ =====

    rank_value = data.get("rank") or "E"
    rank_value = str(rank_value)
    rank_col = rank_color(rank_value)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("##### УРОВЕНЬ")
        st.markdown(
            f"<span style='color:#FBBF24;font-size:28px;font-weight:800'>{data.get('level', 1)}</span>",
            unsafe_allow_html=True
        )

    with col2:
        st.markdown("##### РАНГ")
        st.markdown(
            f"<span style='color:{rank_col};font-size:28px;font-weight:800'>{rank_value}</span>",
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)


    # ===== ВЛАСТЬ И СИЛА ДУХА (без рамок) =====

    power = round(data["stats"].get("Власть", 0), 2)
    spirit = round(data["stats"].get("Сила духа", 0), 2)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            f"""
            <div style="text-align:center;">
                <div style="
                    font-size:22px;
                    font-weight:700;
                    letter-spacing:2px;
                    color:#D4AF37;
                ">
                    ВЛАСТЬ
                </div>
                <div style="
                    font-size:42px;
                    font-weight:900;
                    color:#D4AF37;
                    margin-top:6px;
                ">
                    {power}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div style="text-align:center;">
                <div style="
                    font-size:22px;
                    font-weight:700;
                    letter-spacing:2px;
                    color:#7F1D1D;
                ">
                    СИЛА ДУХА
                </div>
                <div style="
                    font-size:42px;
                    font-weight:900;
                    color:#B91C1C;
                    margin-top:6px;
                ">
                    {spirit}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    # ===== СТАТЫ =====

    st.markdown("<div style='margin-top:40px;'></div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center;font-size:30px;font-weight:700;color:#D4AF37;letter-spacing:3px;'>СТАТЫ</div>", unsafe_allow_html=True)
    st.markdown("<div style='margin-top:25px;'></div>", unsafe_allow_html=True)

    base_stats = [
        "Сила тела",
        "Интеллект",
        "Социум",
        "Харизма",
        "Финансы"
    ]

    col1, col2 = st.columns(2)

    for i, stat in enumerate(base_stats):

        value = round(data["stats"].get(stat, 0), 2)

        if i % 2 == 0:
            col1.markdown(
                f"""
                <div style="margin-bottom:25px;">
                    <div style="font-size:14px;color:#E5E7EB;font-weight:600;">
                        {stat}
                    </div>
                    <div style="font-size:24px;color:#D4AF37;font-weight:800;">
                        {value}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            col2.markdown(
                f"""
                <div style="margin-bottom:25px;">
                    <div style="font-size:14px;color:#E5E7EB;font-weight:600;">
                        {stat}
                    </div>
                    <div style="font-size:24px;color:#D4AF37;font-weight:800;">
                        {value}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )