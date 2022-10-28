# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from bilibiliq.internal.pb.bilibili.app.interfaces.v1 import (
    media_pb2 as bilibili_dot_app_dot_interfaces_dot_v1_dot_media__pb2,
)


class MediaStub(object):
    """ """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MediaTab = channel.unary_unary(
            '/bilibili.app.interface.v1.Media/MediaTab',
            request_serializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_media__pb2.MediaTabReq.SerializeToString,
            response_deserializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_media__pb2.MediaTabReply.FromString,
        )
        self.MediaDetail = channel.unary_unary(
            '/bilibili.app.interface.v1.Media/MediaDetail',
            request_serializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_media__pb2.MediaDetailReq.SerializeToString,
            response_deserializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_media__pb2.MediaDetailReply.FromString,
        )
        self.MediaVideo = channel.unary_unary(
            '/bilibili.app.interface.v1.Media/MediaVideo',
            request_serializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_media__pb2.MediaVideoReq.SerializeToString,
            response_deserializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_media__pb2.MediaVideoReply.FromString,
        )
        self.MediaRelation = channel.unary_unary(
            '/bilibili.app.interface.v1.Media/MediaRelation',
            request_serializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_media__pb2.MediaRelationReq.SerializeToString,
            response_deserializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_media__pb2.MediaRelationReply.FromString,
        )
        self.MediaFollow = channel.unary_unary(
            '/bilibili.app.interface.v1.Media/MediaFollow',
            request_serializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_media__pb2.MediaFollowReq.SerializeToString,
            response_deserializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_media__pb2.MediaFollowReply.FromString,
        )


class MediaServicer(object):
    """ """

    def MediaTab(self, request, context):
        """ """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MediaDetail(self, request, context):
        """ """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MediaVideo(self, request, context):
        """ """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MediaRelation(self, request, context):
        """ """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MediaFollow(self, request, context):
        """ """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MediaServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'MediaTab': grpc.unary_unary_rpc_method_handler(
            servicer.MediaTab,
            request_deserializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_media__pb2.MediaTabReq.FromString,
            response_serializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_media__pb2.MediaTabReply.SerializeToString,
        ),
        'MediaDetail': grpc.unary_unary_rpc_method_handler(
            servicer.MediaDetail,
            request_deserializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_media__pb2.MediaDetailReq.FromString,
            response_serializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_media__pb2.MediaDetailReply.SerializeToString,
        ),
        'MediaVideo': grpc.unary_unary_rpc_method_handler(
            servicer.MediaVideo,
            request_deserializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_media__pb2.MediaVideoReq.FromString,
            response_serializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_media__pb2.MediaVideoReply.SerializeToString,
        ),
        'MediaRelation': grpc.unary_unary_rpc_method_handler(
            servicer.MediaRelation,
            request_deserializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_media__pb2.MediaRelationReq.FromString,
            response_serializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_media__pb2.MediaRelationReply.SerializeToString,
        ),
        'MediaFollow': grpc.unary_unary_rpc_method_handler(
            servicer.MediaFollow,
            request_deserializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_media__pb2.MediaFollowReq.FromString,
            response_serializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_media__pb2.MediaFollowReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'bilibili.app.interface.v1.Media', rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Media(object):
    """ """

    @staticmethod
    def MediaTab(
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
            '/bilibili.app.interface.v1.Media/MediaTab',
            bilibili_dot_app_dot_interfaces_dot_v1_dot_media__pb2.MediaTabReq.SerializeToString,
            bilibili_dot_app_dot_interfaces_dot_v1_dot_media__pb2.MediaTabReply.FromString,
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
    def MediaDetail(
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
            '/bilibili.app.interface.v1.Media/MediaDetail',
            bilibili_dot_app_dot_interfaces_dot_v1_dot_media__pb2.MediaDetailReq.SerializeToString,
            bilibili_dot_app_dot_interfaces_dot_v1_dot_media__pb2.MediaDetailReply.FromString,
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
    def MediaVideo(
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
            '/bilibili.app.interface.v1.Media/MediaVideo',
            bilibili_dot_app_dot_interfaces_dot_v1_dot_media__pb2.MediaVideoReq.SerializeToString,
            bilibili_dot_app_dot_interfaces_dot_v1_dot_media__pb2.MediaVideoReply.FromString,
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
    def MediaRelation(
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
            '/bilibili.app.interface.v1.Media/MediaRelation',
            bilibili_dot_app_dot_interfaces_dot_v1_dot_media__pb2.MediaRelationReq.SerializeToString,
            bilibili_dot_app_dot_interfaces_dot_v1_dot_media__pb2.MediaRelationReply.FromString,
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
    def MediaFollow(
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
            '/bilibili.app.interface.v1.Media/MediaFollow',
            bilibili_dot_app_dot_interfaces_dot_v1_dot_media__pb2.MediaFollowReq.SerializeToString,
            bilibili_dot_app_dot_interfaces_dot_v1_dot_media__pb2.MediaFollowReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )