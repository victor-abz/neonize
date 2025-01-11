"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class QP(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _FilterResult:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _FilterResultEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[QP._FilterResult.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        TRUE: QP._FilterResult.ValueType  # 1
        FALSE: QP._FilterResult.ValueType  # 2
        UNKNOWN: QP._FilterResult.ValueType  # 3

    class FilterResult(_FilterResult, metaclass=_FilterResultEnumTypeWrapper): ...
    TRUE: QP.FilterResult.ValueType  # 1
    FALSE: QP.FilterResult.ValueType  # 2
    UNKNOWN: QP.FilterResult.ValueType  # 3

    class _FilterClientNotSupportedConfig:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _FilterClientNotSupportedConfigEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[QP._FilterClientNotSupportedConfig.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        PASS_BY_DEFAULT: QP._FilterClientNotSupportedConfig.ValueType  # 1
        FAIL_BY_DEFAULT: QP._FilterClientNotSupportedConfig.ValueType  # 2

    class FilterClientNotSupportedConfig(_FilterClientNotSupportedConfig, metaclass=_FilterClientNotSupportedConfigEnumTypeWrapper): ...
    PASS_BY_DEFAULT: QP.FilterClientNotSupportedConfig.ValueType  # 1
    FAIL_BY_DEFAULT: QP.FilterClientNotSupportedConfig.ValueType  # 2

    class _ClauseType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ClauseTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[QP._ClauseType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        AND: QP._ClauseType.ValueType  # 1
        OR: QP._ClauseType.ValueType  # 2
        NOR: QP._ClauseType.ValueType  # 3

    class ClauseType(_ClauseType, metaclass=_ClauseTypeEnumTypeWrapper): ...
    AND: QP.ClauseType.ValueType  # 1
    OR: QP.ClauseType.ValueType  # 2
    NOR: QP.ClauseType.ValueType  # 3

    @typing.final
    class FilterClause(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        CLAUSETYPE_FIELD_NUMBER: builtins.int
        CLAUSES_FIELD_NUMBER: builtins.int
        FILTERS_FIELD_NUMBER: builtins.int
        clauseType: global___QP.ClauseType.ValueType
        @property
        def clauses(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___QP.FilterClause]: ...
        @property
        def filters(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___QP.Filter]: ...
        def __init__(
            self,
            *,
            clauseType: global___QP.ClauseType.ValueType | None = ...,
            clauses: collections.abc.Iterable[global___QP.FilterClause] | None = ...,
            filters: collections.abc.Iterable[global___QP.Filter] | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["clauseType", b"clauseType"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["clauseType", b"clauseType", "clauses", b"clauses", "filters", b"filters"]) -> None: ...

    @typing.final
    class Filter(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        FILTERNAME_FIELD_NUMBER: builtins.int
        PARAMETERS_FIELD_NUMBER: builtins.int
        FILTERRESULT_FIELD_NUMBER: builtins.int
        CLIENTNOTSUPPORTEDCONFIG_FIELD_NUMBER: builtins.int
        filterName: builtins.str
        filterResult: global___QP.FilterResult.ValueType
        clientNotSupportedConfig: global___QP.FilterClientNotSupportedConfig.ValueType
        @property
        def parameters(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___QP.FilterParameters]: ...
        def __init__(
            self,
            *,
            filterName: builtins.str | None = ...,
            parameters: collections.abc.Iterable[global___QP.FilterParameters] | None = ...,
            filterResult: global___QP.FilterResult.ValueType | None = ...,
            clientNotSupportedConfig: global___QP.FilterClientNotSupportedConfig.ValueType | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["clientNotSupportedConfig", b"clientNotSupportedConfig", "filterName", b"filterName", "filterResult", b"filterResult"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["clientNotSupportedConfig", b"clientNotSupportedConfig", "filterName", b"filterName", "filterResult", b"filterResult", "parameters", b"parameters"]) -> None: ...

    @typing.final
    class FilterParameters(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str | None = ...,
            value: builtins.str | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    def __init__(
        self,
    ) -> None: ...

global___QP = QP
