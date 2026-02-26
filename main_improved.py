import requests

class NovelDownloader:
    def __init__(self, verify_ssl=True):
        self.session = requests.Session()
        self.session.verify = verify_ssl

    def download_novel(self, url):
        try:
            response = self.session.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        finally:
            self.cleanup()

    def cleanup(self):
        self.session.close()  # Ensure the session is closed

# Usage example
if __name__ == "__main__":
    downloader = NovelDownloader(verify_ssl=False)  # Set to True for production
    novel_content = downloader.download_novel("http://example.com/novel")
    print(novel_content)