import zmq
import time
import json

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://*:15555")  # 监听本地端口

socket.send_string("Hello, World!")  # 发送一条简单消息

# 要发送的 JSON 对象
messages = [
    {"id": 1, "msg": "first"},
    {"id": 2, "msg": "second"},
    {"id": 3, "msg": "third"},
    {"id": 4, "msg": "fourth"},
    {"id": 5, "msg": "fifth"}
]
print("abc")

# 发送前 3 条
for msg in messages[:3]:
    json_str = json.dumps(msg)
    socket.send_string(json_str)
    print("in for")

    print(f"Sent: {json_str}")

# 暂停 5 秒
time.sleep(5)

# 再发送后 2 条
for msg in messages[3:]:
    json_str = json.dumps(msg)
    socket.send_string(json_str)
    print(f"Sent: {json_str}")
