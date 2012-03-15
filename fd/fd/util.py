
from subprocess import Popen, PIPE


def sys_call(args, raise_err=True):
    """ Little wrapper around system Popen """
    print " ".join(args)
        
    p = Popen(args, shell=False, stdout=PIPE, stderr=PIPE )
    p.wait()
    err = p.stderr.read()
    if err != '':
        if raise_err:
            raise Exception(err)
        else: 
            return False
        
    p.stderr.close()
    p.stdout.close()
    return True
    