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
