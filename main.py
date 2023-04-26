import os

print("请确保是否为sudo执行该脚本")
while (True):
    try:
        j = int(input("输入1回车确定为sudo执行该脚本，则不是请输入任意数字退出："))
        break
    except:
        print("请根据提示输入！")
if (j != 1):
    print("请使用sudo来执行该脚本，否则出现不可预想的后果！")
    exit()
while (True):
    print("*********************")
    print("**                 **")
    print("**                 **")
    print("**    Linux工具集   **")
    print("**                 **")
    print("**                 **")
    print("*********************")
    while True:
        try:
            i = int(input("选择操作：1.更换软件源 2.更新软件源并升级软件包 0.退出\n请输入："))
            break
        except:
            print("请根据提示输入！")
    if (i==0):
        exit("您已退出！")
    if (i == 1):
        i1 = int(input("选择操作系统：1.Ubuntu22.04LTS 2.Kali 0.退出\n请输入："))
        if (i1 == 1):
            i2 = int(input("选择软件源：1.清华大学镜像源 2.北京外国语大学镜像源 3.中国科学技术大学镜像源 0.退出\n请输入："))
            if (i2 == 1):
                print("WARN：操作过程中可能需要输入sudo密码")
                os.system("sudo rm -rf /etc/apt/sources.list")
                os.system("sudo touch /etc/apt/sources.list")
                f1 = open('/etc/apt/sources.list', 'w+')
                f1.write(
                    "deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse\ndeb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse\ndeb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse\ndeb http://security.ubuntu.com/ubuntu/ jammy-security main restricted universe multiverse"
                )
                f1.close()
                print("已更换至清华大学镜像源")
                print("正在更新软件源")
                os.system("sudo apt update")
                continue
            if (i2 == 2):
                print("WARN：操作过程中可能需要输入sudo密码")
                os.system("sudo rm -rf /etc/apt/sources.list")
                os.system("sudo touch /etc/apt/sources.list")
                f1 = open('/etc/apt/sources.list', 'w+')
                f1.write(
                    "deb https://mirrors.bfsu.edu.cn/ubuntu/ jammy main restricted universe multiverse\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse\ndeb https://mirrors.bfsu.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse\ndeb http://security.ubuntu.com/ubuntu/ jammy-security main restricted universe multiverse"
                )
                f1.close()
                print("已切换至北京外国语大学镜像源")
                print("正在更新软件源")
                os.system("sudo apt update")
                continue
            if (i2 == 3):
                print("WARN：操作过程中可能需要输入sudo密码")
                os.system("sudo rm -rf /etc/apt/sources.list")
                os.system("sudo touch /etc/apt/sources.list")
                f1 = open('/etc/apt/sources.list', 'w+')
                f1.write(
                    "deb https://mirrors.ustc.edu.cn/ubuntu/ jammy main restricted universe multiverse\ndeb https://mirrors.ustc.edu.cn/ubuntu/ jammy-security main restricted universe multiverse\ndeb https://mirrors.ustc.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse\ndeb https://mirrors.ustc.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse"
                )
                f1.close()
                print("已切换至中国科学技术大学镜像源")
                print("正在更新软件源")
                os.system("sudo apt update")
                continue
            if (i2 == 0):
                break
                exit("您已退出！")
        if (i1 == 2):
            i2 = int(input("选择软件源：1.清华大学镜像源 2.北京外国语大学镜像源 3.中国科学技术大学镜像源 0.退出\n请输入："))
            if (i2 == 1):
                print("WARN：操作过程中可能需要输入sudo密码")
                os.system("sudo rm -rf /etc/apt/sources.list")
                os.system("sudo touch /etc/apt/sources.list")
                f1 = open('/etc/apt/sources.list', 'w+')
                f1.write(
                    "deb https://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main non-free contrib"
                )
                f1.close()
                print("已更换至清华大学镜像源!")
                print("正在更新软件源")
                os.system("sudo apt update")
                continue
            if (i2 == 2):
                print("WARN：操作过程中可能需要输入sudo密码")
                os.system("sudo rm -rf /etc/apt/sources.list")
                os.system("sudo touch /etc/apt/sources.list")
                f1 = open('/etc/apt/sources.list', 'w+')
                f1.write(
                    "deb https://mirrors.bfsu.edu.cn/kali kali-rolling main non-free contrib"
                )
                f1.close()
                print("已切换至北京外国语大学镜像源")
                print("正在更新软件源")
                os.system("sudo apt update")
                continue
            if (i2 == 3):
                print("WARN：操作过程中可能需要输入sudo密码")
                os.system("sudo rm -rf /etc/apt/sources.list")
                os.system("sudo touch /etc/apt/sources.list")
                f1 = open('/etc/apt/sources.list', 'w+')
                f1.write(
                    "deb https://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib"
                )
                f1.close()
                print("已切换至中国科学技术大学镜像源")
                print("正在更新软件源")
                os.system("sudo apt update")
                continue
            if (i2 == 0):
                break
                exit("您已退出!")
    if (i == 2):
        print("WARN：操作过程中可能需要输入sudo密码")
        print("正在更新软件源并升级软件包")
        os.system("sudo apt update && upgrade")
        print("已更新完成")
        continue