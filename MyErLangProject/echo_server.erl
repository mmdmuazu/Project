-module(echo_server).
-export([start/0, send/2]).

start() ->
    Pid = spawn(fun loop/0),  % Start server process
    io:format("Server started with PID: ~p~n", [Pid]),
    Pid.

loop() ->
    receive
        {From, Message} ->  
            io:format("Received: ~p~n", [Message]),  
            From ! {reply, Message},  % Send back the same message
            loop()  % Keep running
    end.

send(Pid, Message) ->
    Pid ! {self(), Message},  % Send message to server
    receive
        {reply, Reply} -> io:format("Reply: ~p~n", [Reply])
    end.
