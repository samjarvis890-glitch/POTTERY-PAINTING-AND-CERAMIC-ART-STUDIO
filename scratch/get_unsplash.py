import urllib.request
import re

def get_unsplash_ids(query):
    url = f"https://unsplash.com/s/photos/{query}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        ids = re.findall(r'"id":"([a-zA-Z0-9_-]{10,12})"', html)
        # Filter out some common non-photo ids
        ids = [i for i in ids if not i.startswith('search')][:5]
        return ids
    except Exception as e:
        print(e)
        return []

print("Pottery wheel:", get_unsplash_ids("pottery-wheel"))
print("Kiln fire:", get_unsplash_ids("kiln-fire"))
