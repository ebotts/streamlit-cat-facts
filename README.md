# 🐱 streamlit-cat-facts

A delightfully simple [Streamlit](https://streamlit.io) app that fetches random cat facts from the [Cat Fact API](https://catfact.ninja/). Built as a test run to explore API integration, Streamlit app development, and deployment with Streamlit Cloud.

🟢 **Live Demo:** [https://ebotts-streamlit-cat-facts-app-oys8hq.streamlit.app/](https://ebotts-streamlit-cat-facts-app-oys8hq.streamlit.app/)

---

## 🚀 Features

- 🐾 One-click button to fetch a random cat fact
- ✨ Clean UI with instant interactivity
- 🌐 Live-deployed using Streamlit Cloud
- 🧠 Easy to expand with more APIs or UI features


---

## 🔧 Tech Stack

- **Python 3.9**
- **Streamlit** for UI
- **Requests** to call the [Cat Fact API](https://catfact.ninja/)

---

## 🛠️ How to Run Locally

Clone the repo and run the app in a virtual environment:

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/streamlit-cat-facts.git
cd streamlit-cat-facts

# 2. (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
