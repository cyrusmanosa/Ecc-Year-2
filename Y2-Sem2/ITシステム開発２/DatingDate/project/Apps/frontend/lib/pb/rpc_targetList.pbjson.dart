//
//  Generated code. Do not modify.
//  source: rpc_targetList.proto
//
// @dart = 2.12

// ignore_for_file: annotate_overrides, camel_case_types, comment_references
// ignore_for_file: constant_identifier_names, library_prefixes
// ignore_for_file: non_constant_identifier_names, prefer_final_fields
// ignore_for_file: unnecessary_import, unnecessary_this, unused_import

import 'dart:convert' as $convert;
import 'dart:core' as $core;
import 'dart:typed_data' as $typed_data;

@$core.Deprecated('Use createTargetListRequestDescriptor instead')
const CreateTargetListRequest$json = {
  '1': 'CreateTargetListRequest',
  '2': [
    {'1': 'SessionID', '3': 1, '4': 1, '5': 9, '10': 'SessionID'},
    {'1': 'Target1ID', '3': 2, '4': 1, '5': 5, '10': 'Target1ID'},
    {'1': 'T1Type', '3': 3, '4': 1, '5': 9, '10': 'T1Type'},
    {'1': 'Target2ID', '3': 4, '4': 1, '5': 5, '10': 'Target2ID'},
    {'1': 'T2Type', '3': 5, '4': 1, '5': 9, '10': 'T2Type'},
    {'1': 'Target3ID', '3': 6, '4': 1, '5': 5, '10': 'Target3ID'},
    {'1': 'T3Type', '3': 7, '4': 1, '5': 9, '10': 'T3Type'},
  ],
};

/// Descriptor for `CreateTargetListRequest`. Decode as a `google.protobuf.DescriptorProto`.
final $typed_data.Uint8List createTargetListRequestDescriptor = $convert.base64Decode(
    'ChdDcmVhdGVUYXJnZXRMaXN0UmVxdWVzdBIcCglTZXNzaW9uSUQYASABKAlSCVNlc3Npb25JRB'
    'IcCglUYXJnZXQxSUQYAiABKAVSCVRhcmdldDFJRBIWCgZUMVR5cGUYAyABKAlSBlQxVHlwZRIc'
    'CglUYXJnZXQySUQYBCABKAVSCVRhcmdldDJJRBIWCgZUMlR5cGUYBSABKAlSBlQyVHlwZRIcCg'
    'lUYXJnZXQzSUQYBiABKAVSCVRhcmdldDNJRBIWCgZUM1R5cGUYByABKAlSBlQzVHlwZQ==');

@$core.Deprecated('Use createTargetListResponseDescriptor instead')
const CreateTargetListResponse$json = {
  '1': 'CreateTargetListResponse',
  '2': [
    {'1': 'tl', '3': 1, '4': 1, '5': 11, '6': '.pb.Targetlist', '10': 'tl'},
  ],
};

/// Descriptor for `CreateTargetListResponse`. Decode as a `google.protobuf.DescriptorProto`.
final $typed_data.Uint8List createTargetListResponseDescriptor = $convert.base64Decode(
    'ChhDcmVhdGVUYXJnZXRMaXN0UmVzcG9uc2USHgoCdGwYASABKAsyDi5wYi5UYXJnZXRsaXN0Ug'
    'J0bA==');

@$core.Deprecated('Use getTargetListRequestDescriptor instead')
const GetTargetListRequest$json = {
  '1': 'GetTargetListRequest',
  '2': [
    {'1': 'SessionID', '3': 1, '4': 1, '5': 9, '10': 'SessionID'},
    {'1': 'UserID', '3': 2, '4': 1, '5': 5, '10': 'UserID'},
  ],
};

/// Descriptor for `GetTargetListRequest`. Decode as a `google.protobuf.DescriptorProto`.
final $typed_data.Uint8List getTargetListRequestDescriptor = $convert.base64Decode(
    'ChRHZXRUYXJnZXRMaXN0UmVxdWVzdBIcCglTZXNzaW9uSUQYASABKAlSCVNlc3Npb25JRBIWCg'
    'ZVc2VySUQYAiABKAVSBlVzZXJJRA==');

@$core.Deprecated('Use getTargetListResponseDescriptor instead')
const GetTargetListResponse$json = {
  '1': 'GetTargetListResponse',
  '2': [
    {'1': 'tl', '3': 1, '4': 1, '5': 11, '6': '.pb.Targetlist', '10': 'tl'},
  ],
};

/// Descriptor for `GetTargetListResponse`. Decode as a `google.protobuf.DescriptorProto`.
final $typed_data.Uint8List getTargetListResponseDescriptor = $convert.base64Decode(
    'ChVHZXRUYXJnZXRMaXN0UmVzcG9uc2USHgoCdGwYASABKAsyDi5wYi5UYXJnZXRsaXN0UgJ0bA'
    '==');

@$core.Deprecated('Use updateTargetListRequestDescriptor instead')
const UpdateTargetListRequest$json = {
  '1': 'UpdateTargetListRequest',
  '2': [
    {'1': 'SessionID', '3': 1, '4': 1, '5': 9, '10': 'SessionID'},
    {'1': 'Target1ID', '3': 2, '4': 1, '5': 5, '10': 'Target1ID'},
    {'1': 'T1Type', '3': 3, '4': 1, '5': 9, '10': 'T1Type'},
    {'1': 'Target2ID', '3': 4, '4': 1, '5': 5, '10': 'Target2ID'},
    {'1': 'T2Type', '3': 5, '4': 1, '5': 9, '10': 'T2Type'},
    {'1': 'Target3ID', '3': 6, '4': 1, '5': 5, '10': 'Target3ID'},
    {'1': 'T3Type', '3': 7, '4': 1, '5': 9, '10': 'T3Type'},
  ],
};

/// Descriptor for `UpdateTargetListRequest`. Decode as a `google.protobuf.DescriptorProto`.
final $typed_data.Uint8List updateTargetListRequestDescriptor = $convert.base64Decode(
    'ChdVcGRhdGVUYXJnZXRMaXN0UmVxdWVzdBIcCglTZXNzaW9uSUQYASABKAlSCVNlc3Npb25JRB'
    'IcCglUYXJnZXQxSUQYAiABKAVSCVRhcmdldDFJRBIWCgZUMVR5cGUYAyABKAlSBlQxVHlwZRIc'
    'CglUYXJnZXQySUQYBCABKAVSCVRhcmdldDJJRBIWCgZUMlR5cGUYBSABKAlSBlQyVHlwZRIcCg'
    'lUYXJnZXQzSUQYBiABKAVSCVRhcmdldDNJRBIWCgZUM1R5cGUYByABKAlSBlQzVHlwZQ==');

@$core.Deprecated('Use updateTargetListResponseDescriptor instead')
const UpdateTargetListResponse$json = {
  '1': 'UpdateTargetListResponse',
  '2': [
    {'1': 'tl', '3': 1, '4': 1, '5': 11, '6': '.pb.Targetlist', '10': 'tl'},
  ],
};

/// Descriptor for `UpdateTargetListResponse`. Decode as a `google.protobuf.DescriptorProto`.
final $typed_data.Uint8List updateTargetListResponseDescriptor = $convert.base64Decode(
    'ChhVcGRhdGVUYXJnZXRMaXN0UmVzcG9uc2USHgoCdGwYASABKAsyDi5wYi5UYXJnZXRsaXN0Ug'
    'J0bA==');

@$core.Deprecated('Use deleteTargetListRequestDescriptor instead')
const DeleteTargetListRequest$json = {
  '1': 'DeleteTargetListRequest',
  '2': [
    {'1': 'SessionID', '3': 1, '4': 1, '5': 9, '10': 'SessionID'},
  ],
};

/// Descriptor for `DeleteTargetListRequest`. Decode as a `google.protobuf.DescriptorProto`.
final $typed_data.Uint8List deleteTargetListRequestDescriptor = $convert.base64Decode(
    'ChdEZWxldGVUYXJnZXRMaXN0UmVxdWVzdBIcCglTZXNzaW9uSUQYASABKAlSCVNlc3Npb25JRA'
    '==');

