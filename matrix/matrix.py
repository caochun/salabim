import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.PULL)                 # 创建订阅端 socket
socket.connect("tcp://localhost:15555")           # 连接到发布端
# socket.setsockopt_string(zmq.SUBSCRIBE, "")      # 订阅所有消息（空字符串表示不做过滤）

while True:
    msg = socket.recv_string()

    print(f"Received raw message: {msg}")  # 打印接收到的原始消息

    try:
        obj = json.loads(msg)  # 解析 JSON 字符串为字典
        # component = obj.get("component")

        # # 判断 component 是否是目标值
        # if isinstance(component, str) and component.startswith("TrafficLight"):
        print(f"Received: {msg}") 

    except json.JSONDecodeError as e:
        print("JSON 解析失败:", e)

