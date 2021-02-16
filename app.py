#!/usr/bin/env python3

from aws_cdk import core

from ge_tutorials_infrastructure.ge_tutorials_infrastructure_stack import GeTutorialsInfrastructureStack


app = core.App()
GeTutorialsInfrastructureStack(app, "ge-tutorials-infrastructure")

app.synth()
