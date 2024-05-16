cd SDN-Forensics-IDS

Mở 1 terminal
sudo python net.py
Mở 1 terminal
ryu-manager --ofp-tcp-listen-port 6633 cont1.py
Mở 1 terminal
ryu-manager --ofp-tcp-listen-port 6634 cont2.py

Các tác vụ:
Khởi tạo mạng
Giả lập tấn công 
Đo lường mạng và vẽ biểu đồ
Lưu và hiển thị file plot.pdf
