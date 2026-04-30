import requests

def main():
    # Sample API interaction: Fetch a post from JSONPlaceholder
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print("Fetched data from API:")
        print(f"Title: {data['title']}")
        print(f"Body: {data['body']}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

if __name__ == "__main__":
    main()