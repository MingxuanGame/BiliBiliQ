# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from bilibiliq.internal.pb.bilibili.app.interfaces.v1 import (
    search_pb2 as bilibili_dot_app_dot_interfaces_dot_v1_dot_search__pb2,
)


class SearchStub(object):
    """搜索"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Suggest3 = channel.unary_unary(
            '/bilibili.app.interface.v1.Search/Suggest3',
            request_serializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_search__pb2.SuggestionResult3Req.SerializeToString,
            response_deserializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_search__pb2.SuggestionResult3Reply.FromString,
        )
        self.DefaultWords = channel.unary_unary(
            '/bilibili.app.interface.v1.Search/DefaultWords',
            request_serializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_search__pb2.DefaultWordsReq.SerializeToString,
            response_deserializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_search__pb2.DefaultWordsReply.FromString,
        )


class SearchServicer(object):
    """搜索"""

    def Suggest3(self, request, context):
        """获取搜索建议"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DefaultWords(self, request, context):
        """ """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SearchServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Suggest3': grpc.unary_unary_rpc_method_handler(
            servicer.Suggest3,
            request_deserializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_search__pb2.SuggestionResult3Req.FromString,
            response_serializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_search__pb2.SuggestionResult3Reply.SerializeToString,
        ),
        'DefaultWords': grpc.unary_unary_rpc_method_handler(
            servicer.DefaultWords,
            request_deserializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_search__pb2.DefaultWordsReq.FromString,
            response_serializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_search__pb2.DefaultWordsReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'bilibili.app.interface.v1.Search', rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Search(object):
    """搜索"""

    @staticmethod
    def Suggest3(
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
            '/bilibili.app.interface.v1.Search/Suggest3',
            bilibili_dot_app_dot_interfaces_dot_v1_dot_search__pb2.SuggestionResult3Req.SerializeToString,
            bilibili_dot_app_dot_interfaces_dot_v1_dot_search__pb2.SuggestionResult3Reply.FromString,
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
    def DefaultWords(
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
            '/bilibili.app.interface.v1.Search/DefaultWords',
            bilibili_dot_app_dot_interfaces_dot_v1_dot_search__pb2.DefaultWordsReq.SerializeToString,
            bilibili_dot_app_dot_interfaces_dot_v1_dot_search__pb2.DefaultWordsReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )


class SearchTestStub(object):
    """ """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.NotExist = channel.unary_unary(
            '/bilibili.app.interface.v1.SearchTest/NotExist',
            request_serializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_search__pb2.SuggestionResult3Req.SerializeToString,
            response_deserializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_search__pb2.SuggestionResult3Reply.FromString,
        )


class SearchTestServicer(object):
    """ """

    def NotExist(self, request, context):
        """ """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SearchTestServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'NotExist': grpc.unary_unary_rpc_method_handler(
            servicer.NotExist,
            request_deserializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_search__pb2.SuggestionResult3Req.FromString,
            response_serializer=bilibili_dot_app_dot_interfaces_dot_v1_dot_search__pb2.SuggestionResult3Reply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'bilibili.app.interface.v1.SearchTest', rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class SearchTest(object):
    """ """

    @staticmethod
    def NotExist(
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
            '/bilibili.app.interface.v1.SearchTest/NotExist',
            bilibili_dot_app_dot_interfaces_dot_v1_dot_search__pb2.SuggestionResult3Req.SerializeToString,
            bilibili_dot_app_dot_interfaces_dot_v1_dot_search__pb2.SuggestionResult3Reply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
