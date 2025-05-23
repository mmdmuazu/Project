-module(chat_server).
-export([start/1, accept/1, handle_client/1, broadcast/1]).

start(Port) ->
    {ok, ListenSocket} = gen_tcp:listen(Port, [binary, {packet, 0}, {reuseaddr, true}]),
    io:format("Chat server running on port ~p~n", [Port]),
    accept(ListenSocket).

accept(ListenSocket) ->
    {ok, Socket} = gen_tcp:accept(ListenSocket),
    spawn(fun() -> handle_client(Socket) end),
    accept(ListenSocket).

handle_client(Socket) ->
    gen_tcp:send(Socket, "Enter your username: "),
    case gen_tcp:recv(Socket, 0) of
        {ok, Username} ->
            io:format("User ~s joined the chat~n", [Username]),
            broadcast("** " ++ Username ++ " joined **"),
            client_loop(Socket, Username);
        {error, _} -> gen_tcp:close(Socket)
    end.

client_loop(Socket, Username) ->
    case gen_tcp:recv(Socket, 0) of
        {ok, Message} ->
            broadcast(Username ++ ": " ++ Message),
            client_loop(Socket, Username);
        {error, closed} ->
            broadcast("** " ++ Username ++ " left **"),
            gen_tcp:close(Socket)
    end.

broadcast(Message) ->
    io:format("Broadcasting: ~s~n", [Message]).
