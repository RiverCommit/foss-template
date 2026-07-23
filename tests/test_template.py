from hypothesis import given, strategies as st

from foss_template import is_pinned, __version__


def test_version_present():
    assert __version__


def test_pinned_requirement_detected():
    assert is_pinned("httpx==0.28.1")


@given(st.text().filter(lambda s: "==" not in s))
def test_unpinned_requirement_rejected(req):
    assert not is_pinned(req)
