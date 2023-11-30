from scapy.all import sniff, IP

# 设置捕获时长（秒）
capture_duration = 3

# 定义处理捕获到的数据包的回调函数
def packet_callback(pkt):
    if IP in pkt:
        target_ip = pkt[IP].dst
        packet_length = len(pkt)
        print(f"访问目标 IP 地址: {target_ip}, 数据包长度: {packet_length}")

# 开始捕获数据包
# 在 scapy 的 sniff 函数中，prn 参数是一个可选的回调函数，用于在每次捕获到数据包时进行处理。
# 具体来说，prn 函数会在每个捕获到的数据包上调用，允许你定义自己的处理逻辑。
sniff(prn=packet_callback, timeout=capture_duration)
