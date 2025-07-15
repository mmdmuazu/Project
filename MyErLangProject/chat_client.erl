-module(chat_client).
-include_lib("wx/include/wx.hrl").
-export([start/0, create_gui/0, send_message/1]).

start() ->
    wx:new(),
    %create_gui(),
    wx:main_loop().

create_gui() ->
    Frame = wxFrame:new(wx:null(), -1, "Erlang Chat Client", [{size, {400, 300}}]),
    Panel = wxPanel:new(Frame),
    Vbox = wxBoxSizer:new(?wxVERTICAL),

    ChatBox = wxTextCtrl:new(Panel, -1, [{style, ?wxTE_MULTILINE, size, {380, 200}}]),
    MsgBox = wxTextCtrl:new(Panel, -1, [{size, {380, 30}}]),
    SendButton = wxButton:new(Panel, -1, "Send"),

    wxSizer:add(Vbox, ChatBox, [{flag, ?wxEXPAND, proportion, 1}]),
    wxSizer:add(Vbox, MsgBox, [{flag, ?wxEXPAND}]),
    wxSizer:add(Vbox, SendButton, [{flag, ?wxEXPAND}]),

    wxPanel:setSizer(Panel, Vbox),
    wxFrame:show(Frame),

    wxFrame:connect(SendButton, command_button_clicked, fun(_) -> send_message(MsgBox) end).

send_message(MsgBox) ->
    Msg = wxTextCtrl:getValue(MsgBox),
    io:format("Sending message: ~s~n", [Msg]),
    wxTextCtrl:setValue(MsgBox, "").
