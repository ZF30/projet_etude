import json
import dns.resolver

def dns_footprinting(domain):
    results = {}
    
    # Perform DNS queries
    try:
        answers = dns.resolver.resolve(domain, 'A')
        results['A_records'] = [str(r) for r in answers]
    except dns.resolver.NoAnswer:
        results['A_records'] = []
    
    try:
        answers = dns.resolver.resolve(domain, 'MX')
        results['MX_records'] = [str(r.exchange) for r in answers]
    except dns.resolver.NoAnswer:
        results['MX_records'] = []
    
    try:
        answers = dns.resolver.resolve(domain, 'NS')
        results['NS_records'] = [str(r) for r in answers]
    except dns.resolver.NoAnswer:
        results['NS_records'] = []
    print(results)
    with open("dns_footprinting.json", 'w') as file:
        json.dump(results, file, indent=4)
    return results


if __name__ == "__main__":
    domain = input("Enter the domain name: ")
    results = dns_footprinting(domain)
    print("DNS footprinting results have been exported to")
