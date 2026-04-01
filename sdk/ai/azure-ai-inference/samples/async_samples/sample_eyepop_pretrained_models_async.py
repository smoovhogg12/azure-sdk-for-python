# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""
DESCRIPTION:
    This sample demonstrates how to use EyePop pretrained models for computer
    vision inference using the asynchronous client. EyePop provides a variety
    of pretrained models in its registry that can be used for detecting people,
    animals, vehicles, and more.

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
    python sample_eyepop_pretrained_models_async.py

    Set these environment variables before running the sample:
    1) EYEPOP_API_KEY - Your EyePop API key. Keep it secret.
    2) EYEPOP_IMAGE_PATH - Optional. Path to a local image file to analyze.
       Defaults to using a sample URL if not provided.
"""


# [START eyepop_person_detection_async]
async def sample_person_detection_async():
    """Detect people in an image using the eyepop.person:latest model (async)."""
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

    async with EyePopSdk.workerEndpoint(api_key=api_key, is_async=True) as endpoint:
        await endpoint.set_pop(pop)
        if image_path:
            job = await endpoint.upload(Path(image_path))
        else:
            job = await endpoint.load_from("https://eyepop.ai/assets/examples/example_photo.jpg")
        while result := await job.predict():
            print(json.dumps(result, indent=2))


# [END eyepop_person_detection_async]


# [START eyepop_common_objects_detection_async]
async def sample_common_objects_detection_async():
    """Detect people and common everyday objects using eyepop.common-objects:latest (async)."""
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

    async with EyePopSdk.workerEndpoint(api_key=api_key, is_async=True) as endpoint:
        await endpoint.set_pop(pop)
        if image_path:
            job = await endpoint.upload(Path(image_path))
        else:
            job = await endpoint.load_from("https://eyepop.ai/assets/examples/example_photo.jpg")
        while result := await job.predict():
            print(json.dumps(result, indent=2))


# [END eyepop_common_objects_detection_async]


# [START eyepop_animal_detection_async]
async def sample_animal_detection_async():
    """Detect people and animals using eyepop.animal:latest (async)."""
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

    async with EyePopSdk.workerEndpoint(api_key=api_key, is_async=True) as endpoint:
        await endpoint.set_pop(pop)
        if image_path:
            job = await endpoint.upload(Path(image_path))
        else:
            job = await endpoint.load_from("https://eyepop.ai/assets/examples/example_photo.jpg")
        while result := await job.predict():
            print(json.dumps(result, indent=2))


# [END eyepop_animal_detection_async]


# [START eyepop_vehicle_detection_async]
async def sample_vehicle_detection_async():
    """Detect people and vehicles using eyepop.vehicle:latest (async)."""
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

    async with EyePopSdk.workerEndpoint(api_key=api_key, is_async=True) as endpoint:
        await endpoint.set_pop(pop)
        if image_path:
            job = await endpoint.upload(Path(image_path))
        else:
            job = await endpoint.load_from("https://eyepop.ai/assets/examples/example_photo.jpg")
        while result := await job.predict():
            print(json.dumps(result, indent=2))


# [END eyepop_vehicle_detection_async]


# [START eyepop_device_detection_async]
async def sample_device_detection_async():
    """Detect people and electronic devices using eyepop.device:latest (async)."""
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

    async with EyePopSdk.workerEndpoint(api_key=api_key, is_async=True) as endpoint:
        await endpoint.set_pop(pop)
        if image_path:
            job = await endpoint.upload(Path(image_path))
        else:
            job = await endpoint.load_from("https://eyepop.ai/assets/examples/example_photo.jpg")
        while result := await job.predict():
            print(json.dumps(result, indent=2))


# [END eyepop_device_detection_async]


# [START eyepop_sports_detection_async]
async def sample_sports_detection_async():
    """Detect people with sports equipment and activities using eyepop.sports:latest (async)."""
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

    async with EyePopSdk.workerEndpoint(api_key=api_key, is_async=True) as endpoint:
        await endpoint.set_pop(pop)
        if image_path:
            job = await endpoint.upload(Path(image_path))
        else:
            job = await endpoint.load_from("https://eyepop.ai/assets/examples/example_photo.jpg")
        while result := await job.predict():
            print(json.dumps(result, indent=2))


# [END eyepop_sports_detection_async]


# [START eyepop_pose_estimation_async]
async def sample_pose_estimation_async():
    """Estimate human pose using eyepop.person.pose:latest (async)."""
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

    async with EyePopSdk.workerEndpoint(api_key=api_key, is_async=True) as endpoint:
        await endpoint.set_pop(pop)
        if image_path:
            job = await endpoint.upload(Path(image_path))
        else:
            job = await endpoint.load_from("https://eyepop.ai/assets/examples/example_photo.jpg")
        while result := await job.predict():
            print(json.dumps(result, indent=2))


# [END eyepop_pose_estimation_async]


# [START eyepop_2d_body_points_async]
async def sample_2d_body_keypoints_async():
    """Detect 2D body keypoints using eyepop.person.2d-body-points:latest (async)."""
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

    async with EyePopSdk.workerEndpoint(api_key=api_key, is_async=True) as endpoint:
        await endpoint.set_pop(pop)
        if image_path:
            job = await endpoint.upload(Path(image_path))
        else:
            job = await endpoint.load_from("https://eyepop.ai/assets/examples/example_photo.jpg")
        while result := await job.predict():
            print(json.dumps(result, indent=2))


# [END eyepop_2d_body_points_async]


# [START eyepop_3d_body_points_async]
async def sample_3d_body_pose_async():
    """Estimate full 3D body pose using eyepop.person.3d-body-points.full:latest (async).

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

    async with EyePopSdk.workerEndpoint(api_key=api_key, is_async=True) as endpoint:
        await endpoint.set_pop(pop)
        if image_path:
            job = await endpoint.upload(Path(image_path))
        else:
            job = await endpoint.load_from("https://eyepop.ai/assets/examples/example_photo.jpg")
        while result := await job.predict():
            print(json.dumps(result, indent=2))


# [END eyepop_3d_body_points_async]


# [START eyepop_3d_hand_points_async]
async def sample_3d_hand_keypoints_async():
    """Detect 3D hand keypoints using eyepop.person.3d-hand-points:latest (async)."""
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

    async with EyePopSdk.workerEndpoint(api_key=api_key, is_async=True) as endpoint:
        await endpoint.set_pop(pop)
        if image_path:
            job = await endpoint.upload(Path(image_path))
        else:
            job = await endpoint.load_from("https://eyepop.ai/assets/examples/example_photo.jpg")
        while result := await job.predict():
            print(json.dumps(result, indent=2))


# [END eyepop_3d_hand_points_async]


async def main():
    print("=== Person Detection (eyepop.person:latest) ===")
    await sample_person_detection_async()

    print("\n=== Common Objects Detection (eyepop.common-objects:latest) ===")
    await sample_common_objects_detection_async()

    print("\n=== Animal Detection (eyepop.animal:latest) ===")
    await sample_animal_detection_async()

    print("\n=== Vehicle Detection (eyepop.vehicle:latest) ===")
    await sample_vehicle_detection_async()

    print("\n=== Device Detection (eyepop.device:latest) ===")
    await sample_device_detection_async()

    print("\n=== Sports Detection (eyepop.sports:latest) ===")
    await sample_sports_detection_async()

    print("\n=== Human Pose Estimation (eyepop.person.pose:latest) ===")
    await sample_pose_estimation_async()

    print("\n=== 2D Body Keypoints (eyepop.person.2d-body-points:latest) ===")
    await sample_2d_body_keypoints_async()

    print("\n=== 3D Body Pose (eyepop.person.3d-body-points.full:latest) ===")
    await sample_3d_body_pose_async()

    print("\n=== 3D Hand Keypoints (eyepop.person.3d-hand-points:latest) ===")
    await sample_3d_hand_keypoints_async()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
