import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from metisse.metisse import MetisseClass
from metisse.params import ImageRecognitionParams, SaveParams

TEMPLATE = {"template_image_secondary_dir": "front_line_base", "compare_times_counter": 3}
COMMON_TEMPLATE = {"template_image_secondary_dir": "common", "compare_times_counter": 3}


class scipt_front_line_base(MetisseClass):
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
        if self.default_tap(ImageRecognitionParams("menu_front_line_base", **TEMPLATE)):
            self.execute_time_sleep(15)
            if self.default_tap(ImageRecognitionParams("flb_dispatch_icon", **TEMPLATE)):
                if self.default_tap(ImageRecognitionParams("flb_dispatch_get_all", **TEMPLATE)):
                    self.default_tap(ImageRecognitionParams("reward_text", **COMMON_TEMPLATE))
                if self.default_tap(ImageRecognitionParams("flb_dispatch_send_all", **TEMPLATE)):
                    self.default_tap(ImageRecognitionParams("flb_dispatch_send_all_confirm", **TEMPLATE))

        self.default_tap(ImageRecognitionParams("close_white_icon", **COMMON_TEMPLATE))
        self.default_tap(ImageRecognitionParams("home_icon", **COMMON_TEMPLATE))


if __name__ == "__main__":
    script_obj = scipt_front_line_base("d8602c7c", None, None, "android")
    script_obj()
