import csv
sophos_hosts=[]
iventi_hosts=[]
newhosts=[]

def sophos_devices():
    with open('/Users/bkwok/Downloads/sophos-devices.csv', 'r') as input_files:
        for line in input_files:
            line = line.strip()
            if line not in sophos_hosts:
                sophos_hosts.append(line)
    return sophos_hosts

def sophos_servers():
    with open('/Users/bkwok/Downloads/sophos-servers.csv', 'r') as input_file:
        for line in input_file:
            line=line.strip()
            if line  not in sophos_hosts:
                sophos_hosts.append(line)
    return sophos_hosts

def iventi_devices():
    with open('/Users/bkwok/Downloads/Iventi-All-devices.csv', 'r') as input_file:
        for line in input_file:
            line = line.strip()
            if line not in iventi_hosts:
                iventi_hosts.append(line)
    return iventi_hosts

def add_to_sophos(newhosts):
    with open('/Users/bkwok/Downloads/add_to_sophos.csv', 'w') as output_file:
        line:str
        for line in newhosts:
            output_file.write(line)
            output_file.write(",")

def main():
    sophos_devices()
    sophos_servers()
    iventi_devices()
    newhosts= list(filter(lambda x: x not in sophos_hosts, iventi_hosts))
    print("Iventi hosts to be added into  Sophos : ", list(newhosts))
    add_to_sophos(newhosts)
    #print ("Sophos : ", list(sophos_hosts))
    #print ("Iventi : ", list(iventi_hosts))
    #print ("Intercept : ", list(filter(lambda x: x in sophos_hosts, iventi_hosts)))
    #print ("Iventi hosts not in Sophos : ", list(filter(lambda x: x not in sophos_hosts, iventi_hosts)))
    #print ("Iventi hosts not in Sophos : ", list(newhosts))
    #print ("Sophos hosts not in Iventi : ", list(filter(lambda x: x not in iventi_hosts, sophos_hosts)))
    print ("# of Sophos hosts: ", len(list(sophos_hosts)))
    print ("# of Iventi hosts: ", len(list(iventi_hosts)))
    print ("# of the Intercept : ", len(list(filter(lambda x: x in sophos_hosts, iventi_hosts))))
    print ("# of Iventi hosts not in Sophos : ", len(list(filter(lambda x: x not in sophos_hosts, iventi_hosts))))
    print ("# of Sophos hosts not in Iventi : ", len(list(filter(lambda x: x not in iventi_hosts, sophos_hosts))))
if __name__=="__main__":
    main()