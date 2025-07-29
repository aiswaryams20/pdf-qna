from utils.groq_engine import get_groq_answer

context = "The mitochondria is the powerhouse of the cell."
question = "What is mitochondria?"

answer = get_groq_answer(context, question)
print(answer)
