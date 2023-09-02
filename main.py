import os
import requests
import zipfile


def download_file(url, save_path):
  try:
    response = requests.get(url)
    if response.status_code == 200:
      filename = url.split("/")[-1]
      with open(save_path, "wb") as file:
        file.write(response.content)
      print(f"Downloaded {filename} and saved as {save_path}")
      return True
    else:
      print("Failed to download file (HTTP status code:", response.status_code,
            ")")
  except Exception as e:
    print("An error occurred:", e)
  return False


def unzip_file(zip_path, extract_folder):
  with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_folder)
    print("Extracted files to:", extract_folder)


if __name__ == "__main__":
  url = "https://zip.baipiao.eu.org"  # 修改为你需要下载的压缩文件的 URL
  save_path = os.path.join(os.path.dirname(__file__),
                           "downloaded_file.zip")  # 修改保存路径和文件名
  extract_folder = os.path.dirname(__file__)  # 解压缩文件的目标文件夹为当前脚本所在文件夹

  print("Downloading from:", url)
  if download_file(url, save_path):
    unzip_file(save_path, extract_folder)
    os.remove(save_path)  # 删除下载的压缩文件
