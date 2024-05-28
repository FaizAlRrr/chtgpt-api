import openai
import requests

openai.api_key = "MASUKKAN SECRET API KEY"

while True:
     pertanyaan = input("Masukkan pertanyaan : ")
     if pertanyaan:
          response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
               messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": pertanyaan},
                    {"role": "assistant", "content": "Apa kabar hari ini?"},
               ]
          )

          print(f"{'='*80:^20}")
          print(response.choices[0].message.content)
     else:
          break
# for message in response['choices'][0]['messages']:
#     if message['role'] == 'assistant':
#         print("Jawaban Asisten:", message['content'])
# print(response["choices"][2]['content'])
