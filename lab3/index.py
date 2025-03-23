import socket
import dns.resolver
import dns.reversename
import dns.exception
import ipaddress

current_dns = None

def is_valid_ip(ip_str):
    try:
        ipaddress.ip_address(ip_str)
        return True
    except ValueError:
        return False

def validate_dns_server(dns_ip):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [dns_ip]
    resolver.lifetime = 2
    try:
        resolver.resolve('example.com', 'A')
        return True
    except dns.exception.DNSException:
        return False

def resolve_domain_system(domain):
    try:
        _, _, ips = socket.gethostbyname_ex(domain)
        return ips, []
    except socket.gaierror as e:
        return None, [str(e)]

def resolve_ip_system(ip):
    try:
        hostname, _, _ = socket.gethostbyaddr(ip)
        return [hostname], []
    except socket.herror as e:
        return None, [str(e)]

def resolve_domain_custom(domain, dns_ip):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [dns_ip]
    resolver.lifetime = 2
    ips = []
    errors = []
    
    try:
        answers_a = resolver.resolve(domain, 'A')
        ips.extend([str(r) for r in answers_a])
    except dns.resolver.NXDOMAIN:
        return None, ["Domain not found."]
    except dns.resolver.NoAnswer:
        pass
    except dns.resolver.Timeout:
        errors.append("A record query timed out.")
    except dns.exception.DNSException as e:
        errors.append(f"A record error: {e}")
    
    try:
        answers_aaaa = resolver.resolve(domain, 'AAAA')
        ips.extend([str(r) for r in answers_aaaa])
    except dns.resolver.NXDOMAIN:
        errors.append("Domain not found during AAAA query.")
    except dns.resolver.NoAnswer:
        pass
    except dns.resolver.Timeout:
        errors.append("AAAA record query timed out.")
    except dns.exception.DNSException as e:
        errors.append(f"AAAA record error: {e}")
    
    if not ips and errors:
        return None, errors
    elif not ips and not errors:
        return None, ["No IP addresses found."]
    return ips, errors

def resolve_ip_custom(ip_str, dns_ip):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [dns_ip]
    resolver.lifetime = 2
    try:
        rev_name = dns.reversename.from_address(ip_str)
        answers = resolver.resolve(rev_name, 'PTR')
        domains = [str(r.target) for r in answers]
        return domains, []
    except dns.resolver.NXDOMAIN:
        return None, ["No PTR records found."]
    except dns.resolver.NoAnswer:
        return None, ["No PTR records found."]
    except dns.resolver.Timeout:
        return None, ["DNS query timed out."]
    except dns.exception.DNSException as e:
        return None, [f"DNS error: {e}"]

def main():
    global current_dns
    print("DNS Client Application. Commands: 'resolve <domain/ip>' or 'use dns <ip>'")
    
    while True:
        try:
            command = input("> ").strip()
            if not command:
                continue
            
            parts = command.split()
            if not parts:
                continue
            
            if parts[0] == "resolve" and len(parts) == 2:
                target = parts[1]
                is_ip = False
                
                try:
                    ipaddress.ip_address(target)
                    is_ip = True
                except ValueError:
                    pass
                
                if current_dns is None:
                    if is_ip:
                        result, errors = resolve_ip_system(target)
                    else:
                        result, errors = resolve_domain_system(target)
                else:
                    if is_ip:
                        result, errors = resolve_ip_custom(target, current_dns)
                    else:
                        result, errors = resolve_domain_custom(target, current_dns)
                
                if errors:
                    print("Errors:")
                    for error in errors:
                        print(f" - {error}")
                if result:
                    print("Domains:" if is_ip else "IPs:")
                    for item in result:
                        print(item)
                elif not errors:
                    print("No results found.")
                
            elif parts[0] == "use" and len(parts) == 3 and parts[1] == "dns":
                new_dns = parts[2]
                if not is_valid_ip(new_dns):
                    print("Error: Invalid IP address format")
                    continue
                
                if validate_dns_server(new_dns):
                    current_dns = new_dns
                    print(f"DNS server changed to {new_dns}")
                else:
                    print("Error: DNS server is unreachable or not responding")
            
            else:
                print("Invalid command. Usage:")
                print("resolve <domain/ip>")
                print("use dns <ip>")
        
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()