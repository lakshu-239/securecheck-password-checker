import streamlit as st
from password_checker import check_password

st.set_page_config(
    page_title="SecureCheck",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 SecureCheck")
st.subheader("Smart Password Security Checker")

st.write(
    "Evaluate password strength and discover ways "
    "to improve your password security."
)

st.info(
    "Use sample passwords only. Passwords are processed "
    "by the application runtime and are not saved by this project."
)

password = st.text_input(
    "Enter a sample password",
    type="password",
    placeholder="Enter your password here"
)

if st.button("Analyze Password", use_container_width=True):

    if not password:
        st.warning("Please enter a password first.")

    else:
        result = check_password(password)

        st.divider()
        st.subheader("Security Analysis")

        st.metric(
            "Security Score",
            f"{result['score']}/6"
        )

        st.progress(result["score"] / 6)

        if result["strength"] == "Strong":
            st.success("Strength: Strong")
        elif result["strength"] == "Moderate":
            st.warning("Strength: Moderate")
        else:
            st.error(f"Strength: {result['strength']}")

        st.subheader("Recommendations")

        for suggestion in result["feedback"]:
            st.write("✓", suggestion)

st.divider()
st.caption("SecureCheck | Password Security Checker")
