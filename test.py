"""
Test file for stubs.

Copyright 2024 Vlad Emelianov
"""

from awscrt.auth import AwsCredentialsProvider

provider = AwsCredentialsProvider("binding")
provider.new_process("str")
provider.new_process(None)
provider.new_process(123)
