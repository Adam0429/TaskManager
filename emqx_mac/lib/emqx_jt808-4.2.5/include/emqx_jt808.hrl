%% Copyright (c) 2013-2019 EMQ Technologies Co., Ltd. All Rights Reserved.
%%
%% Licensed under the Apache License, Version 2.0 (the "License");
%% you may not use this file except in compliance with the License.
%% You may obtain a copy of the License at
%%
%%     http://www.apache.org/licenses/LICENSE-2.0
%%
%% Unless required by applicable law or agreed to in writing, software
%% distributed under the License is distributed on an "AS IS" BASIS,
%% WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
%% See the License for the specific language governing permissions and
%% limitations under the License.

-ifndef(EMQX_JT808_HRL).
-define(EMQX_JT808_HRL, true).

-define(APP, emqx_jt808).

%%--------------------------------------------------------------------
%% Message Ids
%%--------------------------------------------------------------------

%% Message Ids of client to server
-define(MC_GENERAL_RESPONSE,        16#0001).
-define(MC_HEARTBEAT,               16#0002).
-define(MC_REGISTER,                16#0100).
-define(MC_DEREGISTER,              16#0003).
-define(MC_AUTH,                    16#0102).
-define(MC_QUERY_PARAM_ACK,         16#0104).
-define(MC_QUERY_ATTRIB_ACK,        16#0107).
-define(MC_OTA_ACK,                 16#0108).
-define(MC_LOCATION_REPORT,         16#0200).
-define(MC_QUERY_LOCATION_ACK,      16#0201).
-define(MC_EVENT_REPORT,            16#0301).
-define(MC_QUESTION_ACK,            16#0302).
-define(MC_INFO_REQ_CANCEL,         16#0303).
-define(MC_VEHICLE_CTRL_ACK,        16#0500).
-define(MC_DRIVE_RECORD_REPORT,     16#0700).
-define(MC_WAYBILL_REPORT,          16#0701).
-define(MC_DRIVER_ID_REPORT,        16#0702).
-define(MC_BULK_LOCATION_REPORT,    16#0704).
-define(MC_CAN_BUS_REPORT,          16#0705).
-define(MC_MULTIMEDIA_EVENT_REPORT, 16#0800).
-define(MC_MULTIMEDIA_DATA_REPORT,  16#0801).
-define(MC_CAMERA_SHOT_ACK,         16#0805).
-define(MC_MM_DATA_SEARCH_ACK,      16#0802).
-define(MC_SEND_TRANSPARENT_DATA,   16#0900).
-define(MC_SEND_ZIP_DATA,           16#0901).
-define(MC_RSA_KEY,                 16#0A00).

%% Message Ids of server to client
-define(MS_GENERAL_RESPONSE,       16#8001).
-define(MS_REQUEST_FRAGMENT,       16#8003).
-define(MS_REGISTER_ACK,           16#8100).
-define(MS_SET_CLIENT_PARAM,       16#8103).
-define(MS_QUERY_CLIENT_ALL_PARAM, 16#8104).
-define(MS_CLIENT_CONTROL,         16#8105).
-define(MS_QUERY_CLIENT_PARAM,     16#8106).
-define(MS_QUERY_CLIENT_ATTRIB,    16#8107).
-define(MS_OTA,                    16#8108).
-define(MS_QUERY_LOCATION,         16#8201).
-define(MS_TRACE_LOCATION,         16#8202).
-define(MS_CONFIRM_ALARM,          16#8203).
-define(MS_SEND_TEXT,              16#8300).
-define(MS_SET_EVENT,              16#8301).
-define(MS_SEND_QUESTION,          16#8302).
-define(MS_SET_MENU,               16#8303).
-define(MS_INFO_CONTENT,           16#8304).
-define(MS_PHONE_CALLBACK,         16#8400).
-define(MS_SET_PHONE_NUMBER,       16#8401).
-define(MS_VEHICLE_CONTROL,        16#8500).
-define(MS_SET_CIRCLE_AREA,        16#8600).
-define(MS_DEL_CIRCLE_AREA,        16#8601).
-define(MS_SET_RECT_AREA,          16#8602).
-define(MS_DEL_RECT_AREA,          16#8603).
-define(MS_SET_POLY_AREA,          16#8604).
-define(MS_DEL_POLY_AREA,          16#8605).
-define(MS_SET_PATH,               16#8606).
-define(MS_DEL_PATH,               16#8607).
-define(MS_DRIVE_RECORD_CAPTURE,   16#8700).
-define(MS_DRIVE_REC_PARAM_SEND,   16#8701).
-define(MS_REQ_DRIVER_ID,          16#8702).
-define(MS_MULTIMEDIA_DATA_ACK,    16#8800).
-define(MS_CAMERA_SHOT,            16#8801).
-define(MS_MM_DATA_SEARCH,         16#8802).
-define(MS_MM_DATA_UPLOAD,         16#8803).
-define(MS_VOICE_RECORD,           16#8804).
-define(MS_SINGLE_MM_DATA_CTRL,    16#8805).
-define(MS_SEND_TRANSPARENT_DATA,  16#8900).
-define(MS_RSA_KEY,                16#8A00).

%% Client Params
-define(CP_HEARTBEAT_DURATION,                  16#0001).
-define(CP_TCP_TIMEOUT,                         16#0002).
-define(CP_TCP_RETX,                            16#0003).
-define(CP_UDP_TIMEOUT,                         16#0004).
-define(CP_UDP_RETX,                            16#0005).
-define(CP_SMS_TIMEOUT,                         16#0006).
-define(CP_SMS_RETX,                            16#0007).
-define(CP_SERVER_APN,                          16#0010).
-define(CP_DIAL_USERNAME,                       16#0011).
-define(CP_DIAL_PASSWORD,                       16#0012).
-define(CP_SERVER_ADDRESS,                      16#0013).
-define(CP_BACKUP_SERVER_APN,                   16#0014).
-define(CP_BACKUP_DIAL_USERNAME,                16#0015).
-define(CP_BACKUP_DIAL_PASSWORD,                16#0016).
-define(CP_BACKUP_SERVER_ADDRESS,               16#0017).
-define(CP_SERVER_TCP_PORT,                     16#0018).
-define(CP_SERVER_UDP_PORT,                     16#0019).
-define(CP_IC_CARD_SERVER_ADDRESS,              16#001A).
-define(CP_IC_CARD_SERVER_TCP_PORT,             16#001B).
-define(CP_IC_CARD_SERVER_UDP_PORT,             16#001C).
-define(CP_IC_CARD_BACKUP_SERVER_ADDRESS,       16#001D).
-define(CP_POS_REPORT_POLICY,                   16#0020).
-define(CP_POS_REPORT_CONTROL,                  16#0021).
-define(CP_DRIVER_NLOGIN_REPORT_INTERVAL,       16#0022).
-define(CP_REPORT_INTERVAL_DURING_SLEEP,        16#0027).
-define(CP_EMERGENCY_ALARM_REPORT_INTERVAL,     16#0028).
-define(CP_DEFAULT_REPORT_INTERVAL,             16#0029).
-define(CP_DEFAULT_DISTANCE_INTERVAL,           16#002C).
-define(CP_DRIVER_NLOGIN_DISTANCE_INTERVAL,     16#002D).
-define(CP_DISTANCE_INTERVAL_DURING_SLEEP,      16#002E).
-define(CP_EMERGENCY_ALARM_DISTANCE_INTERVAL,   16#002F).
-define(CP_SET_TURN_ANGLE,                      16#0030).
-define(CP_EFENCE_RADIUS,                       16#0031).
-define(CP_MONITOR_PHONE,                       16#0040).
-define(CP_RESETING_PHONE,                      16#0041).
-define(CP_RECOVERY_PHONE,                      16#0042).
-define(CP_SMS_MONITOR_PHONE,                   16#0043).
-define(CP_EMERGENCY_SMS_PHONE,                 16#0044).
-define(CP_ACCEPT_CALL_POLICY,                  16#0045).
-define(CP_MAX_CALL_DURATION,                   16#0046).
-define(CP_MAX_CALL_DURATION_OF_MONTH,          16#0047).
-define(CP_SPY_PHONE,                           16#0048).
-define(CP_PRIVILEGE_SMS_PHONE,                 16#0049).
-define(CP_ALARM_MASK,                          16#0050).
-define(CP_ALARM_SEND_SMS_MASK,                 16#0051).
-define(CP_ALARM_CAMERA_SHOT_MASK,              16#0052).
-define(CP_ALARM_PICTURE_SAVE_MASK,             16#0053).
-define(CP_ALARM_KEY_MASK,                      16#0054).
-define(CP_MAX_SPEED,                           16#0055).
-define(CP_OVERSPEED_ELAPSED,                   16#0056).
-define(CP_CONT_DRIVE_THRESHOLD,                16#0057).
-define(CP_ACC_DRIVE_TIME_ONE_DAY_THRESHOLD,    16#0058).
-define(CP_MIN_BREAK_TIME,                      16#0059).
-define(CP_MAX_PARK_TIME,                       16#005A).
-define(CP_OVERSPEED_ALARM_DELTA,               16#005B).
-define(CP_DRIVER_FATIGUE_ALARM_DELTA,          16#005C).
-define(CP_SET_CRASH_ALARM_PARAM,               16#005D).
-define(CP_SET_ROLLOVER_PARAM,                  16#005E).
-define(CP_TIME_CONTROLED_CAMERA,               16#0064).
-define(CP_DISTANCE_CONTROLED_CAMERA,           16#0065).
-define(CP_PICTURE_QUALITY,                     16#0070).
-define(CP_PICTURE_BRIGHTNESS,                  16#0071).
-define(CP_PICTURE_CONTRAST,                    16#0072).
-define(CP_PICTURE_SATURATE,                    16#0073).
-define(CP_PICTURE_CHROMATICITY,                16#0074).
-define(CP_ODOMETER,                            16#0080).
-define(CP_REGISTERED_PROVINCE,                 16#0081).
-define(CP_REGISTERED_CITY,                     16#0082).
-define(CP_VEHICLE_LICENSE_NUMBER,              16#0083).
-define(CP_VEHICLE_LICENSE_PLATE_COLOR,         16#0084).
-define(CP_GNSS_MODE,                           16#0090).
-define(CP_GNSS_BAUDRATE,                       16#0091).
-define(CP_GNSS_OUTPUT_RATE,                    16#0092).
-define(CP_GNSS_SAMPLING_RATE,                  16#0093).
-define(CP_GNSS_UPLOAD_MODE,                    16#0094).
-define(CP_GNSS_UPLOAD_UNIT,                    16#0095).
-define(CP_CAN_BUS_CH1_SAMPLING,                16#0100).
-define(CP_CAN_BUS_CH1_UPLOAD,                  16#0101).
-define(CP_CAN_BUS_CH2_SAMPLING,                16#0102).
-define(CP_CAN_BUS_CH2_UPLOAD,                  16#0103).
-define(CP_SET_CAN_BUS_ID_PARAM,                16#0110).

%% Extra info types in Position Report
-define(CP_POS_EXTRA_MILEAGE,           16#01).
-define(CP_POS_EXTRA_FUEL_METER,        16#02).
-define(CP_POS_EXTRA_SPEED,             16#03).
-define(CP_POS_EXTRA_ALARM_ID,          16#04).
-define(CP_POS_EXTRA_OVERSPEED_ALARM,   16#11).
-define(CP_POS_EXTRA_IN_OUT_ALARM,      16#12).
-define(CP_POS_EXTRA_PATH_TIME_ALARM,   16#13).
-define(CP_POS_EXTRA_EXPANDED_SIGNAL,   16#25).
-define(CP_POS_EXTRA_IO_STATUS,         16#2A).
-define(CP_POS_EXTRA_ANALOG,            16#2B).
-define(CP_POS_EXTRA_RSSI,              16#30).
-define(CP_POS_EXTRA_GNSS_SAT_NUM,      16#31).
-define(CP_POS_EXTRA_CUSTOME,           16#E0).

-endif.
