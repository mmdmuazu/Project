-module(tcp_server).
-export([start/1]).

start(Port) ->
    {ok, ListenSocket} = gen_tcp:listen(Port, [binary, {packet, 0}, {active, false}, {reuseaddr, true}]),
    io:format("Server listening on port ~p~n", [Port]),
    accept(ListenSocket).

accept(ListenSocket) ->
    {ok, Socket} = gen_tcp:accept(ListenSocket),  % Wait for client
    spawn(fun() -> handle_client(Socket) end),  % Start a process for client
    accept(ListenSocket).  % Keep accepting clients

handle_client(Socket) ->
    gen_tcp:send(Socket, "Welcome to the server!\n"),
    loop(Socket).

loop(Socket) ->
    case gen_tcp:recv(Socket, 0) of
        {ok, Data} ->  
            io:format("Received: ~p~n", [Data]),
            gen_tcp:send(Socket, Data),  % Echo back the data
            loop(Socket);
        {error, closed} ->  
            io:format("Client disconnected~n"),
            gen_tcp:close(Socket)
    end.
