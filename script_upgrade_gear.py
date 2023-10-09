import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from metisse.metisse import MetisseClass
from metisse.params import ImageRecognitionParams, SaveParams

TEMPLATE = {"template_image_secondary_dir": "upgrade_gear", "compare_times_counter": 3}
COMMON_TEMPLATE = {"template_image_secondary_dir": "common", "compare_times_counter": 3}


class script_upgrade_gear(MetisseClass):
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
        if self.default_tap(ImageRecognitionParams("menu_niki_list_icon", **TEMPLATE)) and self.default_tap(
            ImageRecognitionParams("niki_list_target1_avatar", **TEMPLATE)
        ):
            if self.default_tap(ImageRecognitionParams("niki_detail_gear_icon", **TEMPLATE)):
                if self.default_tap(ImageRecognitionParams("niki_detail_gear_upgrade_icon", **TEMPLATE)):
                    if self.default_tap(
                        ImageRecognitionParams("niki_detail_gear_upgrade_common_element_icon", **TEMPLATE)
                    ):
                        self.default_tap(ImageRecognitionParams("niki_detail_gear_upgrade_confurm_icon", **TEMPLATE))
                    self.default_tap(ImageRecognitionParams("close_blue_icon", **COMMON_TEMPLATE))
                else:
                    self.default_tap(ImageRecognitionParams("close_white_icon", **COMMON_TEMPLATE))
        self.default_tap(ImageRecognitionParams("home_icon", **COMMON_TEMPLATE))


if __name__ == "__main__":
    script_obj = script_upgrade_gear("d8602c7c", None, None, "android")
    script_obj()
