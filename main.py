import glob
import logging
import os.path
import shutil

from hbutils.system import TemporaryDirectory
from imgutils.data import load_image

logging.basicConfig(level=logging.INFO)


def test_img(gif_file: str):
    with TemporaryDirectory(ignore_cleanup_errors=True) as td:
        dst_gif_file = os.path.join(td, os.path.basename(gif_file))
        shutil.copyfile(gif_file, dst_gif_file)

        assert os.path.exists(dst_gif_file)
        image = load_image(dst_gif_file)
        image.load()

        p_image = image.convert('RGB')
        p_image.save(os.path.join(td, 'p_image.png'))


if __name__ == '__main__':
    for file in glob.glob(os.path.join('files', '*.gif')):
        logging.info(f'Test file {file!r} ...')
        test_img(file)
