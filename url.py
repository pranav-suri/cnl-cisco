from urllib.parse import urlparse

# Sample URL
url = "https://www.example.com:8080/path/to/resource?query=1#fragment1"

# Parse the URL into components
parsed_url = urlparse(url)

# Extract components
protocol = parsed_url.scheme
domain = parsed_url.hostname
port = parsed_url.port
path = parsed_url.path
query = parsed_url.query
fragment = parsed_url.fragment

print("Protocol:", protocol)
print("Domain:", domain)
print("Port:", port)
print("Path:", path)
print("Query:", query)
print("Fragment:", fragment)
