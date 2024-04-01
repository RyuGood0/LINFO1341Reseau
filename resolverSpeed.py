import subprocess

# run dig drive.shadow.tech +trace @n.n.n.n 100 times and get the average time from line containing "from 1.1.1.1#53(1.1.1.1) in 87 ms"
# n.n.n.n is the resolver IP

from time import sleep
def get_resolver_speed(resolver_ip, runs=100):
    total_time = 0
    for i in range(runs):
        result = subprocess.run(['dig', 'drive.shadow.tech', '+trace', '@' + resolver_ip], stdout=subprocess.PIPE)
        result = result.stdout.decode('utf-8')
        for line in result.split('\n'):
            if 'from ' + resolver_ip + '#53(' + resolver_ip + ') in ' in line:
                time = int(line.split(' in ')[1].split(' ')[0])
                total_time += time
                break
        
        sleep(0.1)

    return total_time / runs

print(get_resolver_speed('1.1.1.1'))
print(get_resolver_speed('8.8.8.8'))