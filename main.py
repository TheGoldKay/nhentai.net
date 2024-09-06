import os
import sys
import json

from nhentai import constant
from nhentai.cmdline import load_config
from nhentai.downloader import Downloader
from nhentai.parser import doujinshi_parser
from nhentai.doujinshi import Doujinshi
from nhentai.utils import generate_html, generate_cbz

from imgs2pdf import save_pdf


class DownloadHentai():
    def __init__(self, download_dir):
        self.download_dir = download_dir

    def save_info(self, data):
        with open(os.path.join(self.download_dir, str(data["id"]), 'info.json'), 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
            
    def test_download(self, did):
        info = Doujinshi(**doujinshi_parser(did), name_format='%i')
        info.downloader = Downloader(path=self.download_dir, size=5)
        info.download(regenerate_cbz=True)
        self.save_info(info.get_data())


def main(did):
    download_dir = os.path.join(os.getcwd(), 'download')
    download = DownloadHentai(download_dir)
    download.test_download(did)
    save_pdf(did)
    
if __name__ == '__main__':
    if len(sys.argv) > 1:
        did = sys.argv[1]
        main(did)
    else:
        raise ValueError('No doujinshi id is provided')
    