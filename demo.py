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
            st.markdown("### Example Ad Results:")

            # Mocked real-like ad data
            ads = [
                {
                    "page_name": "Green Estonia",
                    "ad_snapshot_url": "https://www.facebook.com/ads/library/?id=1234567890",
                    "ad_creative_body": "Support clean energy for a sustainable future.",
                    "spend": "€150-199",
                    "ad_delivery_start_time": "2025-04-10",
                    "ad_delivery_stop_time": "2025-04-18"
                },
                {
                    "page_name": "Vote Smart EE",
                    "ad_snapshot_url": "https://www.facebook.com/ads/library/?id=0987654321",
                    "ad_creative_body": "Make your voice heard. Register to vote today.",
                    "spend": "€100-149",
                    "ad_delivery_start_time": "2025-03-28",
                    "ad_delivery_stop_time": "2025-04-04"
                }
            ]

            for ad in ads:
                st.markdown(f"**Page:** {ad['page_name']}")
                st.markdown(f"**Ad Text:** {ad['ad_creative_body']}")
                st.markdown(f"**Spend:** {ad['spend']}")
                st.markdown(f"**Active Dates:** {ad['ad_delivery_start_time']} → {ad['ad_delivery_stop_time']}")
                st.markdown(f"[📌 View on Facebook Ad Library]({ad['ad_snapshot_url']})")
                st.markdown("---")
