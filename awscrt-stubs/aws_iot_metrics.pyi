"""
Type annotations for awscrt.aws_iot_metrics module.

Copyright 2026 Vlad Emelianov
"""

from dataclasses import dataclass

IOT_SDK_METRICS_FEATURE_VERSION: int = ...

@dataclass
class IoTMetricsMetadata:
    key: str
    value: str

@dataclass
class AWSIoTMetrics:
    library_name: str = ...
    metadata_entries: list[IoTMetricsMetadata] | None = ...
