# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""
DESCRIPTION:
    This sample demonstrates how to use EyePop pretrained models for computer
    vision inference. EyePop provides a variety of pretrained models in its
    registry that can be used for detecting people, animals, vehicles, and more.

    Pretrained Models Available in the EyePop Registry:

    Model                                   Description
    -------                                 -----------
    eyepop.common-objects:latest            Detect people + common everyday objects
    eyepop.animal:latest                    People + Animal detection and classification
    eyepop.vehicle:latest                   People + Vehicle detection
    eyepop.device:latest                    People + Electronic device detection
    eyepop.sports:latest                    People + Sports equipment and activity detection
    eyepop.person:latest                    Person detection
    eyepop.person.pose:latest               Human pose estimation
    eyepop.person.2d-body-points:latest     2D body keypoint detection
    eyepop.person.3d-body-points.full:latest    Full 3D body pose estimation
    eyepop.person.3d-body-points.heavy:latest   High-accuracy 3D body pose model
    eyepop.person.3d-body-points.lite:latest    Lightweight 3D body pose model
    eyepop.person.3d-hand-points:latest     3D hand keypoint detection

PREREQUISITES:
    Install the eyepop package:
        pip install eyepop==3.12.0

USAGE:
    python sample_eyepop_pretrained_models.py

    Set these environment variables before running the sample:
    1) EYEPOP_API_KEY - Your EyePop API key. Keep it secret.
    2) EYEPOP_IMAGE_PATH - Optional. Path to a local image file to analyze.
       Defaults to using a sample URL if not provided.
"""


# [START eyepop_person_detection]
def sample_person_detection():
    """Detect people in an image using the eyepop.person:latest model."""
    import json
    import os
    from pathlib import Path

    from eyepop import EyePopSdk
    from eyepop.worker.worker_types import InferenceComponent, Pop

    api_key = os.environ.get("EYEPOP_API_KEY", "")
    if not api_key:
        print("Missing environment variable 'EYEPOP_API_KEY'")
        print("Set it before running this sample.")
        return

    pop = Pop(components=[InferenceComponent(ability="eyepop.person:latest")])

    image_path = os.environ.get("EYEPOP_IMAGE_PATH")

    with EyePopSdk.workerEndpoint(api_key=api_key) as endpoint:
        endpoint.set_pop(pop)
        if image_path:
            job = endpoint.upload(Path(image_path))
        else:
            job = endpoint.load_from("https://eyepop.ai/assets/examples/example_photo.jpg")
        while result := job.predict():
            print(json.dumps(result, indent=2))


# [END eyepop_person_detection]


# [START eyepop_common_objects_detection]
def sample_common_objects_detection():
    """Detect people and common everyday objects using eyepop.common-objects:latest."""
    import json
    import os
    from pathlib import Path

    from eyepop import EyePopSdk
    from eyepop.worker.worker_types import InferenceComponent, Pop

    api_key = os.environ.get("EYEPOP_API_KEY", "")
    if not api_key:
        print("Missing environment variable 'EYEPOP_API_KEY'")
        print("Set it before running this sample.")
        return

    pop = Pop(components=[InferenceComponent(ability="eyepop.common-objects:latest")])

    image_path = os.environ.get("EYEPOP_IMAGE_PATH")

    with EyePopSdk.workerEndpoint(api_key=api_key) as endpoint:
        endpoint.set_pop(pop)
        if image_path:
            job = endpoint.upload(Path(image_path))
        else:
            job = endpoint.load_from("https://eyepop.ai/assets/examples/example_photo.jpg")
        while result := job.predict():
            print(json.dumps(result, indent=2))


# [END eyepop_common_objects_detection]


# [START eyepop_animal_detection]
def sample_animal_detection():
    """Detect people and animals using eyepop.animal:latest."""
    import json
    import os
    from pathlib import Path

    from eyepop import EyePopSdk
    from eyepop.worker.worker_types import InferenceComponent, Pop

    api_key = os.environ.get("EYEPOP_API_KEY", "")
    if not api_key:
        print("Missing environment variable 'EYEPOP_API_KEY'")
        print("Set it before running this sample.")
        return

    pop = Pop(components=[InferenceComponent(ability="eyepop.animal:latest")])

    image_path = os.environ.get("EYEPOP_IMAGE_PATH")

    with EyePopSdk.workerEndpoint(api_key=api_key) as endpoint:
        endpoint.set_pop(pop)
        if image_path:
            job = endpoint.upload(Path(image_path))
        else:
            job = endpoint.load_from("https://eyepop.ai/assets/examples/example_photo.jpg")
        while result := job.predict():
            print(json.dumps(result, indent=2))


# [END eyepop_animal_detection]


# [START eyepop_vehicle_detection]
def sample_vehicle_detection():
    """Detect people and vehicles using eyepop.vehicle:latest."""
    import json
    import os
    from pathlib import Path

    from eyepop import EyePopSdk
    from eyepop.worker.worker_types import InferenceComponent, Pop

    api_key = os.environ.get("EYEPOP_API_KEY", "")
    if not api_key:
        print("Missing environment variable 'EYEPOP_API_KEY'")
        print("Set it before running this sample.")
        return

    pop = Pop(components=[InferenceComponent(ability="eyepop.vehicle:latest")])

    image_path = os.environ.get("EYEPOP_IMAGE_PATH")

    with EyePopSdk.workerEndpoint(api_key=api_key) as endpoint:
        endpoint.set_pop(pop)
        if image_path:
            job = endpoint.upload(Path(image_path))
        else:
            job = endpoint.load_from("https://eyepop.ai/assets/examples/example_photo.jpg")
        while result := job.predict():
            print(json.dumps(result, indent=2))


# [END eyepop_vehicle_detection]


# [START eyepop_device_detection]
def sample_device_detection():
    """Detect people and electronic devices using eyepop.device:latest."""
    import json
    import os
    from pathlib import Path

    from eyepop import EyePopSdk
    from eyepop.worker.worker_types import InferenceComponent, Pop

    api_key = os.environ.get("EYEPOP_API_KEY", "")
    if not api_key:
        print("Missing environment variable 'EYEPOP_API_KEY'")
        print("Set it before running this sample.")
        return

    pop = Pop(components=[InferenceComponent(ability="eyepop.device:latest")])

    image_path = os.environ.get("EYEPOP_IMAGE_PATH")

    with EyePopSdk.workerEndpoint(api_key=api_key) as endpoint:
        endpoint.set_pop(pop)
        if image_path:
            job = endpoint.upload(Path(image_path))
        else:
            job = endpoint.load_from("https://eyepop.ai/assets/examples/example_photo.jpg")
        while result := job.predict():
            print(json.dumps(result, indent=2))


# [END eyepop_device_detection]


# [START eyepop_sports_detection]
def sample_sports_detection():
    """Detect people with sports equipment and activities using eyepop.sports:latest."""
    import json
    import os
    from pathlib import Path

    from eyepop import EyePopSdk
    from eyepop.worker.worker_types import InferenceComponent, Pop

    api_key = os.environ.get("EYEPOP_API_KEY", "")
    if not api_key:
        print("Missing environment variable 'EYEPOP_API_KEY'")
        print("Set it before running this sample.")
        return

    pop = Pop(components=[InferenceComponent(ability="eyepop.sports:latest")])

    image_path = os.environ.get("EYEPOP_IMAGE_PATH")

    with EyePopSdk.workerEndpoint(api_key=api_key) as endpoint:
        endpoint.set_pop(pop)
        if image_path:
            job = endpoint.upload(Path(image_path))
        else:
            job = endpoint.load_from("https://eyepop.ai/assets/examples/example_photo.jpg")
        while result := job.predict():
            print(json.dumps(result, indent=2))


# [END eyepop_sports_detection]


# [START eyepop_pose_estimation]
def sample_pose_estimation():
    """Estimate human pose using eyepop.person.pose:latest."""
    import json
    import os
    from pathlib import Path

    from eyepop import EyePopSdk
    from eyepop.worker.worker_types import InferenceComponent, Pop

    api_key = os.environ.get("EYEPOP_API_KEY", "")
    if not api_key:
        print("Missing environment variable 'EYEPOP_API_KEY'")
        print("Set it before running this sample.")
        return

    pop = Pop(components=[InferenceComponent(ability="eyepop.person.pose:latest")])

    image_path = os.environ.get("EYEPOP_IMAGE_PATH")

    with EyePopSdk.workerEndpoint(api_key=api_key) as endpoint:
        endpoint.set_pop(pop)
        if image_path:
            job = endpoint.upload(Path(image_path))
        else:
            job = endpoint.load_from("https://eyepop.ai/assets/examples/example_photo.jpg")
        while result := job.predict():
            print(json.dumps(result, indent=2))


# [END eyepop_pose_estimation]


# [START eyepop_2d_body_points]
def sample_2d_body_keypoints():
    """Detect 2D body keypoints using eyepop.person.2d-body-points:latest."""
    import json
    import os
    from pathlib import Path

    from eyepop import EyePopSdk
    from eyepop.worker.worker_types import InferenceComponent, Pop

    api_key = os.environ.get("EYEPOP_API_KEY", "")
    if not api_key:
        print("Missing environment variable 'EYEPOP_API_KEY'")
        print("Set it before running this sample.")
        return

    pop = Pop(components=[InferenceComponent(ability="eyepop.person.2d-body-points:latest")])

    image_path = os.environ.get("EYEPOP_IMAGE_PATH")

    with EyePopSdk.workerEndpoint(api_key=api_key) as endpoint:
        endpoint.set_pop(pop)
        if image_path:
            job = endpoint.upload(Path(image_path))
        else:
            job = endpoint.load_from("https://eyepop.ai/assets/examples/example_photo.jpg")
        while result := job.predict():
            print(json.dumps(result, indent=2))


# [END eyepop_2d_body_points]


# [START eyepop_3d_body_points]
def sample_3d_body_pose():
    """Estimate full 3D body pose using eyepop.person.3d-body-points.full:latest.

    Also available:
    - eyepop.person.3d-body-points.heavy:latest  (high-accuracy)
    - eyepop.person.3d-body-points.lite:latest   (lightweight / fast)
    """
    import json
    import os
    from pathlib import Path

    from eyepop import EyePopSdk
    from eyepop.worker.worker_types import InferenceComponent, Pop

    api_key = os.environ.get("EYEPOP_API_KEY", "")
    if not api_key:
        print("Missing environment variable 'EYEPOP_API_KEY'")
        print("Set it before running this sample.")
        return

    pop = Pop(components=[InferenceComponent(ability="eyepop.person.3d-body-points.full:latest")])

    image_path = os.environ.get("EYEPOP_IMAGE_PATH")

    with EyePopSdk.workerEndpoint(api_key=api_key) as endpoint:
        endpoint.set_pop(pop)
        if image_path:
            job = endpoint.upload(Path(image_path))
        else:
            job = endpoint.load_from("https://eyepop.ai/assets/examples/example_photo.jpg")
        while result := job.predict():
            print(json.dumps(result, indent=2))


# [END eyepop_3d_body_points]


# [START eyepop_3d_hand_points]
def sample_3d_hand_keypoints():
    """Detect 3D hand keypoints using eyepop.person.3d-hand-points:latest."""
    import json
    import os
    from pathlib import Path

    from eyepop import EyePopSdk
    from eyepop.worker.worker_types import InferenceComponent, Pop

    api_key = os.environ.get("EYEPOP_API_KEY", "")
    if not api_key:
        print("Missing environment variable 'EYEPOP_API_KEY'")
        print("Set it before running this sample.")
        return

    pop = Pop(components=[InferenceComponent(ability="eyepop.person.3d-hand-points:latest")])

    image_path = os.environ.get("EYEPOP_IMAGE_PATH")

    with EyePopSdk.workerEndpoint(api_key=api_key) as endpoint:
        endpoint.set_pop(pop)
        if image_path:
            job = endpoint.upload(Path(image_path))
        else:
            job = endpoint.load_from("https://eyepop.ai/assets/examples/example_photo.jpg")
        while result := job.predict():
            print(json.dumps(result, indent=2))


# [END eyepop_3d_hand_points]


if __name__ == "__main__":
    print("=== Person Detection (eyepop.person:latest) ===")
    sample_person_detection()

    print("\n=== Common Objects Detection (eyepop.common-objects:latest) ===")
    sample_common_objects_detection()

    print("\n=== Animal Detection (eyepop.animal:latest) ===")
    sample_animal_detection()

    print("\n=== Vehicle Detection (eyepop.vehicle:latest) ===")
    sample_vehicle_detection()

    print("\n=== Device Detection (eyepop.device:latest) ===")
    sample_device_detection()

    print("\n=== Sports Detection (eyepop.sports:latest) ===")
    sample_sports_detection()

    print("\n=== Human Pose Estimation (eyepop.person.pose:latest) ===")
    sample_pose_estimation()

    print("\n=== 2D Body Keypoints (eyepop.person.2d-body-points:latest) ===")
    sample_2d_body_keypoints()

    print("\n=== 3D Body Pose (eyepop.person.3d-body-points.full:latest) ===")
    sample_3d_body_pose()

    print("\n=== 3D Hand Keypoints (eyepop.person.3d-hand-points:latest) ===")
    sample_3d_hand_keypoints()
