"""Check the official vanilla demo inputs; never bundle Minecraft in the IPA."""
import hashlib
import json
import urllib.request


def fetch(url):
    with urllib.request.urlopen(url, timeout=120) as response:
        return response.read()


def checked(entry):
    data = fetch(entry['url'])
    if hashlib.sha1(data).hexdigest() != entry['sha1']:
        raise ValueError('Official download SHA1 mismatch')
    if 'size' in entry and len(data) != entry['size']:
        raise ValueError('Official download size mismatch')
    return data


manifest = json.loads(fetch('https://piston-meta.mojang.com/mc/game/version_manifest_v2.json'))
entry = next(v for v in manifest['versions'] if v['id'] == '1.21.4')
version = json.loads(checked(entry))
assert version['javaVersion']['majorVersion'] == 21
assert any(isinstance(arg, dict) and arg.get('value') == '--demo'
           and any(rule.get('features', {}).get('is_demo_user') is True
                   for rule in arg.get('rules', []))
           for arg in version['arguments']['game'])
checked(version['downloads']['client'])
assets = json.loads(checked(version['assetIndex']))
assert assets['objects']
print('PASS: official 1.21.4 metadata, Java 21, demo argument, client SHA1 and assets index SHA1')
print('No Minecraft files are packaged. Device downloads, authentication and JIT remain untested.')
