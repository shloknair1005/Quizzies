# 📘 Quizzie – PDF Summarizer & Quiz Generator

Quizzie is a **Streamlit-based app** that takes any uploaded PDF, summarizes the content, and generates a short **5-question quiz** with answers.  
Perfect for quick learning, revision, or testing comprehension.

---

## 🚀 Features
- 📂 Upload a PDF file  
- 📝 Extracts and summarizes key points from the PDF  
- ❓ Generates a 5-question quiz with answers  
- 🎯 Lightweight and easy-to-use Streamlit interface  

---

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/quizzie.git
cd quizzie

2. Create a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows

3. Install Dependencies
pip install -r requirements.txt

If you don’t have a requirements.txt, you can install manually:
pip install streamlit PyMuPDF nltk

4. Run the App
streamlit run main.py

📂 Project Structure
quizzie/
│── main.py              # Streamlit app code
│── sample.pdf           # Demo PDF to test
│── README.md            # Project documentation
│── requirements.txt     # Dependencies

🎮 How to Use
1.Run the Streamlit app.
2.Upload a PDF file using the upload button.
3.View the summary of the PDF.
4.Answer the 5 auto-generated quiz questions.
5.Check the correct answers for self-evaluation.

📌 Example Output
Summary:
"This PDF covers the basics of Artificial Intelligence, including machine learning, deep learning, and neural networks. It explains key concepts with simple examples and applications."

Quiz:
What is AI primarily concerned with?
Name one application of AI in daily life.
What are neural networks inspired by?
Difference between supervised and unsupervised learning?
Why is deep learning popular today?

Answers:
Creating machines that simulate human intelligence.
Virtual assistants like Siri, Alexa.
The human brain.
Supervised uses labeled data, unsupervised does not.
Availability of data + high computing power.

🧑‍💻 Author
Shlok Nair
📌 Data Science Student | Aspiring ML Engineer
