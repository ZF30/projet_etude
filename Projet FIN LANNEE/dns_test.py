import json
import dns.resolver
import whois

def get_dns_records(domain):
    results = {}
    results['Domain'] = domain
    # Perform DNS queries
    try:
        answers = dns.resolver.resolve(domain, 'A')
        results['A_records'] = [str(r) for r in answers]
    except dns.resolver.NoAnswer:
        results['A_records'] = []
    
    try:
        answers = dns.resolver.resolve(domain, 'AAAA')
        results['AAAA_records'] = [str(r) for r in answers]
    except dns.resolver.NoAnswer:
        results['AAAA_records'] = []
    
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
    
    try:
        answers = dns.resolver.resolve(domain, 'CNAME')
        results['CNAME_records'] = [str(r) for r in answers]
    except dns.resolver.NoAnswer:
        results['CNAME_records'] = []
        
    try:
        answers = dns.resolver.resolve(domain, 'TXT')
        results['TXT_records'] = [str(r) for r in answers]
    except dns.resolver.NoAnswer:
        results['TXT_records'] = []
        
    try:
        answers = dns.resolver.resolve(domain, 'SOA')
        results['SOA_records'] = [str(r) for r in answers]
    except dns.resolver.NoAnswer:
        results['SOA_records'] = []
        
    # Also save the results to a JSON file
    with open("./Exports/dns_footprinting_results.json", 'w') as file:
        json.dump(results, file, indent=4)
    return results

