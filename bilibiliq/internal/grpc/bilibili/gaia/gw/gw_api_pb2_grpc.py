# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

from bilibiliq.internal.pb.bilibili.gaia.gw import (
    gw_api_pb2 as bilibili_dot_gaia_dot_gw_dot_gw__api__pb2,
)


class GaiaStub(object):
    """应用列表上报"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ExUploadAppList = channel.unary_unary(
            '/bilibili.gaia.gw.Gaia/ExUploadAppList',
            request_serializer=bilibili_dot_gaia_dot_gw_dot_gw__api__pb2.GaiaEncryptMsgReq.SerializeToString,
            response_deserializer=bilibili_dot_gaia_dot_gw_dot_gw__api__pb2.UploadAppListReply.FromString,
        )
        self.ExFetchPublicKey = channel.unary_unary(
            '/bilibili.gaia.gw.Gaia/ExFetchPublicKey',
            request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            response_deserializer=bilibili_dot_gaia_dot_gw_dot_gw__api__pb2.FetchPublicKeyReply.FromString,
        )


class GaiaServicer(object):
    """应用列表上报"""

    def ExUploadAppList(self, request, context):
        """应用列表上报"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExFetchPublicKey(self, request, context):
        """拉取rsa公钥"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GaiaServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'ExUploadAppList': grpc.unary_unary_rpc_method_handler(
            servicer.ExUploadAppList,
            request_deserializer=bilibili_dot_gaia_dot_gw_dot_gw__api__pb2.GaiaEncryptMsgReq.FromString,
            response_serializer=bilibili_dot_gaia_dot_gw_dot_gw__api__pb2.UploadAppListReply.SerializeToString,
        ),
        'ExFetchPublicKey': grpc.unary_unary_rpc_method_handler(
            servicer.ExFetchPublicKey,
            request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            response_serializer=bilibili_dot_gaia_dot_gw_dot_gw__api__pb2.FetchPublicKeyReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'bilibili.gaia.gw.Gaia', rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Gaia(object):
    """应用列表上报"""

    @staticmethod
    def ExUploadAppList(
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
            '/bilibili.gaia.gw.Gaia/ExUploadAppList',
            bilibili_dot_gaia_dot_gw_dot_gw__api__pb2.GaiaEncryptMsgReq.SerializeToString,
            bilibili_dot_gaia_dot_gw_dot_gw__api__pb2.UploadAppListReply.FromString,
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
    def ExFetchPublicKey(
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
            '/bilibili.gaia.gw.Gaia/ExFetchPublicKey',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            bilibili_dot_gaia_dot_gw_dot_gw__api__pb2.FetchPublicKeyReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
