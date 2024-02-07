import tkinter as tk
from tkinter import ttk
from scapy.all import *


# build mainframe
root = tk.Tk()
root.title("Network Packet Sender")


# sending packets
def send_packet():
    try:
        # data from interface
        ip_src = ip_src_entry.get()
        ip_dst = ip_dst_entry.get()
        packet_type = packet_type_var.get()
        packet_count = int(packet_count_entry.get())
        data = data_entry.get()

        # build packets types
        if packet_type == 'ARP':
            packet = ARP(psrc=ip_src, pdst=ip_dst)
        elif packet_type == 'IP':
            packet = IP(src=ip_src, dst=ip_dst) / Raw(load=data)
        elif packet_type == 'TCP':
            packet = IP(src=ip_src, dst=ip_dst) / TCP(sport=int(src_port_entry.get()),
                                                      dport=int(dst_port_entry.get())) / Raw(load=data)
        elif packet_type == 'UDP':
            packet = IP(src=ip_src, dst=ip_dst) / UDP(sport=int(src_port_entry.get()),
                                                      dport=int(dst_port_entry.get())) / Raw(load=data)
        elif packet_type == 'ICMP':
            packet = IP(src=ip_src, dst=ip_dst) / ICMP() / Raw(load=data)

        # sending
        send(packet, count=packet_count)

        # report
        report_text.insert(tk.END, f"Sent {packet_count} {packet_type} packet(s) from {ip_src} to {ip_dst}\n")
    except Exception as e:
        report_text.insert(tk.END, f"Error: {e}\n")


# interface
ip_src_label = tk.Label(root, text="Source IP:")
ip_src_label.grid(row=0, column=0, sticky="w")
ip_src_entry = tk.Entry(root)
ip_src_entry.grid(row=0, column=1, sticky="ew")

ip_dst_label = tk.Label(root, text="Destination IP:")
ip_dst_label.grid(row=1, column=0, sticky="w")
ip_dst_entry = tk.Entry(root)
ip_dst_entry.grid(row=1, column=1, sticky="ew")

packet_type_var = tk.StringVar()
packet_type_label = tk.Label(root, text="Packet Type:")
packet_type_label.grid(row=2, column=0, sticky="w")
packet_type_combobox = ttk.Combobox(root, textvariable=packet_type_var, values=('ARP', 'IP', 'TCP', 'UDP', 'ICMP'))
packet_type_combobox.grid(row=2, column=1, sticky="ew")
packet_type_combobox.current(0)

packet_count_label = tk.Label(root, text="Number of Packets:")
packet_count_label.grid(row=3, column=0, sticky="w")
packet_count_entry = tk.Entry(root)
packet_count_entry.grid(row=3, column=1, sticky="ew")

src_port_label = tk.Label(root, text="Source Port (TCP/UDP):")
src_port_label.grid(row=4, column=0, sticky="w")
src_port_entry = tk.Entry(root)
src_port_entry.grid(row=4, column=1, sticky="ew")

dst_port_label = tk.Label(root, text="Destination Port (TCP/UDP):")
dst_port_label.grid(row=5, column=0, sticky="w")
dst_port_entry = tk.Entry(root)
dst_port_entry.grid(row=5, column=1, sticky="ew")

data_label = tk.Label(root, text="Data (optional):")
data_label.grid(row=6, column=0, sticky="w")
data_entry = tk.Entry(root)
data_entry.grid(row=6, column=1, sticky="ew")

send_button = tk.Button(root, text="Send Packet", command=send_packet)
send_button.grid(row=7, column=0, columnspan=2)

report_text = tk.Text(root, height=10)
report_text.grid(row=8, column=0, columnspan=2, sticky="ew")

root.mainloop()
