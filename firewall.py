import random

def generate_random_ip():
    return f"172.225.219.{random.randint(0,50)}"

def check_firewall_rules(ip, rules):
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
        return "allow"

def main():
    firewall_rules={
        "172.225.219.33":"block"

    }
    for i in range(12):
        ip_address = generate_random_ip()
        action = check_firewall_rules(ip_address,firewall_rules)
        random_number = random.randint(0,9999)
        print(f"IP: {ip_address}, Action: {action}, Random Number: {random_number}")



if __name__ == '__main__':
    main()