import streamlit as st
import time

st.set_page_config(page_title="Fesari Ad Demo", layout="centered")
st.title("Fesari Ad Library API Demo")
st.markdown("This is a demonstration of how our tool uses the Meta Ad Library API for transparency and research.")

query = st.text_input("Search Keyword", placeholder="e.g., elections, climate change")

if st.button("Search Ads"):
    if not query:
        st.warning("Please enter a keyword.")
    else:
        with st.spinner("Fetching ads from Meta Ad Library API..."):
            time.sleep(2)  # Simulate API call
            st.success("Ads successfully retrieved.")
            st.markdown("### Mocked Ad Results:")

            # Example mocked results
            ads = [
                {
                    "page_name": "Green Estonia",
                    "ad_snapshot_url": "https://www.facebook.com/ads/library/?id=123456",
                    "ad_creative_body": "Support clean energy for a sustainable future."
                },
                {
                    "page_name": "Vote Smart EE",
                    "ad_snapshot_url": "https://www.facebook.com/ads/library/?id=789012",
                    "ad_creative_body": "Make your voice heard. Register to vote today."
                }
            ]

            for ad in ads:
                st.write(f"**Page:** {ad['page_name']}")
                st.write(f"**Ad Preview:** {ad['ad_creative_body']}")
                st.markdown(f"[View on Facebook Ad Library]({ad['ad_snapshot_url']})")
                st.markdown("---")
