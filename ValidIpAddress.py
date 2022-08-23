# O(1) time | O(1) space
def validIPAddresses(string):
    valid_ips = []
    for i in range(1, min(len(string), 4)):
        curr_ip_address_parts = ['', '', '', '']
        
        curr_ip_address_parts[0] = string[:i]
        if not valid_ip(curr_ip_address_parts[0]):
            continue
        
        for j in range(i + 1, i + min(len(string) - i, 4)):
            curr_ip_address_parts[1] = string[i:j]
            if not valid_ip(curr_ip_address_parts[1]):
                continue
            
            for k in range(j + 1, j + min(len(string) - j, 4)):
                curr_ip_address_parts[2] = string[j:k]
                curr_ip_address_parts[3] = string[k:]
                
                if valid_ip(curr_ip_address_parts[2]) and valid_ip(curr_ip_address_parts[3]):
                    valid_ips.append(".".join(curr_ip_address_parts))
    return valid_ips


def valid_ip(string):
    int_ip = int(string)
    if int_ip > 255:
        return False
    return len(string) == len(str(int_ip)) # check for leading 0


def main():
    ip = "1921680"
    print(validIPAddresses(ip))
    
    
if __name__ == "__main__":
    main()