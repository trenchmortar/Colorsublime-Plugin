from .. import settings
import time


def cache(fn):
    """
    A decorator to cache method invocation.
    Cache expires after a set time.
    """
    cacheDB = {}

    def putCache(args, ans):
        if ans:
            cacheDB[args] = (time.time(), ans)

    def getCache(args):
        # Super slow, ghetto-fab cache
        t = time.time()
        cache_time = settings.get('cache_time', 0)
        ans = False
        to_remove = []

        for c in cacheDB:
            age = t - cacheDB[c][0]

            # Mark stale objects for cleaning
            if age > cache_time:
                to_remove.append(c)
                continue

            if c == args:
                ans = cacheDB[args][1]

        for c in to_remove:
            del cacheDB[c]

        return ans

    def wrap(*args):
        # Disable cache for debug.
        if settings.is_debug():
            return fn(*args)

        ans = getCache(args)
        if ans is False:
            ans = fn(*args)
            putCache(args, ans)
        return ans
    return wrap
