import requests
import concurrent.futures
import time

img_urls = [
    "https://images.unsplash.com/photo-1662578108849-6f75d4f8c280",
    "https://images.unsplash.com/photo-1657664049378-c8aadfe323f1",
    "https://images.unsplash.com/photo-1662622194548-f50b20179287"
]

def download_images(img_url):
    image_bytes = requests.get(img_url).content #return in bytes
    image_name = img_url.split('/')[3]
    image_name = f'{image_name}.jpg'
    with open(image_name, 'wb') as image_file:
        image_file.write(image_bytes)
        print(f"{image_name} is downloading.......")


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_images, img_urls)

finish = time.perf_counter()
print("Task is done in {0} second(s)".format(round(finish, 2)))
