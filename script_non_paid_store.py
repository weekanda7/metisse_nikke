import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from metisse.metisse import MetisseClass
from metisse.params import ImageRecognitionParams, SaveParams

TEMPLATE = {"template_image_secondary_dir": "non_paid_store", "compare_times_counter": 3}
COMMON_TEMPLATE = {"template_image_secondary_dir": "common", "compare_times_counter": 3}


class script_non_paid_store(MetisseClass):
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
        if self.default_tap(ImageRecognitionParams("menu_non_paid_store", **TEMPLATE)):
            if self.default_tap(ImageRecognitionParams("nps_com_store_free", **TEMPLATE)):
                self.default_tap(ImageRecognitionParams("nps_com_store_buy", **TEMPLATE))
                self.default_tap(ImageRecognitionParams("reward_text", **COMMON_TEMPLATE))
            if self.default_tap(ImageRecognitionParams("nps_refresh_icon", **TEMPLATE)):
                self.default_tap(ImageRecognitionParams("confirm_circle_tick_btn", **COMMON_TEMPLATE))
            if self.default_tap(ImageRecognitionParams("nps_com_store_free", **TEMPLATE)):
                self.default_tap(ImageRecognitionParams("nps_com_store_buy", **TEMPLATE))
                self.default_tap(ImageRecognitionParams("reward_text", **COMMON_TEMPLATE))
            if self.default_tap(ImageRecognitionParams("nps_diamond_tab", **TEMPLATE)) and self.default_tap(
                ImageRecognitionParams("nps_body_store_discount", **TEMPLATE)
            ):
                self.default_tap(ImageRecognitionParams("nps_com_store_buy", **TEMPLATE))
                self.default_tap(ImageRecognitionParams("reward_text", **COMMON_TEMPLATE))
            if self.default_tap(ImageRecognitionParams("nps_arena_tab", **TEMPLATE)):
                for templat_name in [f"nps_arena_store_{x}" for x in ["wind", "lightning", "water", "box"]]:
                    if self.default_tap(ImageRecognitionParams(templat_name, **TEMPLATE)):
                        self.default_tap(ImageRecognitionParams("nps_com_store_buy", **TEMPLATE))
                        self.default_tap(ImageRecognitionParams("reward_text", **COMMON_TEMPLATE))
            self.default_tap(ImageRecognitionParams("home_icon", **COMMON_TEMPLATE))


if __name__ == "__main__":
    script_obj = script_non_paid_store("d8602c7c", None, None, "android")
    script_obj()
