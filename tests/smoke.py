import urllib.request, json, sys, subprocess, time, os
p=subprocess.Popen([sys.executable,'-m','uvicorn','backend.main:app','--port','8123'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
time.sleep(1.5)
try:
    for path in ['/api/health','/api/content','/']:
        r=urllib.request.urlopen('http://127.0.0.1:8123'+path,timeout=5)
        assert r.status==200, path
    req=urllib.request.Request('http://127.0.0.1:8123/api/verify',data=json.dumps({'content_id':'AH-001'}).encode(),headers={'Content-Type':'application/json'},method='POST')
    d=json.load(urllib.request.urlopen(req)); assert d['verified'] is True
    req=urllib.request.Request('http://127.0.0.1:8123/api/ask',data=json.dumps({'question':'كيف يعمل التحقق؟'}).encode(),headers={'Content-Type':'application/json'},method='POST')
    d=json.load(urllib.request.urlopen(req)); assert d['grounded'] is True and d['sources']
    print('SMOKE TEST PASSED: health, content, verify, assistant, home')
finally:
    p.terminate(); p.wait(timeout=3)
