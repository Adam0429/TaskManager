{application,emqx_license,
             [{description,"EMQ X License"},
              {vsn,"4.2.5"},
              {modules,[emqx_exhook_entr,emqx_license,emqx_license_app,
                        emqx_license_cli,emqx_license_mgr,emqx_license_sup]},
              {registered,[emqx_license_sup]},
              {applications,[kernel,stdlib]},
              {mod,{emqx_license_app,[]}},
              {relup_deps,[emqx]}]}.