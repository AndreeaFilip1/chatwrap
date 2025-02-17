import requests

class LLMClient:

    '''
    connect to LLM server
    send request to LLM server and return response
    '''

    def __init__(self, url):
        self.url = url

        print(f'Connecting to the server at {self.url}')

        response = requests.get(f'{self.url}/models')

        if response.status_code == 200:
            print('Connected to LLM server')

            models = response.json()

            print(f'Available models: {models}')


    def send_request(self, prompt, model='deepseek-r1-distill-qwen-7b', temperature=0.7, streaming=False):
        '''
        curl http://127.0.0.1:1234/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-r1-distill-qwen-7b",
    "messages": [
      { "role": "system", "content": "Always answer in rhymes." },
      { "role": "user", "content": "Introduce yourself." }
    ],
    "temperature": 0.7,
    "max_tokens": -1,
    "stream": true
  }'
        :param prompt:
        :param model:
        :param temperature:
        :param streaming:
        :return:
        '''

        body = {
           "model": model,
           "messages": [
               { "role": "system", "content": "Always answer in rhymes." },
               { "role": "user", "content": prompt }
           ],
           "temperature": temperature,
           "max_tokens": 100,
           "streaming": False
        }

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(f'{self.url}/chat/completions', json=body, headers=headers)

        if (response.status_code == 200):
            print(f'Yesss, you are awesome')
            print(f'{response.json()})')



