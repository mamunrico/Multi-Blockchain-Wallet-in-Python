import subprocess
import json

command = 'php./hd-wallet-derive.php -g --mnemonic="camp silent object faith snow hint music roof vanish dish help carbon" --cols=path,address,privkey,pubkey'
#--format=json'

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, err = p.communicate()
p_status = p.wait()

keys = json.loads(output)
print(keys)