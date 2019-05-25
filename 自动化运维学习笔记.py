import psutil
import datetime

mem = psutil.virtual_memory()
print(mem.total, mem.used, mem)
print(psutil.swap_memory())  # 输出获取SWAP分区信息

# 输出CPU使用情况

cpu = psutil.cpu_stats()
print(cpu.interrupts, cpu.ctx_switches)

psutil.cpu_times(percpu=True)  # 输出每个核心的详细CPU信息
psutil.cpu_times().user  # 获取CPU的单项数据 [用户态CPU的数据]
psutil.cpu_count()  # 获取CPU逻辑核心数，默认logical=True
psutil.cpu_count(logical=False)  # 获取CPU物理核心数

# 输出磁盘信息

psutil.disk_partitions()  # 列出全部的分区信息
psutil.disk_usage('/')  # 显示出指定的挂载点情况【字节为单位】
psutil.disk_io_counters()  # 磁盘总的IO个数
psutil.disk_io_counters(perdisk=True)  # 获取单个分区IO个数

# 输出网卡信息
psutil.net_io_counter()
# 获取网络总的IO，默认参数pernic = False
psutil.net_io_counter(pernic=True)
# 获取网络各个网卡的IO

# 获取进程信息
psutil.pids()  # 列出所有进程的pid号
p = psutil.Process(2047)
p.name()
# 列出进程名称
p.exe()
# 列出进程bin路径
p.cwd()
# 列出进程工作目录的绝对路径
p.status()
# 进程当前状态[sleep等状态]
p.create_time()
# 进程创建的时间[时间戳格式]
p.uids()
p.gids()
p.cputimes()  #【进程的CPU时间，包括用户态、内核态】
p.cpu_affinity()  # 显示CPU亲缘关系
p.memory_percent()
# 进程内存利用率
p.meminfo()
# 进程的RSS、VMS信息
p.io_counters()
# 进程IO信息，包括读写IO数及字节数
p.connections()
# 返回打开进程socket的namedutples列表
p.num_threads()
# 进程打开的线程数

# 下面的例子中，Popen类的作用是获取用户启动的应用程序进程信息，以便跟踪程序进程的执行情况

import psutil
from subprocess import PIPE

p = psutil.Popen(["/usr/bin/python", "-c", "print 'helloworld'"], stdout=PIPE)
p.name()
p.username()
p.communicate()
p.cpu_times()

# 其它
psutil.users()  # 显示当前登录的用户，和Linux的who命令差不多

# 获取开机时间
psutil.boot_time()
# 结果是个UNIX时间戳，下面我们来转换它为标准时间格式，如下：
datetime.datetime.fromtimestamp(
    psutil.boot_time())  # 得出的结果不是str格式，继续进行转换 datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d%H:%M:%S')