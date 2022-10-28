# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

from bilibiliq.internal.pb.bilibili.broadcast.message.tv import (
    proj_pb2 as bilibili_dot_broadcast_dot_message_dot_tv_dot_proj__pb2,
)


class TvStub(object):
    """ """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Proj = channel.unary_stream(
            '/bilibili.broadcast.message.tv.Tv/Proj',
            request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            response_deserializer=bilibili_dot_broadcast_dot_message_dot_tv_dot_proj__pb2.ProjReply.FromString,
        )
        self.LiveStatus = channel.unary_stream(
            '/bilibili.broadcast.message.tv.Tv/LiveStatus',
            request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            response_deserializer=bilibili_dot_broadcast_dot_message_dot_tv_dot_proj__pb2.LiveStatusNotify.FromString,
        )
        self.Esports = channel.unary_stream(
            '/bilibili.broadcast.message.tv.Tv/Esports',
            request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            response_deserializer=bilibili_dot_broadcast_dot_message_dot_tv_dot_proj__pb2.EsportsNotify.FromString,
        )
        self.Publicity = channel.unary_stream(
            '/bilibili.broadcast.message.tv.Tv/Publicity',
            request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            response_deserializer=bilibili_dot_broadcast_dot_message_dot_tv_dot_proj__pb2.PublicityNotify.FromString,
        )
        self.LiveSkip = channel.unary_stream(
            '/bilibili.broadcast.message.tv.Tv/LiveSkip',
            request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            response_deserializer=bilibili_dot_broadcast_dot_message_dot_tv_dot_proj__pb2.LiveSkipNotify.FromString,
        )


class TvServicer(object):
    """ """

    def Proj(self, request, context):
        """投屏"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LiveStatus(self, request, context):
        """直播状态"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Esports(self, request, context):
        """赛事比分通知"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Publicity(self, request, context):
        """直播插卡"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LiveSkip(self, request, context):
        """直转点"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TvServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Proj': grpc.unary_stream_rpc_method_handler(
            servicer.Proj,
            request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            response_serializer=bilibili_dot_broadcast_dot_message_dot_tv_dot_proj__pb2.ProjReply.SerializeToString,
        ),
        'LiveStatus': grpc.unary_stream_rpc_method_handler(
            servicer.LiveStatus,
            request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            response_serializer=bilibili_dot_broadcast_dot_message_dot_tv_dot_proj__pb2.LiveStatusNotify.SerializeToString,
        ),
        'Esports': grpc.unary_stream_rpc_method_handler(
            servicer.Esports,
            request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            response_serializer=bilibili_dot_broadcast_dot_message_dot_tv_dot_proj__pb2.EsportsNotify.SerializeToString,
        ),
        'Publicity': grpc.unary_stream_rpc_method_handler(
            servicer.Publicity,
            request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            response_serializer=bilibili_dot_broadcast_dot_message_dot_tv_dot_proj__pb2.PublicityNotify.SerializeToString,
        ),
        'LiveSkip': grpc.unary_stream_rpc_method_handler(
            servicer.LiveSkip,
            request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            response_serializer=bilibili_dot_broadcast_dot_message_dot_tv_dot_proj__pb2.LiveSkipNotify.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'bilibili.broadcast.message.tv.Tv', rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Tv(object):
    """ """

    @staticmethod
    def Proj(
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
            '/bilibili.broadcast.message.tv.Tv/Proj',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            bilibili_dot_broadcast_dot_message_dot_tv_dot_proj__pb2.ProjReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def LiveStatus(
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
            '/bilibili.broadcast.message.tv.Tv/LiveStatus',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            bilibili_dot_broadcast_dot_message_dot_tv_dot_proj__pb2.LiveStatusNotify.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Esports(
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
            '/bilibili.broadcast.message.tv.Tv/Esports',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            bilibili_dot_broadcast_dot_message_dot_tv_dot_proj__pb2.EsportsNotify.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Publicity(
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
            '/bilibili.broadcast.message.tv.Tv/Publicity',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            bilibili_dot_broadcast_dot_message_dot_tv_dot_proj__pb2.PublicityNotify.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def LiveSkip(
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
            '/bilibili.broadcast.message.tv.Tv/LiveSkip',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            bilibili_dot_broadcast_dot_message_dot_tv_dot_proj__pb2.LiveSkipNotify.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
