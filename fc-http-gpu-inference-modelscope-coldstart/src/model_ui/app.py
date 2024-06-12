from PIL import Image
import gradio as gr
import io
import os
import requests
import base64
import random
import time
import threading
from openai import OpenAI

## global variables inherited from env
demo = None
model_id = os.getenv('MODEL_ID', '')
model_revision = os.getenv('MODEL_VERSION', '')
model_task = os.getenv('TASK', '')
api_url = os.getenv('API_URL')
api_url_others = []
pp_size = int(os.getenv('PP_SIZE'))
title = "魔搭社区x函数计算 : 一键部署模型"
description = "本页面提供图形化方式调用部署后的魔搭模型，更多FAQ请见 [ModelScope一键部署模型：新手村实操FAQ篇](https://developer.aliyun.com/article/1307460?spm=5176.28261954.J_7341193060.1.43f42fdewvfTyq&scm=20140722.S_community@@%E6%96%87%E7%AB%A0@@1307460._.ID_1307460-RL_%E9%AD%94%E6%90%AD%20%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2-LOC_search~UND~community~UND~item-OR_ser-V_3-P0_0)"
article = '''
- 模型ID: [{}](https://www.modelscope.cn/models/{})
- 模型版本: {}
- 模型任务类型: {}
- 模型推理URL: {}/invoke'''.format(model_id, model_id, model_revision, model_task, api_url)

print("[debug] model_id=", model_id)
print("[debug] model_revision=", model_revision)
print("[debug] model_task=", model_task)
print("[debug] api_url=", api_url)

model_id = model_id.replace('.', '___')

if model_task == None or len(model_task) == 0:
    gr.Warning("Missing necessary model task")
if api_url == None or len(api_url) == 0:
    gr.Warning("Missing necessary api url")
else:
    api_url += "/v1"

client = OpenAI(
    base_url=api_url,
    api_key="token"
)

## utils
def post_request(url, json):
    with requests.Session() as session:
        start_time = time.time()
        response = session.post(url,json=json,)
        elapsed = time.time() - start_time
        resp_json = response.json()
        if "Message" in resp_json:
            resp_json = resp_json["Message"]
            actual_runtime = resp_json["elapsed_time"]
            invoke_time = elapsed - actual_runtime
            print(f"warmup: function [{json['pp_stage']}] total elapsed time = {elapsed} s, invoke time cost = {invoke_time} seconds")
        return response

threads = []

def do_warmup():
    # warmup stages [1,...,pp_size-1]
    global api_url_others
    global threads

    if pp_size == 1:
        return
    if api_url_others == []:
        # init api_url
        for i in range(1, pp_size):
            url = os.getenv('API_URL_' + str(i))
            url = url + "/warmup"
            api_url_others.append(url)
    # warmup
    for i in range(0, pp_size - 1):
        payload = { "warmup": "yes", "pp_stage": str(i + 1)}
        thread = threading.Thread(target=post_request, args=(api_url_others[i], payload))
        thread.start()
        threads.append(thread)

messages = []

def chat_setup():
    def handler(message, history):
        global messages
        if message == None or len(message) == 0:
            raise gr.Error("Missing necessary input message, please retry.")
        do_warmup()

        if len(history) == 0:
            messages = []

        messages.append({"role": "user", "content": message})
        start_time = time.time()
        chat = client.chat.completions.create(
            model=model_id, messages=messages
        )
        reply = chat.choices[0].message.content
        elpased = time.time() - start_time
        print(f"messages = {messages}")
        print(f"reply = {reply}")
        print(f"generation finished, time cost = {elpased} seconds")
        messages.append({"role": "assistant", "content": reply})

        if "<|im_start|>" in reply:
            reply = reply.replace("<|im_start|>", "")
        if "<|im_end|>" in reply:
            reply = reply.replace("<|im_end|>", "")

        return reply

    with gr.Blocks() as demo:
        gr.ChatInterface(fn=handler,
                         examples=["hello", "您好", "你能做什么"],
                         title=title,
                         description=description)
        gr.Markdown(article)

    return demo

def default_setup():
    def default_callback():
        return "invalid model task"

    return gr.Interface(fn=default_callback, inputs=None, outputs="text", title="404", description="invalid model task")

## initiailzie
model_task_handlers = {
    "chat" : chat_setup,
    "default" : default_setup,
}

if model_task_handlers.get(model_task) == None:
    demo = model_task_handlers["default"]()
else:
    demo = model_task_handlers[model_task]()
    
demo.launch(server_name="0.0.0.0")
