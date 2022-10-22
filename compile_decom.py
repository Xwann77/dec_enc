import marshal
import zlib
import base64
exec marshal.loads(zlib.decompress(base64.b64decode('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')))
