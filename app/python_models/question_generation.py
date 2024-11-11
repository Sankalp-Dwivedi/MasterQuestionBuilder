import pickle
import numpy as np

# Load the model
with open('app/python_models/question_model.pkl', 'rb') as f:
    nlp, question_generator = pickle.load(f)

# Predefined list of possible distractors
distractor_pool = {
    "data": ["information", "noise", "metadata"],
    "neural networks": ["convolutional networks", "decision trees", "support vector machines"],
    "features": ["patterns", "labels", "objects"],
    "weights": ["biases", "thresholds", "parameters"],
    "learning rule": ["activation function", "transfer function", "loss function"]
}

# Function to generate options (correct + distractors)
def generate_options(question, correct_answer):
    if correct_answer.lower() in distractor_pool:
        distractors = distractor_pool[correct_answer.lower()]
    else:
        distractors = [correct_answer[::-1], "None of the above", "All of the above"]
    options = [correct_answer] + distractors
    np.random.shuffle(options)
    return options

# Function to generate questions and options
def generate_questions_and_options(text):
    doc = nlp(text)
    qa_pairs = []
    for sent in doc.sents:
        for token in sent:
            if token.pos_ == "NOUN":
                highlighted_sentence = str(sent).replace(token.text, f"<hl> {token.text} <hl>")
                generated_questions = question_generator(highlighted_sentence, max_length=64, num_beams=3)
                correct_answer = token.text
                for question in generated_questions:
                    qa_pairs.append({
                        "question": question['generated_text'],
                        "options": generate_options(question['generated_text'], correct_answer),
                        "correct_answer": correct_answer
                    })
    return qa_pairs

# Function to take a paragraph and return generated QA pairs
def process_paragraph(paragraph):
    return generate_questions_and_options(paragraph)

if __name__ == "__main__":
    import sys
    paragraph = sys.argv[1]
    qa_pairs = process_paragraph(paragraph)
    print(qa_pairs)
