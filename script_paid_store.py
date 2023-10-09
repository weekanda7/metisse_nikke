import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from metisse.metisse import MetisseClass
from metisse.params import ImageRecognitionParams, SaveParams

TEMPLATE = {"template_image_secondary_dir": "paid_store", "compare_times_counter": 3}
COMMON_TEMPLATE = {"template_image_secondary_dir": "common", "compare_times_counter": 3}


class script_paid_store(MetisseClass):
    def __init__(self, device_id="", relatively_path="", pyqt6_ui_label={}, os_environment=""):
        MetisseClass.__init__(
            self,
            device_id=device_id,
            relatively_path=relatively_path,
            pyqt6_ui_label=pyqt6_ui_label,
            os_environment=os_environment,
        )
        self.device_id = device_id

    def __call__(self, *args, **kwargs):
        if self.default_tap(ImageRecognitionParams("menu_paid_store", **TEMPLATE)):
            if self.default_tap(ImageRecognitionParams("paid_store_gift_tab", **TEMPLATE)):
                self.default_tap(ImageRecognitionParams("paid_store_gift_tab_everyday_subtab", **TEMPLATE))
                self.default_tap(ImageRecognitionParams("free_text", **COMMON_TEMPLATE))
                self.default_tap(ImageRecognitionParams("reward_text", **COMMON_TEMPLATE))
        self.default_tap(ImageRecognitionParams("home_icon", **COMMON_TEMPLATE))


if __name__ == "__main__":
    script_obj = script_paid_store("d8602c7c", None, None, "android")
    script_obj()
