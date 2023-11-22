data = {
    'id': 'chatcmpl-8NdXnZjzuRms91LsD7nF9GKvBQa8N',
    'object': 'chat.completion',
    'created': 1700644243,
    'model': 'gpt-3.5-turbo-0613',
    'choices': [
        {
            'index': 0,
            'message': {
                'role': 'assistant',
                'content':'daf'
            },
            'finish_reason': 'stop'
        }
    ],
    'usage': {'prompt_tokens': 308, 'completion_tokens': 206, 'total_tokens': 514}
}
print(data['choices'][0]['message']['content'])