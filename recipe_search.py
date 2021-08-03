import requests

app_key = "58013a85133c520ea3a78c7a63b02a46"
app_id = "e68bae38"


def recipe_serch(user_input):
    result = requests.get(f"https://api.edamam.com/search?q={user_input}&app_id={app_id}&app_key={app_key}")
    data = result.json()
    data = data['hits']

    recipe_list = []
    for item in data:
        recipe = item['recipe']
        recipe_label = recipe['label']
        image = recipe['image']
        recipe_link = recipe['url']

        myDict = {
            'recipe': recipe_label,
            'url': recipe_link,
            'image': image
        }
        recipe_list.append(myDict)

        content = recipe['label'] + '\n' + recipe['url'] + '\n\n'
        with open('recipe_found.txt', 'a') as f:
            f.write(content)

    return recipe_list
