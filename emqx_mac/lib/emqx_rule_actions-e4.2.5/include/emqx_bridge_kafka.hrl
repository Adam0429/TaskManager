-define(APP, emqx_bridge_kafka).

-define(KAFKA_MESSAGES, [
    {counter, 'kafka/sync/sent'},        % produce kafkaServer Messages sent
    {counter, 'kafka/sync/responsed'},   % produce kafkaServer Messages responsed
    {counter, 'kafka/async/sent'}, % produce kafkaServer Messages sent
    {counter, 'kafka/async/responsed'}, % produce kafkaServer Messages responsed
    {counter, 'kafka/async_batched/sent'}, % produce kafkaServer Messages sent
    {counter, 'kafka/async_batched/responsed'} % produce kafkaServer Messages responsed
]).
