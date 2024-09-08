import json

def get_company_data(_data):
    filtered_result = []
    for company in _data:
        filtered_result.append((company['title'], company['id']))
        if 'children' in company:
            filtered_result.extend(get_company_data(company['children']))
    return filtered_result

with open('new_test_hw.json', 'r', encoding="utf-8") as f:
    data = json.load(f)
    result = tuple(get_company_data(data['children']))
    print(result)