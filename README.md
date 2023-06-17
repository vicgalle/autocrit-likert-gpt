# autocrit-likert-gpt ⚖️
Automatic and zero-shot critique of outputs using the OpenAI API with json outputs.

This repository showcases a generic technique to use the OpenAI API as an automatic evaluator for any given task, in a zero-shot manner. It relies in the `functions` argument to output a structured json.

## Explanation

Write a prompt template following a Likert scale. For instance, for a sentiment analysis task, you could write:

```python
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

```

Then, you need to specify the output schema for the OpenAI API. For the previous example, a possible schema would be this one, specifying a field for the score, and another one for the reasoning:
    
```json
{
            "name": "sentiment_likert",
            "description": "Extracts the sentiment score of the response, plus a reasoning for that score.",
            "parameters": {
                "type": "object",
                "properties": {
                    "sentiment": {
                        "type": "integer",
                        "description": "The score of the sentiment, from 1 to 5.",
                    },
                    "reasoning": {
                        "type": "string",
                        "description": "The reasoning for the score.",
                    },
                },
                "required": ["sentiment", "reasoning"],
            },
        }
```

## Example: automatic critique of movie revies

Just execute the following command:

```
python likert.py
```

For the following movie generations:

```json
[
            "The film was simply amazing. The acting was great, the plot was interesting, and the cinematography was beautiful. I would recommend this movie to anyone who enjoys a good drama.",
            "I'm not sure if I liked this movie. It was a bit too long and the plot was confusing. The acting was good, but the cinematography was a bit too dark. I would recommend this movie to anyone who enjoys a good drama.",
            "What a waste of time. The acting was terrible, the plot was boring, and the cinematography was awful. I would not recommend this movie to anyone.",
        ]
```

the corresponding json outputs are 

```json
[
  {
    "sentiment": 5,
    "reasoning": "The submission expresses consistently positive emotions and opinions about the movie. It highlights the amazing acting, interesting plot, and beautiful cinematography. The reviewer also recommends the movie to others who enjoy a good drama. There are no negative or neutral perspectives provided, making the review one-sided and unbalanced."
  },
  {
    "sentiment": 2,
    "reasoning": "The submission has a predominantly negative tone, mentioning that the movie was too long, the plot was confusing, and the cinematography was too dark. However, it also mentions that the acting was good and recommends the movie to anyone who enjoys a good drama. Overall, the submission provides a limited perspective that leans towards the negative side."
  },
  {
    "sentiment": 1,
    "reasoning": "The submission has a consistently negative tone and conveys entirely negative emotions and opinions. It does not provide any positive or neutral perspectives, making it one-sided and unbalanced."
  }
]

```