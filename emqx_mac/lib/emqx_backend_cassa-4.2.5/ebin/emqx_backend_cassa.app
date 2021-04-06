{application,emqx_backend_cassa,
             [{description,"EMQ X Cassandra Backend"},
              {vsn,"4.2.5"},
              {modules,[emqx_backend_cassa,emqx_backend_cassa_app,
                        emqx_backend_cassa_cli,emqx_backend_cassa_sup]},
              {registered,[emqx_backend_cassa_sup]},
              {applications,[kernel,stdlib,ecql,ecpool]},
              {mod,{emqx_backend_cassa_app,[]}},
              {relup_deps,[emqx]}]}.