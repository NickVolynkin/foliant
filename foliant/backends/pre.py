from shutil import copytree, rmtree

from foliant.utils import spinner
from foliant.backends.base import BaseBackend


class Backend(BaseBackend):
    targets = 'pre',

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._preprocessed_dir_name = f'{self.get_slug()}.pre'

    def make(self, target: str) -> str:
        rmtree(self._preprocessed_dir_name, ignore_errors=True)
        copytree(self.working_dir, self._preprocessed_dir_name)

        return self._preprocessed_dir_name