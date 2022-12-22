import logging
from concurrent import futures

import grpc
import tobii_remote_pb2_grpc
from tobii_remote_pb2 import EyeTrackerInfo, GazePosOnScreen
from tracker import Tracker


class TobiiRemoteServicer(tobii_remote_pb2_grpc.TobiiRemoteServicer):
    def __init__(self):
        super().__init__()
        self.tracker: Tracker = None

    def get_gaze_pos(self):
        x, y = self.tracker.get_gaze_pos()
        return GazePosOnScreen(pos_x=x, pos_y=y)

    def GetGazePosOnScreen(self, request, context):
        gaze_pos = self.get_gaze_pos()
        if gaze_pos is None:
            return GazePosOnScreen(pos_x=-1.0, pos_y=-1.0)
        else:
            return gaze_pos

    def GetEyeTrackerInfo(self, request, context):
        info = EyeTrackerInfo(eyetracker_model_id="")
        return info


def serve():
    tracker = Tracker()
    servicer = TobiiRemoteServicer()
    servicer.tracker = tracker

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tobii_remote_pb2_grpc.add_TobiiRemoteServicer_to_server(
        servicer, server
    )
    server.add_insecure_port("[::]:50051")

    servicer.tracker.start()
    server.start()

    server.wait_for_termination()
    tracker.stop()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
