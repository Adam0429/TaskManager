{application,eredis,
             [{description,"Erlang Redis Client"},
              {vsn,"1.2.2"},
              {modules,[basho_bench_driver_eredis,basho_bench_driver_erldis,
                        eredis,eredis_client,eredis_parser,eredis_sentinel,
                        eredis_sentinel_client,eredis_sentinel_masters,
                        eredis_sentinel_sup,eredis_sub,eredis_sub_client]},
              {registered,[]},
              {applications,[kernel,stdlib]}]}.
