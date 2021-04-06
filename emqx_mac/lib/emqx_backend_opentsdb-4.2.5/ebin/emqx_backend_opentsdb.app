{application,emqx_backend_opentsdb,
             [{description,"EMQ X OpenTSDB Backend"},
              {vsn,"4.2.5"},
              {modules,[emqx_backend_opentsdb,emqx_backend_opentsdb_app,
                        emqx_backend_opentsdb_cli,emqx_backend_opentsdb_sup]},
              {registered,[emqx_backend_opentsdb_sup]},
              {applications,[kernel,stdlib,opentsdb,ecpool]},
              {mod,{emqx_backend_opentsdb_app,[]}},
              {relup_deps,[emqx]}]}.