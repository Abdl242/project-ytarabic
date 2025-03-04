import openai
import os
import json
#API_KEY = os.environ.get("OPENAI_API_KEY")
#openai.api_key=API_KEY
client = openai.OpenAI()
def ask_chatgpt(prompt):
    """
    Sends a prompt to ChatGPT and retrieves the response.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are ChatGPT, a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=150,
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"GPT ISSUE: {e}")

def application_gpt(text,client):
    """
    Processes the input text and sends it to ChatGPT for transformation
    into an exhaustive, structured Markdown format.
    """
    # Define the API key
    API_KEY = os.environ.get("API_KEY")

    # Set up the prompt for Markdown rewriting
    prompt = f"""
    You will receive a transcripted text. Your task is to rewrite it in an exhaustive, detailed manner, organizing it into a structured format using Markdown. The rewritten content should include the following elements:

    1. **Introduction:** Summarize the context or purpose of the text in a concise opening section.
    2. **Main Sections:** Break down the content into logically organized sections with appropriate headings and subheadings (`#`, `##`, `###`, etc.).
    3. **Key Points:** Expand on the details, making sure all relevant information is included, clarified, and well-organized.
    4. **Lists:** Use bullet points (`-`) or numbered lists (`1.`, `2.`) to outline key ideas, steps, or concepts where appropriate.
    5. **Emphasis:** Highlight important terms, phrases, or points using bold (`**bold**`) or italic (`*italic*`) styling as needed.
    6. **Conclusion:** Provide a concluding section summarizing the key takeaways or insights from the text.
    7. **List all the sources**
    8. Provide tags

    The output should be in arabic only

    Ensure the rewritten text is clear, engaging, and easy to read. You may add clarifying details to enhance understanding but stay true to the original message.
    Return it in json format as {"summary":}

    The text to process is below:

    {text}

    Return it in json format with only one key as {"text":}. The whole result should be saved under the key text
    """

    try:
        # Send the prompt to ChatGPT
        #client = openai.OpenAI(api_key=API_KEY)
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "assistant", "content": prompt},
                {"role": "user", "content": text}
            ],
            max_tokens=2000,response_format={ "type": "json_object" }
        )
        #print(json.loads(completion.choices[0].message.content))
        return json.loads(completion.choices[0].message.content)["text"]
    except Exception as e:
        print(f"GPT ISSUE: {e}")


def application_gpt_2(text,client,language):
    """
    Processes the input text and sends it to ChatGPT for transformation
    into an exhaustive, structured Markdown format.
    """
    # Define the API key
    API_KEY = os.environ.get("API_KEY")

    # Set up the prompt for Markdown rewriting
    prompt = f"""
    You will receive a transcripted text. Your task is to rewrite it in an exhaustive, detailed manner, organizing it into a structured format using Markdown. The rewritten content should include the following elements:

    1. **Introduction:** Summarize the context or purpose of the text in a concise opening section.
    2. **Main Sections:** Break down the content into logically organized sections with appropriate headings and subheadings (`#`, `##`, `###`, etc.).
    3. **Key Points:** Expand on the details, making sure all relevant information is included, clarified, and well-organized.
    4. **Lists:** Use bullet points (`-`) or numbered lists (`1.`, `2.`) to outline key ideas, steps, or concepts where appropriate.
    5. **Emphasis:** Highlight important terms, phrases, or points using bold (`**bold**`) or italic (`*italic*`) styling as needed.
    6. **Conclusion:** Provide a concluding section summarizing the key takeaways or insights from the text.
    7. **List all the sources**
    8. Provide tags

    The output should be in {language} only

    Ensure the rewritten text is clear, engaging, and easy to read. You may add clarifying details to enhance understanding but stay true to the original message.
    Return it in json format as {"summary":}

    The text to process is below:

    {text}

    Return it in json format with only one key as {"text":}. The whole result should be saved under the key text
    """

    try:
        # Send the prompt to ChatGPT
        #client = openai.OpenAI(api_key=API_KEY)
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "assistant", "content": prompt},
                {"role": "user", "content": text}
            ],
            max_tokens=2000,response_format={ "type": "json_object" }
        )
        #print(json.loads(completion.choices[0].message.content))
        return json.loads(completion.choices[0].message.content)["text"]
    except Exception as e:
        print(f"GPT ISSUE: {e}")
