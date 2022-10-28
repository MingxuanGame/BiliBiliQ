# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from bilibiliq.internal.pb.bilibili.app.show.region.v1 import (
    region_pb2 as bilibili_dot_app_dot_show_dot_region_dot_v1_dot_region__pb2,
)


class RegionStub(object):
    """ """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Region = channel.unary_unary(
            '/bilibili.app.show.region.v1.Region/Region',
            request_serializer=bilibili_dot_app_dot_show_dot_region_dot_v1_dot_region__pb2.RegionReq.SerializeToString,
            response_deserializer=bilibili_dot_app_dot_show_dot_region_dot_v1_dot_region__pb2.RegionReply.FromString,
        )


class RegionServicer(object):
    """ """

    def Region(self, request, context):
        """ """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RegionServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Region': grpc.unary_unary_rpc_method_handler(
            servicer.Region,
            request_deserializer=bilibili_dot_app_dot_show_dot_region_dot_v1_dot_region__pb2.RegionReq.FromString,
            response_serializer=bilibili_dot_app_dot_show_dot_region_dot_v1_dot_region__pb2.RegionReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'bilibili.app.show.region.v1.Region', rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Region(object):
    """ """

    @staticmethod
    def Region(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/bilibili.app.show.region.v1.Region/Region',
            bilibili_dot_app_dot_show_dot_region_dot_v1_dot_region__pb2.RegionReq.SerializeToString,
            bilibili_dot_app_dot_show_dot_region_dot_v1_dot_region__pb2.RegionReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
