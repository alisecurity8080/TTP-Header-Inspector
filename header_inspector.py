import requests

# HTTP Header & API Response Inspector Tool
print("=" * 50)
print("   HTTP HEADER & SECURITY RESPONSE INSPECTOR   ")
print("=" * 50)

# Target URL input with default fallback
target_url = input("\nEnter target API or URL [Default: jsonplaceholder.typicode.com/posts/1]: ").strip()
if not target_url:
    target_url = "https://jsonplaceholder.typicode.com/posts/1"

# Ensure protocol is present
if not target_url.startswith("http://") and not target_url.startswith("https://"):
    target_url = "https://" + target_url

# Custom Headers to bypass basic bot filters or identify security tool
custom_headers = {
    "User-Agent": "AliSecurity-HTTPInspector/1.0",
    "Accept": "application/json"
}

print(f"\n[+] Sending GET Request to: {target_url}...")

try:
    response = requests.get(target_url, headers=custom_headers, timeout=10)

    print(f"[*] HTTP Status Code: {response.status_code}")
    print("\n" + "=" * 25 + " SERVER HEADERS " + "=" * 25)
    
    # Iterate through server response headers
    for header, value in response.headers.items():
        print(f"{header:<30}: {value}")

    print("\n" + "=" * 25 + " RESPONSE BODY " + "=" * 25)
    print(response.text[:500])  # Print first 500 characters
    
    if len(response.text) > 500:
        print("\n[...] Response truncated for clean output.")

except requests.exceptions.RequestException as e:
    print(f"[-] Request Failed: {e}")
