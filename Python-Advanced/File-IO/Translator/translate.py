import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

with open('./input.txt', mode='r') as text:
    text_to_translate = text.read()
    print(text_to_translate.strip())
    text.close()

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"Translate text from English into Japanese.\n\n#Examples\nPrompt: A tree is only as hard as it's wood.\nTranslation: 木材が強いほど、木は強い。\nPrompt: Water yearns to be at rest but will move when it is time.\nTranslation: 水は安らかな状態に憧れるが、時が来れば動く。\n#End Examples\n\nPrompt: {text_to_translate}\n\nTranslation:",
  temperature=0.3,
  max_tokens=100,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

with open('./translation.txt', mode='a') as text:
    text.seek(0, 2)
    text.write(f"\n{text_to_translate.strip()}\n{response.choices[0].text.strip()}")
    text.close()
