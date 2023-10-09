import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from metisse.metisse import MetisseClass
from metisse.params import ImageRecognitionParams, SaveParams

TEMPLATE = {"template_image_secondary_dir": "login", "compare_times_counter": 3}
COMMON_TEMPLATE = {"template_image_secondary_dir": "common", "compare_times_counter": 3}


class script_login(MetisseClass):
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
        os.system(f"adb -s {self.device_id}  shell am force-stop com.gamamobi.nikke")
        os.system(f"adb -s {self.device_id}  shell am start -n com.gamamobi.nikke/com.shiftup.nk.MainActivity")
        self.execute_time_sleep(20)
        self.default_tap(ImageRecognitionParams("confirm_tick_btn", **COMMON_TEMPLATE))
        self.execute_time_sleep(30)
        while not self.default_tap(ImageRecognitionParams("ready_for_login", **TEMPLATE)):
            self.execute_time_sleep(5)
        self.execute_time_sleep(15)
        while not self.default_tap(ImageRecognitionParams("menu_check_flag", **COMMON_TEMPLATE)):
            self.default_tap(ImageRecognitionParams("reward_text", **COMMON_TEMPLATE))
            self.default_tap(ImageRecognitionParams("reward_text", **COMMON_TEMPLATE))
            self.default_tap(ImageRecognitionParams("close_blue_icon", **COMMON_TEMPLATE))
            if self.default_tap(ImageRecognitionParams("get_daily_login", **COMMON_TEMPLATE)):
                self.default_tap(ImageRecognitionParams("reward_text", **COMMON_TEMPLATE))
                self.default_tap(ImageRecognitionParams("close_pink_icon", **COMMON_TEMPLATE))
            if self.default_tap(ImageRecognitionParams("get_daily_all", **COMMON_TEMPLATE)):
                self.default_tap(ImageRecognitionParams("reward_text", **COMMON_TEMPLATE))
                self.default_tap(ImageRecognitionParams("close_sp_icon", **COMMON_TEMPLATE))
        self.execute_time_sleep(1)  # wait 1 second


if __name__ == "__main__":
    script_obj = script_login("d8602c7c", None, None, "android")
    script_obj()
