{application,emqx_jt808,
             [{description,"JT/T808 Connector"},
              {vsn,"4.2.5"},
              {modules,[emqx_jt808_app,emqx_jt808_auth,emqx_jt808_connection,
                        emqx_jt808_frame,emqx_jt808_protocol,emqx_jt808_sup]},
              {registered,[emqx_jt808_sup]},
              {applications,[kernel,stdlib,esockd]},
              {mod,{emqx_jt808_app,[]}},
              {relup_deps,[emqx]}]}.