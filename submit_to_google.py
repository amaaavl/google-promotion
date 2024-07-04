import requests

def submit_to_google(sitemap_url):
    google_url = f"https://www.google.com/ping?sitemap={sitemap_url}"
    response = requests.get(google_url)
    return response.status_code

sitemap_url = "https://smegig.ng/sitemap.xml"  # Replace with your actual sitemap URL
response_code = submit_to_google(sitemap_url)
print(f"Submitted to Google with response code: {response_code}")
