#!/usr/bin/env python3
import os
import aws_cdk as cdk
from ezapp3.ezapp3_stack import Ezapp3Stack

app = cdk.App()
Ezapp3Stack(app, "Ezapp3Stack")

app.synth()
