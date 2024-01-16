import psutil
import matplotlib.pyplot as plt

def get_disk_info():
    disks_info = []
    for disk in psutil.disk_partitions():
        if disk.fstype:
            usage = psutil.disk_usage(disk.mountpoint)
            disk_data = {
                "device": disk.device,
                "mountpoint": disk.mountpoint,
                "fstype": disk.fstype,
                "total": usage.total,
                "used": usage.used,
                "free": usage.free,
                "percent": usage.percent
            }
            disks_info.append(disk_data)
    return disks_info

def plot_disk_usage(disks_info):
    labels = [disk['device'] for disk in disks_info]
    sizes = [disk['percent'] for disk in disks_info]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.axis('equal')
    plt.title('Disk Usage')
    plt.show()

def main():
    disks_info = get_disk_info()
    for disk in disks_info:
        print(f"{disk['device']} - {disk['percent']}% used")
    plot_disk_usage(disks_info)

if __name__ == "__main__":
    main()
