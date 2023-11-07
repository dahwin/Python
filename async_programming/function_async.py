import random
import openai
import asyncio

p = 'Im going to sleep'

def promptt(prompt):
    return prompt

async def gpt_summarizer(prompt):
    # Your gpt_summarizer function code here
    # List of API keys
    api_keys = [
        "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",
        "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",
        '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'
    ]

    # Randomly select an API key
    selected_api_key = random.choice(api_keys)

    openai.api_key = selected_api_key  # Set the selected API key

    messages = [
        {"role": "system", "content": 'you are a helpful assistant'},
        {"role": "user", "content": prompt}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.1,
        max_tokens=200  # You can adjust this based on the desired length of the summary
    )

    response_text = response.choices[0].message["content"]


    data = {
        prompt:response_text
    }
    return response_text
async def get_function(p):
    # # Your get_function function code here
    #   results =collection.query(
    #     query_texts=[p],
    #     n_results=2
    # )
    #   functions = results['documents'][0]
      functions = 'I love dahyun'
      return functions


async def hi(p):
    # Create an event loop
    loop = asyncio.get_event_loop()

    # Run both functions concurrently
    gpt_summary = loop.create_task(gpt_summarizer(promptt(p)))
    function_result = loop.create_task(get_function(p))

    # Wait for both tasks to complete
    await asyncio.gather(gpt_summary, function_result)

    # Print the results at the same time
    print("GPT Summary:")
    print(gpt_summary.result())  # Get the result of the gpt_summary task
    print("\nFunction Result:")
    print(function_result.result())  # Get the result of the function_result task


asyncio.run(hi(p))
