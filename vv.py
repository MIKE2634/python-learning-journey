logs = [
    {"user": "admin", "ip": "192.168.1.10", "country": "Kenya", "status": "failed", "severity": "high"},
    {"user": "john", "ip": "10.0.0.5", "country": "USA", "status": "success", "severity": "low"},
    {"user": "mike", "ip": "172.16.0.3", "country": "kenya", "status": "failed", "severity": "medium"},
    {"user": "sarah", "ip": "8.8.8.8", "country": "UK", "status": "success", "severity": "low"},
    {"user": "david", "ip": "192.168.0.1", "country": "KENYA", "status": "failed", "severity": "high"},
    {"user": "alice", "ip": "10.10.10.10", "country": "Nigeria", "status": "failed", "severity": "high"},
    {"user": "bob", "ip": "172.16.5.4", "country": "Kenya", "status": "success", "severity": "low"},
]
i=0
for log in logs: 
    print(log["user"],log["ip"])
    print()
for log in logs:
    if log["severity"].lower()=="high":
        print(log["user"],log["country"])
        print()
for log in logs:
    if log["country"].lower()=="kenya" and log["status"].lower()=="failed":
        print(log)
        print()
        i =i+1
print(i)
failed_logs = []
for log in logs:
    if log["status"].lower()=="failed":
        
        failed_logs.append(log["country"])
print(failed_logs)
        

