import requests
import json



def cout(input_text):
    url = 'http://localhost:11434/api/chat'
    headers = {
        'Authorization': 'Bearer ollama',
        'Content-Type': 'application/json',
    }# 请求体
    data = {
        'model': 'llama3.1',
        'messages': [
            {
                'role': 'user',
                'content': input_text,
            }
        ]
    }

    # 发送请求
    response = requests.post(url, headers=headers, json=data)

    # 检查响应状态码
    if response.status_code == 200:
        l = response.text.splitlines()  # 按行分割响应文本
        lst = []
        
        for i in l:
            if i.strip():  # 检查行不为空
                try:
                    d = json.loads(i)  # 使用 json.loads() 解析 JSON 字符串
                    if "message" in d and "content" in d["message"]:
                        lst.append(d["message"]["content"])  # 添加内容到列表
                except json.JSONDecodeError as e:
                    print(f"JSON decode error: {e}")

        return "".join(lst)  # 返回合并后的内容
    else:
        return f"请求失败: {response.status_code} - {response.text}"
