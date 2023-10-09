import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from metisse.metisse import MetisseClass
from metisse.params import ImageRecognitionParams, SaveParams

TEMPLATE = {"template_image_secondary_dir": "outpost", "compare_times_counter": 3}
COMMON_TEMPLATE = {"template_image_secondary_dir": "common", "compare_times_counter": 3}


class script_outpost(MetisseClass):
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
        if self.default_tap(ImageRecognitionParams("menu_outpost", **COMMON_TEMPLATE)):
            if self.default_tap(ImageRecognitionParams("outpost_reward", **TEMPLATE)):
                self.default_tap(ImageRecognitionParams("reward_text", **COMMON_TEMPLATE))
                self.default_tap(ImageRecognitionParams("close_blue_icon", **COMMON_TEMPLATE))
                self.default_tap(ImageRecognitionParams("close_blue_icon", **COMMON_TEMPLATE))
        if self.default_tap(ImageRecognitionParams("menu_outpost", **COMMON_TEMPLATE)):
            if self.default_tap(ImageRecognitionParams("outpost_extra_get", **TEMPLATE)):
                self.default_tap(ImageRecognitionParams("reward_text", **COMMON_TEMPLATE))
            if self.default_tap(ImageRecognitionParams("outpost_extra_get", **TEMPLATE)):
                self.default_tap(ImageRecognitionParams("confirm_tick_btn", **COMMON_TEMPLATE))
                self.default_tap(ImageRecognitionParams("reward_text", **COMMON_TEMPLATE))
            self.default_tap(ImageRecognitionParams("cancel_white_btn", **COMMON_TEMPLATE))
            self.default_tap(ImageRecognitionParams("close_blue_icon", **COMMON_TEMPLATE))


if __name__ == "__main__":
    script_obj = script_outpost("d8602c7c", None, None, "android")
    script_obj()
