import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)                 # 创建订阅端 socket
socket.connect("tcp://localhost:5555")           # 连接到发布端
socket.setsockopt_string(zmq.SUBSCRIBE, "")      # 订阅所有消息（空字符串表示不做过滤）

while True:
    msg = socket.recv_string()
    print(f"Received: {msg}")