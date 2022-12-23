import logging
from time import sleep

import grpc

from tobii_remote import tobii_remote_pb2_grpc
from tobii_remote.tobii_remote_pb2 import (
    EyeTrackerInfo,
    GazePosOnScreen,
    google_dot_protobuf_dot_empty__pb2,
)

"""
Sample program of gRPC Tobii Remote Client
"""


def main():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = tobii_remote_pb2_grpc.TobiiRemoteStub(channel)
        empty = google_dot_protobuf_dot_empty__pb2.Empty()

        model_name: EyeTrackerInfo = stub.GetEyeTrackerInfo(empty).eyetracker_model_id
        print("Eye tracker: ", model_name)

        while True:
            gaze_pos: GazePosOnScreen = stub.GetGazePosOnScreen(empty)
            print(f"x: {gaze_pos.pos_x}, y: {gaze_pos.pos_y}")
            sleep(1)


if __name__ == "__main__":
    logging.basicConfig()
    main()
