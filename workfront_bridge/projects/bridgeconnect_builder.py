from .display_builder import DisplayProjectBuilder
from .bridge_connect import WFProjectBridgeConnectContainer


class BridgeConnectProjectBuilder(DisplayProjectBuilder):
    def build(self):
        return super(BridgeConnectProjectBuilder, self).build(container_class=WFProjectBridgeConnectContainer)
