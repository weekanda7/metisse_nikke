import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from metisse.metisse import MetisseClass
from metisse.params import ImageRecognitionParams, SaveParams

TEMPLATE = {"template_image_secondary_dir": "draw", "compare_times_counter": 3}
TEMPLATE_ONCE = {"template_image_secondary_dir": "draw", "compare_times_counter": 1}
COMMON_TEMPLATE = {"template_image_secondary_dir": "common", "compare_times_counter": 3}


class script_draw(MetisseClass):
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
        if self.default_tap(ImageRecognitionParams("menu_draw_icon", **TEMPLATE)):
            _counter = 0
            while not self.default_tap(ImageRecognitionParams("draw_friend_icon", **TEMPLATE_ONCE)):
                self.default_tap(ImageRecognitionParams("draw_right_icon", **TEMPLATE))
                _counter += 1
                if _counter > 3:
                    break
            self.execute_time_sleep(10)
            self.default_tap(ImageRecognitionParams("draw_skip", **TEMPLATE))
            self.default_tap(ImageRecognitionParams("draw_confirm", **TEMPLATE))
            self.default_tap(ImageRecognitionParams("menu_main", **COMMON_TEMPLATE))


if __name__ == "__main__":
    script_obj = script_draw("d8602c7c", None, None, "android")
    script_obj()
