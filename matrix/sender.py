import zmq
import time
import json

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.connect("tcp://localhost:6666")  # 监听本地端口

# 要发送的 JSON 对象
messages = [
    {"component": "trafficlight.0", "msg": "first"},
    {"component": "trafficlight.1", "msg": "second"},
    {"component": "trafficlight.2", "msg": "third"},
    {"component": "trafficlight.3", "msg": "fourth"},
    {"component": "trafficlight.4", "msg": "fifth"}   
]
print("abc")

# 发送前 3 条
for msg in messages[:3]:
    json_str = json.dumps(msg)
    print(f"Sending: {json_str}")
    socket.send_string(json_str)
    print(f"Sent: {json_str}")

# 暂停 5 秒
time.sleep(5)

# 再发送后 2 条
for msg in messages[3:]:
    json_str = json.dumps(msg)
    socket.send_string(json_str)
    print(f"Sent: {json_str}")
