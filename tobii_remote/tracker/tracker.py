from typing import Optional, Tuple

import tobii_research as tr

# TODO
# add capability to configure eyetracker settings


class TrackerNotFoundError(Exception):
    "Raised when supported eyetrackers not found"
    pass


class Tracker:
    def __init__(self) -> None:
        self.pos_x: float = -1.0
        self.pos_y: float = -1.0

        self._get_tracker()

    def start(self):
        self._set_callback()

    def stop(self):
        self.eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA)

    def get_gaze_pos(self) -> Tuple[float, float]:
        return (self.pos_x, self.pos_y)

    def _get_tracker(self, idx: Optional[int] = 0):
        eyetrackers = tr.find_all_eyetrackers()
        if len(eyetrackers) >= 1:
            self.eyetracker = eyetrackers[idx]
        else:
            raise TrackerNotFoundError("No EyeTracker Found")

    def _set_callback(self):
        def visual_callback(gaze_data):
            if self._check_data_validity(gaze_data):
                left_point = gaze_data.left_eye.gaze_point.position_on_display_area
                right_point = gaze_data.right_eye.gaze_point.position_on_display_area
                self.pos_x: float = (left_point[0] + right_point[0]) / 2.0
                self.pos_y: float = (left_point[1] + right_point[1]) / 2.0

        self.eyetracker.subscribe_to(
            tr.EYETRACKER_GAZE_DATA, visual_callback, as_dictionary=False
        )

    def _check_data_validity(self, gaze_data):
        cond = (
            gaze_data.right_eye.gaze_point.validity
            and gaze_data.left_eye.gaze_point.validity
        )
        return cond
