from instagram_auto_like_comments.libs.crawler import crawl

url = "https://instagram.com"
page_string = crawl(url)
print(page_string)