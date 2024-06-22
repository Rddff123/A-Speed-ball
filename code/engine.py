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
    def add_to_startup(file_path,value):
        if value == 1:
    # Open the registry key
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                r"Software\Microsoft\Windows\CurrentVersion\Run",
                                0, winreg.KEY_ALL_ACCESS)

            # Set the value of the registry key to the Python file path
            winreg.SetValueEx(key, "Aspeedball", 0, winreg.REG_SZ, file_path)

            # Close the registry key
            winreg.CloseKey(key)
            messagebox.showinfo("Success", "The program will start automatically when you log in.")
        else:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                r"Software\Microsoft\Windows\CurrentVersion\Run",
                                0, winreg.KEY_ALL_ACCESS)

            # Delete the value of the registry key
            winreg.DeleteValue(key, "Aspeedball")

            # Close the registry key
            winreg.CloseKey(key)
            messagebox.showinfo("Success", "The program will not start automatically when you log in.")
    def rainbow_text():
        r, g, b = 252, 3, 3

        while True:
            while g != 252:
                g += 1
                yield f"#{r:02X}{g:02X}{b:02X}"
                time.sleep(0.01)
            while r != 3:
                r -= 1
                yield f"#{r:02X}{g:02X}{b:02X}"
                time.sleep(0.01)
            while b != 252:
                b += 1
                yield f"#{r:02X}{g:02X}{b:02X}"
                time.sleep(0.01)
            while g != 3:
                g -= 1
                yield f"#{r:02X}{g:02X}{b:02X}"
                time.sleep(0.01)
            while r != 252:
                r += 1
                yield f"#{r:02X}{g:02X}{b:02X}"
                time.sleep(0.01)
            while b != 3:
                b -= 1
                yield f"#{r:02X}{g:02X}{b:02X}"
                time.sleep(0.01)   
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

        messagebox.showinfo("Success", f"Deleted {len(all_files)} files and {not_deleted} files not deleted.")


class tool:      #for toolbox
    def DisableSearchBoxSuggestions(self,value):
        if value == 1:
            key_path = r'Software\Policies\Microsoft\Windows\explorer'
            value_name = 'DisableSearchBoxSuggestions'
            value_data = 1

            # Open the registry key
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE)

            # Set the value
            winreg.SetValueEx(key, value_name, 0, winreg.REG_DWORD, value_data)

            # Close the key
            winreg.CloseKey(key)
            messagebox.showinfo("Success", "Search box internet suggestions have been disabled.")
        else:
            key_path = r'Software\Policies\Microsoft\Windows\explorer'
            value_name = 'DisableSearchBoxSuggestions'

            # Open the registry key
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE)

            # Delete the value
            winreg.DeleteValue(key, value_name)

            # Close the key
            winreg.CloseKey(key)
            messagebox.showinfo("Success", "Search box internet suggestions have been enabled.")
    def TraditionalRightClickMenu(self,value):
        if value == 1:
            key_path = r"HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32"
            value_name = None  # This corresponds to /ve in the command
            value_data = ""  # Empty string value


            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE)
            winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, value_data)
            winreg.CloseKey(key)
            print("Registry key added successfully!")
        else:
            key_path = r"HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32"

            winreg.DeleteKey(winreg.HKEY_CURRENT_USER, key_path)
            print("Registry key deleted successfully!")