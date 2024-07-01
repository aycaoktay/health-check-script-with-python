import psutil
import logging
import shutil
import os
from datetime import datetime , timedelta


#Logging kısmı için ayarlar + olarak 30 günde bir log doyasını yedekleyecek kodlar eklenmiştir
LOG_DIR = 'logs'
LOG_FILE = os.path.join(LOG_DIR, 'health_check.log')
BACKUP_DIR = os.path.join(LOG_DIR, 'backup')

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
if not os.path.exists(BACKUP_DIR):
    os.makedirs(BACKUP_DIR)


logging.basicConfig(filename='logs/health_check.log' , level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


def backup_logs():  
    current_time = datetime.now()
    last_backup_time_file = os.path.join(LOG_DIR, 'last_backup_time.txt')

    if os.path.exists(last_backup_time_file):
        with open(last_backup_time_file, 'r') as file:
            last_backup_time = datetime.strptime(file.read(), '%Y-%m-%d %H:%M:%S')
    else:
        last_backup_time = current_time - timedelta(days=31)

    if (current_time - last_backup_time).days >= 30:
        backup_filename = os.path.join(BACKUP_DIR, f'health_check_{current_time.strftime("%Y%m%d%H%M%S")}.log')
        shutil.copy(LOG_FILE, backup_filename )
        logging.info(f'Log dosyası yedeklendi: {backup_filename}')
        with open(last_backup_time_file, 'w') as file:
            file.write(current_time.strftime('%Y-%m-%d %H:%M:%S'))    



def check_cpu_usage():
    usage = psutil.cpu_percent(interval=1)
    logging.info(f'CPU Usage: {usage}%')
    if usage > 80:
        warning_message = 'WARNING: CPU usage is over 80%'
        logging.warning(warning_message)

def check_memory_usage():
    memory = psutil.virtual_memory()
    logging.info(f'Memory Usage: {memory.percent}%')
    if memory.percent > 80:
        warning_message = 'WARNING: Memory usage is dengerously high!'
        logging.warning(warning_message)

def check_disk_usage():
    disk = psutil.disk_usage('/')   
    logging.info(f'Disk Usage: {disk.percent}%')
    if disk.percent > 80:
        warning_message = 'WARNING: Disk usage is dangerously high!'
        logging.warning(warning_message)
    

def main():
    logging.info('Health Check Started...')
    backup_logs()
    check_cpu_usage()
    check_memory_usage()    
    check_disk_usage()
    logging.info('Health Check Completed...')

if __name__ == '__main__':
    main()