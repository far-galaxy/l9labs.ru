import os, json


def get_stuff_index():
    files = [name for name in os.listdir('./stuff/videos/')]
    index_json = {'subjects': []}
    for file in files:
        with open(f'./stuff/videos/{file}', encoding='utf-8') as f:
            subject = json.load(f)
            index_json['subjects'].append(
                {
                    'key': file.replace('.json', ''),
                    'name': subject['name'],
                    'image': subject['image'],
                }
            )
    return str(index_json).replace("'", '"')
