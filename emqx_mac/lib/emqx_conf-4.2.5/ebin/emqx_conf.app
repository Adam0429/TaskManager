{application,emqx_conf,
             [{description,"EMQ X Hot Configuration"},
              {vsn,"4.2.5"},
              {modules,[emqx_conf,emqx_conf_api,emqx_conf_app,emqx_conf_sup]},
              {registered,[emqx_conf_app]},
              {applications,[kernel,stdlib]},
              {mod,{emqx_conf_app,[]}},
              {relup_deps,[emqx]}]}.