# import spacy
# import numpy as np
# import json
# import sentencepiece
# from transformers import pipeline
# # import pickle

# nlp = spacy.load("en_core_web_sm")
# question_generator = pipeline("text2text-generation", model="valhalla/t5-base-qg-hl")



# # Predefined list of possible distractors
# distractor_pool = {
#     "data": ["information", "noise", "metadata"],
#     "neural networks": ["convolutional networks", "decision trees", "support vector machines"],
#     "features": ["patterns", "labels", "objects"],
#     "weights": ["biases", "thresholds", "parameters"],
#     "learning rule": ["activation function", "transfer function", "loss function"]
# }

# # Function to generate options (correct + distractors)
# def generate_options(question, correct_answer):
#     # Extract predefined distractors from pool or generate some default ones
#     if correct_answer.lower() in distractor_pool:
#         distractors = distractor_pool[correct_answer.lower()]
#     else:
#         # Generate generic distractors if none available in the pool
#         distractors = [correct_answer[::-1], "None of the above", "All of the above"]

#     # Combine correct answer with distractors and shuffle
#     options = [correct_answer] + distractors
#     np.random.shuffle(options)

#     return options

# # Function to generate questions and answers
# def generate_questions_and_options(text, nlp):
#     doc = nlp(text)
#     qa_pairs = []

#     # Extract sentences from the text and generate questions
#     for sent in doc.sents:
#         for token in sent:
#             if token.pos_ == "NOUN":  # Focus on nouns for question generation
#                 highlighted_sentence = str(sent).replace(token.text, f"<hl> {token.text} <hl>")
#                 generated_questions = question_generator(highlighted_sentence, max_length=64, num_beams=3)

#                 # Extract correct answer (the highlighted noun in this case)
#                 correct_answer = token.text

#                 # Generate question-answer pairs with options
#                 for question in generated_questions:
#                     qa_pairs.append({
#                         "question": question['generated_text'],
#                         "options": generate_options(question['generated_text'], correct_answer),
#                         "correct_answer": correct_answer
#                     })
#     return qa_pairs

# # # Example paragraph
# # paragraph = """In Banaras District there is a village called Bira in which an old, childless
# # widow used to live. She was a Gond woman named Bhungi and she didn't
# # own either a scrap of land or a house to live in. Her only source of livelihood
# # was a parching oven. The village folk customarily have one meal a day of
# # parched grains, so there was always a crowd around Bhungi's oven.
# # Whatever grain she was paid for parching she would grind or fry and eat it.
# # She slept in a corner of the same little shack that sheltered the oven. As soon
# # as it was light she'd get up and go out to gather dry leaves from all around to
# # make her fire. She would stack the leaves right next to the oven, and after
# # twelve, light the fire. But on the days when she had to parch grain for Pandit
# # Udaybhan Pandey, the owner of the village, she went to bed hungry. She
# # was obliged to work without pay for Pandit Udaybhan Pandey She also had
# # to fetch water for his house. And, for this reason, from time to time the oven
# # was not lit. She lived in the Pandit's village, therefore he had full authority to
# # make her do any sort of odd job. In his opinion if she received food for
# # working from him, how could it be considered as work done without pay?
# # He was doing her a favour, in fact, by letting her live in the village at all.
# #  It was spring, a day on which the fresh grain was fried and eaten and given
# # as a gift. No fire was lit in the houses Bhungi's oven was being put to good
# # use today. There was a crowd worthy of a village fair around her. She had
# # scarcely opportunity to draw a breath. Because of the customer's impatience,
# # squabbles kept breaking out. Then two servants arrived, each carrying a
# # heaped basket of grain from Pandit Udaybhan with the order to parch it right
# # away. When Bhungi saw the two baskets she was alarmed. It was already
# # after twelve and even by sunset, she would not have time to parch so much
# # grain. Now she would have to stay at the oven parching until after dark for
# # no payment. In despair she took the two baskets. One of the flunkeys said
# # menacingly, 'Don't waste any time or you'll be sorry.' """

# # # Generate QA pairs from paragraph
# # qa_pairs = generate_questions_and_options(paragraph, nlp)

# # # Display the questions and options
# # for qa in qa_pairs:
# #     print("\nQuestion: ", qa['question'])
# #     print("Options: ", qa['options'])
# #     print("Correct Answer: ", qa['correct_answer'])





# def process_paragraph(paragraph):
#     return generate_questions_and_options(paragraph)


# if __name__ == "__main__":
#     import sys
#     paragraph = sys.argv[1]
#     print("------------------------------")
#     print(paragraph)
#     print("------------------------------")
#     qa_pairs = process_paragraph(paragraph)
#     # print(qa_pairs)
#     print(json.dumps(qa_pairs))



























import spacy
import numpy as np
import json
import sentencepiece
from transformers import pipeline

nlp = spacy.load("en_core_web_sm")
question_generator = pipeline("text2text-generation", model="valhalla/t5-base-qg-hl")

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

# Function to generate questions and answers
def generate_questions_and_options(text, nlp):
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

def process_paragraph(paragraph, nlp):
    return generate_questions_and_options(paragraph, nlp)

if __name__ == "__main__":
    import sys
    paragraph = sys.argv[1]
    qa_pairs = process_paragraph(paragraph, nlp)
    print(json.dumps(qa_pairs))
