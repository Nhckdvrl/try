"""Work around fvcrc14's broken physical GPU 1 during vLLM's warning-only scan.

Loaded only when the G31 runner explicitly adds this directory to PYTHONPATH.
GPU 1 is never placed in CUDA_VISIBLE_DEVICES for G31. Calls outside vLLM's
log_warnings remain unmodified and still fail rather than silently remapping.
"""

import inspect
import os

if os.environ.get("G31_FVCRC14_NVML_WORKAROUND") == "1":
    from vllm.third_party import pynvml

    _original = pynvml.nvmlDeviceGetHandleByIndex

    def _safe_handle(index):
        if index == 1 and any(frame.function == "log_warnings" for frame in inspect.stack()):
            return _original(0)
        return _original(index)

    pynvml.nvmlDeviceGetHandleByIndex = _safe_handle
