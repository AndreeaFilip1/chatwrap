from argparse import ArgumentParser
from chatwrap.client import LLMClient

LLM_SERVER_URL = 'http://localhost:1234/v1'

def cli(params):
    print(f'Hello World! {params.prompt}')

    client = LLMClient(LLM_SERVER_URL)

    response = client.send_request(params.prompt, model=params.model, temperature=params.temperature, streaming=params.streaming)
    print(f'Response = {response}')

if __name__ == '__main__':
    parser = ArgumentParser('Chat wrap')

    parser.add_argument('prompt', help='prompt to generate text from')
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')
    parser.add_argument('--temperature', help='temperature for sampling', default=0.7)
    parser.add_argument('--model', help='model to use', default='gpt2')
    parser.add_argument('--streaming', action='store_false', help='streaming_mode')

    args = parser.parse_args()

    cli(args)