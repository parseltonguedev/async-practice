# MQ broker

### Example output:

* Message broker (server):

  ```console
    python message_queue_server.py  
  
    Remote ('127.0.0.1', 50324) subscribed to b'/null'
    Remote ('127.0.0.1', 50325) subscribed to b'/topic/foo'
    Remote ('127.0.0.1', 50327) subscribed to b'/topic/foo'
    Full data: b'Message 0 from 11133c02'
    Sending to b'/topic/foo': b'Message 0 from 11133c02'..
    Place the data onto each subscriber's own send queue
    Task exception was never retrieved
    future: <Task finished name='Task-12' coro=<channel_sender() done, defined at /Users/Bohdan_Solianyk/PycharmProjects/async-practice/message_queue/message_queue_server.py:110> exception=TypeError("object bytes can't be used in 'await' expression")>
    Traceback (most recent call last):
      File "/Users/Bohdan_Solianyk/PycharmProjects/async-practice/message_queue/message_queue_server.py", line 149, in channel_sender
        message = await message
                  ^^^^^^^^^^^^^
    TypeError: object bytes can't be used in 'await' expression
    Full data: b'Message 1 from 11133c02'
    Full data: b'Message 2 from 11133c02'
    Full data: b'Message 3 from 11133c02'
    Full data: b'Message 4 from 11133c02'
    Remote ('127.0.0.1', 50324) disconnected. disconnect_error=IncompleteReadError('0 bytes read on a total of 4 expected bytes')
    Remote ('127.0.0.1', 50324) closed. Clean up..
    Wait for sender task to finish..
    Remove the entry in the SEND_QUEUES
    Remote ('127.0.0.1', 50325) disconnected. disconnect_error=IncompleteReadError('0 bytes read on a total of 4 expected bytes')
    Remote ('127.0.0.1', 50325) closed. Clean up..
    Wait for sender task to finish..
    Remove the entry in the SEND_QUEUES
    Remote ('127.0.0.1', 50327) disconnected. disconnect_error=IncompleteReadError('0 bytes read on a total of 4 expected bytes')
    Remote ('127.0.0.1', 50327) closed. Clean up..
    Wait for sender task to finish..
    Remove the entry in the SEND_QUEUES
    Remote ('127.0.0.1', 50332) subscribed to b'/null'
    Full data: b'Message 0 from 31e93720'
    No subscribers.. wait for 1 second and try again
    Full data: b'Message 1 from 31e93720'
    No subscribers.. wait for 1 second and try again
    Full data: b'Message 2 from 31e93720'
    No subscribers.. wait for 1 second and try again
    Full data: b'Message 3 from 31e93720'
    No subscribers.. wait for 1 second and try again
    Full data: b'Message 4 from 31e93720'
    No subscribers.. wait for 1 second and try again
    Full data: b'Message 5 from 31e93720'
    No subscribers.. wait for 1 second and try again
    Full data: b'Message 6 from 31e93720'
    No subscribers.. wait for 1 second and try again
    Full data: b'Message 7 from 31e93720'
    No subscribers.. wait for 1 second and try again
    Full data: b'Message 8 from 31e93720'
    No subscribers.. wait for 1 second and try again
    Full data: b'Message 9 from 31e93720'
    No subscribers.. wait for 1 second and try again
    Full data: b'Message 10 from 31e93720'
    No subscribers.. wait for 1 second and try again
    No subscribers.. wait for 1 second and try again
    No subscribers.. wait for 1 second and try again
    No subscribers.. wait for 1 second and try again
    Remote ('127.0.0.1', 50334) subscribed to b'/queue/blah'
    No subscribers.. wait for 1 second and try again
    Sending to b'/queue/blah': b'Message 0 from 31e93720'..
    Place the data onto each subscriber's own send queue
    Sending to b'/queue/blah': b'Message 1 from 31e93720'..
    Place the data onto each subscriber's own send queue
    Sending to b'/queue/blah': b'Message 2 from 31e93720'..
    Place the data onto each subscriber's own send queue
    Sending to b'/queue/blah': b'Message 3 from 31e93720'..
    Place the data onto each subscriber's own send queue
    Sending to b'/queue/blah': b'Message 4 from 31e93720'..
    Place the data onto each subscriber's own send queue
    Sending to b'/queue/blah': b'Message 5 from 31e93720'..
    Place the data onto each subscriber's own send queue
    Sending to b'/queue/blah': b'Message 6 from 31e93720'..
    Place the data onto each subscriber's own send queue
    Sending to b'/queue/blah': b'Message 7 from 31e93720'..
    Place the data onto each subscriber's own send queue
    Sending to b'/queue/blah': b'Message 8 from 31e93720'..
    Place the data onto each subscriber's own send queue
    Sending to b'/queue/blah': b'Message 9 from 31e93720'..
    Place the data onto each subscriber's own send queue
    Full data: b'Message 11 from 31e93720'
    Full data: b'Message 12 from 31e93720'
    Full data: b'Message 13 from 31e93720'
    Full data: b'Message 14 from 31e93720'
    Sending to b'/queue/blah': b'Message 10 from 31e93720'..
    Place the data onto each subscriber's own send queue
    Sending to b'/queue/blah': b'Message 11 from 31e93720'..
    Place the data onto each subscriber's own send queue
    Sending to b'/queue/blah': b'Message 12 from 31e93720'..
    Place the data onto each subscriber's own send queue
    Sending to b'/queue/blah': b'Message 13 from 31e93720'..
    Place the data onto each subscriber's own send queue
    Sending to b'/queue/blah': b'Message 14 from 31e93720'..
    Place the data onto each subscriber's own send queue
    Full data: b'Message 15 from 31e93720'
    Sending to b'/queue/blah': b'Message 15 from 31e93720'..
    Place the data onto each subscriber's own send queue
    Full data: b'Message 16 from 31e93720'
    Sending to b'/queue/blah': b'Message 16 from 31e93720'..
    Place the data onto each subscriber's own send queue
    Full data: b'Message 17 from 31e93720'
    Sending to b'/queue/blah': b'Message 17 from 31e93720'..
    Place the data onto each subscriber's own send queue
    Full data: b'Message 18 from 31e93720'
    Sending to b'/queue/blah': b'Message 18 from 31e93720'..
    Place the data onto each subscriber's own send queue
    Full data: b'Message 19 from 31e93720'
    Sending to b'/queue/blah': b'Message 19 from 31e93720'..
    Place the data onto each subscriber's own send queue
    Full data: b'Message 20 from 31e93720'
    Sending to b'/queue/blah': b'Message 20 from 31e93720'..
    Place the data onto each subscriber's own send queue
    Full data: b'Message 21 from 31e93720'
    Sending to b'/queue/blah': b'Message 21 from 31e93720'..
    Place the data onto each subscriber's own send queue
    Full data: b'Message 22 from 31e93720'
    Sending to b'/queue/blah': b'Message 22 from 31e93720'..
    Place the data onto each subscriber's own send queue
    Full data: b'Message 23 from 31e93720'
    Sending to b'/queue/blah': b'Message 23 from 31e93720'..
    Place the data onto each subscriber's own send queue
    Full data: b'Message 24 from 31e93720'
  ```
  
* Sender (client):

    ```console
    python message_queue_sender.py --channel /queue/blah
  
  Start up sender 31e93720
  Opened connection.. sender writer socket name ('127.0.0.1', 50332)
  Connection ended
    ```
  
* Listener (client):

    ```console
    python message_queue_listener.py
  
  Starting up listener 55a70d94
  Opened connection.. listener writer socket name ('127.0.0.1', 50325)
  Received data by 55a70d94: b'Message 0 from 11133'
  ^CBye!
  (async-practice-py3.11) ➜  message_queue git:(improve_mq) ✗ python message_queue_listener.py --listen /queue/blah
  Starting up listener a4adca67
  Opened connection.. listener writer socket name ('127.0.0.1', 50334)
  Received data by a4adca67: b'Message 0 from 31e93'
  Received data by a4adca67: b'Message 1 from 31e93'
  Received data by a4adca67: b'Message 2 from 31e93'
  Received data by a4adca67: b'Message 3 from 31e93'
  Received data by a4adca67: b'Message 4 from 31e93'
  Received data by a4adca67: b'Message 5 from 31e93'
  Received data by a4adca67: b'Message 6 from 31e93'
  Received data by a4adca67: b'Message 7 from 31e93'
  Received data by a4adca67: b'Message 8 from 31e93'
  Received data by a4adca67: b'Message 9 from 31e93'
  Received data by a4adca67: b'Message 10 from 31e9'
  Received data by a4adca67: b'Message 11 from 31e9'
  Received data by a4adca67: b'Message 12 from 31e9'
  Received data by a4adca67: b'Message 13 from 31e9'
  Received data by a4adca67: b'Message 14 from 31e9'
  Received data by a4adca67: b'Message 15 from 31e9'
  Received data by a4adca67: b'Message 16 from 31e9'
  Received data by a4adca67: b'Message 17 from 31e9'
  Received data by a4adca67: b'Message 18 from 31e9'
  Received data by a4adca67: b'Message 19 from 31e9'
  Received data by a4adca67: b'Message 20 from 31e9'
  Received data by a4adca67: b'Message 21 from 31e9'
  Received data by a4adca67: b'Message 22 from 31e9'
  Received data by a4adca67: b'Message 23 from 31e9'
  Received data by a4adca67: b'Message 24 from 31e9'
  Received data by a4adca67: b'Message 25 from 31e9'
  Received data by a4adca67: b'Message 26 from 31e9'
  Received data by a4adca67: b'Message 27 from 31e9'
  Received data by a4adca67: b'Message 28 from 31e9'
  Received data by a4adca67: b'Message 29 from 31e9'
  Received data by a4adca67: b'Message 30 from 31e9'
  Received data by a4adca67: b'Message 31 from 31e9'
  Received data by a4adca67: b'Message 32 from 31e9'
  Received data by a4adca67: b'Message 33 from 31e9'
  Received data by a4adca67: b'Message 34 from 31e9'
  Received data by a4adca67: b'Message 35 from 31e9'
  Received data by a4adca67: b'Message 37 from 31e9'
  Received data by a4adca67: b'Message 39 from 31e9'
  Received data by a4adca67: b'Message 41 from 31e9'
  Received data by a4adca67: b'Message 43 from 31e9'
  Received data by a4adca67: b'Message 45 from 31e9'
  Received data by a4adca67: b'Message 47 from 31e9'
  Received data by a4adca67: b'Message 49 from 31e9'
  Received data by a4adca67: b'Message 51 from 31e9'
  Received data by a4adca67: b'Message 53 from 31e9'
  Received data by a4adca67: b'Message 55 from 31e9'
  Received data by a4adca67: b'Message 57 from 31e9'
  Received data by a4adca67: b'Message 59 from 31e9'
  Received data by a4adca67: b'Message 61 from 31e9'
  Received data by a4adca67: b'Message 63 from 31e9'
  Received data by a4adca67: b'Message 65 from 31e9'
  Received data by a4adca67: b'Message 67 from 31e9'
  Received data by a4adca67: b'Message 69 from 31e9'
  Received data by a4adca67: b'Message 71 from 31e9'
  Received data by a4adca67: b'Message 73 from 31e9'
  Received data by a4adca67: b'Message 75 from 31e9'
  Received data by a4adca67: b'Message 77 from 31e9'
  Received data by a4adca67: b'Message 79 from 31e9'
  Received data by a4adca67: b'Message 81 from 31e9'
  Received data by a4adca67: b'Message 83 from 31e9'
  Received data by a4adca67: b'Message 85 from 31e9'
  Received data by a4adca67: b'Message 87 from 31e9'
  Received data by a4adca67: b'Message 89 from 31e9'
  Received data by a4adca67: b'Message 91 from 31e9'
  Received data by a4adca67: b'Message 93 from 31e9'
  Received data by a4adca67: b'Message 95 from 31e9'
  Received data by a4adca67: b'Message 97 from 31e9'
  Received data by a4adca67: b'Message 99 from 31e9'
  Received data by a4adca67: b'Message 101 from 31e'
  Received data by a4adca67: b'Message 103 from 31e'
  Received data by a4adca67: b'Message 105 from 31e'
  Received data by a4adca67: b'Message 107 from 31e'
  Received data by a4adca67: b'Message 109 from 31e'
  Received data by a4adca67: b'Message 111 from 31e'
  Received data by a4adca67: b'Message 113 from 31e'
  Received data by a4adca67: b'Message 115 from 31e'
  Received data by a4adca67: b'Message 117 from 31e'
  Received data by a4adca67: b'Message 119 from 31e'
  Received data by a4adca67: b'Message 121 from 31e'
  Received data by a4adca67: b'Message 123 from 31e'
  Received data by a4adca67: b'Message 125 from 31e'
  Received data by a4adca67: b'Message 127 from 31e'
  Received data by a4adca67: b'Message 129 from 31e'
  Received data by a4adca67: b'Message 131 from 31e'
  Received data by a4adca67: b'Message 133 from 31e'
  Received data by a4adca67: b'Message 135 from 31e'
  Received data by a4adca67: b'Message 137 from 31e'
  Received data by a4adca67: b'Message 139 from 31e'
  Received data by a4adca67: b'Message 141 from 31e'
  Received data by a4adca67: b'Message 143 from 31e'
  Received data by a4adca67: b'Message 145 from 31e'
  Received data by a4adca67: b'Message 147 from 31e'
  Received data by a4adca67: b'Message 149 from 31e'
  Received data by a4adca67: b'Message 151 from 31e'
  Received data by a4adca67: b'Message 153 from 31e'
  Received data by a4adca67: b'Message 155 from 31e'
  Received data by a4adca67: b'Message 157 from 31e'
  Received data by a4adca67: b'Message 159 from 31e'
  Received data by a4adca67: b'Message 161 from 31e'
  Received data by a4adca67: b'Message 163 from 31e'
  Received data by a4adca67: b'Message 165 from 31e'
  Received data by a4adca67: b'Message 167 from 31e'
  Received data by a4adca67: b'Message 169 from 31e'
  Received data by a4adca67: b'Message 171 from 31e'
  Received data by a4adca67: b'Message 173 from 31e'
  Received data by a4adca67: b'Message 175 from 31e'
  Received data by a4adca67: b'Message 177 from 31e'
  Received data by a4adca67: b'Message 179 from 31e'
  Received data by a4adca67: b'Message 181 from 31e'
  Received data by a4adca67: b'Message 183 from 31e'
  Received data by a4adca67: b'Message 185 from 31e'
  Received data by a4adca67: b'Message 187 from 31e'
  Received data by a4adca67: b'Message 189 from 31e'
  Received data by a4adca67: b'Message 191 from 31e'
  Received data by a4adca67: b'Message 193 from 31e'
  Received data by a4adca67: b'Message 195 from 31e'
  Server closed. server_closed_error=IncompleteReadError('0 bytes read on a total of 4 expected bytes')
    ```
  
* Listener (client):

    ```console
    python message_queue_listener.py --listen /queue/blah
  
  Starting up listener ba2c4f22
  Opened connection.. listener writer socket name ('127.0.0.1', 50336)
  Received data by ba2c4f22: b'Message 36 from 31e9'
  Received data by ba2c4f22: b'Message 38 from 31e9'
  Received data by ba2c4f22: b'Message 40 from 31e9'
  Received data by ba2c4f22: b'Message 42 from 31e9'
  Received data by ba2c4f22: b'Message 44 from 31e9'
  Received data by ba2c4f22: b'Message 46 from 31e9'
  Received data by ba2c4f22: b'Message 48 from 31e9'
  Received data by ba2c4f22: b'Message 50 from 31e9'
  Received data by ba2c4f22: b'Message 52 from 31e9'
  Received data by ba2c4f22: b'Message 54 from 31e9'
  Received data by ba2c4f22: b'Message 56 from 31e9'
  Received data by ba2c4f22: b'Message 58 from 31e9'
  Received data by ba2c4f22: b'Message 60 from 31e9'
  Received data by ba2c4f22: b'Message 62 from 31e9'
  Received data by ba2c4f22: b'Message 64 from 31e9'
  Received data by ba2c4f22: b'Message 66 from 31e9'
  Received data by ba2c4f22: b'Message 68 from 31e9'
  Received data by ba2c4f22: b'Message 70 from 31e9'
  Received data by ba2c4f22: b'Message 72 from 31e9'
  Received data by ba2c4f22: b'Message 74 from 31e9'
  Received data by ba2c4f22: b'Message 76 from 31e9'
  Received data by ba2c4f22: b'Message 78 from 31e9'
  Received data by ba2c4f22: b'Message 80 from 31e9'
  Received data by ba2c4f22: b'Message 82 from 31e9'
  Received data by ba2c4f22: b'Message 84 from 31e9'
  Received data by ba2c4f22: b'Message 86 from 31e9'
  Received data by ba2c4f22: b'Message 88 from 31e9'
  Received data by ba2c4f22: b'Message 90 from 31e9'
  Received data by ba2c4f22: b'Message 92 from 31e9'
  Received data by ba2c4f22: b'Message 94 from 31e9'
  Received data by ba2c4f22: b'Message 96 from 31e9'
  Received data by ba2c4f22: b'Message 98 from 31e9'
  Received data by ba2c4f22: b'Message 100 from 31e'
  Received data by ba2c4f22: b'Message 102 from 31e'
  Received data by ba2c4f22: b'Message 104 from 31e'
  Received data by ba2c4f22: b'Message 106 from 31e'
  Received data by ba2c4f22: b'Message 108 from 31e'
  Received data by ba2c4f22: b'Message 110 from 31e'
  Received data by ba2c4f22: b'Message 112 from 31e'
  Received data by ba2c4f22: b'Message 114 from 31e'
  Received data by ba2c4f22: b'Message 116 from 31e'
  Received data by ba2c4f22: b'Message 118 from 31e'
  Received data by ba2c4f22: b'Message 120 from 31e'
  Received data by ba2c4f22: b'Message 122 from 31e'
  Received data by ba2c4f22: b'Message 124 from 31e'
  Received data by ba2c4f22: b'Message 126 from 31e'
  Received data by ba2c4f22: b'Message 128 from 31e'
  Received data by ba2c4f22: b'Message 130 from 31e'
  Received data by ba2c4f22: b'Message 132 from 31e'
  Received data by ba2c4f22: b'Message 134 from 31e'
  Received data by ba2c4f22: b'Message 136 from 31e'
  Received data by ba2c4f22: b'Message 138 from 31e'
  Received data by ba2c4f22: b'Message 140 from 31e'
  Received data by ba2c4f22: b'Message 142 from 31e'
  Received data by ba2c4f22: b'Message 144 from 31e'
  Received data by ba2c4f22: b'Message 146 from 31e'
  Received data by ba2c4f22: b'Message 148 from 31e'
  Received data by ba2c4f22: b'Message 150 from 31e'
  Received data by ba2c4f22: b'Message 152 from 31e'
  Received data by ba2c4f22: b'Message 154 from 31e'
  Received data by ba2c4f22: b'Message 156 from 31e'
  Received data by ba2c4f22: b'Message 158 from 31e'
  Received data by ba2c4f22: b'Message 160 from 31e'
  Received data by ba2c4f22: b'Message 162 from 31e'
  Received data by ba2c4f22: b'Message 164 from 31e'
  Received data by ba2c4f22: b'Message 166 from 31e'
  Received data by ba2c4f22: b'Message 168 from 31e'
  Received data by ba2c4f22: b'Message 170 from 31e'
  Received data by ba2c4f22: b'Message 172 from 31e'
  Received data by ba2c4f22: b'Message 174 from 31e'
  Received data by ba2c4f22: b'Message 176 from 31e'
  Received data by ba2c4f22: b'Message 178 from 31e'
  Received data by ba2c4f22: b'Message 180 from 31e'
  Received data by ba2c4f22: b'Message 182 from 31e'
  Received data by ba2c4f22: b'Message 184 from 31e'
  Received data by ba2c4f22: b'Message 186 from 31e'
  Received data by ba2c4f22: b'Message 188 from 31e'
  Received data by ba2c4f22: b'Message 190 from 31e'
  Received data by ba2c4f22: b'Message 192 from 31e'
  Received data by ba2c4f22: b'Message 194 from 31e'
  Server closed. server_closed_error=IncompleteReadError('0 bytes read on a total of 4 expected bytes')
    ```
