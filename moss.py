import configparser
import glob
import logging
import os
from tkinter.filedialog import askdirectory

import mosspy


class Config:
    userid: str  # Moss userid
    source_dir: str  # 掃描資料夾路徑
    base_dir: str  # base資料夾路徑

    def __init__(self, config_file_path):
        # 讀取配置檔案並獲取userid
        # 請在config.ini中設置userid，如下所示:
        # [moss]
        # userid = 123456789
        self._config = configparser.ConfigParser()
        self._config.read(config_file_path)
        self.userid = self.get("moss", "userid")

        # 選擇base資料夾路徑 (template / starter code)
        self.base_dir = askdirectory(title="Select base directory (Template / Starter code)", initialdir="./")
        # 選擇掃描資料夾路徑 (學生作業)
        self.source_dir = askdirectory(title="Select source directory (The folder to be scanned)", initialdir="./")

        # 若無讀取到路徑則退出程式
        if self.source_dir == "":
            print("Invalid directory path")
            exit(1)

    def get(self, section, key):
        try:
            return self._config.get(section, key)
        except ValueError:
            print(f"Please set '{key}' in '{section}' section of 'config.ini' file")
            exit(1)


def main():
    # 初始化1. moss userid 2. 掃描資料夾路徑 3. base資料夾路徑
    config = Config("config.ini")

    # 創建Moss實例，並設置語言為Java
    moss = mosspy.Moss(config.userid, "java")

    # 以各個學生子目錄為單位而非單個檔案進行比較
    moss.setDirectoryMode(1)

    # 加入base檔案 (template / starter code)
    if config.base_dir != "":
        for file in glob.glob(f"{config.base_dir}/**/*.java", recursive=True):
            moss.addBaseFile(file)

    # 加入掃描檔案 (學生作業)
    for file in glob.glob(f"{config.source_dir}/**/*.java", recursive=True):
        moss.addFile(file)

    # 生成報告
    print("Checking plagiarism...")
    url = moss.send()
    print("Report Url: " + url)

    # 詢問是否下載本地報告(包含代碼差異頁面)
    if input("Download report? (y/n): ").lower() == "y":
        print("Downloading...")
        folder_name = os.path.basename(config.source_dir)
        mosspy.download_report(url, f"report/{folder_name}_report/", log_level=logging.INFO)
        print(f"Downloaded to 'report/{folder_name}_report' directory")


def test():
    config = Config("config.ini")
    print(config.userid)
    print(config.source_dir)
    print(config.base_dir)


if __name__ == "__main__":
    main()
    # test()
