# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

from bilibiliq.internal.pb.bilibili.broadcast.message.main import (
    resource_pb2 as bilibili_dot_broadcast_dot_message_dot_main_dot_resource__pb2,
)


class ResourceStub(object):
    """ """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TopActivity = channel.unary_stream(
            '/bilibili.broadcast.message.main.Resource/TopActivity',
            request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            response_deserializer=bilibili_dot_broadcast_dot_message_dot_main_dot_resource__pb2.TopActivityReply.FromString,
        )


class ResourceServicer(object):
    """ """

    def TopActivity(self, request, context):
        """ """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ResourceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'TopActivity': grpc.unary_stream_rpc_method_handler(
            servicer.TopActivity,
            request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            response_serializer=bilibili_dot_broadcast_dot_message_dot_main_dot_resource__pb2.TopActivityReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'bilibili.broadcast.message.main.Resource', rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Resource(object):
    """ """

    @staticmethod
    def TopActivity(
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
        return grpc.experimental.unary_stream(
            request,
            target,
            '/bilibili.broadcast.message.main.Resource/TopActivity',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            bilibili_dot_broadcast_dot_message_dot_main_dot_resource__pb2.TopActivityReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
