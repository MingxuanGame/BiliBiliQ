# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from bilibiliq.internal.pb.bilibili.pgc.gateway.player.v2 import (
    playurl_pb2 as bilibili_dot_pgc_dot_gateway_dot_player_dot_v2_dot_playurl__pb2,
)


class PlayURLStub(object):
    """视频url"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PlayView = channel.unary_unary(
            '/bilibili.pgc.gateway.player.v2.PlayURL/PlayView',
            request_serializer=bilibili_dot_pgc_dot_gateway_dot_player_dot_v2_dot_playurl__pb2.PlayViewReq.SerializeToString,
            response_deserializer=bilibili_dot_pgc_dot_gateway_dot_player_dot_v2_dot_playurl__pb2.PlayViewReply.FromString,
        )
        self.PlayViewComic = channel.unary_unary(
            '/bilibili.pgc.gateway.player.v2.PlayURL/PlayViewComic',
            request_serializer=bilibili_dot_pgc_dot_gateway_dot_player_dot_v2_dot_playurl__pb2.PlayViewReq.SerializeToString,
            response_deserializer=bilibili_dot_pgc_dot_gateway_dot_player_dot_v2_dot_playurl__pb2.PlayViewReply.FromString,
        )


class PlayURLServicer(object):
    """视频url"""

    def PlayView(self, request, context):
        """播放页信息"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PlayViewComic(self, request, context):
        """ """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PlayURLServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'PlayView': grpc.unary_unary_rpc_method_handler(
            servicer.PlayView,
            request_deserializer=bilibili_dot_pgc_dot_gateway_dot_player_dot_v2_dot_playurl__pb2.PlayViewReq.FromString,
            response_serializer=bilibili_dot_pgc_dot_gateway_dot_player_dot_v2_dot_playurl__pb2.PlayViewReply.SerializeToString,
        ),
        'PlayViewComic': grpc.unary_unary_rpc_method_handler(
            servicer.PlayViewComic,
            request_deserializer=bilibili_dot_pgc_dot_gateway_dot_player_dot_v2_dot_playurl__pb2.PlayViewReq.FromString,
            response_serializer=bilibili_dot_pgc_dot_gateway_dot_player_dot_v2_dot_playurl__pb2.PlayViewReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'bilibili.pgc.gateway.player.v2.PlayURL', rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class PlayURL(object):
    """视频url"""

    @staticmethod
    def PlayView(
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
            '/bilibili.pgc.gateway.player.v2.PlayURL/PlayView',
            bilibili_dot_pgc_dot_gateway_dot_player_dot_v2_dot_playurl__pb2.PlayViewReq.SerializeToString,
            bilibili_dot_pgc_dot_gateway_dot_player_dot_v2_dot_playurl__pb2.PlayViewReply.FromString,
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
    def PlayViewComic(
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
            '/bilibili.pgc.gateway.player.v2.PlayURL/PlayViewComic',
            bilibili_dot_pgc_dot_gateway_dot_player_dot_v2_dot_playurl__pb2.PlayViewReq.SerializeToString,
            bilibili_dot_pgc_dot_gateway_dot_player_dot_v2_dot_playurl__pb2.PlayViewReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
