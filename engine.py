import psutil,time
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