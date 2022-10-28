# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

from bilibiliq.internal.pb.bilibili.broadcast.message.fission import (
    notify_pb2 as bilibili_dot_broadcast_dot_message_dot_fission_dot_notify__pb2,
)


class FissionStub(object):
    """ """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GameNotify = channel.unary_stream(
            '/bilibili.broadcast.message.fission.Fission/GameNotify',
            request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            response_deserializer=bilibili_dot_broadcast_dot_message_dot_fission_dot_notify__pb2.GameNotifyReply.FromString,
        )


class FissionServicer(object):
    """ """

    def GameNotify(self, request, context):
        """ """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FissionServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GameNotify': grpc.unary_stream_rpc_method_handler(
            servicer.GameNotify,
            request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            response_serializer=bilibili_dot_broadcast_dot_message_dot_fission_dot_notify__pb2.GameNotifyReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'bilibili.broadcast.message.fission.Fission', rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Fission(object):
    """ """

    @staticmethod
    def GameNotify(
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
            '/bilibili.broadcast.message.fission.Fission/GameNotify',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            bilibili_dot_broadcast_dot_message_dot_fission_dot_notify__pb2.GameNotifyReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
