import json


with open('data/yacht_training_data.json') as f:
    data = json.load(f)

with open('data/formatted_train_data.jsonl', 'w') as outfile:
    for key in data:
        if ''.join(data[key]) != "":
            for paragraph in data[key]:
                if paragraph != "":
                    json.dump({"messages": [{"role": "system", "content": "you are a helpful guide to boat related queries."}, {"role": "user", "content": f"tell me something about {key}"}, {"role": "assistant", "content": f"{paragraph}"}]}, outfile)
                    outfile.write('\n')
        
