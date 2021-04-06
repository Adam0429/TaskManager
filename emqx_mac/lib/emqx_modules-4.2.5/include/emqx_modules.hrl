%%--------------------------------------------------------------------
%% Copyright (c) 2020 EMQ Technologies Co., Ltd. All Rights Reserved.
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
%%--------------------------------------------------------------------

-define(APP, emqx_modules).

-type(maybe(T) :: T | undefined).


-type(module_id() :: binary()).

-type(module_type_name() :: atom()).

-type(descr() :: #{en := binary(), zh => binary()}).

-type(mf() :: {Module::atom(), Fun::atom()}).

-type(module_status() :: #{ alive := boolean()
                            , atom() => binary() | atom() | list(binary()|atom())
                            }).

-define(descr, #{en => <<>>, zh => <<>>}).

-record(module,
        { id :: module_id()
        , type :: module_type_name()
        , config :: #{} %% the configs got from API for initializing module
        , enabled :: boolean()
        , created_at :: erlang:timestamp()
        , description :: binary()
        }).

-record(module_type,
        { name :: module_type_name()
        , type :: atom()
        , provider :: atom()
        , params_spec :: #{atom() => term()} %% params specs
        , on_create :: mf()
        , on_status :: mf()
        , on_update :: mf()
        , on_destroy :: mf()
        , title = ?descr :: descr()
        , description = ?descr :: descr()
        }).

-record(module_params,
        { id :: module_id()
        , params :: #{} %% the params got after initializing the module
        , status = #{is_alive => false} :: #{is_alive := boolean(), atom() => term()}
        }).

-define(RAISE(_EXP_, _ERROR_),
        begin
          fun() ->
            try (_EXP_) catch _:_REASON_:_STK_ -> throw({_ERROR_, _STK_}) end
          end()
        end).

-define(THROW(_EXP_, _ERROR_),
        begin
            try (_EXP_) catch _:_ -> throw(_ERROR_) end
        end).

%% Tables
-define(MODULE_TAB, emqx_modules).
-define(MODULE_TYPE_TAB, emqx_modules_type).
-define(MODULE_PARAMS_TAB, emqx_modules_params).
