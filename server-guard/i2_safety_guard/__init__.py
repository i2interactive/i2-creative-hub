"""
i2 Safety Guard - server-side content policy for ComfyUI.        v2 (1.21.1)

Copy the i2_safety_guard folder into ComfyUI/custom_nodes/ and restart ComfyUI.

Every job sent to this ComfyUI is checked before it is validated or queued,
whichever front end sent it: the i2 Creative Hub, ComfyUI's own interface, or a
raw API call. A blocked job is refused with a normal ComfyUI error, so nothing
runs and the sender sees the reason.

The rules match the Creative Hub's built-in filter: sexual content, sexual
content involving minors, and graphic violence. For a shared or managed machine,
make this folder read-only for everyone but the admin.
"""
import inspect
import re

_NSFW = ["nude", "nudity", "naked", "topless", "bottomless", "explicit", "nsfw", "porn", "porno",
         "pornographic", "sex", "sexual", "sexually", "erotic", "erotica", "xxx", "hardcore",
         "genitals", "genitalia", "penis", "vagina", "vulva", "breasts", "nipples", "areola",
         "cleavage", "lingerie", "underwear", "panties", "thong", "fellatio", "cunnilingus",
         "masturbat", "orgasm", "ejaculat", "cum", "aroused", "seductive", "provocative",
         "suggestive", "fetish", "bdsm", "bondage", "hentai", "rule34", "onlyfans", "camgirl",
         "stripper", "striptease", "escort", "intercourse", "coitus", "fornicat"]
_MINOR = ["child", "children", "kid", "kids", "minor", "minors", "infant", "toddler", "baby",
          "babies", "preteen", "pre-teen", "tween", "teen", "teenage", "teenager", "adolescent",
          "underage", "schoolgirl", "schoolboy", "loli", "lolita", "shota", "juvenile",
          "youngster", "little girl", "little boy", "young girl", "young boy", "grade school",
          "elementary school", "middle school", "primary school", "newborn", "prepubescent",
          "pubescent"]
_GORE = ["gore", "gory", "blood", "bloody", "dismember", "decapitat", "mutilat", "corpse", "torture"]


def _rx(terms):
    # same matching as the hub: a term matches at the start of a word (so stems catch their
    # endings); multi-word phrases match anywhere
    parts = [re.escape(t) if " " in t else r"(?<![a-z0-9])" + re.escape(t) for t in terms]
    return re.compile("|".join(parts), re.IGNORECASE)


_RX_N, _RX_M, _RX_G = _rx(_NSFW), _rx(_MINOR), _rx(_GORE)


def _classify(text):
    t = (text or "").lower()
    if not t.strip():
        return None
    n, m, g = bool(_RX_N.search(t)), bool(_RX_M.search(t)), bool(_RX_G.search(t))
    if (n or g) and m:
        return "Sexual or violent terms appear alongside terms that can refer to minors."
    if n:
        return "The prompt contains explicit or adult terms."
    if g:
        return "The prompt contains graphic violence or gore terms."
    return None


_FILE = re.compile(r"\.[A-Za-z0-9]{2,5}$")  # model files, images, videos: not prompt text


def _scan(prompt):
    """Check every text value in the workflow, including text that comes from string or
    primitive nodes. File names (models, uploads) are skipped."""
    if not isinstance(prompt, dict):
        return None
    # negative prompts say what to keep OUT ("nsfw, blurry"), so they're not judged
    negs = set()
    for node in prompt.values():
        inputs = node.get("inputs") if isinstance(node, dict) else None
        if isinstance(inputs, dict):
            for k, v in inputs.items():
                if "negative" in k and isinstance(v, list) and v:
                    negs.add(str(v[0]))
    texts = []
    for nid, node in prompt.items():
        if str(nid) in negs or not isinstance(node, dict):
            continue
        inputs = node.get("inputs")
        if not isinstance(inputs, dict):
            continue
        for k, v in inputs.items():
            if "negative" in k:
                continue
            if isinstance(v, str) and v.strip() and not _FILE.search(v.strip()):
                texts.append(v)
    # judge the workflow as a whole, so a minor in one field and adult terms in another are caught
    return _classify("\n".join(texts))


def _find_prompt(args, kwargs):
    if isinstance(kwargs.get("prompt"), dict):
        return kwargs["prompt"]
    for a in list(args) + list(kwargs.values()):
        if isinstance(a, dict) and a and any(isinstance(v, dict) and "class_type" in v for v in a.values()):
            return a
    return None


def _refusal(reason):
    print("[i2_safety_guard] blocked a job :: " + reason)
    err = {"type": "i2_safety_block",
           "message": "Blocked by the i2 safety guard: " + reason,
           "details": reason,
           "extra_info": {}}
    return (False, err, [], {})


try:
    import execution

    _orig = execution.validate_prompt
    if getattr(_orig, "_i2_guarded", False):
        raise RuntimeError("already installed")

    if inspect.iscoroutinefunction(_orig):          # ComfyUI 0.3.4x and newer
        async def _guarded(*args, **kwargs):
            prompt = _find_prompt(args, kwargs)
            reason = _scan(prompt) if prompt else None
            if reason:
                return _refusal(reason)
            return await _orig(*args, **kwargs)
    else:                                             # older ComfyUI
        def _guarded(*args, **kwargs):
            prompt = _find_prompt(args, kwargs)
            reason = _scan(prompt) if prompt else None
            if reason:
                return _refusal(reason)
            return _orig(*args, **kwargs)

    _guarded._i2_guarded = True
    execution.validate_prompt = _guarded
    print("[i2_safety_guard] active - every job is checked before it is queued.")
except Exception as e:  # never take ComfyUI down; say loudly that nothing is being filtered
    if str(e) != "already installed":
        print("[i2_safety_guard] WARNING: could not install the check (%s). "
              "Jobs are NOT being filtered on this server." % e)

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}
