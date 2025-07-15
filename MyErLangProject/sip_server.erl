-module(sip_server).
-export([start/1, listen/1, handle_client/1]).

start(Port) ->
    {ok, ListenSocket} = gen_tcp:listen(Port, [binary, {packet, line}, {active, false}]),
    io:format("SIP Server started on port ~p~n", [Port]),
    listen(ListenSocket).

listen(ListenSocket) ->
    {ok, ClientSocket} = gen_tcp:accept(ListenSocket),
    spawn(?MODULE, handle_client, [ClientSocket]),
    listen(ListenSocket).

handle_client(Socket) ->
    gen_tcp:send(Socket, "SIP/2.0 200 OK\r\n"),
    loop(Socket).

loop(Socket) ->
    case gen_tcp:recv(Socket, 0) of
        {ok, Data} ->
            io:format("Received: ~s", [Data]),
            gen_tcp:send(Socket, "SIP/2.0 200 OK\r\n"),
            loop(Socket);
        {error, closed} ->
            io:format("Client disconnected.~n"),
            ok
    end.
