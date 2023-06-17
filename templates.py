sentiment_likert_prompt = """You are evaluating a response that has been submitted for a particular task, using a specific set of standards. Below is the data:
[BEGIN DATA]
***
[Task]: {task}
***
[Submission]: {submission}
***
[Criterion]: Sentiment rating:
"1": "Strongly negative - The generated text has a consistently negative tone or conveys entirely negative emotions and opinions. It does not provide any positive or neutral perspectives, making it one-sided and unbalanced."
"2": "Somewhat negative - The generated text has a predominantly negative tone, but may include some neutral or mildly positive aspects. It provides a limited perspective that may not be suitable for users looking for a more balanced or unbiased view."
"3": "Neutral - The generated text reveals an impartial or unbiased tone, lacking either strongly positive or negative emotions or opinions. It provides a balanced perspective but may lack depth or insight that would enrich the user's understanding."
"4": "Somewhat positive - The generated text has a predominantly positive tone, but may include some neutral or mildly negative aspects. It provides a mostly optimistic perspective that may be useful for users seeking encouragement or affirmation, but may not be entirely comprehensive."
"5": "Strongly positive - The generated text has a consistently positive tone or conveys entirely positive emotions and opinions. It does not provide any negative or neutral perspectives, making it one-sided and unbalanced."
***
[END DATA]

Does the submission meet the criterion? First, write out in a step by step manner your reasoning about the criterion to be sure that your conclusion is correct. Avoid simply stating the correct answers at the outset. Then print the choice only from “1, 2, 3, 4, 5” (without quotes or punctuation)."""

helpfulness_likert_prompt = """You are evaluating a response that has been submitted for a particular task, using a specific set of standards. Below is the data:
[BEGIN DATA]
***
[Task]: {task}
***
[Submission]: {submission}
***
[Criterion]: helpfulness:
"1": "Not helpful - The generated text is completely irrelevant, unclear, or incomplete. It does not provide any useful information to the user."
"2": "Somewhat helpful - The generated text has some relevance to the user’s question, but it may be unclear or incomplete. It provides only partial information, or the information provided may not be useful for the user’s needs."
"3": "Moderately helpful - The generated text is relevant to the user’s question, and it provides a clear and complete answer. However, it may lack detail or explanation that would be helpful for the user."
"4": "Helpful - The generated text is quite relevant to the user’s question, and it provides a clear, complete, and detailed answer. It offers additional information or explanations that are useful for the user. However, some of the points of the response are somewhat repetitive or could be combined for greater clarity and concision"
"5": "Very helpful - The generated text is highly relevant to the user’s question, and it provides a clear, complete, and detailed answer. It offers additional information, explanations, or analogies that are not only useful but also insightful and valuable to the user. However, the structured of the response is not well-organized and there is no clear progression or logical sequence of different points in the response."
"6": "Highly helpful - The generated text provides a clear, complete, and detailed answer. It offers additional information or explanations that are not only useful but also insightful and valuable to the user. The response is also in a logical and easy-to-follow manner by explicitly using headings, bullet points, or numbered lists to break up the information and make it easier to read."
***
[END DATA]
Does the submission meet the criterion? First, write out in a step by step manner your reasoning about the criterion to be sure that your conclusion is correct. Avoid simply stating the correct answers at the outset. Then print the choice only from “1, 2, 3, 4, 5, 6” (without quotes or punctuation)."""
