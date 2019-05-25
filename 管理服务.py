from os import system
from argparse import ArgumentParser

def start_service(service):
    system("service {} start".format(service))

def stop_service(service):
    system("service {} stop".format(service))

def restart_service(service):
    print(service)
    system("service {} restart".format(service))

def manage_service():
    services = []
    services.append("xinetd")
    services.append("lighttpd")
    return services

def set_args():
    parser = ArgumentParser()
    parser.add_argument("service", help = "the service to be managed.")
    parser.add_argument("-s", "--start", help = "start the service(s).", action = "store_true")
    parser.add_argument("-r", "--restart", help = "restart the service(s).", action = "store_true")
    parser.add_argument("-p", "--stop", help = "stop the service(s).", action = "store_true")
    return parser.parse_args()

def deal(args,services):
    global start_service, restart_service, stop_service
    services = services if not args.service else services if args.service == "all"else [args.service]
    operation = start_service if args.start else restart_service if args.restart else stop_service
    for  service in services:
       operation(service)

if __name__ == "__main__":
    deal(set_args(),manage_service())


# 运行
# 开启服务
# (env) root@DESKTOP-1DDIIV2:~# python pyops.py all -s
# initctl: 无法连接到 Upstart: Failed to connect to socket /com/ubuntu/upstart: 拒绝连接
#  * Starting internet superserver xinetd                                                                                                                          [fail]
#  * Starting web server lighttpd                                                                                                                                  [ OK ]
# (env) root@DESKTOP-1DDIIV2:~#
# 关闭服务
# (env) root@DESKTOP-1DDIIV2:~# python pyops.py xinetd -p
# initctl: 无法连接到 Upstart: Failed to connect to socket /com/ubuntu/upstart: 拒绝连接
#  * Stopping internet superserver xinetd                                                                                                                          [ OK ]
# (env) root@DESKTOP-1DDIIV2:~#
# 重启服务
# (env) root@DESKTOP-1DDIIV2:~# python pyops.py xinetd -r
# xinetd
# initctl: 无法连接到 Upstart: Failed to connect to socket /com/ubuntu/upstart: 拒绝连接
#  * Stopping internet superserver xinetd                                                                                                                          [ OK ]
#  * Starting internet superserver xinetd                                                                                                                          [ OK ]
# (env) root@DESKTOP-1DDIIV2:~#
# 感想
# Python脚本还是比shell脚本好写很多啊。