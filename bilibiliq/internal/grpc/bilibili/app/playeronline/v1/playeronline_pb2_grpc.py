# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from bilibiliq.internal.pb.bilibili.app.playeronline.v1 import (
    playeronline_pb2 as bilibili_dot_app_dot_playeronline_dot_v1_dot_playeronline__pb2,
)


class PlayerOnlineStub(object):
    """在线人数"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PlayerOnline = channel.unary_unary(
            '/bilibili.app.playeronline.v1.PlayerOnline/PlayerOnline',
            request_serializer=bilibili_dot_app_dot_playeronline_dot_v1_dot_playeronline__pb2.PlayerOnlineReq.SerializeToString,
            response_deserializer=bilibili_dot_app_dot_playeronline_dot_v1_dot_playeronline__pb2.PlayerOnlineReply.FromString,
        )
        self.PremiereInfo = channel.unary_unary(
            '/bilibili.app.playeronline.v1.PlayerOnline/PremiereInfo',
            request_serializer=bilibili_dot_app_dot_playeronline_dot_v1_dot_playeronline__pb2.PremiereInfoReq.SerializeToString,
            response_deserializer=bilibili_dot_app_dot_playeronline_dot_v1_dot_playeronline__pb2.PremiereInfoReply.FromString,
        )
        self.ReportWatch = channel.unary_unary(
            '/bilibili.app.playeronline.v1.PlayerOnline/ReportWatch',
            request_serializer=bilibili_dot_app_dot_playeronline_dot_v1_dot_playeronline__pb2.ReportWatchReq.SerializeToString,
            response_deserializer=bilibili_dot_app_dot_playeronline_dot_v1_dot_playeronline__pb2.NoReply.FromString,
        )


class PlayerOnlineServicer(object):
    """在线人数"""

    def PlayerOnline(self, request, context):
        """获取在线人数"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PremiereInfo(self, request, context):
        """ """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReportWatch(self, request, context):
        """ """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PlayerOnlineServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'PlayerOnline': grpc.unary_unary_rpc_method_handler(
            servicer.PlayerOnline,
            request_deserializer=bilibili_dot_app_dot_playeronline_dot_v1_dot_playeronline__pb2.PlayerOnlineReq.FromString,
            response_serializer=bilibili_dot_app_dot_playeronline_dot_v1_dot_playeronline__pb2.PlayerOnlineReply.SerializeToString,
        ),
        'PremiereInfo': grpc.unary_unary_rpc_method_handler(
            servicer.PremiereInfo,
            request_deserializer=bilibili_dot_app_dot_playeronline_dot_v1_dot_playeronline__pb2.PremiereInfoReq.FromString,
            response_serializer=bilibili_dot_app_dot_playeronline_dot_v1_dot_playeronline__pb2.PremiereInfoReply.SerializeToString,
        ),
        'ReportWatch': grpc.unary_unary_rpc_method_handler(
            servicer.ReportWatch,
            request_deserializer=bilibili_dot_app_dot_playeronline_dot_v1_dot_playeronline__pb2.ReportWatchReq.FromString,
            response_serializer=bilibili_dot_app_dot_playeronline_dot_v1_dot_playeronline__pb2.NoReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'bilibili.app.playeronline.v1.PlayerOnline', rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class PlayerOnline(object):
    """在线人数"""

    @staticmethod
    def PlayerOnline(
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
            '/bilibili.app.playeronline.v1.PlayerOnline/PlayerOnline',
            bilibili_dot_app_dot_playeronline_dot_v1_dot_playeronline__pb2.PlayerOnlineReq.SerializeToString,
            bilibili_dot_app_dot_playeronline_dot_v1_dot_playeronline__pb2.PlayerOnlineReply.FromString,
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
    def PremiereInfo(
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
            '/bilibili.app.playeronline.v1.PlayerOnline/PremiereInfo',
            bilibili_dot_app_dot_playeronline_dot_v1_dot_playeronline__pb2.PremiereInfoReq.SerializeToString,
            bilibili_dot_app_dot_playeronline_dot_v1_dot_playeronline__pb2.PremiereInfoReply.FromString,
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
    def ReportWatch(
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
            '/bilibili.app.playeronline.v1.PlayerOnline/ReportWatch',
            bilibili_dot_app_dot_playeronline_dot_v1_dot_playeronline__pb2.ReportWatchReq.SerializeToString,
            bilibili_dot_app_dot_playeronline_dot_v1_dot_playeronline__pb2.NoReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
