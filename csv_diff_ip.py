import csv
import pandas as pd
from typing import List, Any

sophos_all_hosts = []
sophos_device_hosts = []
sophos_server_hosts = []
sophos_all_ips = []
sophos_device_ips = []
sophos_server_ips = []
iventi_hosts: List[Any] = []
iventi_ips = []
nessus_ips = []
newhosts = []


def sophos_devices():
    device = '/Users/bkwok/Downloads/sophos_devices_full.csv'  # date: 05-21-2020
    with open(device, 'r') as f1:
        line_count = 0
        for row in f1:
            if line_count == 0:
                line_count = 1  # skip the column name
                continue
            else:
                if row[1] not in sophos_device_hosts:
                    # print (row)
                    row_list = row.rsplit(',')
                    sophos_all_hosts.append(row_list[1])
                    sophos_device_hosts.append(row_list[1])
                    ip_list = row_list[3].rsplit(';')
                    for ip in ip_list:
                        sophos_device_ips.append(ip)
                        sophos_all_ips.append(ip)
    return sophos_all_hosts, sophos_device_hosts, sophos_device_ips, sophos_all_ips

def sophos_servers():
    server = '/Users/bkwok/Downloads/sophos_servers_full.csv'  # date: 05-21-2020
    with open(server, 'r') as f1:
        line_count = 0
        for row in f1:
            if line_count == 0:
                line_count = 1  # skip the column name
                continue
            else:
                if row[1] not in sophos_server_hosts:
                    # print (row)
                    row_list = row.rsplit(',')
                    sophos_all_hosts.append(row_list[1])
                    sophos_server_hosts.append(row_list[1])
                    ip_list = row_list[3].rsplit(';')
                    for ip in ip_list:
                        sophos_all_ips.append(ip)
                        sophos_server_ips.append(ip)

    return sophos_all_hosts, sophos_all_ips, sophos_server_hosts, sophos_server_ips


def iventi_devices():
    iventi = '/Users/bkwok/Downloads/Iventi-All devices_0521.csv'  # date: 05-21-2020
    with open(iventi, 'r') as f1:
        line_count = 0
        for row in f1:
            if line_count == 0:
                line_count += 1  # skip the column name
                # print ("Here is my first row", row)
                continue
            else:
                # print (row)
                row_list: List[str] = row.rsplit(',')
                if row_list[0] not in iventi_hosts:
                    iventi_hosts.append(row_list[0])
                    iventi_ips.append(row_list[2])

    return iventi_hosts, iventi_ips

def add_sophos_column_to_Iventi(sophos_device_hosts):
    iventi = pd.read_csv('/Users/bkwok/Downloads/Iventi-All devices_0521.csv' )
    iventi.columns = iventi.columns.str.strip().str.lower().str.replace(' ', '_')
    #print (iventi.head())
    #print (iventi.columns)
    #print (iventi.owner)
    #print (type (iventi.device_name))
    iventi['Is in Sophos'] = iventi.device_name.isin(sophos_device_hosts)
    #print (iventi.head())
    iventi.to_csv('/Users/bkwok/Downloads/Iventi_Sophos.csv', index=False)
    print ("Writing file to .../Users/bkwok/Downloads/Iventi_Sophos.csv")
def nessus():
    with open('/Users/bkwok/Downloads/xperi_internal_nessus_ip.txt', 'r') as f1:
        for row in f1:
            nessus_ip = row.strip()
            if nessus_ip not in nessus_ips:
                nessus_ips.append(nessus_ip)
    return nessus_ips
"""
def add_to_sophos(newhosts):
    with open('/Users/bkwok/Downloads/add_to_sophos.csv', 'w') as output_file:
        line: str
        for line in newhosts:
            output_file.write(line)
            output_file.write(",")
"""
def main():
    sophos_devices()
    sophos_servers()
    iventi_devices()
    nessus()

    newhosts = list(filter(lambda x: x not in sophos_device_hosts, iventi_hosts))
    # print("Iventi hosts to be added into  Sophos : ", list(newhosts))
    # add_to_sophos(newhosts)
    add_sophos_column_to_Iventi(sophos_device_hosts)
    # print ("Sophos hosts: ", list(sophos_hosts))
    # print ("Sophos IPs: ", list(sophos_ips))
    # print ("Iventi hosts: ", list(iventi_hosts))
    # print ("Iventi IPs: ", list(iventi_ips))
    # print ("Nessus IPs : ", list(nessus_ips))
    # print ("Host found in both Sophos and Iventi : ", list(filter(lambda x: x in sophos_hosts, iventi_hosts)))
    # print ("IPs found in both Sophos and Iventi : ", list(filter(lambda x: x in sophos_ips, iventi_ips)))
    # print ("IPs found in both Nessus and Iventi : ", list(filter(lambda x: x in nessus_ips, iventi_ips)))
    # print ("Iventi hosts not in Sophos : ", list(filter(lambda x: x not in sophos_hosts, iventi_hosts)))
    # print ("Iventi hosts not in Sophos : ", list(newhosts))
    # print ("Sophos hosts not in Iventi : ", list(filter(lambda x: x not in iventi_hosts, sophos_hosts)))
    print("Total No. of Sophos hosts: ", len(list(sophos_all_hosts)))
    print("Total No. of Sophos IPs: ", len(list(sophos_all_ips)))
    print("No. of Sophos Devices: ", len(list(sophos_device_hosts)))
    print("No. of Sophos Servers: ", len(list(sophos_server_hosts)))

    print("No. of Iventi hosts: ", len(list(iventi_hosts)))
    print("No. of Iventi IPs: ", len(list(iventi_ips)))
    print("No. of Nessus IPs: ", len(list(nessus_ips)))
    print("No. of devices found in both Sophos and Iventi : ",
          len(list(filter(lambda x: x in sophos_device_hosts, iventi_hosts))))
    print("No. of Iventi devices not in Sophos : ", len(list(filter(lambda x: x not in sophos_device_hosts, iventi_hosts))))
    print("No. of Sophos devices not in Iventi : ", len(list(filter(lambda x: x not in iventi_hosts, sophos_device_hosts))))
    #print("No. of IPs found in both Sophos and Iventi : ", len(list(filter(lambda x: x in sophos_ips, iventi_ips))))
    print("No. of IPs found in both Sophos and Nessus : ", len(list(filter(lambda x: x in sophos_all_ips, nessus_ips))))
    print("No. of IPs found in both Iventi and Nessus : ", len(list(filter(lambda x: x in iventi_ips, nessus_ips))))
    #print("No. of Sophos IPs not in Iventi IPs: ", len(list(filter(lambda x: x not in iventi_ips, sophos_ips))))
    #print("No. of Iventi IPs not in Sophos IPs: ", len(list(filter(lambda x: x not in sophos_ips, iventi_ips))))
    print("No. of Nessus IPs not in Iventi IPs: ", len(list(filter(lambda x: x not in iventi_ips, nessus_ips))))
    print("No. of Iventi IPs not in Nessus IPs: ", len(list(filter(lambda x: x not in nessus_ips, iventi_ips))))
    #print("No. of Nessus IPs not in Sophos IPs: ", len(list(filter(lambda x: x not in sophos_ips, nessus_ips))))


if __name__ == "__main__":
    main()
