import requests
import streamlit as st


st.set_page_config(page_title='Proxy Checker', page_icon='pc.png', layout="centered", initial_sidebar_state="auto", menu_items=None)


def check_proxy(proxy):
    proxies = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy
    }
    try:
        response = requests.get('https://www.google.com', proxies=proxies, timeout=5)
        if response.status_code == 200:
            return True
    except:
        pass
    return False

def main():
    st.title("Quixotic Proxy Checker")
    proxy_list = st.text_area("Enter a List of Proxies (One Per Line)", height=180)
    proxies = proxy_list.split('\n')

    if st.button("Check Proxies"):
        live_proxies = []
        dead_proxies = []
        with st.spinner(text="Checking Proxies..."):
            for proxy in proxies:
                proxy = proxy.strip()
                if proxy:
                    if check_proxy(proxy):
                        live_proxies.append(proxy)
                    else:
                        dead_proxies.append(proxy)

        st.success("Proxy Check Completed.")

        st.subheader("Live Proxies:")
        live_proxies_text = st.empty()
        if live_proxies:
            live_proxies_text.text_area("This is LIVE Box !!", '\n'.join(live_proxies), height=150)
        else:
            live_proxies_text.text("No Live Proxies Found.")

        st.subheader("Dead Proxies:")
        dead_proxies_text = st.empty()
        if dead_proxies:
            dead_proxies_text.text_area('This is DEAD Box !!', '\n'.join(dead_proxies), height=150)
        else:
            dead_proxies_text.text("No Dead Proxies Found.")

if __name__ == "__main__":
    main()
