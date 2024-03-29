# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from bilibiliq.internal.pb.bilibili.dynamic.common import (
    dynamic_pb2 as bilibili_dot_dynamic_dot_common_dot_dynamic__pb2,
)
from bilibiliq.internal.pb.bilibili.dynamic.interfaces.feed.v1 import (
    api_pb2 as bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2,
)


class FeedStub(object):
    """ """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateInitCheck = channel.unary_unary(
            '/bilibili.main.dynamic.feed.v1.Feed/CreateInitCheck',
            request_serializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.CreateInitCheckReq.SerializeToString,
            response_deserializer=bilibili_dot_dynamic_dot_common_dot_dynamic__pb2.CreateCheckResp.FromString,
        )
        self.SubmitCheck = channel.unary_unary(
            '/bilibili.main.dynamic.feed.v1.Feed/SubmitCheck',
            request_serializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.SubmitCheckReq.SerializeToString,
            response_deserializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.SubmitCheckRsp.FromString,
        )
        self.CreateDyn = channel.unary_unary(
            '/bilibili.main.dynamic.feed.v1.Feed/CreateDyn',
            request_serializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.CreateDynReq.SerializeToString,
            response_deserializer=bilibili_dot_dynamic_dot_common_dot_dynamic__pb2.CreateResp.FromString,
        )
        self.GetUidByName = channel.unary_unary(
            '/bilibili.main.dynamic.feed.v1.Feed/GetUidByName',
            request_serializer=bilibili_dot_dynamic_dot_common_dot_dynamic__pb2.GetUidByNameReq.SerializeToString,
            response_deserializer=bilibili_dot_dynamic_dot_common_dot_dynamic__pb2.GetUidByNameRsp.FromString,
        )
        self.AtList = channel.unary_unary(
            '/bilibili.main.dynamic.feed.v1.Feed/AtList',
            request_serializer=bilibili_dot_dynamic_dot_common_dot_dynamic__pb2.AtListReq.SerializeToString,
            response_deserializer=bilibili_dot_dynamic_dot_common_dot_dynamic__pb2.AtListRsp.FromString,
        )
        self.AtSearch = channel.unary_unary(
            '/bilibili.main.dynamic.feed.v1.Feed/AtSearch',
            request_serializer=bilibili_dot_dynamic_dot_common_dot_dynamic__pb2.AtSearchReq.SerializeToString,
            response_deserializer=bilibili_dot_dynamic_dot_common_dot_dynamic__pb2.AtListRsp.FromString,
        )
        self.ReserveButtonClick = channel.unary_unary(
            '/bilibili.main.dynamic.feed.v1.Feed/ReserveButtonClick',
            request_serializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.ReserveButtonClickReq.SerializeToString,
            response_deserializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.ReserveButtonClickResp.FromString,
        )
        self.CreatePlusButtonClick = channel.unary_unary(
            '/bilibili.main.dynamic.feed.v1.Feed/CreatePlusButtonClick',
            request_serializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.CreatePlusButtonClickReq.SerializeToString,
            response_deserializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.CreatePlusButtonClickRsp.FromString,
        )
        self.HotSearch = channel.unary_unary(
            '/bilibili.main.dynamic.feed.v1.Feed/HotSearch',
            request_serializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.HotSearchReq.SerializeToString,
            response_deserializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.HotSearchRsp.FromString,
        )
        self.Suggest = channel.unary_unary(
            '/bilibili.main.dynamic.feed.v1.Feed/Suggest',
            request_serializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.SuggestReq.SerializeToString,
            response_deserializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.SuggestRsp.FromString,
        )
        self.DynamicButtonClick = channel.unary_unary(
            '/bilibili.main.dynamic.feed.v1.Feed/DynamicButtonClick',
            request_serializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.DynamicButtonClickReq.SerializeToString,
            response_deserializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.DynamicButtonClickRsp.FromString,
        )
        self.CreatePermissionButtonClick = channel.unary_unary(
            '/bilibili.main.dynamic.feed.v1.Feed/CreatePermissionButtonClick',
            request_serializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.CreatePermissionButtonClickReq.SerializeToString,
            response_deserializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.CreatePermissionButtonClickRsp.FromString,
        )
        self.CreatePageInfos = channel.unary_unary(
            '/bilibili.main.dynamic.feed.v1.Feed/CreatePageInfos',
            request_serializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.CreatePageInfosReq.SerializeToString,
            response_deserializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.CreatePageInfosRsp.FromString,
        )


class FeedServicer(object):
    """ """

    def CreateInitCheck(self, request, context):
        """发布页预校验"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubmitCheck(self, request, context):
        """ """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateDyn(self, request, context):
        """创建动态"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUidByName(self, request, context):
        """根据name取uid"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AtList(self, request, context):
        """at用户推荐列表"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AtSearch(self, request, context):
        """at用户搜索列表"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReserveButtonClick(self, request, context):
        """ """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreatePlusButtonClick(self, request, context):
        """ """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HotSearch(self, request, context):
        """ """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Suggest(self, request, context):
        """ """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DynamicButtonClick(self, request, context):
        """ """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreatePermissionButtonClick(self, request, context):
        """ """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreatePageInfos(self, request, context):
        """ """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FeedServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'CreateInitCheck': grpc.unary_unary_rpc_method_handler(
            servicer.CreateInitCheck,
            request_deserializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.CreateInitCheckReq.FromString,
            response_serializer=bilibili_dot_dynamic_dot_common_dot_dynamic__pb2.CreateCheckResp.SerializeToString,
        ),
        'SubmitCheck': grpc.unary_unary_rpc_method_handler(
            servicer.SubmitCheck,
            request_deserializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.SubmitCheckReq.FromString,
            response_serializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.SubmitCheckRsp.SerializeToString,
        ),
        'CreateDyn': grpc.unary_unary_rpc_method_handler(
            servicer.CreateDyn,
            request_deserializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.CreateDynReq.FromString,
            response_serializer=bilibili_dot_dynamic_dot_common_dot_dynamic__pb2.CreateResp.SerializeToString,
        ),
        'GetUidByName': grpc.unary_unary_rpc_method_handler(
            servicer.GetUidByName,
            request_deserializer=bilibili_dot_dynamic_dot_common_dot_dynamic__pb2.GetUidByNameReq.FromString,
            response_serializer=bilibili_dot_dynamic_dot_common_dot_dynamic__pb2.GetUidByNameRsp.SerializeToString,
        ),
        'AtList': grpc.unary_unary_rpc_method_handler(
            servicer.AtList,
            request_deserializer=bilibili_dot_dynamic_dot_common_dot_dynamic__pb2.AtListReq.FromString,
            response_serializer=bilibili_dot_dynamic_dot_common_dot_dynamic__pb2.AtListRsp.SerializeToString,
        ),
        'AtSearch': grpc.unary_unary_rpc_method_handler(
            servicer.AtSearch,
            request_deserializer=bilibili_dot_dynamic_dot_common_dot_dynamic__pb2.AtSearchReq.FromString,
            response_serializer=bilibili_dot_dynamic_dot_common_dot_dynamic__pb2.AtListRsp.SerializeToString,
        ),
        'ReserveButtonClick': grpc.unary_unary_rpc_method_handler(
            servicer.ReserveButtonClick,
            request_deserializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.ReserveButtonClickReq.FromString,
            response_serializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.ReserveButtonClickResp.SerializeToString,
        ),
        'CreatePlusButtonClick': grpc.unary_unary_rpc_method_handler(
            servicer.CreatePlusButtonClick,
            request_deserializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.CreatePlusButtonClickReq.FromString,
            response_serializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.CreatePlusButtonClickRsp.SerializeToString,
        ),
        'HotSearch': grpc.unary_unary_rpc_method_handler(
            servicer.HotSearch,
            request_deserializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.HotSearchReq.FromString,
            response_serializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.HotSearchRsp.SerializeToString,
        ),
        'Suggest': grpc.unary_unary_rpc_method_handler(
            servicer.Suggest,
            request_deserializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.SuggestReq.FromString,
            response_serializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.SuggestRsp.SerializeToString,
        ),
        'DynamicButtonClick': grpc.unary_unary_rpc_method_handler(
            servicer.DynamicButtonClick,
            request_deserializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.DynamicButtonClickReq.FromString,
            response_serializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.DynamicButtonClickRsp.SerializeToString,
        ),
        'CreatePermissionButtonClick': grpc.unary_unary_rpc_method_handler(
            servicer.CreatePermissionButtonClick,
            request_deserializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.CreatePermissionButtonClickReq.FromString,
            response_serializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.CreatePermissionButtonClickRsp.SerializeToString,
        ),
        'CreatePageInfos': grpc.unary_unary_rpc_method_handler(
            servicer.CreatePageInfos,
            request_deserializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.CreatePageInfosReq.FromString,
            response_serializer=bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.CreatePageInfosRsp.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'bilibili.main.dynamic.feed.v1.Feed', rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Feed(object):
    """ """

    @staticmethod
    def CreateInitCheck(
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
            '/bilibili.main.dynamic.feed.v1.Feed/CreateInitCheck',
            bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.CreateInitCheckReq.SerializeToString,
            bilibili_dot_dynamic_dot_common_dot_dynamic__pb2.CreateCheckResp.FromString,
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
    def SubmitCheck(
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
            '/bilibili.main.dynamic.feed.v1.Feed/SubmitCheck',
            bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.SubmitCheckReq.SerializeToString,
            bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.SubmitCheckRsp.FromString,
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
    def CreateDyn(
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
            '/bilibili.main.dynamic.feed.v1.Feed/CreateDyn',
            bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.CreateDynReq.SerializeToString,
            bilibili_dot_dynamic_dot_common_dot_dynamic__pb2.CreateResp.FromString,
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
    def GetUidByName(
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
            '/bilibili.main.dynamic.feed.v1.Feed/GetUidByName',
            bilibili_dot_dynamic_dot_common_dot_dynamic__pb2.GetUidByNameReq.SerializeToString,
            bilibili_dot_dynamic_dot_common_dot_dynamic__pb2.GetUidByNameRsp.FromString,
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
    def AtList(
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
            '/bilibili.main.dynamic.feed.v1.Feed/AtList',
            bilibili_dot_dynamic_dot_common_dot_dynamic__pb2.AtListReq.SerializeToString,
            bilibili_dot_dynamic_dot_common_dot_dynamic__pb2.AtListRsp.FromString,
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
    def AtSearch(
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
            '/bilibili.main.dynamic.feed.v1.Feed/AtSearch',
            bilibili_dot_dynamic_dot_common_dot_dynamic__pb2.AtSearchReq.SerializeToString,
            bilibili_dot_dynamic_dot_common_dot_dynamic__pb2.AtListRsp.FromString,
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
    def ReserveButtonClick(
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
            '/bilibili.main.dynamic.feed.v1.Feed/ReserveButtonClick',
            bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.ReserveButtonClickReq.SerializeToString,
            bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.ReserveButtonClickResp.FromString,
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
    def CreatePlusButtonClick(
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
            '/bilibili.main.dynamic.feed.v1.Feed/CreatePlusButtonClick',
            bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.CreatePlusButtonClickReq.SerializeToString,
            bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.CreatePlusButtonClickRsp.FromString,
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
    def HotSearch(
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
            '/bilibili.main.dynamic.feed.v1.Feed/HotSearch',
            bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.HotSearchReq.SerializeToString,
            bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.HotSearchRsp.FromString,
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
    def Suggest(
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
            '/bilibili.main.dynamic.feed.v1.Feed/Suggest',
            bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.SuggestReq.SerializeToString,
            bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.SuggestRsp.FromString,
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
    def DynamicButtonClick(
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
            '/bilibili.main.dynamic.feed.v1.Feed/DynamicButtonClick',
            bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.DynamicButtonClickReq.SerializeToString,
            bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.DynamicButtonClickRsp.FromString,
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
    def CreatePermissionButtonClick(
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
            '/bilibili.main.dynamic.feed.v1.Feed/CreatePermissionButtonClick',
            bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.CreatePermissionButtonClickReq.SerializeToString,
            bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.CreatePermissionButtonClickRsp.FromString,
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
    def CreatePageInfos(
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
            '/bilibili.main.dynamic.feed.v1.Feed/CreatePageInfos',
            bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.CreatePageInfosReq.SerializeToString,
            bilibili_dot_dynamic_dot_interfaces_dot_feed_dot_v1_dot_api__pb2.CreatePageInfosRsp.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
