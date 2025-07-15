-module(messenger).
-export([start/0, send_message/2]).

start() ->
    Pid = spawn(fun loop/0),  % Start a new process
    Pid.  % Return process ID (Pid)

loop() ->
    receive  % Wait for a message
        {From, Message} ->
            io:format("Received: ~p~n", [Message]),
            From ! {reply, "Got your message!"},  % Send reply
            loop()  % Keep running
    end.

send_message(Pid, Message) ->
    Pid ! {self(), Message},  % Send message
    receive
        {reply, Reply} -> io:format("Reply: ~p~n", [Reply])
    end.
