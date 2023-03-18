Logger: homeassistant.components.device_tracker
Source: components/bbox/device_tracker.py:83
Integration: Dispositif de suivi (documentation, issues)
First occurred: 09:42:01 (1 occurrences)
Last logged: 09:42:01

Error setting up platform legacy bbox
Traceback (most recent call last):
  File "/usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "/usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py", line 386, in _make_request
    self._validate_conn(conn)
  File "/usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py", line 1042, in _validate_conn
    conn.connect()
  File "/usr/local/lib/python3.10/site-packages/urllib3/connection.py", line 414, in connect
    self.sock = ssl_wrap_socket(
  File "/usr/local/lib/python3.10/site-packages/urllib3/util/ssl_.py", line 449, in ssl_wrap_socket
    ssl_sock = _ssl_wrap_socket_impl(
  File "/usr/local/lib/python3.10/site-packages/urllib3/util/ssl_.py", line 493, in _ssl_wrap_socket_impl
    return ssl_context.wrap_socket(sock, server_hostname=server_hostname)
  File "/usr/local/lib/python3.10/ssl.py", line 513, in wrap_socket
    return self.sslsocket_class._create(
  File "/usr/local/lib/python3.10/ssl.py", line 1071, in _create
    self.do_handshake()
  File "/usr/local/lib/python3.10/ssl.py", line 1342, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLError: [SSL: DH_KEY_TOO_SMALL] dh key too small (_ssl.c:997)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.10/site-packages/requests/adapters.py", line 489, in send
    resp = conn.urlopen(
  File "/usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "/usr/local/lib/python3.10/site-packages/urllib3/util/retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='mabbox.bytel.fr', port=443): Max retries exceeded with url: /api/v1/hosts (Caused by SSLError(SSLError(1, '[SSL: DH_KEY_TOO_SMALL] dh key too small (_ssl.c:997)')))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/src/homeassistant/homeassistant/components/device_tracker/legacy.py", line 248, in async_setup_legacy
    scanner = await hass.async_add_executor_job(
  File "/usr/local/lib/python3.10/concurrent/futures/thread.py", line 58, in run
    result = self.fn(*self.args, **self.kwargs)
  File "/usr/src/homeassistant/homeassistant/components/bbox/device_tracker.py", line 36, in get_scanner
    scanner = BboxDeviceScanner(config[DOMAIN])
  File "/usr/src/homeassistant/homeassistant/components/bbox/device_tracker.py", line 55, in __init__
    self.success_init = self._update_info()
  File "/usr/src/homeassistant/homeassistant/util/__init__.py", line 192, in wrapper
    result = method(*args, **kwargs)
  File "/usr/src/homeassistant/homeassistant/components/bbox/device_tracker.py", line 83, in _update_info
    result = box.get_all_connected_devices()
  File "/usr/local/lib/python3.10/site-packages/pybbox/__init__.py", line 112, in get_all_connected_devices
    resp = api.execute_api_request()
  File "/usr/local/lib/python3.10/site-packages/pybbox/bboxApiCall.py", line 48, in execute_api_request
    resp = self.call_method(self.api_url.get_url())
  File "/usr/local/lib/python3.10/site-packages/requests/api.py", line 73, in get
    return request("get", url, params=params, **kwargs)
  File "/usr/local/lib/python3.10/site-packages/requests/api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "/usr/local/lib/python3.10/site-packages/requests/sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "/usr/local/lib/python3.10/site-packages/requests/sessions.py", line 723, in send
    history = [resp for resp in gen]
  File "/usr/local/lib/python3.10/site-packages/requests/sessions.py", line 723, in <listcomp>
    history = [resp for resp in gen]
  File "/usr/local/lib/python3.10/site-packages/requests/sessions.py", line 266, in resolve_redirects
    resp = self.send(
  File "/usr/local/lib/python3.10/site-packages/requests/sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "/usr/local/lib/python3.10/site-packages/requests/adapters.py", line 563, in send
    raise SSLError(e, request=request)
requests.exceptions.SSLError: HTTPSConnectionPool(host='mabbox.bytel.fr', port=443): Max retries exceeded with url: /api/v1/hosts (Caused by SSLError(SSLError(1, '[SSL: DH_KEY_TOO_SMALL] dh key too small (_ssl.c:997)')))


- platform: bbox
    name: bbox
    monitored_variables:
      - down_max_bandwidth
      - up_max_bandwidth
      - current_down_bandwidth
      - current_up_bandwidth
      - uptime
      - number_of_reboots

