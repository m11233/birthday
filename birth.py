import streamlit as st
from datetime import date

# 🎉 Title and emoji
st.set_page_config(page_title="Happy Birthday!", page_icon="🎂")
st.title("🎉 Happy Birthday, Bestie! 🎈")


# Create two columns


# Put images inside each column

st.image(""st.image("images/Screenshot (54).png", caption="Birthday Fun 🎉", width=300))







# 📝 Personal message
st.markdown("""
## 🎂 Dear my everything,

Wishing you a day filled with love, laughter, and happiness!  
You deserve all the amazing things this world has to offer.

Thank you for being such an incredible friend.  
Here's to another year of great memories and dreams coming true! 🎁

**Happy Birthday!! 🥳**

With love,  
**Menna 💖**
""")

# 🎊 Button to trigger confetti
if st.button("Click here for a surprise! 🎁"):
    st.balloons()

# 🕒 Footer
st.caption(f"Sent on {date.today().strftime('%B %d, %Y')} 💌")





