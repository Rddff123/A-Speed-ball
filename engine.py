import psutil,time,winreg,getpass,os
from tkinter import messagebox
class engine_ud:
    def updownload(self):
        network_stats_start = psutil.net_io_counters()  # Get the network statistics
        upload_speed_start = network_stats_start.bytes_sent  # Convert bytes to MB
        download_speed_start = network_stats_start.bytes_recv   # Convert bytes to MB
        time_start = time.time()
        while True:
                time.sleep(1)
                network_stats_end = psutil.net_io_counters() 
                duration = time.time() - time_start
                upload_speed_new = network_stats_end.bytes_sent # Convert bytes to MB
                download_speed_new = network_stats_end.bytes_recv
                upload_speed =(upload_speed_new-upload_speed_start)/duration   # Convert bytes to MB
                download_speed = (download_speed_new-download_speed_start)/duration
                upload_mb =False;download_mb = False
                if upload_speed > 100:
                    upload_speed = upload_speed/1024
                    upload_mb = True
                if download_speed > 100:
                    download_speed = download_speed/1024
                    download_mb = True
                if download_mb and upload_mb:
                    upload= f"U: {upload_speed:.2f} M/s"
                    download= f"D: {download_speed:.2f} M/s"
                elif download_mb:
                    upload= f"U: {upload_speed:.2f} B/s"
                    download= f"D: {download_speed:.2f} M/s"
                elif upload_mb:
                    upload= f"U: {upload_speed:.2f} M/s"
                    download= f"D: {download_speed:.2f} B/s"
                else:
                    upload= f"U: {upload_speed:.2f} B/s"
                    download= f"D: {download_speed:.2f} B/s"
                yield upload,download
                
    def update_CPUMEM(self):
        while True:
            time.sleep(1)
            cpu_percent = psutil.cpu_percent(interval=None)  # Get the CPU usage percentage
            memory_percent = psutil.virtual_memory().percent  # Get the memory usage percentage
            yield f'CPU:{cpu_percent}%',f'Mem:{memory_percent}%'
class setting:
    def add_to_startup(file_path):
    # Open the registry key
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                            r"Software\Microsoft\Windows\CurrentVersion\Run",
                            0, winreg.KEY_ALL_ACCESS)

        # Set the value of the registry key to the Python file path
        winreg.SetValueEx(key, "MyPythonScript", 0, winreg.REG_SZ, file_path)

        # Close the registry key
        winreg.CloseKey(key)
        messagebox.showinfo("Success", "The program will start automatically when you log in.")
class free_space:
    global username
    username = getpass.getuser()

    def clean_space():
        not_deleted = 0
        global all_files
        all_files = []
        clean_path_list = [f"C:/Users/{username}/AppData/Local/Temp"]  # THERE WILL BE MORE

        for path in clean_path_list:
            for root, dirs, files in os.walk(path):
                # Delete files
                for file in files:
                    file_path = os.path.join(root, file)
                    all_files.append(file_path)
                    try:
                        os.remove(file_path)
                    except:
                        not_deleted += 1
                        continue

                # Delete empty directories
                for dir_path in dirs:
                    dir_path = os.path.join(root, dir_path)
                    try:
                        os.rmdir(dir_path)
                    except:
                        continue

        if not_deleted == 0:
            messagebox.showinfo("Success", "All temporary files have been deleted.")
        else:
            messagebox.showinfo("Success", f"{not_deleted} temporary files were not deleted due to insufficient permissions.")