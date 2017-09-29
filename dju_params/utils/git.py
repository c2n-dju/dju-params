import subprocess

def gitsha1(wd):
    p = subprocess.Popen(("git", "log", "-1", "--pretty=oneline"), cwd=wd, stdout=subprocess.PIPE)
    out, err = p.communicate()
    return out.decode('utf-8').split(' ')[0]

def gitstatus(wd):
    p = subprocess.Popen(("git", "status", "--short"), cwd=wd, stdout=subprocess.PIPE)
    out, err = p.communicate()
    if len(out) > 0:
        r = "+" + ", ".join(out.decode('utf-8').split('\n')[:-1])
    else:
        r = ""
    return(r)

